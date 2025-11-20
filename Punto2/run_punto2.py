import sys
from antlr4 import *
from MatrixLangLexer import MatrixLangLexer
from MatrixLangParser import MatrixLangParser
from punto2_eval import EvalVisitor

def main():
    if len(sys.argv) != 2:
        print("Uso: python run_punto2.py archivo.mlg")
        sys.exit(1)

    archivo = sys.argv[1]
    input_stream = FileStream(archivo)

    lexer = MatrixLangLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MatrixLangParser(tokens)

    tree = parser.program()
    visitor = EvalVisitor()
    visitor.visit(tree)


if __name__ == "__main__":
    main()

