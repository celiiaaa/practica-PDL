import os
import sys
import ply.yacc as yacc
from mylexer import LexerClass


class ParserClass:

    tokens = LexerClass.tokens

    def __init__(self):
        self.lexer = LexerClass().lexer
        self.parser = yacc.yacc(module=self)
        self.contenido = None
        self.simbolos = {}          # Tabla de símbolos
        self.registro = {}          # Tabla de registro
        self.local_symbols = {}     # Tabla de símbolos local para funciones
        self.local_aux = {}
        self.valor_retorno = {}
        self.dentro_funcion = False
        self.registro_local = {}
        self.registro_local_aux = {}

    start = 'axioma'

    precedence = (
        ('left', 'DISJUNCTION'),
        ('left', 'CONJUNCTION'),
        ('nonassoc', 'EQ'),
        ('nonassoc', 'LT', 'GT', 'LE', 'GE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIV'),
        ('right', 'UPLUS', 'UMINUS'),
        ('right', 'NEG'), 
        ('right', 'EQUAL')
    )

    # Vacio
    def p_empty(self, p):
        '''empty :'''
        pass

    # Axioma
    def p_axioma(self, p):
        '''axioma : programa
                  | empty'''
        pass

    # Programa
    def p_programa(self, p):
        '''programa : bloque_programa'''
        pass

    # Bloque de programa
    def p_bloque_programa(self, p):
        '''bloque_programa : sentencia
                           | sentencia bloque_programa'''
        # print("Bloque programa: ", p[1])
        """ if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[1] + p[2] """
        pass

    # Sentencia
    def p_sentencia(self, p):
        '''sentencia : declaracion SEMICOLON
                     | asignacion SEMICOLON
                     | declaracion_objeto SEMICOLON
                     | asignacion_objeto SEMICOLON
                     | funcion_call SEMICOLON
                     | condicion
                     | bucle
                     | funcion'''
        p[0] = p[1]
        # print("Sentencia: ", p[0])
        pass

    # ------------------- DECLARACIONES Y ASIGNACIONES -------------------

    # SE PERMITE concaternar variables de tipo basico (int, float, char, bool) con variables de tipo complejo (AJSON)
    # PERO NO al asignar mientras se declara

    # Declaración
    def p_declaracion(self, p):
        '''declaracion : LET lista_id
                       | LET lista_id_mas EQUAL expresion'''
        # declaración simple
        if len(p) == 3:
            for id, tipo in p[2]:
                # declaración de una variable global
                if self.dentro_funcion == False:
                    if id in self.simbolos:
                        print(f"ERROR[Sem] La re-declaración de la variable {id} no está permitida.")
                    else:
                        self.simbolos[id] = (tipo, None)
                # declaración de una variable local
                else:
                    if id in self.local_aux:
                        print(f"ERROR[Sem] La re-declaración de la variable {id} no está permitida.")
                    else:
                        self.local_aux[id] = (tipo, None)
        # declaración con asignación
        elif len(p) == 5:
            for id in p[2]:
                # si la expresión es válida, se asigna el valor
                if p[4] != None:
                    # declaración de una variable global
                    if self.dentro_funcion == False:
                        if id in self.simbolos:
                            print(f"ERROR[Sem] La re-declaración de la variable {id} no está permitida.")
                        else:
                            self.simbolos[id] = p[4]
                    # declaración de una variable local
                    else:
                        if id in self.local_aux:
                            print(f"ERROR[Sem] La re-declaración de la variable {id} no está permitida.")
                        else:
                            self.local_aux[id] = p[4]
        pass

    # Lista de identificadores para la declaración
    def p_lista_id(self, p):
        '''lista_id : ID
                    | ID COMA lista_id'''
        # para una variable simple (int, float, char, bool)
        if len(p) == 2:
            # nombre de la variable y tipo
            elem = (p[1], None)
            # lista de identificadores
            p[0] = [elem]
        elif len(p) == 4:
            # nombre de la variable y tipo
            elem = (p[1], None)
            # lista de identificadores
            p[0] = [elem] + p[3]
        pass

    def p_lista_id2(self, p):
        '''lista_id : ID COLON ID
                    | ID COLON ID COMA lista_id'''
        # para una variable compleja (objetos AJSON)
        if len(p) == 4:
            # nombre de la variable y tipo
            elem = (p[1], p[3])
            # lista de identificadores
            p[0] = [elem]
        elif len(p) == 6:
            # nombre de la variable y tipo
            elem = (p[1], p[3])
            # lista de identificadores
            p[0] = [elem] + p[5]
        pass

    # Asignación
    def p_asignacion(self, p):
        '''asignacion : lista_id_mas EQUAL expresion'''
        for id in p[1]:
            expr = p[3]
            if expr == -1:
                # si la expresión no es válida
                print(f"ERROR[Sem] El valor no coincide con el tipo de la variable {id}.")
                return
            if isinstance(id, list):
                # si se trata de un acceso a una propiedad de un objeto
                name_var = id[0]
                val  = self.simbolos.get(name_var, self.local_aux.get(name_var))
                if val is None:
                    print(f"ERROR[Sem] La variable {name_var} no existe.")
                    p[0] = None
                    return
                # lista de propiedades a acceder
                lista = id[1:]
                for key in lista[:-1]:
                    dic = val[1]
                    if key in dic:
                        dic = dic[key]
                        val = dic
                    else:
                        # si la propiedad no existe
                        print(f"ERROR[Sem] La propiedad {key} no existe en el objeto {name_var}.")
                        p[0] = None
                        return
                # si se trata de la última propiedad, la que se va a modificar
                dic = val[1]
                if lista[-1] in dic:
                    # si la propiedad existe
                    if dic[lista[-1]][0] != expr[0]:
                        # si el tipo de la propiedad no coincide con el tipo de la expresión
                        print(f"ERROR[Sem] El tipo de la propiedad {lista[-1]} no coincide con el tipo de la asignación.")
                        return
                    # asignar el valor
                    dic[lista[-1]] = expr
                else:
                    # si la propiedad no existe
                    print(f"ERROR[Sem] La propiedad {lista[-1]} no existe en el objeto {id[0]}.")
                    return
            else:
                # si se trata de cualquier otra cosa
                if id not in self.simbolos and id not in self.local_aux:
                    # si la variable no existe
                    print(f"ERROR[Sem] La variable {id} no existe.")
                    return
                else:
                    # si la variable existe
                    if p[3] != None:
                        # si la expresión es válida
                        if self.simbolos.get(id, self.local_aux.get(id))[0] != None:
                            # si el tipo de la variable no coincide con el tipo de la expresión
                            if self.simbolos.get(id, self.local_aux.get(id))[0] != p[3][0]:
                                # print(f"ERROR[Sem] El tipo de la variable {id} no coincide con el tipo de la asignación.")
                                return
                        if self.dentro_funcion == False:
                            self.simbolos[id] = p[3]
                        self.local_aux[id] = p[3]
            pass

    # Lista de identificadores para la asignación
    def p_lista_id_mas(self, p):
        '''lista_id_mas : ID
                        | ID COMA lista_id_mas'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]
        pass

    def p_lista_id_mas2(self, p):
        '''lista_id_mas : acceso_propiedad
                        | acceso_propiedad COMA lista_id_mas'''
        # acceso a una propiedad de un objeto
        # lista con las propiedades a acceder
        if len(p) == 2:
            p[0] = [(p[1])]
        else:
            p[0] = [(p[1])] + p[3]
        pass

    # ------------------- EXPRESIONES -------------------

    # Expresión
    def p_expresion(self, p):
        '''expresion : binaria
                     | unaria
                     | termino
                     | PARENTHESISOPEN expresion PARENTHESISCLOSE'''
        if len(p) == 4:
            p[0] = p[2]
        else:
            p[0] = p[1]
        pass

    def p_binaria_aritmetica1(self, p):
        '''binaria : expresion PLUS expresion
                   | expresion MINUS expresion'''
        num1, op, num2 = p[1], p[2], p[3]
        # si no se puede realizar la operación
        if num1 is None or num2 is None:
            print("ERROR[Sem] No se puede realizar la operación.")
            return
        # verificar los tipos válidos de las expresiones
        tipos = ['int', 'float', 'char']
        if num1[0] not in tipos or num2[0] not in tipos:
            print(f"ERROR[Sem] La operacion {num1[0]} {op} {num2[0]} no es válida.")
            p[0] = None
        else:
            if num1[0] == num2[0] == 'char':
                a = ord(num1[1])
                b = ord(num2[1])
                if op == '+':
                    try:
                        p[0] = ('char', chr(a + b))
                    except:
                        print(f"ERROR[Sem] La suma de los caracteres {num1[1]} y {num2[1]} no es posible.")
                        p[0] = None
                elif op == '-':
                    try:
                        p[0] = ('char', chr(a - b))
                    except:
                        print(f"ERROR[Sem] La resta de los caracteres {num1[1]} y {num2[1]} no es posible.")
                        p[0] = None
            else:
                if num1[0] != num2[0]:
                    if num1[0] == 'char':
                        num1 = ('int', ord(num1[1]))
                    elif num2[0] == 'char':
                        num2 = ('int', ord(num2[1]))
                    # Operar
                    res = num1[1] + num2[1] if op == '+' else num1[1] - num2[1]
                    p[0] = ('int', res) if res.is_integer() else ('float', res)
                
                else:
                    res = num1[1] + num2[1] if op == '+' else num1[1] - num2[1]
                    p[0] = (num1[0], res)
        pass

    def p_binaria_aritmetica2(self, p):
        '''binaria : expresion TIMES expresion
                   | expresion DIV expresion'''
        num1, op, num2 = p[1], p[2], p[3]
        if num1 is None or num2 is None:
            print("ERROR[Sem] No se puede realizar la operación.")
            p[0] = None
            return
        tipos = ['int', 'float']
        if num1[0] not in tipos or num2[0] not in tipos:
            print(f"ERROR[Sem] La operacion {num1[0]} {op} {num2[0]} no es válida.")
            p[0] = None
        else:
            # Operar
            if (num1[0] != num2[0]) or (num1[0] == num2[0] == 'float'):
                if op == '*':
                    p[0] = ('float', num1[1] * num2[1])
                elif op == '/':
                    p[0] = ('float', num1[1] / num2[1])
            elif num1[0] == num1[0] == 'int':
                if op == '*':
                    p[0] = ('int', num1[1] * num2[1])
                elif op == '/':
                    p[0] = ('int', num1[1] / num2[1])
        pass

    def p_binaria_comparacion1(self, p):
        '''binaria : expresion LT expresion
                   | expresion GT expresion
                   | expresion LE expresion
                   | expresion GE expresion'''
        num1, op, num2 = p[1], p[2], p[3]
        if num1 is None or num2 is None:
            print("ERROR[Sem] No se puede realizar la operación.")
            p[0] = None
            return
        tipos = ['int', 'float', 'char']
        if num1[0] not in tipos or num2[0] not in tipos:
            print(f"ERROR[Sem] La operacion {num1[0]} {op} {num2[0]} no es válida.")
            p[0] = None
        else:
            # Cast de char a int
            if num1[0] == 'char':
                num1 = ('int', ord(num2[1]))
            elif num2[0] == 'char':
                num2 = ('int', ord(num1[1]))
            # Operar
            if op == '<':
                p[0] = ('bool', num1[1] < num2[1])
            elif op == '>':
                p[0] = ('bool', num1[1] > num2[1])
            elif op == '<=':
                p[0] = ('bool', num1[1] <= num2[1])
            elif op == '>=':
                p[0] = ('bool', num1[1] >= num2[1])
        pass

    def p_binaria_comparacion2(self, p):
        '''binaria : expresion EQ expresion'''
        num1, op, num2 = p[1], p[2], p[3]
        # si no se puede realizar la operación
        if num1 is None or num2 is None:
            print("ERROR[Sem] No se puede realizar la operación.")
            p[0] = None
            return
        # verificar los tipos válidos de las expresiones
        tipos = ['int', 'float', 'char', 'bool']
        if num1[0] not in tipos or num2[0] not in tipos:
            print(f"ERROR[Sem] La operacion {num1[0]} {op} {num2[0]} no es válida.")
            p[0] = None
        # si uno de los dos es booleano y el otro no
        elif num1[0] != num2[0] and (num1[0] == 'bool' or num2[0] == 'bool'):
            print(f"ERROR[Sem] La operacion {num1[0]} {op} {num2[0]} no es válida.")
            p[0] = None
        else:
            # Cast de char a int
            if num1[0] == 'char':
                num1 = ('int', ord(num2[1]))
            elif num2[0] == 'char':
                num2 = ('int', ord(num1[1]))
            # Operar
            if op == '==':
                p[0] = ('bool', num1[1] == num2[1])
        pass

    def p_binaria_boolean(self, p):
        '''binaria : expresion CONJUNCTION expresion
                   | expresion DISJUNCTION expresion'''
        num1, op, num2 = p[1], p[2], p[3]
        # si no se puede realizar la operación
        if num1 is None or num2 is None:
            print("ERROR[Sem] No se puede realizar la operación.")
            p[0] = None
            return
        # verificar los tipos válidos de las expresiones
        if num1[0] != 'bool' or num2[0] != 'bool':
            print(f"ERROR[Sem] La operacion {num1[0]} {op} {num2[0]} no es válida.")
            p[0] = None
        else:
            # Operar
            if op == '&&':
                p[0] = ('bool', num1[1] and num2[1])
            elif op == '||':
                p[0] = ('bool', num1[1] or num2[1])
        pass

    def p_unaria(self, p):
        '''unaria : MINUS expresion %prec UMINUS
                  | PLUS expresion %prec UPLUS
                  | NEG expresion'''
        op, num = p[1], p[2]
        # si no se puede realizar la operación
        if num is None:
            print("ERROR[Sem] No se puede realizar la operación.")
            return
        # verificar los tipos válidos de las expresiones
        tipo = ['int', 'float', 'char']
        if op == '+':
            # suma unario
            if num[0]  not in tipo:
                print(f"ERROR[Sem] La expresión {num[1]} no permite el operador unario suma.")
                p[0] = None
            else:
                p[0] = (num[0], +num[1])
        elif op == '-':
            # resta unario
            if num[0]  not in tipo:
                    print(f"ERROR[Sem] La expresión {num[1]} no permite el operador unario resta.")
                    p[0] = None
            else:
                p[0] = (num[0], -num[1])
        elif op == '!':
            # negación
            if num[0] != 'bool':
                # si el tipo de la expresión no es booleano
                print(f"ERROR[Sem] La expresión {num[1]} no permite el operador not.")
                p[0] = None
            else:
                p[0] = (num[0], not num[1])
        pass

    # Término
    def p_termino_identificador(self, p):
        '''termino : ID'''
        # verificar si la variable existe
        if p[1] in self.local_aux and self.dentro_funcion == True:
            p[0] = self.local_aux.get(p[1])
        elif p[1] in self.simbolos and self.dentro_funcion == False:
            p[0] = self.simbolos.get(p[1])
        else:
            column = self.find_column(p.lexer.lexdata, p.slice[1])
            print(f"[ERROR][Sem] Variable {p[1]} no existe. line: {p.lineno(1)} position: {column}")
            p[0] = None
            return
        pass

    def p_termino_entero(self, p):
        '''termino : ENTERO
                   | BIN
                   | OCT
                   | HEX'''
        # tipo y valor
        p[0] = ('int', p[1])
        pass

    def p_termino_real(self, p):
        '''termino : REAL
                   | NCIENT'''
        # tipo y valor
        p[0] = ('float', p[1])
        pass

    def p_termino_caracter(self, p):
        '''termino : CHAR'''
        # tipo y valor
        p[0] = ('char', p[1])
        pass

    def p_termino_booleano(self, p):
        '''termino : TR
                   | FL'''
        # tipo y valor
        p[0] = ('bool', p[1])
        pass

    def p_termino_nulo(self, p):
        '''termino : NULL'''
        # tipo y valor
        p[0] = ('null', None)
        pass

    def p_termino_propiedad(self, p):
        '''termino : acceso_propiedad'''
        # acceso a una propiedad de un objeto
        name_var = p[1][0]
        val  = self.simbolos.get(name_var, self.registro_local.get(name_var))
        # recorrerse las propiedades
        lista = p[1][1:]
        for key in lista:
            dic = val[1]
            if key in dic:
                dic = dic[key]
                val = dic
            else:
                # si la propiedad no existe
                print(f"ERROR[Sem] La propiedad {key} no existe en el objeto {name_var}.")
                p[0] = None
                return
        p[0] = val
        pass

    def p_termino_llamada(self, p):
        '''termino : funcion_call'''
        # llamada a una función
        p[0] = p[1]
        pass

    def p_termino_objeto(self, p):
        '''termino : objeto_asg'''
        # asignación de un objeto
        tipo = self.obtener_tipo_objeto(p[1])
        if tipo is None:
            # si el objeto no existe
            print("ERROR[Sem] El tipo de objeto no existe.")
            p[0] = -1
        else:
            p[0] = (tipo, p[1])
        pass

    # ------------------- CONDICIONALES Y BUCLES -------------------

    # Condición
    def p_condicion(self, p):
        '''condicion : IF PARENTHESISOPEN expresion PARENTHESISCLOSE bloque_llaves otra_condicion'''
        valor_cond = p[3]
        # verificar si la condición es una expresión válida
        if valor_cond[0] != 'bool':
            print("ERRROR[Sem] La condicion del if solo permite expresiones de tipo booleano.")
        pass

    def p_otra_condicion(self, p):
        '''otra_condicion :
                          | ELSE bloque_llaves'''
        # si no hay else
        if len(p) == 1:
            p[0] = None
        # si hay else
        elif len(p) == 3:
            p[0] = p[2]
        pass

    # Bucle
    def p_bucle(self, p):
        '''bucle : WHILE PARENTHESISOPEN expresion PARENTHESISCLOSE bloque_llaves'''
        valor_cond = p[3]
        # Verificar si la condición es una expresión válida
        if valor_cond[0] != 'bool':
            print("ERRROR[Sem] La condicion del bucle while solo permite expresiones de tipo booleano.")
        pass

    # Bloque de llaves
    def p_bloque_llaves(self, p):
        '''bloque_llaves : LLAVEA bloque_programa LLAVEC'''
        # bloque con el programa de ejecución
        p[0] = p[2]
        pass

    # ------------------- FUNCIONES Y SUS LLAMADAS -------------------

    # Tipos de las funciones
    def p_tipo(self, p):
        '''tipo : INT
                | FLOAT
                | CHARACTER
                | BOOLEAN'''
        tipo = p[1]
        if p[1] == 'character':
            tipo = 'char'
        elif p[1] == 'boolean':
            tipo = 'bool'
        p[0] = tipo
        pass

    def p_tipo_objeto(self, p):
        '''tipo : ID'''
        # tipo de un objeto AJSON
        if self.registro.get(p[1]) is None:
            print(f"ERROR[Sem] El objeto {p[1]} no existe.")
            p[0] = -1
        else:
            p[0] = (p[1], self.registro.get(p[1]))
        pass

    # Función
    def p_funcion(self, p):
        '''funcion : FUNCTION ID PARENTHESISOPEN lista_arg PARENTHESISCLOSE COLON tipo LLAVEA axioma RETURN expresion SEMICOLON LLAVEC'''
        funcion_nombre = p[2]
        parametros = p[4]
        self.local_symbols[funcion_nombre] = parametros
        self.valor_retorno[funcion_nombre] = p[7]
        if p[11] == None:
            return_expr = None
        else:
            if p[11][0] != 'char' and p[11][0] != 'int' and p[11][0] != 'float' and p[11][0] != 'bool':
                if isinstance(p[11][0], tuple):
                    if p[7] != p[11][0]:
                        print(f"ERROR[Sem] El tipo de la función {p[2]} no coincide con el tipo de retorno.")
                else:
                    if p[7][0] != p[11][0]:
                            print(f"ERROR[Sem] El tipo de la función {p[2]} no coincide con el tipo de retorno.")
                    else:
                        # Comparar los tipos de los campos internos de las estructuras
                        return_type_fields = p[7][1]
                        return_expr_fields = p[11][1]
                        for field in return_type_fields:
                            expected_type = return_type_fields[field]
                            actual_value = return_expr_fields[field]
                            if isinstance(actual_value, tuple):
                                actual_type = actual_value[0]
                            else:
                                actual_type = actual_value
                            if expected_type != actual_type:
                                return 
            else:
                return_type, return_expr = p[7], p[11][0]
                if return_type != return_expr:
                    print(f"ERROR[Sem] El tipo de la función {p[2]} no coincide con el tipo de retorno.")
        p[0] = ('funcion', p[2], p[4], p[7], p[11])
        self.dentro_funcion = False
        pass

    # Lista de argumentos
    def p_lista_arg(self, p):
        '''lista_arg :
                     | lista_arg_rec'''
        self.dentro_funcion = True
        if len(p) == 1:
            p[0] = []
        else:
            p[0] = p[1]
            # Actualizar la tabla de simbolos con nuevas variables
            for id in p[1]:
                if id[1] == 'char':
                    self.local_aux[id[0]] = (id[1], '0')  
                elif id[1] == 'int':
                    self.local_aux[id[0]] = (id[1], 0)
                elif id[1] == 'float':  
                    self.local_aux[id[0]] = (id[1], 0.0)
                elif id[1] == 'bool':
                    self.local_aux[id[0]] = (id[1], False) 
                else:
                    dic = {}                    
                    for key in id[1][1]:
                        tipo = id[1][1][key]
                        if tipo == 'char':
                            dic[key] = (tipo, '0')
                        elif tipo == 'int':
                            dic[key] = (tipo, 0)
                        elif tipo == 'float':
                            dic[key] = (tipo, 0.0)
                        elif tipo == 'bool':
                            dic[key] = (tipo, False)
                    self.registro_local[id[0]] = (id[1][0], dic)  
                    self.local_aux[id[0]] = (id[1][0], dic)   
                    
        pass

    def p_lista_arg_rec(self, p):
        '''lista_arg_rec : ID COLON tipo
                         | ID COLON tipo COMA lista_arg_rec'''
        if len(p) == 4:
            p[0] = [(p[1], p[3])]
        else:
            p[0] = [(p[1], p[3])] + p[5]
        pass

    # Llamada a una función
    def p_funcion_call(self, p):
        '''funcion_call : ID PARENTHESISOPEN lista_param PARENTHESISCLOSE'''
        funcion_nombre = p[1]
        parametros_llamada = p[3]
        # Verificar si la función existe en los símbolos locales
        if funcion_nombre not in self.local_symbols:
            print(f"ERROR[Sem] La función {funcion_nombre} no está definida.")
            return
        parametros_definidos = self.local_symbols[funcion_nombre]
        # Verificar si la cantidad de parámetros coincide
        if len(parametros_llamada) != len(parametros_definidos):
            print(f"ERROR[Sem] La cantidad de argumentos no coincide con los parámetros de la función {funcion_nombre}.")
            return
        # Verificar tipos de parámetros
        for i, (arg_name, arg_type) in enumerate(parametros_definidos):
            parametro_llamada = parametros_llamada[i]
            if isinstance(arg_type, tuple):
                if parametro_llamada[0] != arg_type[0]:
                    print(f"ERROR[Sem] El argumento {parametro_llamada[1]} de tipo {parametro_llamada[0]} no coincide con el tipo del parámetro {arg_name} de tipo {arg_type}.")
                    return
            else:
                if parametro_llamada[0] != arg_type:
                    print(f"ERROR[Sem] El argumento {parametro_llamada[1]} de tipo {parametro_llamada[0]} no coincide con el tipo del parámetro {arg_name} de tipo {arg_type}.")
                    return
        if self.valor_retorno[funcion_nombre] == 'char':
            p[0] = (self.valor_retorno[funcion_nombre], '0')
        elif self.valor_retorno[funcion_nombre] == 'int':
            p[0] = (self.valor_retorno[funcion_nombre], 0)
        elif self.valor_retorno[funcion_nombre] == 'float':
            p[0] = (self.valor_retorno[funcion_nombre], 0.0)
        elif self.valor_retorno[funcion_nombre] == 'bool':
            p[0] = (self.valor_retorno[funcion_nombre], False)
        else:
            p[0] = (self.valor_retorno[funcion_nombre], {})
        pass

    # Lista de parámetros
    def p_lista_param(self, p):
        '''lista_param : 
                       | lista_param_rec'''
        if len(p) == 1:
            p[0] = []
        else:
            p[0] = p[1]
        pass

    def p_lista_param_rec(self, p):
        '''lista_param_rec : expresion
                           | expresion COMA lista_param_rec'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]
        pass

    # ------------------- OBJETOS AJSON -------------------

    # Definición de un objeto
    def p_declaracion_objeto(self, p):
        '''declaracion_objeto : TYPE ID EQUAL objeto_dec'''
        # verificar si estoy dentro de una función
        if self.dentro_funcion:
            # verificar si el objeto ya existe
            if p[2] in self.registro_local_aux:
                print(f"ERROR[Sem] La re-declaración del objeto {p[2]} no está permitida.")
                return
            else:
                self.registro_local_aux[p[2]] = p[4]
        # si no estoy dentro de una función
        else:
            # verificar si el objeto ya existe
            if p[2] in self.registro:
                print(f"ERROR[Sem] La re-declaración del objeto {p[2]} no está permitida.")
                return
            else:
                # asignar el valor del objeto
                if p[4] == {}:
                    self.registro[p[2]] = {}
                else:                    
                    self.registro[p[2]] = p[4]
        pass

    def p_objeto_dec(self, p):
        '''objeto_dec : LLAVEA propiedades_dec LLAVEC'''
       # diccionario con las propiedades del objeto y sus tipos
        dic = {}
        if len(p) == 4:
            for elem in p[2]:
                key, value = elem[0], elem[1]
                if key is None and value == -1:
                    continue
                dic[key] = value
            p[0] = dic
        pass

    def p_propiedades_dec(self, p):
        '''propiedades_dec : 
                           | propiedad_dec
                           | propiedad_dec COMA propiedades_dec'''
        # lista con las propiedades del objeto
        if len(p) == 1:
            p[0] = []
        elif len(p) == 2:
            p[0] = [p[1]]
        elif len(p) == 4:
            p[0] = [p[1]] + p[3]
        pass

    def p_propiedad_dec(self, p):
        '''propiedad_dec : ID COLON tipo
                         | STRING COLON tipo'''
        # propiedad del objeto
        if p[3] == -1:
            p[0] = (None, -1)
        else:
            p[0] = (p[1], p[3])
        pass

    def p_propeidad_dec2(self, p):
        '''propiedad_dec : ID COLON objeto_dec
                         | STRING COLON objeto_dec'''
        # propiedad del objeto -> objeto anidado
        p[0] = (p[1], p[3])
        pass

    # Asignación de un objeto
    def p_asignacion_objeto(self, p):
        '''asignacion_objeto : LET ID COLON ID EQUAL objeto_asg'''
        var_name, obj_name = p[2], p[4]
        # verificar si estoy dentro de una función
        if self.dentro_funcion:
            # verificar si el objeto ya existe
            if obj_name in self.registro_local_aux:
                print(f"ERROR[Sem] El objeto {obj_name} no existe.")
                return
            # verificar si la variable ya existe
            if var_name in self.registro_local:
                print(f"ERROR[Sem] La re-declaración de la variable {var_name} no está permitida.")
                return
        # si no estoy dentro de una función
        else:
            # verificar si el objeto ya existe
            if var_name in self.simbolos:
                print(f"ERROR[Sem] La re-declaración de la variable {var_name} no está permitida.")
                return
            # verificar si el objeto ya existe
            if obj_name not in self.registro:
                print(f"ERROR[Sem] El objeto {obj_name} no existe.")
                return
        # asignar el valor del objeto
        valores = p[6]
        valores = (obj_name, valores)
        if len(p) == 7:
            # Comprobar que las propiedades del objeto coinciden con las propiedades definidas
            if self.comprobar_objeto(obj_name, valores):
                if self.dentro_funcion:
                    self.registro_local_aux[var_name] = valores
                else:
                    self.simbolos[var_name] = valores
            else:
                print(f"ERROR[Sem] Las propiedades del objeto {obj_name} no coinciden con las propiedades definidas.")
                return
        pass

    def p_objeto_asg(self, p):
        '''objeto_asg : LLAVEA propiedades_asg LLAVEC'''
        # diccionario con las propiedades del objeto y sus valores
        dic = {}
        if len(p) == 4:
            for elem in p[2]:
                key, value = elem[0], elem[1]
                if key is None and value == -1:
                    continue
                dic[key] = value
            p[0] = dic
        pass

    def p_propiedades_asg(self, p):
        '''propiedades_asg : 
                           | propiedad_asg
                           | propiedad_asg COMA propiedades_asg'''
        # lsita con las propiedades del objeto y sus valores asignados
        if len(p) == 1:
            p[0] = []
        elif len(p) == 2:
            p[0] = [p[1]]
        elif len(p) == 4:
            p[0] = [p[1]] + p[3]
        pass

    def p_propiedad_asg(self, p):
        '''propiedad_asg : ID COLON expresion
                         | STRING COLON expresion'''
        # propiedad del objeto con su valor asignado -> tipo y valor
        if p[3] == -1:
            p[0] = (None, -1)
        else:
            p[0] = (p[1], p[3])
        pass

    # Acceso a la propiedad de un objeto
    def p_acceso_propiedad(self, p):
        '''acceso_propiedad : ID DOT ID acceso_propiedad_rec
                            | ID BRACKETOPEN STRING BRACKETCLOSE acceso_propiedad_rec'''
        # acceso a una propiedad de un objeto
        # lista con las propiedades a acceder
        if len(p) == 5:
            p[0] = [p[1], p[3]] + p[4]
        elif len(p) == 6:
            p[0] = [p[1], p[3]] + p[5]
        pass

    def p_acceso_propiedad_rec(self, p):
        '''acceso_propiedad_rec : 
                                | DOT ID acceso_propiedad_rec
                                | BRACKETOPEN STRING BRACKETCLOSE acceso_propiedad_rec'''
        # lista con las propiedades a acceder
        if len(p) == 1:
            p[0] = []
        elif len(p) == 4:
            p[0] = [p[2]] + p[3]
        elif len(p) == 5:
            p[0] = [p[2]] + p[4]
        pass
    
    # ------------------- FUNCIONES AUXILIARES -------------------

    def obtener_tipo_objeto(self, valor: dict):
        """Devolver el nombre del tipo del objeto."""
        for tipo_objeto, propiedades in self.registro.items():
            # comprobar si el objeto es un objeto AJSON anidado
            if isinstance(propiedades, dict):
                # comprobar si las propiedades del objeto coinciden con las definidas
                if propiedades.keys() == valor.keys(): 
                    return tipo_objeto
        return None

    def _comprobar_objeto(self, name_obj, propiedades, valor):
        # Comprobamos si el tipo de objeto coincide
        if all(key in propiedades for key in valor[1]):
            for key, value in valor[1].items():
                if isinstance(value[1], dict):
                    if not self._comprobar_objeto(key, propiedades[key][1], value):
                        return False
        else:
            for key in valor[1]:
                if key not in propiedades:
                    print(f"ERROR[Sem] La propiedad {key} no coincide con las propiedades definidas.")
                    return False
        return True
    
    def comprobar_objeto(self, name_obj: str, valor: tuple):
        """Comprobar si las propiedades del objeto coinciden con las definidas."""
        propiedades = self.registro[name_obj]
        if all(key in propiedades for key in valor[1]):
            for val in valor[1].items():
                key, value = val
                # si el valor es un objeto anidado
                if isinstance(value[1], dict):
                    # comprobar si las propiedades del objeto coinciden con las definidas
                    if not self._comprobar_objeto(key, propiedades[key], value):
                        return False
                else:
                    if propiedades[key] != value[0]:
                        print(f"ERROR[Sem] El tipo de la propiedad {key} no coincide con el tipo definido.")
                        return False
        else:
            for key in valor[1]:
                if key not in propiedades:
                    print(f"ERROR[Sem] La propiedad {key} no coincide con las propiedades definidas.")
                    return False
        return True
    
    # ------------------- TEST Y ERRORES -------------------

    def find_column(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1
    
    def p_error(self, p):
        if p:
            print(f"[Syntax Error] At value {p.value} at line {p.lineno} at column {self.find_column(p.lexer.lexdata, p)}")
        else:
            print(f"[Syntax Error] EOF at line {p.lineno}")
   
    def test(self, data):
        self.parser.parse(data)

    def test_with_files(self, path):
        file = open(path)
        content = file.read()  
        self.test(content)
        # Escribir el fichero de salida
        directory, filename = os.path.split(path)
        filename = os.path.splitext(filename)[0]
        output_filename1 = os.path.join(directory, filename + ".symbols")
        output_filename2 = os.path.join(directory, filename + ".register")
        with open(output_filename1, 'w') as f1:
            for simbolo in self.simbolos:
                f1.write(f"{simbolo}: {self.simbolos[simbolo]}\n")
        with open(output_filename2, 'w') as f2:
            for simbolo in self.registro:
                f2.write(f"{simbolo}: {self.registro[simbolo]}\n")


if __name__ == "__main__":
    parser = ParserClass()
    if len(sys.argv) > 1:
        parser.test_with_files(sys.argv[1])
