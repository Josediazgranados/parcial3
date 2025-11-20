from antlr4 import *
from MatrixLangLexer import MatrixLangLexer
from MatrixLangParser import MatrixLangParser
from MatrixLangVisitor import MatrixLangVisitor

class EvalVisitor(MatrixLangVisitor):
    def visitProg(self, ctx):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx):
        m1 = self.visit(ctx.matrix(0))
        m2 = self.visit(ctx.matrix(1))

        # Verificación de dimensiones
        if len(m1[0]) != len(m2):
            raise Exception("Dimensiones incompatibles para producto punto")

        result = []

        # Producto punto entre matrices
        for i in range(len(m1)):
            fila_res = []
            for j in range(len(m2[0])):
                suma = 0
                for k in range(len(m2)):
                    suma += m1[i][k] * m2[k][j]
                fila_res.append(suma)
            result.append(fila_res)

        return result

    def visitMatrix(self, ctx):
        return [self.visit(r) for r in ctx.row()]

    def visitRow(self, ctx):
        return [int(n.getText()) for n in ctx.NUMBER()]

def main():
    input_stream = FileStream("matrices.txt")
    lexer = MatrixLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MatrixLangParser(stream)
    tree = parser.prog()

    visitor = EvalVisitor()
    result = visitor.visit(tree)
    print("Resultado:", result)

if __name__ == "__main__":
    main()
