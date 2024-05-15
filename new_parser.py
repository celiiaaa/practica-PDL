import sys
import ply.yacc as yacc
from mylexer import LexerClass


class ParserClass:

    tokens = LexerClass.tokens

    def __init__(self):
        self.lexer = LexerClass().lexer
        self.parser = yacc.yacc(module=self)
        self.contenido = None
    
    simbolos = {}           # Tabla de símbolos

    registro = {}           # Tabla de registro

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
        pass

    def p_programa(self, p):
        '''programa : bloque_programa'''
        pass

    def p_bloque_programa(self, p):
        '''bloque_programa : sentencia
                           | sentencia bloque_programa'''
        pass

    # No se va a poder una sentencia de una expresion! es decir esto "1 + 2;"

    def p_sentencia(self, p):
        '''sentencia : declaracion SEMICOLON
                     | asignacion SEMICOLON
                     | condicion
                     | bucle 
                     | funcion
                     | declaracion_objeto SEMICOLON
                     | asignacion_objeto SEMICOLON
                     | function_call SEMICOLON'''
        pass
    
    def p_expresion(self, p):
        '''expresion : binaria
                     | unaria
                     | literal
                     | PARENTHESISOPEN expresion PARENTHESISCLOSE
                     | asg_ajson'''
        pass

    def p_binaria_aritmetica1(self, p):
        '''binaria : expresion PLUS expresion
                   | expresion MINUS expresion'''
        
        num1, op, num2 = p[1], p[2], p[3]
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
            else:
                print(f"ERROR[Sem] La operación {num1} {op} {num2} no es válida.")
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

        pass

    def p_binaria_booleana2(self, p):
        '''binaria : expresion EQ expresion'''

        num1, op, num2 = p[1], p[2], p[3]

        pass

    def p_binaria_conjunto(self, p):
        '''binaria : expresion CONJUNCTION expresion
                   | expresion DISJUNCTION expresion'''
        
        num1, op, num2 = p[1], p[2], p[3]

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
            p[0] = (num[0], +num[1])
        
        # NO SÉ HACER EL NEGADO!!

        pass

    # No se puede aceptar una asignacion if (char == 'a' && i = (4 + 5))

    def p_literal_identificador(self, p):
        '''literal : ID'''
        name_var = p[1]
        if name_var not in self.simbolos:
            print(f"[ERROR][Sem] Variable {name_var} no existe.")
        else:
            p[0] = self.simbolos[name_var]
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

        p[0] = (None, p[1])
        pass


    def p_literal(self, p):
        '''literal : function_call
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
            # Actualizar la tabla de simbolos con nuevas variables
            for id in p[2]:
                self.simbolos[id] = (None, None)
        elif len(p) == 5:
            # Verificar l
            for id in p[2]:
                # Asignar el tipo del valor asignado a la variable.
                self.simbolos[id] = p[4]
        
        pass

    def p_lista_id(self, p):
        '''lista_id : ID
                    | ID COMA lista_id
                    | ID COLON ID COMA
                    | ID COLON ID COMA lista_id
                    | acceso_propiedad'''
        pass

    def p_asignacion(self, p):
        '''asignacion : lista_id EQUAL expresion'''

        if len(p) == 4:
            name_var = p[1]
            valor_var = p[3]
            tipo_var = self.simbolos[name_var]
            if tipo_var != self.get_tipo_expresion(valor_var):
                print("ERROR[sem] Tipo incompatible en la asignación.")
        
        pass

    # Las expresiones entre parentesis de condiciones y bucles son obligatorias, no pueden ser vacias!

    # Hay un if / if – else.
    # Condición
    def p_condicion(self, p):
        '''condicion : IF PARENTHESISOPEN expresion PARENTHESISCLOSE bloque_llaves otra_condicion'''
        pass

    def p_otra_condicion(self, p):
        '''otra_condicion : 
                          | ELSE bloque_llaves'''
        pass

    # Se decide que lo que haya entre llaves no puede ser vacío.

    def p_bloque_llaves(self, p):
        '''bloque_llaves : LLAVEA bloque_programa LLAVEC'''
        pass

    # Bucle
    def p_bucle(self, p):
        '''bucle : WHILE PARENTHESISOPEN expresion PARENTHESISCLOSE bloque_llaves'''
        pass

     # Tipo de las funciones
    def p_tipo(self, p):
        '''tipo : INT
                | FLOAT
                | CHARACTER
                | BOOLEAN
                | ID'''         # ID un tanto sospechoso deberiamos mirarlo!!
        pass

    # Se decide que lo que haya entre llaves no puede ser vacío.

    # Función
    def p_funcion(self, p):
        '''funcion : FUNCTION ID PARENTHESISOPEN lista_arg PARENTHESISCLOSE COLON tipo LLAVEA bloque_programa RETURN expresion SEMICOLON LLAVEC'''
        pass
    
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

    def p_lista_param(self, p):
        '''lista_param : 
                       | lista_param_rec'''
        pass

    def p_lista_param_rec(self, p):
        '''lista_param_rec : expresion COMA lista_param_rec
                           | expresion'''
        pass

    # OBJETOS AJSON.
    def p_declaracion_objeto(self, p):
        '''declaracion_objeto : TYPE ID EQUAL def_ajson'''
        pass
    
    def p_def_ajson(self, p):
        '''def_ajson : LLAVEA def_propiedades LLAVEC'''
        pass
    
    # Puede ser que las propiedades de los objetos estén vacías

    def p_def_propiedades(self, p):
        '''def_propiedades : 
                           | ID COLON valor_def_propiedad def_propiedades_rec
                           | STRING COLON valor_def_propiedad def_propiedades_rec'''
        pass
        
    def p_def_propiedades_rec(self, p):
        '''def_propiedades_rec : COMA def_propiedades
                               | '''
        pass
    
    def p_valor_def_propiedad(self, p):
        '''valor_def_propiedad : tipo
                               | def_ajson'''
        pass

    def p_asignacion_objeto(self, p):
        '''asignacion_objeto : LET ID COLON ID EQUAL asg_ajson'''
        pass
    
    def p_asg_ajson(self, p):
        '''asg_ajson : LLAVEA asg_propiedades LLAVEC''' 
        pass
    
    def p_asg_propiedades(self, p):
        '''asg_propiedades :
                           | ID COLON valor_asg_propiedad asg_propiedades_rec
                           | STRING COLON valor_asg_propiedad asg_propiedades_rec'''
        pass
    
    def p_asg_propiedades_rec(self, p):
        '''asg_propiedades_rec : COMA asg_propiedades
                               | '''
        pass

    def p_valor_asg_propiedad(self, p):
        '''valor_asg_propiedad : expresion''' 
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