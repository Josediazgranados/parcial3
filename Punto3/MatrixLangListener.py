# Generated from MatrixLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MatrixLangParser import MatrixLangParser
else:
    from MatrixLangParser import MatrixLangParser

# This class defines a complete listener for a parse tree produced by MatrixLangParser.
class MatrixLangListener(ParseTreeListener):

    # Enter a parse tree produced by MatrixLangParser#prog.
    def enterProg(self, ctx:MatrixLangParser.ProgContext):
        pass

    # Exit a parse tree produced by MatrixLangParser#prog.
    def exitProg(self, ctx:MatrixLangParser.ProgContext):
        pass


    # Enter a parse tree produced by MatrixLangParser#expr.
    def enterExpr(self, ctx:MatrixLangParser.ExprContext):
        pass

    # Exit a parse tree produced by MatrixLangParser#expr.
    def exitExpr(self, ctx:MatrixLangParser.ExprContext):
        pass


    # Enter a parse tree produced by MatrixLangParser#matrix.
    def enterMatrix(self, ctx:MatrixLangParser.MatrixContext):
        pass

    # Exit a parse tree produced by MatrixLangParser#matrix.
    def exitMatrix(self, ctx:MatrixLangParser.MatrixContext):
        pass


    # Enter a parse tree produced by MatrixLangParser#row.
    def enterRow(self, ctx:MatrixLangParser.RowContext):
        pass

    # Exit a parse tree produced by MatrixLangParser#row.
    def exitRow(self, ctx:MatrixLangParser.RowContext):
        pass



del MatrixLangParser