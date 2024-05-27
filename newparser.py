"""PARSER OTRO NUEVO INTENTOOO:((("""
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
        pass

    # Declaración
    def p_declaracion(self, p):
        '''declaracion : LET lista_id
                       | LET lista_id_mas EQUAL expresion'''
        pass

    # Lista de identificadores para la declaración
    def p_lista_id(self, p):
        '''lista_id : ID
                    | ID COMA lista_id
                    | ID COLON ID
                    | ID COLON ID COMA lista_id'''
        pass

    # Asignación
    def p_asignacion(self, p):
        '''asignacion : lista_id_mas EQUAL expresion'''
        pass

    # Lista de identificadores para la asignación
    def p_lista_id_mas(self, p):
        '''lista_id_mas : ID
                        | ID COMA lista_id_mas
                        | acceso_propiedad
                        | acceso_propiedad COMA lista_id_mas'''
        pass

    # Expresión
    def p_expresion(self, p):
        '''expresion : binaria
                     | unaria
                     | termino
                     | PARENTHESISOPEN expresion PARENTHESISCLOSE'''
        pass

    def p_binaria(self, p):
        '''binaria : expresion PLUS expresion
                   | expresion MINUS expresion
                   | expresion TIMES expresion
                   | expresion DIV expresion
                   | expresion EQ expresion
                   | expresion LT expresion
                   | expresion GT expresion
                   | expresion LE expresion
                   | expresion GE expresion
                   | expresion CONJUNCTION expresion
                   | expresion DISJUNCTION expresion'''
        pass

    def p_unaria(self, p):
        '''unaria : MINUS expresion %prec UMINUS
                  | PLUS expresion %prec UPLUS
                  | NEG expresion'''
        pass

    # Término
    def p_termino(self, p):
        '''termino : ID
                   | ENTERO
                   | BIN
                   | OCT
                   | HEX
                   | REAL
                   | NCIENT
                   | CHAR
                   | TR
                   | FL
                   | NULL
                   | acceso_obj
                   | funcion_call
                   | objeto_asg'''
        pass

    # Condición
    def p_condicion(self, p):
        '''condicion : IF PARENTHESISOPEN expresion PARENTHESISCLOSE bloque_llaves otra_condicion'''
        pass

    def p_otra_condicion(self, p):
        '''otra_condicion : ELSE bloque_llaves
                          | '''
        pass

    # Bucle
    def p_bucle(self, p):
        '''bucle : WHILE PARENTHESISOPEN expresion PARENTHESISCLOSE bloque_llaves'''
        pass

    # Bloque de llaves
    def p_bloque_llaves(self, p):
        '''bloque_llaves : LLAVEA bloque_programa LLAVEC'''
        pass

    # Tipos de las funciones
    def p_tipo(self, p):
        '''tipo : INT
                | FLOAT
                | CHARACTER
                | BOOLEAN
                | ID'''
        pass

    # Función
    def p_funcion(self, p):
        '''funcion : FUNCTION ID PARENTHESISOPEN lista_arg PARENTHESISCLOSE COLON tipo LLAVEA axioma RETURN expresion SEMICOLON LLAVEC'''
        pass

    # Lista de argumentos
    def p_lista_arg(self, p):
        '''lista_arg :
                     | lista_arg_rec'''
        pass

    def p_lista_arg_rec(self, p):
        '''lista_arg_rec : ID COLON tipo
                         | ID COLON tipo COMA lista_arg_rec'''
        pass

    # Llamada a una función
    def p_funcion_call(self, p):
        '''funcion_call : ID PARENTHESISOPEN lista_param PARENTHESISCLOSE'''
        pass

    # Lista de parámetros
    def p_lista_param(self, p):
        '''lista_param : 
                       | lista_param_rec'''
        pass

    def p_lista_param_rec(self, p):
        '''lista_param_rec : expresion
                           | expresion COMA lista_param_rec'''
        pass

    # ------------------- OBJETOS -------------------

    # Definición de un objeto
    def p_declaracion_objeto(self, p):
        '''declaracion_objeto : TYPE ID EQUAL objeto_dec'''
        pass

    def p_objeto_dec(self, p):
        '''objeto_dec : LLAVEA propiedades_dec LLAVEC'''        
        pass

    def p_propiedades_dec(self, p):
        '''propiedades_dec : 
                           | propiedad_dec
                           | propiedad_dec COMA propiedades_dec'''
        pass

    def p_propiedad_dec(self, p):
        '''propiedad_dec : ID COLON tipo
                         | STRING COLON tipo'''
        pass

    def p_propeidad_dec2(self, p):
        '''propiedad_dec : ID COLON objeto_dec
                         | STRING COLON objeto_dec'''
        pass

    # Asignación de un objeto
    def p_asignacion_objeto(self, p):
        '''asignacion_objeto : LET ID COLON ID EQUAL objeto_asg'''
        pass

    def p_objeto_asg(self, p):
        '''objeto_asg : LLAVEA propiedades_asg LLAVEC'''
        pass

    def p_propiedades_asg(self, p):
        '''propiedades_asg : 
                           | propiedad_asg
                           | propiedad_asg COMA propiedades_asg'''
        pass

    def p_propiedad_asg(self, p):
        '''propiedad_asg : ID COLON expresion
                         | STRING COLON expresion'''
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

    # ------------------- FIN -------------------

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


