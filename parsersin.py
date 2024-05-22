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

    start = 'axioma'

    precedence = (
        ('left', 'DISJUNCTION'),
        ('left', 'CONJUNCTION'),
        ('nonassoc', 'EQ', 'LT', 'GT', 'LE', 'GE'),
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
        if len(p) == 2:
            p[0] = p[1]  # Una sola sentencia
        else:
            p[0] = p[1] + p[2]  # Varias sentencias
        pass


    def p_sentencia(self, p):
        '''sentencia : especial
                     | no_especial SEMICOLON'''
        p[0] = p[1]
        # print("Sentencia: ", p[0])
        pass

    def p_especial(self, p):
        '''especial : bucle 
                    | funcion'''
        p[0] = p[1]
        # print("Sentencia especial: ", p[0])
        pass

    def p_especial(self, p):
        '''especial : condicion'''
        cond, true, false = p[1][1], p[1][2], p[1][3]
        print("COND: ", cond)
        print("TRUE: ", true)
        print("FALSE: ", false)
        if (cond) :
            print("TRUE!!")
            p[0] = true
        else :
            print("FALSE!!")
            p[0] = false

        p[0] = p[1]
        print("CONDICION: ", p[0])
        pass

    # Ya que en JS se acepta una expresion, se implementa que también se permita aqui.

    def p_no_especial(self, p):
        '''no_especial : expresion
                       | declaracion
                       | asignacion
                       | definicion_objeto'''
        p[0] = p[1]
        # print("Sentencia no especial: ", p[0])

        pass
    
    def p_expresion(self, p):
        '''expresion : binaria
                     | unaria
                     | PARENTHESISOPEN expresion PARENTHESISCLOSE'''
        if len(p) == 4:
            p[0] = p[2]
        else:
            p[0] = p[1]

        # print("Expresión: ", p[0])
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
            print(f"ERROR[Sem] {num1[1]} {op} {num2[1]} -> type error.")
            return
        
        # JUSTIFICAR SUMAR LOS CHAR
        if num1[0] == 'char':
            num1 = ('int', ord(num2[1]))
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
        if op == '+':
            p[0] = (num1[0], num1[1] + num2[1])
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
            print(f"ERROR[Sem] {num1[1]} {op} {num2[1]} -> type error.")
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

    def p_expresion_identificador(self, p):
        '''expresion : ID'''
        name_var = p[1]
        if name_var not in self.simbolos:
            column = self.find_column(p.lexer.lexdata, p.slice[1])
            print(f"[ERROR][Sem] Variable {name_var} no existe. line: {p.lineno(1)} position: {column}")
            p[0] = None
        else:
            p[0] = self.simbolos[name_var]
        pass

    def p_expresion_entero(self, p):
        '''expresion : ENTERO
                     | BIN
                     | OCT
                     | HEX'''
        p[0] = ('int', p[1])
        print("Entero: ", p[0])
        pass

    def p_expresion_real(self, p):
        '''expresion : REAL
                     | NCIENT'''
        p[0] = ('float', p[1])
        print("Real: ", p[0])
        pass
    
    def p_expresion_char(self, p):
        '''expresion : CHAR'''
        p[0] = ('char', p[1])
        print("Caracter: ", p[0])
        pass

    def p_expresion_bool(self, p):
        '''expresion : TR
                     | FL'''
        if p[1] == 'tr':
            p[0] = ('bool', p[1])
        elif p[1] == 'fl':
            p[0] = ('bool', p[1])
        print("Booleano: ", p[0])
        pass

    def p_expresion_nulo(self, p):
        '''expresion : NULL'''
        p[0] = (None, None)
        print("Nulo: ", p[0])
        pass

    def p_expresion_otra(self, p):
        '''expresion : function_call
                     | acceso_propiedad'''
        pass

    def p_acceso_propiedad(self, p):
        '''acceso_propiedad : ID DOT ID acceso_propiedad_rec
                            | ID BRACKETOPEN STRING BRACKETCLOSE acceso_propiedad_rec'''
        pass
        
    def p_acceso_propiedad_rec(self, p):
        '''acceso_propiedad_rec : 
                                | DOT ID acceso_propiedad_rec
                                | BRACKETOPEN STRING BRACKETCLOSE acceso_propiedad_rec'''
        pass

    def p_declaracion(self, p):
        '''declaracion : LET lista_id
                       | LET lista_id EQUAL expresion'''
        
        if len(p) == 3:
            # Actualizar la tabla de simbolos con nuevas variables
            for id in p[2]:
                if id in self.simbolos:
                    print(f"ERROR[Sem] La re-declaración de la variable {id} no está permitida.")
                else:
                    self.simbolos[id] = (None, None)
                    print(f"Declaracion: {id}")
            p[0] = ('declaracion', id)
        elif len(p) == 5:
            # Verificar l
            for id in p[2]:
                # Asignar el tipo del valor asignado a la variable.
                self.simbolos[id] = p[4]
                print(f"Declasign: {id} con valor {p[4]}")
            p[0] = ('declasign', id, p[4])
        
        pass

    def p_lista_id(self, p):
        '''lista_id : ID
                    | ID COMA lista_id'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]
        pass

    def p_asignacion(self, p):
        '''asignacion : lista_id EQUAL expresion'''

        for id in p[1]:
            if id not in self.simbolos:
                print(f"ERROR[Sem] La variable {id} no existe. line: {p.lexpos(1)}")
            else:
                self.simbolos[id] = p[3]
                print(f"Asignacion: {id} con valor {p[3]}")
        p[0] = ('asignacion', id, p[3])

        pass

    # Las expresiones entre parentesis de condiciones y bucles son obligatorias, no pueden ser vacias!

    # Hay un if / if – else.
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
            p[0] = p[2]  # Si existe el bloque else, se asigna
        else:
            p[0] = None  # No hay bloque else

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

        pass

     # Tipo de las funciones
    def p_tipo(self, p):
        '''tipo : INT
                | FLOAT
                | CHARACTER
                | BOOLEAN
                | ID'''         # ID un tanto sospechoso deberiamos mirarlo!!
        pass

    # Se decide que debe haber minimo un return en el bloque de ejecuciones de la función.

    # Función
    def p_funcion(self, p):
        '''funcion : FUNCTION ID PARENTHESISOPEN lista_arg PARENTHESISCLOSE COLON tipo LLAVEA axioma RETURN expresion SEMICOLON LLAVEC'''
        tipo_fcn, tipo_rtrn = p[7], p[11]
        print("Tipo de la función es: ", tipo_fcn)
        print("Tipo del valor de retorno: ", tipo_rtrn)
        pass

    # La función puede no tener argumentos
    
    def p_lista_arg(self, p):
        '''lista_arg : 
                     | lista_arg_rec'''
        pass

    def p_lista_arg_rec(self, p):
        '''lista_arg_rec : ID COLON tipo
                         | ID COLON tipo COMA lista_arg_rec'''
        pass
    
    def p_function_call(self, p):
        '''function_call : ID PARENTHESISOPEN lista_param PARENTHESISCLOSE'''
        pass

    # Como los argumentos pueden ser vacíos, se define así

    def p_lista_param(self, p):
        '''lista_param : 
                       | lista_param_rec'''
        pass

    def p_lista_param_rec(self, p):
        '''lista_param_rec : expresion COMA lista_param_rec
                           | expresion'''
        pass

    # OBJETOS AJSON

    def p_definicion_objeto(self, p):
        '''definicion_objeto : TYPE ID COLON ID'''
        pass

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