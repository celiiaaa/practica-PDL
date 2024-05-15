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
                     | primaria
                     | asg_ajson'''
        pass

    def p_binaria(self, p):
        '''binaria : expresion PLUS expresion
                   | expresion MINUS expresion
                   | expresion TIMES expresion
                   | expresion DIV expresion
                   | expresion CONJUNCTION expresion
                   | expresion DISJUNCTION expresion
                   | expresion EQ expresion
                   | expresion LT expresion
                   | expresion GT expresion
                   | expresion LE expresion
                   | expresion GE expresion'''
        pass

    # Operaciones aritmeticas unitarias
    def p_unaria(self, p):
        '''unaria : PLUS expresion %prec UPLUS
                  | MINUS expresion %prec UMINUS
                  | NEG expresion'''
        pass

    # No se puede aceptar una asignacion if (char == 'a' && i = (4 + 5))

    def p_primaria(self, p):
        '''primaria : literal
                    | ID
                    | PARENTHESISOPEN expresion PARENTHESISCLOSE'''
        pass

    def p_literal(self, p):
        '''literal : ENTERO
                   | REAL
                   | BIN
                   | OCT
                   | NCIENT
                   | HEX
                   | CHAR
                   | TR
                   | FL
                   | NULL
                   | function_call
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
        pass

    # Se decide que lo que haya entre llaves no puede ser vacío.
    # Hay un if / if – else.

    # Condición
    def p_condicion(self, p):
        '''condicion : IF PARENTHESISOPEN expresion PARENTHESISCLOSE LLAVEA bloque_programa LLAVEC otra_condicion'''
        pass

    def p_otra_condicion(self, p):
        '''otra_condicion : 
                          | ELSE LLAVEA bloque_programa LLAVEC'''
        
    # Se decide que lo que haya entre llaves no puede ser vacío.

    # Bucle
    def p_bucle(self, p):
        '''bucle : WHILE PARENTHESISOPEN expresion PARENTHESISCLOSE LLAVEA bloque_programa LLAVEC'''
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
        '''function_call : ID PARENTHESISOPEN lista_expresion PARENTHESISCLOSE'''
        pass

    def p_lista_expresion(self, p):
        '''lista_expresion : 
                           | lista_expresion_rec'''
        pass

    def p_lista_expresion_rec(self, p):
        '''lista_expresion_rec : expresion COMA lista_expresion_rec
                               | expresion'''
        pass

    # OBJETOS AJSON.
    def p_declaracion_objeto(self, p):
        '''declaracion_objeto : TYPE ID EQUAL def_ajson'''
        pass
    
    def p_def_ajson(self, p):
        '''def_ajson : LLAVEA propiedades LLAVEC'''
        pass
    
    # Puede ser que las propiedades de los objetos estén vacías

    def p_propiedades(self, p):
        '''propiedades : 
                       | ID COLON valor_propiedad propiedades_rec
                       | STRING COLON valor_propiedad propiedades_rec'''
        pass
        
    def p_propiedades_rec(self, p):
        '''propiedades_rec : COMA propiedades
                           | '''
        pass
    
    def p_valor_propiedad(self, p):
        '''valor_propiedad : tipo
                           | def_ajson'''
        pass

    def p_asignacion_objeto(self, p):
        '''asignacion_objeto : LET ID COLON ID EQUAL asg_ajson'''
        pass
    
    def p_asg_ajson(self, p):
        '''asg_ajson : LLAVEA propiedades_asg LLAVEC''' 
        pass
    
    def p_propiedades_asg(self, p):
        '''propiedades_asg :
                           | ID COLON valor_propiedad_asg propiedades_asg_rec
                           | STRING COLON valor_propiedad_asg propiedades_asg_rec'''
        pass
    
    def p_propiedades_asg_rec(self, p):
        '''propiedades_asg_rec : COMA propiedades_asg
                               | '''
        pass

    def p_valor_propiedad_asg(self, p):
        '''valor_propiedad_asg : expresion''' 
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