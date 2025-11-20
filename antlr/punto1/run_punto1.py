# run_punto1.py
import sys
from antlr4 import *
from Punto1SQLLexer import Punto1SQLLexer
from Punto1SQLParser import Punto1SQLParser
from punto1_semantic import SemanticVisitor

def run_file(path):
    data = open(path, 'r', encoding='utf-8').read()
    input_stream = InputStream(data)
    lexer = Punto1SQLLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = Punto1SQLParser(tokens)
    tree = parser.program()

    visitor = SemanticVisitor()
    visitor.visit(tree)

    if visitor.errors:
        print("Errores semánticos:")
        for e in visitor.errors:
            print(" -", e)
    else:
        print("Sin errores semánticos. Esquema resultante:")
        for t, s in visitor.env.items():
            print(f" - {t}: {s}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 run_punto1.py archivo.sql")
        sys.exit(1)
    run_file(sys.argv[1])
