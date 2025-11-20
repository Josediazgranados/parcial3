# Generated from MatrixLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MatrixLangParser import MatrixLangParser
else:
    from MatrixLangParser import MatrixLangParser

# This class defines a complete generic visitor for a parse tree produced by MatrixLangParser.

class MatrixLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MatrixLangParser#prog.
    def visitProg(self, ctx:MatrixLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixLangParser#expr.
    def visitExpr(self, ctx:MatrixLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixLangParser#matrix.
    def visitMatrix(self, ctx:MatrixLangParser.MatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixLangParser#row.
    def visitRow(self, ctx:MatrixLangParser.RowContext):
        return self.visitChildren(ctx)



del MatrixLangParser