import sys
from mylexer import LexerClass
from parsersin import ParserClass

def analisis_lexico(input_file):
    lexer = LexerClass()
    lexer.test_with_files(input_file)

def analisis_sintactico(input_file):
    parser = ParserClass()
    parser.test_with_files(input_file)

def main():
    
    if sys.argv[2] == "-lex":
        analisis_lexico(sys.argv[1])
    elif sys.argv[2] == "-par":
        analisis_sintactico(sys.argv[1])
    else:
        print("Opción no válida. Debe ser 'lex' o 'par'.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 ./PL_P2_MONIZ_PATRICIO/main.py {input_file} -{lex/par}")
        sys.exit(1)
    else:
        main()