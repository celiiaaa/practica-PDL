import sys
import ply.lex as lex
from ply.lex import TOKEN 
import os


int_val = r'(0|[1-9][0-9]*)'
bin_val = r'(0b|0B)[01]+'
oct_val = r'0[0-7]+'
hex_val = r'(0x|0X)[0-9A-Fa-f]+'
float_val = r'((' + int_val + r')?\.[0-9]+)|((' + int_val + r')\.[0-9]*)'
ncient_val = r'(' + float_val + r'|' + int_val + r')(e|E){1}(-?' + int_val + r')'
char_val = r"\'[\x00-\xFF]\'"
identifier = r"[_a-zA-Z][_a-zA-Z0-9]*"
string_val = r'\"([^\\\n]|(\\.))*?\"'
nulo_val = r"null"

class LexerClass:
    
    reserved = (
        "TR",
        "FL",
        "LET", 
        "INT",
        "FLOAT",
        "CHARACTER",
        "WHILE",
        "BOOLEAN",
        "FUNCTION",
        "RETURN", 
        "TYPE",
        "IF",
        "ELSE",
        "NULL"
    )

    tokens = (
        "NCIENT",
        "BIN",
        "OCT",
        "HEX",
        "REAL",
        "ENTERO",
        "CHAR",
        "STRING",
        "EQ",
        "LT",
        "GT",
        "LE",
        "GE",
        "LLAVEA",
        "LLAVEC",
        "COMA",
        "NEG", 
        "CONJUNCTION",
        "DISJUNCTION",
        "PLUS",
        "MINUS",
        "TIMES",
        "DIV",
        "EQUAL",
        "ID", 
        "COLON",
        "SEMICOLON",
        "PARENTHESISOPEN",
        "PARENTHESISCLOSE",
        "BRACKETOPEN",
        "BRACKETCLOSE",
        "DOT"
    ) + reserved

    reserved_map = {}
    for r in reserved:
        reserved_map[r.lower()]= r
    
    def __init__(self):
        self.lexer = lex.lex(module = self)
        self.reserved_map = LexerClass.reserved_map
    
    t_ignore = " \t"
    t_EQ = r'=='
    t_LT = r'<'
    t_GT = r'>'
    t_LE = r'<='
    t_GE = r'>='
    t_LLAVEA = r'\{'
    t_LLAVEC = r'\}'
    t_COMA = r','
    t_DOT = r'\.'
    t_NEG = r'!'
    t_CONJUNCTION = r'&&'
    t_DISJUNCTION = r'\|\|'
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIV = r'/'
    t_EQUAL = r'='
    t_COLON = r':'
    t_SEMICOLON = r';'
    t_PARENTHESISOPEN = r'\('
    t_PARENTHESISCLOSE = r'\)'
    t_BRACKETOPEN = r'\['
    t_BRACKETCLOSE = r'\]'
    
    @TOKEN(ncient_val)
    def t_NCIENT(self, t):
        t.value = float(t.value)
        return t
    
    @TOKEN(bin_val)
    def t_BIN(self, t):
        t.value = int(t.value, 2)
        return t
    
    @TOKEN(oct_val)
    def t_OCT(self, t):
        t.value = int(t.value, 8)
        return t
    
    @TOKEN(hex_val)
    def t_HEX(self, t):
        t.value = int(t.value, 16)
        return t
    
    @TOKEN(float_val)
    def t_REAL(self, t):
        t.value = float(t.value) 
        """ if t.value[-1] == '.':
            t.value = float(t.value + '0')
        else:
            t.value = float(t.value)  """
        return t
    
    @TOKEN(int_val)
    def t_ENTERO(self, t):
        t.value = int(t.value)
        return t

    @TOKEN(string_val)
    def t_STRING(self, t):
        t.value = t.value[1:-1]
        return t
    
    @TOKEN(char_val)
    def t_CHAR(self, t):
        t.value = t.value[1]
        return t
    
    @TOKEN(nulo_val)
    def t_NULL(self, t):
        t.value = None
        return t 
    
    def t_TR(self, t):
        r"tr"
        t.value = True
        return t
    
    def t_FL(self, t):
        r"fl"
        t.value = False
        return t

    @TOKEN(identifier) 
    def t_ID(self, t):
        t.type = LexerClass.reserved_map.get(t.value, "ID")
        return t
    
    """ def t_UNICOMMENT(self, t):
        r'\/\/.*'
        t.value = t.value[2:].strip() # Elimina los caracteres // y elimina espacios en blanco al principio y al final
        pass
    
    def t_MULTICOMMENT(self, t):
        r'/\*(.|\n)*?\*/'
        t.value = t.value[2:-2].strip()  # Elimina los caracteres /* y */ y elimina espacios en blanco al principio y al final
        pass """

    def t_ignore_COMMENT(self, t):
        r'//.*|/\*(.|\n)*?\*/'
        t.lexer.lineno += t.value.count('\n')
        pass

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def find_column(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1
    
    def t_error(self, t):
        print(f"[Lexer Error] Illegal character {t.value[0]} at line {t.lineno} at position {self.find_column(t.lexer.lexdata, t)}")
        t.lexer.skip(len(t.value[0]))

    def test(self, data):
        self.lexer.input(data)
        """ for token in self.lexer:
            print(token.type, token.value) """
        output_tokens = []
        for token in self.lexer:
            output_tokens.append((token.type, token.value))
        return output_tokens
    
    def test_with_files(self, path):
        with open(path, 'r') as file:
            content = file.read()
            output_tokens = self.test(content)
            directory, filename = os.path.split(path)
            filename = os.path.splitext(filename)[0]
            output_filename = os.path.join(directory, filename + ".token")
            # Escribir la salida
            with open(output_filename, 'w') as output_file:
                for token_type, token_value in output_tokens:
                    output_file.write(f"{token_type} {token_value}\n")

if __name__ == "__main__":
    lexer = LexerClass()
    if len(sys.argv) > 1:
        lexer.test_with_files(sys.argv[1])