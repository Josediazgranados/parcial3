# Generated from MatrixLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MatrixLangParser import MatrixLangParser
else:
    from MatrixLangParser import MatrixLangParser

# This class defines a complete generic visitor for a parse tree produced by MatrixLangParser.

class MatrixLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MatrixLangParser#program.
    def visitProgram(self, ctx:MatrixLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixLangParser#StmtMatrixDecl.
    def visitStmtMatrixDecl(self, ctx:MatrixLangParser.StmtMatrixDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixLangParser#StmtAssign.
    def visitStmtAssign(self, ctx:MatrixLangParser.StmtAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixLangParser#StmtPrint.
    def visitStmtPrint(self, ctx:MatrixLangParser.StmtPrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixLangParser#matrixDecl.
    def visitMatrixDecl(self, ctx:MatrixLangParser.MatrixDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixLangParser#row.
    def visitRow(self, ctx:MatrixLangParser.RowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixLangParser#assignStmt.
    def visitAssignStmt(self, ctx:MatrixLangParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixLangParser#ExprMatrixMul.
    def visitExprMatrixMul(self, ctx:MatrixLangParser.ExprMatrixMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixLangParser#ExprVarRef.
    def visitExprVarRef(self, ctx:MatrixLangParser.ExprVarRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixLangParser#printStmt.
    def visitPrintStmt(self, ctx:MatrixLangParser.PrintStmtContext):
        return self.visitChildren(ctx)



del MatrixLangParser