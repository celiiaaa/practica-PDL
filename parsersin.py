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

    start = 'axioma'

    precedence = (
        ('left', 'DISJUNCTION'),
        ('left', 'CONJUNCTION'),
        ('nonassoc', 'EQ'),
        ('nonassoc', 'LT', 'GT', 'LE', 'GE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIV'),
        ('right', 'UPLUS', 'UMINUS'),
        ('right', 'NEG')
    )

    # Vacio
    def p_empty(self, p):
        '''empty :'''
        pass

    # Axioma
    def p_axioma(self, p):
        '''axioma : programa
                  | empty'''
        p[0] = p[1]
        pass

    def p_programa(self, p):
        '''programa : bloque_programa'''
        p[0] = ('programa', p[1])
        pass

    def p_bloque_programa(self, p):
        '''bloque_programa : sentencia
                           | sentencia bloque_programa'''
        # print("Bloque programa: ", p[1])
        """ if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[1] + p[2] """
        pass

    def p_sentencia(self, p):
        '''sentencia : declaracion SEMICOLON
                     | asignacion SEMICOLON
                     | condicion
                     | bucle 
                     | funcion
                     | declaracion_objeto SEMICOLON
                     | asignacion_objeto SEMICOLON
                     | function_call SEMICOLON'''
        p[0] = p[1]
        # print("Sentencia: ", p[0])
        pass

    # Ya que en JS se acepta una expresion, se implementa que también se permita aqui.

    def p_expresion(self, p):
        '''expresion : literal
                     | binaria
                     | unaria
                     | PARENTHESISOPEN expresion PARENTHESISCLOSE'''
        if len(p) == 4:
            p[0] = p[2]
        else:
            p[0] = p[1]

        # print("Expresión: ", p[0])
        pass

    def p_binaria_aritmetica1(self, p):
        '''binaria : expresion PLUS expresion
                   | expresion MINUS expresion'''
        
        num1, op, num2 = p[1], p[2], p[3]
        print(f"Aritmetica 1: {num1} {op} {num2}")
        if num1 is None:
            print(f"[ERROR][Sem] Variable no existe.")
            return
        if num2 is None:
            print(f"[ERROR][Sem] Variable no existe.")
            return
        
        if num1[0] == 'bool' or num2[0] == 'bool':
            print(f"ERROR[Sem] {num1[0]} {op} {num2[0]} -> type error.")
            return
        
        # JUSTIFICAR SUMAR LOS CHAR
        print(f"Num1: {num1[0]}")
        print(f"Num2: {num2[0]}")
        if num1[0] == 'char' or num1[0] == 'character':
            print(f"Char: {num2[1]}")
            num1 = ('int', ord(num2[1]))
        if num2[0] == 'char' or num2[0] == 'character':
            num2 = ('int', ord(num2[1]))
        
        if num1[0] != num2[0]:
        # Casting
            if num1[0] == 'float':
                num2 = ('float', float(num2[1]))
            elif num2[0] == 'float':
                num1 = ('float', float(num1[1]))
            elif num1[0] == 'int':
                num2 = ('int', int(num2[1]))
            elif num2[0] == 'int':
                num1 = ('int', int(num1[1]))
        # Operar
        if op == '+':
            p[0] = (num1[0], num1[1] + num2[1])
            print(f"Resultado: {p[0]}")
        elif op == '-':
            p[0] = (num1[0], num1[1] - num2[1])

        pass

    def p_binaria_aritmetica2(self, p):
        '''binaria : expresion TIMES expresion
                   | expresion DIV expresion'''
        num1, op, num2 = p[1], p[2], p[3]
        print(f"Aritmetica 2: {num1} {op} {num2}")
        
        if num1 is None:
            print(f"[ERROR][Sem] Variable no existe.")
            return
        if num2 is None:
            print(f"[ERROR][Sem] Variable no existe.")
            return
        
        # JUSTIFICAR QUE NO SE PUEDEN MULTIPLICAR DOS CHAR
        
        if (num1[0] not in ['int', 'float', 'char'] or num2[0] not in ['int', 'float', 'char']) or (num1[0] == 'char' and num2[0] == 'char'):
            print(f"ERROR[Sem] {num1[0]} {op} {num2[0]} -> type error.")
            return 
        
        if num1[0] == 'char':
            num1 = ('int', ord(num1[1]))
        if num2[0] == 'char':
            num2 = ('int', ord(num2[1]))


        if num1[0] != num2[0]:
            # Casting
            if num1[0] == 'float':
                num2 = ('float', float(num2[1]))
            elif num2[0] == 'float':
                num1 = ('float', float(num1[1]))
            elif num1[0] == 'int':
                num2 = ('int', int(num2[1]))
            elif num2[0] == 'int':
                num1 = ('int', int(num1[1]))
        
        # Operar
        if op == '*':
            p[0] = (num1[0], num1[1] * num2[1])
        elif op == '/':
            p[0] = (num1[0], num1[1] / num2[1])

        pass
        
    def p_binaria_booleana1(self, p):
        '''binaria : expresion LT expresion
                   | expresion GT expresion
                   | expresion LE expresion
                   | expresion GE expresion'''
        
        num1, op, num2 = p[1], p[2], p[3]
        print(f"Booleana 1: {num1} {op} {num2}")
        # Casting
        if num1[0] == 'char':
            num1 = ('int', ord(num1[1]))
        if num2[0] == 'char':
            num2 = ('int', ord(num2[1])) 

        if num1[0] != num2[0]:
            if num1[0] == 'float':
                num2 = ('float', float(num2[1]))
            elif num2[0] == 'float':
                num1 = ('float', float(num1[1]))
            elif num1[0] == 'int':
                num2 = ('int', int(num2[1]))
            elif num2[0] == 'int':
                num1 = ('int', int(num1[1]))
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

    def p_binaria_booleana2(self, p):
        '''binaria : expresion EQ expresion'''

        num1, op, num2 = p[1], p[2], p[3]
        print(f"Booleana 2: {num1} {op} {num2}")
        # Casting
        if num1[0] != num2[0]:
            if num1[0] == 'float':
                num2 = ('float', float(num2[1]))
            elif num2[0] == 'float':
                num1 = ('float', float(num1[1]))
            elif num1[0] == 'int':
                num2 = ('int', int(num2[1]))
            elif num2[0] == 'int':
                num1 = ('int', int(num1[1]))
            elif num1[0] == 'bool' or num2[0] == 'bool':
                print(f"ERROR[Sem] La operacion {num1[1]} {op} {num2[1]} no es válida.")
                return
        # Operar
        if op == '==':
            p[0] = ('bool', num1[1] == num2[1])
        
        pass

    def p_binaria_conjunto(self, p):
        '''binaria : expresion CONJUNCTION expresion
                   | expresion DISJUNCTION expresion'''
        
        num1, op, num2 = p[1], p[2], p[3]
        print(f"Conjunto: {num1} {op} {num2}")
        if num1[0] != 'bool' or num2[0] != 'bool':
            print(f"ERROR[Sem] La operacion {num1[1]} {op} {num2[1]} no es válida.")
            pass
        # Operar
        if op == '&&':
            p[0] = ('bool', num1[1] and num2[1])
        elif op == '||':
            p[0] = ('bool', num1[1] or num2[1])

        pass

    # Operaciones aritmeticas unitarias
    def p_unaria(self, p):
        '''unaria : PLUS expresion %prec UPLUS
                  | MINUS expresion %prec UMINUS
                  | NEG expresion'''
        
        op, num = p[1], p[2]
        if op == '+':
            p[0] = (num[0], +num[1])
        elif op == '-':
            p[0] = (num[0], -num[1])
        elif op == '!':
            if num[0] != 'bool':
                print(f"ERROR[Sem] La expresión {num[1]} no permite el operador not.")
            p[0] = (num[0], not num[1])

        pass

    # No se puede aceptar una asignacion if (char == 'a' && i = (4 + 5))    // "i ="

    def p_literal_identificador(self, p):
        '''literal : ID'''
        name_var = p[1]
        if name_var not in self.simbolos and name_var not in self.local_aux:
            column = self.find_column(p.lexer.lexdata, p.slice[1])
            print(f"[ERROR][Sem] Variable {name_var} no existe. line: {p.lineno(1)} position: {column}")
            p[0] = None
        else:
            p[0] = self.simbolos.get(name_var, self.local_aux.get(name_var))
            print(f"Valor de la variable {name_var}: {p[0]}")
        pass

    def p_literal_entero(self, p):
        '''literal : ENTERO
                   | BIN
                   | OCT
                   | HEX'''
        p[0] = ('int', p[1])
        pass

    def p_literal_real(self, p):
        '''literal : REAL
                   | NCIENT'''
        p[0] = ('float', p[1])
        pass
    
    def p_literal_char(self, p):
        '''literal : CHAR'''
        p[0] = ('char', p[1])
        pass

    def p_literal_bool(self, p):
        '''literal : TR
                   | FL'''
        p[0] = ('bool', p[1])
        pass

    def p_literal_nulo(self, p):
        '''literal : NULL'''
        p[0] = ('nulo', None)
        pass

    def p_literal_objeto(self, p):
        '''expresion : objeto_asg'''
        p[0] = ('obj_asg', p[1])
        
        pass

    def p_literal_acceso(self, p):
        '''expresion : acceso_obj'''
        p[0] = ('propiedad', p[1])
        pass

    def p_literal_llamada(self, p):
        '''expresion : function_call'''
        p[0] = ('funcion', p[1])
        pass

    # Acceso a la propiedad de un objeto
    def p_acceso_propiedad(self, p):
        '''acceso_propiedad : ID DOT ID acceso_propiedad_rec
                            | ID BRACKETOPEN STRING BRACKETCLOSE acceso_propiedad_rec'''
        pass

    def p_acceso_propiedad_rec(self, p):
        '''acceso_propiedad_rec : 
                                | DOT ID acceso_propiedad_rec
                                | BRACKETOPEN STRING BRACKETCLOSE acceso_propiedad_rec'''
        pass
    
    # Acceso al valor de una propiedad de un objeto
    def p_acceso_obj(self, p):
        '''acceso_obj : ID DOT ID acceso_obj_rec
                      | ID BRACKETOPEN STRING BRACKETCLOSE acceso_obj_rec'''
        pass

    def p_acceso_obj_rec(self, p):
        '''acceso_obj_rec : 
                          | DOT ID acceso_obj_rec
                          | BRACKETOPEN STRING BRACKETCLOSE acceso_obj_rec'''
        pass

    # Declaración
    def p_declaracion(self, p):
        '''declaracion : LET lista_id
                       | LET lista_id_mas EQUAL expresion'''

        if len(p) == 3:
            # Actualizar la tabla de simbolos con nuevas variables
            for id, tipo in p[2]:
                if id in self.simbolos or id in self.registro:
                    print(f"ERROR[Sem] La re-declaración de la variable {id} no está permitida.")
                else:
                    self.simbolos[id] = (tipo, None)
                    
                    print(f"Declaracion: {id} : {self.simbolos[id]}")
            p[0] = ('declaracion', p)
        
        elif len(p) == 5:
            # Verificar l        
            for id in p[2]:

                # Asignar el tipo del valor asignado a la variable.
                self.simbolos[id] = p[4]
                self.local_aux[id[0]] = p[4]
                print(f"Declasign: {id} con valor {p[4]}")
            p[0] = ('declasign', id, p[4])
        
        pass

    # Lista de identificadores para la declaración
    def p_lista_id(self, p):
        '''lista_id : ID
                    | ID COMA lista_id'''
        pass

        if len(p) == 2:
            elem = (p[1], None)
            p[0] = [elem]
        elif len(p) == 4:
            elem = (p[1], None)
            p[0] = [elem] + p[3]

        print("Lista id: ", p[0])
        pass

    def p_lista_id2(self, p):
        '''lista_id : ID COLON ID
                    | ID COLON ID COMA lista_id'''
        if len(p) == 4:
            elem = (p[1], p[3])
            p[0] = [elem]
        elif len(p) == 6:
            elem = (p[1], p[3])
            p[0] = [elem] + p[5]
        print("Lista id: ", p[0])
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
        if len(p) == 2:
            p[0] = (p[1])
        else:
            p[0] = (p[1]) + p[3]
        pass

    def p_asignacion(self, p):
        '''asignacion : lista_id_mas EQUAL expresion'''

        for id in p[1]:
            if id not in self.simbolos and id not in self.local_aux:
                print(f"ERROR[Sem] La variable {id} no existe. line: {p.lexpos(1)}")
            else:
                self.simbolos[id] = p[3]
                print(f"Asignacion: {id} con valor {p[3]}")
        p[0] = ('asignacion', id, p[3])

        pass

    # Las expresiones entre parentesis de condiciones y bucles son obligatorias, no pueden ser vacias!

    # Condición
    def p_condicion(self, p):
        '''condicion : IF PARENTHESISOPEN expresion PARENTHESISCLOSE bloque_llaves otra_condicion'''

        valor_cond = p[3]
        if valor_cond[0] != 'bool':
            print("ERRROR[Sem] La sentencia if requiere un booleano.")

        p[0] = ('if', p[3], p[5], p[6])
        print("Condicion: ", p[0])
            
        """ if valor_cond[1]:  # Si la condición es verdadera
            print("p5",p[5])
            p[0] = p[5]  # Ejecuta el bloque dentro de las llaves
        else:
            p[0] = p[6]  # Ejecuta el bloque del else si existe
        """            
        pass

    def p_otra_condicion(self, p):
        '''otra_condicion : 
                          | ELSE bloque_llaves'''
        
        if len(p) > 1:
            p[0] = p[2]
        else:
            p[0] = None

        pass

    # Se decide que lo que haya entre llaves no puede ser vacío.

    def p_bloque_llaves(self, p):
        '''bloque_llaves : LLAVEA bloque_programa LLAVEC'''
        p[0] = p[2]
        pass

    # Bucle
    def p_bucle(self, p):
        '''bucle : WHILE PARENTHESISOPEN expresion PARENTHESISCLOSE bloque_llaves'''
        
        valor_cond = p[3]
        if valor_cond[0] != 'bool':
            print("ERRROR[Sem] La sentencia if requiere un booleano.")

        p[0] = ('while', p[3], p[5])

        pass

     # Tipo de las funciones
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
        print("Tipo: ", p[0])

        pass

    def p_tipo_objeto(self, p):
        '''tipo : ID'''
        if self.registro.get(p[1]) is None:
            print(f"ERROR[Sem] El objeto {p[1]} no existe.")
            p[0] = -1
        else:
            p[0] = p[1]
        print("Tipo obj: ", p[0])
        pass

    # DEBE haber minimo un return en el bloque de ejecuciones de la función.

    # Función
    def p_funcion(self, p):
        '''funcion : FUNCTION ID PARENTHESISOPEN lista_arg PARENTHESISCLOSE COLON tipo LLAVEA axioma RETURN expresion SEMICOLON LLAVEC'''
        
        funcion_nombre = p[2]
        parametros = p[4]
        self.local_symbols[funcion_nombre] = parametros
        self.valor_retorno[funcion_nombre] = p[7]
        print(self.local_symbols)
        if p[11] == None:
            return_expr = None
        else:
            if p[11][0] != 'character' and p[11][0] != 'int' and p[11][0] != 'float' and p[11][0] != 'bool':
                print(f"Funcion: {p[2]} con tipo {p[7]} y retorno {p[11][0]}")
            else:
                return_type, return_expr = p[7], p[11][0]
                print(f"Funcion: {p[2]} con tipo {return_type} y retorno {return_expr}")
                if return_type != return_expr:
                    print(f"ERROR[Sem] El tipo de la función {p[2]} no coincide con el tipo de retorno.")
        
        p[0] = ('funcion', p[2], p[4], p[7], p[11])
        pass

    # La función puede no tener argumentos
    def p_lista_arg(self, p):
        '''lista_arg : 
                     | lista_arg_rec'''
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
                    self.local_aux[id[0]] = (id[1], None)         
        pass

    def p_lista_arg_rec(self, p):
        '''lista_arg_rec : ID COLON tipo
                         | ID COLON tipo COMA lista_arg_rec'''
        if len(p) == 4:
            p[0] = [(p[1], p[3])]
        else:
            p[0] = [(p[1], p[3])] + p[5]
        pass
    
    def p_function_call(self, p):
        '''function_call : ID PARENTHESISOPEN lista_param PARENTHESISCLOSE'''
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

        pass

    # Como los argumentos pueden ser vacíos, se define así

    def p_lista_param(self, p):
        '''lista_param : 
                       | lista_param_rec'''
        if len(p) == 1:
            p[0] = []
        else:
            p[0] = p[1]
        pass

    def p_lista_param_rec(self, p):
        '''lista_param_rec : expresion COMA lista_param_rec
                           | expresion'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]
        
        pass

    # OBJETOS AJSON

    def p_declaracion_objeto(self, p):
        '''declaracion_objeto : TYPE ID EQUAL objeto_dec'''
        
        if p[2] in self.registro:
            print(f"ERROR[Sem] El objeto {p[2]} ya existe.")
            return
        
        # CREO QUE ESTO NO ES NECESARIO, ya que no son variables, son tipos de objetos AJSON.
        """ if p[2] in self.simbolos:
            print(f"ERROR[Sem] La re-declaración de la variable {p[2]} no está permitida.")
            return """
        
        if len(p) == 5:
            if p[4] == []:
                self.registro[p[2]] = {}
                print(f"Declaracion de objeto: {p[2]} con propiedades vacías.")
            elif p[4][0] != -1:
                
                self.registro[p[2]] = p[4]
                print(f"Declaracion de objeto: {p[2]} con propiedades {p[4]}")
        pass

    def p_objeto_dec(self, p):
        '''objeto_dec : LLAVEA propiedades_dec LLAVEC'''
        p[0] = p[2]
        
        pass

    def p_propiedades_dec(self, p):
        '''propiedades_dec : 
                           | propiedad_dec
                           | propiedad_dec COMA propiedades_dec'''
        if len(p) == 1:
            p[0] = []
        elif len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]
        pass

    def p_propiedad_dec(self, p):
        '''propiedad_dec : ID COLON tipo
                         | STRING COLON tipo'''
        if p[3] == -1:
            p[0] = -1
        else:
            p[0] = {p[1]: p[3]}
        pass

    def p_propeidad_dec2(self, p):
        '''propiedad_dec : ID COLON objeto_dec
                         | STRING COLON objeto_dec'''
        p[0] = {p[1]: (p[3])}

        pass

    def p_asignacion_objeto(self, p):
        '''asignacion_objeto : LET ID COLON ID EQUAL objeto_asg'''
        var_name, obj_name = p[2], p[4]
        if var_name in self.simbolos:
            print(f"ERROR[Sem] La re-declaración de la variable {var_name} no está permitida.")
            return
        if obj_name not in self.registro:
            print(f"ERROR[Sem] El objeto {obj_name} no existe.")
            return
        
        # Asignar el objeto vacío
        propiedades = self.registro[obj_name]
        valores = []
        for prop in propiedades:
            for key, value in prop.items():
                valores.append({key : (value, None)})
        self.simbolos[var_name] = valores
        print(f"Asignacion de objeto vacío {var_name} con valores {self.simbolos[var_name]}")            
            
        # Comprobar que los tipos de las propiedades coinciden con las del objeto
        lista_valores = p[6]
        print(f"Lista valores: {lista_valores}")
        for i in range(len(lista_valores)):
            for key, value in lista_valores[i].items():
                if key not in propiedades[i]:
                    print(f"ERROR[Sem] La propiedad {key} no existe en el objeto {obj_name}.")
                    return
                if value[0] != propiedades[i][key]:
                    print(f"ERROR[Sem] El tipo de la propiedad {key} no coincide con el del objeto {obj_name}.")
                    return
                
        # Asignar las propiedades al objeto
        self.simbolos[var_name] = (obj_name, lista_valores)
        # Asignar los valores al objeto
        """ for i in range(len(lista_valores)):
            for key, value in lista_valores[i].items():
                self.simbolos[var_name][i][key] = value """

        print(f"Asignacion de objeto {var_name} con valores {self.simbolos[var_name]}")

        pass

    def p_objeto_asg(self, p):
        '''objeto_asg : LLAVEA propiedades_asg LLAVEC'''
        p[0] = p[2]
        pass

    def p_propiedades_asg(self, p):
        '''propiedades_asg : 
                           | propiedad_asg
                           | propiedad_asg COMA propiedades_asg'''
        if len(p) == 1:
            p[0] = []
        elif len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]
        pass

    def p_propiedad_asg(self, p):
        '''propiedad_asg : ID COLON expresion
                         | STRING COLON expresion'''
        p[0] = {p[1]: (p[3])}
        pass



    # EVALUAR LA LÓGICA INTERNA – EXTRA ---------------------------

    # Evaluar expresiones
    def evaluate_expression(self, expression):
        if isinstance(expression, tuple):
            if expression[0] == 'binary':
                return self.evaluate_binary_expression(expression)
            elif expression[0] == 'unary':
                return self.evaluate_unary_expression(expression)
            elif expression[0] == 'literal':
                return expression[1]
            elif expression[0] == 'object':
                return expression[1]
            elif expression[0] == 'call':
                return self.evaluate_function_call(expression)
        elif isinstance(expression, str):
            return self.simbolos.get(expression, None)
        return expression

    # Evaluar cada sentencia
    def evaluate_statement(self, statement):
        if statement[0] == 'if':
            self.evaluate_if(statement)
        elif statement[0] == 'if_else':
            self.evaluate_if_else(statement)
        elif statement[0] == 'while':
            self.evaluate_while(statement)

        """
        elif statement[0] == 'block':
            for stmt in statement[1]:
                evaluate_statement(stmt)
        elif statement[0] == 'declaration':
            pass  # Las declaraciones ya se manejan en p_declaration
        elif statement[0] == 'assignment':
            pass  # Las asignaciones ya se manejan en p_assignment
        elif statement[0] == 'return':
            pass  # El manejo del retorno se puede hacer aquí si es necesario
        elif statement[0] == 'expression':
            evaluate_expression(statement[1])
        """
    
    # Evaluar condicional if
    def evaluate_if(self, statement):
        condition, block = statement
        if self.evaluate_expression(condition):
            self.evaluate_statement(block)

    # Evaluar condicional if-else
    def evaluate_if_else(self ,statement):
        condition, if_block, else_block = statement
        if self.evaluate_expression(condition):
            self.evaluate_statement(if_block)
        else:
            self.evaluate_statement(else_block)

    # Evaluar bucle while
    def evaluate_while(self, statement):
        condition, block = statement
        while self.evaluate_expression(condition):
            self.evaluate_statement(block)



    # ---------------------------------------------------------------

    def print_simbolos(self):
        print("Simbolos: ")
        for key, value in self.simbolos.items():
            print(f"\t{key} : {value}")

    def print_registro(self):
        print("Registro: ")
        for key, value in self.registro.items():
            print(f"\t{key} : {value}")

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

if __name__ == "__main__":
    parser = ParserClass()
    if len(sys.argv) > 1:
        parser.test_with_files(sys.argv[1])