# Generated from MatrixLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MatrixLangParser import MatrixLangParser
else:
    from MatrixLangParser import MatrixLangParser

# This class defines a complete listener for a parse tree produced by MatrixLangParser.
class MatrixLangListener(ParseTreeListener):

    # Enter a parse tree produced by MatrixLangParser#program.
    def enterProgram(self, ctx:MatrixLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MatrixLangParser#program.
    def exitProgram(self, ctx:MatrixLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MatrixLangParser#StmtMatrixDecl.
    def enterStmtMatrixDecl(self, ctx:MatrixLangParser.StmtMatrixDeclContext):
        pass

    # Exit a parse tree produced by MatrixLangParser#StmtMatrixDecl.
    def exitStmtMatrixDecl(self, ctx:MatrixLangParser.StmtMatrixDeclContext):
        pass


    # Enter a parse tree produced by MatrixLangParser#StmtAssign.
    def enterStmtAssign(self, ctx:MatrixLangParser.StmtAssignContext):
        pass

    # Exit a parse tree produced by MatrixLangParser#StmtAssign.
    def exitStmtAssign(self, ctx:MatrixLangParser.StmtAssignContext):
        pass


    # Enter a parse tree produced by MatrixLangParser#StmtPrint.
    def enterStmtPrint(self, ctx:MatrixLangParser.StmtPrintContext):
        pass

    # Exit a parse tree produced by MatrixLangParser#StmtPrint.
    def exitStmtPrint(self, ctx:MatrixLangParser.StmtPrintContext):
        pass


    # Enter a parse tree produced by MatrixLangParser#matrixDecl.
    def enterMatrixDecl(self, ctx:MatrixLangParser.MatrixDeclContext):
        pass

    # Exit a parse tree produced by MatrixLangParser#matrixDecl.
    def exitMatrixDecl(self, ctx:MatrixLangParser.MatrixDeclContext):
        pass


    # Enter a parse tree produced by MatrixLangParser#row.
    def enterRow(self, ctx:MatrixLangParser.RowContext):
        pass

    # Exit a parse tree produced by MatrixLangParser#row.
    def exitRow(self, ctx:MatrixLangParser.RowContext):
        pass


    # Enter a parse tree produced by MatrixLangParser#assignStmt.
    def enterAssignStmt(self, ctx:MatrixLangParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by MatrixLangParser#assignStmt.
    def exitAssignStmt(self, ctx:MatrixLangParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by MatrixLangParser#ExprMatrixMul.
    def enterExprMatrixMul(self, ctx:MatrixLangParser.ExprMatrixMulContext):
        pass

    # Exit a parse tree produced by MatrixLangParser#ExprMatrixMul.
    def exitExprMatrixMul(self, ctx:MatrixLangParser.ExprMatrixMulContext):
        pass


    # Enter a parse tree produced by MatrixLangParser#ExprVarRef.
    def enterExprVarRef(self, ctx:MatrixLangParser.ExprVarRefContext):
        pass

    # Exit a parse tree produced by MatrixLangParser#ExprVarRef.
    def exitExprVarRef(self, ctx:MatrixLangParser.ExprVarRefContext):
        pass


    # Enter a parse tree produced by MatrixLangParser#printStmt.
    def enterPrintStmt(self, ctx:MatrixLangParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by MatrixLangParser#printStmt.
    def exitPrintStmt(self, ctx:MatrixLangParser.PrintStmtContext):
        pass



del MatrixLangParser