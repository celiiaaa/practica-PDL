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
        ('left', 'EQ', 'LT', 'GT', 'LE', 'GE'),
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

    # El programa está compuesto por sentencias acabadas en ; 
    # También puede ser funcion, condicion o bucle
    def p_programa(self, p):
        '''programa : sentencia SEMICOLON
                    | sentencia SEMICOLON programa
                    | funcion
                    | funcion programa
                    | condicion
                    | condicion programa
                    | bucle
                    | bucle programa'''
        pass
    
    # La sentencia puede ser declaracion, asignacion o una declaración – asignación
    def p_sentencia(self, p):
        '''sentencia : declaracion
                     | asignacion
                     | dec_obj
                     | asg_obj
                     | funcion_call'''
        pass

    # Declaración
    def p_declaracion(self, p):
        '''declaracion : LET id_list
                       | LET id_list EQUAL expresion'''
        pass

        if p[1] == "LET":
            var_name = p[2]
            if var_name in ParserClass.simbolos:
                # Ya está declarada, NO SE SI ESTO DEBE SER UN ERROR.
                print("Ya está declarada.")
            else:
                # Añadir la nueva variable a la tabla de simbolos
                ParserClass.simbolos[var_name] = [None, None]       # No tiene el tipo definido todavia


    # Los id recursivos
    def p_id_list(self, p):
        '''id_list : ID val_obj
                   | ID COLON ID COMA id_list
                   | ID val_obj COMA id_list'''
        pass
    
    # Asignación
    def p_asignacion(self, p):
        '''asignacion : id_list EQUAL operacion'''
        pass

    # Declaracion de un objeto
    def p_dec_obj(self, p):
        '''dec_obj : TYPE ID EQUAL obj_declaracion'''
        pass

    # Asignación de un objeto
    def p_asg_obj(self, p) :
        '''asg_obj : LET ID COLON ID EQUAL obj_asignacion'''
        pass

    # Declaración de un objeto
    def p_obj_declaracion(self, p):
        '''obj_declaracion : LLAVEA val_objdec LLAVEC'''
        pass

    # Valor de un objeto en la declaración
    def p_val_objdec(self, p):
        '''val_objdec : ID COLON tipo
                      | ID COLON tipo COMA val_objdec
                      | ID COLON obj_declaracion
                      | ID COLON obj_declaracion COMA val_objdec
                      | STRING COLON tipo
                      | STRING COLON tipo COMA val_objdec
                      | STRING COLON obj_declaracion
                      | STRING COLON obj_declaracion COMA val_objdec
                      | ID COLON ID
                      | ID COLON ID COMA val_objdec
                      | STRING COLON ID
                      | STRING COLON ID COMA val_objdec
                      | '''
        pass

    # Asignación de un objeto ajson
    def p_obj_asignacion(self, p):
        '''obj_asignacion : LLAVEA val_objasig LLAVEC'''
        pass

    # Valor de un objeto en la asignación
    def p_val_objasig(self, p):
        '''val_objasig : ID COLON operacion
                       | ID COLON operacion COMA val_objasig
                       | STRING COLON operacion
                       | STRING COLON operacion COMA val_objasig
                       | ID COLON obj_asignacion
                       | ID COLON obj_asignacion COMA val_objasig
                       | STRING COLON obj_asignacion
                       | STRING COLON obj_asignacion COMA val_objasig
                       | '''
        pass

    def p_tipo(self, p):
        '''tipo : INT
                | FLOAT
                | CHARACTER
                | BOOLEAN'''
        pass

    def p_expresion(self, p):
        '''expresion : binaria
                     | unaria
                     | ...
                     | obj_asignacion'''

    # Operación
    def p_operacion(self, p):
        '''operacion : binaria
                     | unaria
                     | valor
                     | PARENTHESISOPEN operacion PARENTHESISCLOSE''' 
        pass

    # Operación binaria
    def p_binaria(self, p):
        '''binaria : operacion PLUS operacion
                   | operacion MINUS operacion
                   | operacion TIMES operacion
                   | operacion DIV operacion
                   | operacion CONJUNCTION operacion
                   | operacion DISJUNCTION operacion
                   | operacion EQ operacion
                   | operacion LT operacion
                   | operacion GT operacion
                   | operacion LE operacion
                   | operacion GE operacion'''
        pass

    # Operaciones aritmeticas unitarias
    def p_unaria(self, p):
        '''unaria : PLUS numero %prec UPLUS
                 | MINUS numero %prec UMINUS
                 | PLUS ID %prec UPLUS
                 | MINUS ID %prec UMINUS'''
        pass

    # Valor
    def p_valor(self, p):
        '''valor : numero
                 | CHAR
                 | NEG operacion
                 | NULL
                 | funcion_call
                 | ID val_obj
                 | TR
                 | FL'''
        pass
    
    def p_val_obj(self, p):
        '''val_obj : DOT ID val_obj
                   | BRACKETOPEN STRING BRACKETCLOSE val_obj
                   | '''
        pass

    # Número
    def p_numero(self, p):
        '''numero : ENTERO
                  | REAL
                  | BIN
                  | OCT
                  | NCIENT
                  | HEX'''
        pass

    # Condición
    def p_condicion(self, p):
        '''condicion : IF PARENTHESISOPEN expresion PARENTHESISCLOSE LLAVEA axioma LLAVEC otra_condicion'''
        pass

    def p_otra_condicion(self, p):
        '''otra_condicion : 
                          | IF PARENTHESISOPEN expresion PARENTHESISCLOSE LLAVEA axioma LLAVEC ELSE LLAVEA axioma LLAVEC'''

    # Bucle
    def p_bucle(self, p):
        '''bucle : WHILE PARENTHESISOPEN expresion PARENTHESISCLOSE LLAVEA axioma LLAVEC'''
        pass

    # Tipo de las funciones
    def p_tipo_funcion(self, p):
        '''tipo_funcion : tipo
                        | ID'''
        pass
    
    # Función
    def p_funcion(self, p):
        '''funcion : FUNCTION ID PARENTHESISOPEN argumento PARENTHESISCLOSE COLON tipo_funcion LLAVEA axioma RETURN expresion SEMICOLON LLAVEC'''
        pass

    # Argumentos de las funciones
    def p_argumento(self, p):
        '''argumento : 
                     | ID COLON tipo_funcion mas_argumento'''
        pass

    def p_mas_argumento(self, p):
        '''mas_argumento :
                         | COMA ID COLON tipo_funcion mas_argumento'''

    # Llamada a función
    def p_funcion_call(self, p):
        '''funcion_call : ID PARENTHESISOPEN argumento_call PARENTHESISCLOSE'''
        pass

    # Argumentos de las llamadas a función
    def p_argumento_call(self, p):
        '''argumento_call : 
                          | expresion mas_argumento_call'''
        pass

    def p_mas_argumento_call(self, p):
        '''p_mas_argumento_call : 
                                | COMA expresion mas_argumento_call'''

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