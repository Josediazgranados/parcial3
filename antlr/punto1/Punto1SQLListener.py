# Generated from Punto1/Punto1SQL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Punto1SQLParser import Punto1SQLParser
else:
    from Punto1SQLParser import Punto1SQLParser

# This class defines a complete listener for a parse tree produced by Punto1SQLParser.
class Punto1SQLListener(ParseTreeListener):

    # Enter a parse tree produced by Punto1SQLParser#program.
    def enterProgram(self, ctx:Punto1SQLParser.ProgramContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#program.
    def exitProgram(self, ctx:Punto1SQLParser.ProgramContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#CreateStmtLine.
    def enterCreateStmtLine(self, ctx:Punto1SQLParser.CreateStmtLineContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#CreateStmtLine.
    def exitCreateStmtLine(self, ctx:Punto1SQLParser.CreateStmtLineContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#InsertStmtLine.
    def enterInsertStmtLine(self, ctx:Punto1SQLParser.InsertStmtLineContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#InsertStmtLine.
    def exitInsertStmtLine(self, ctx:Punto1SQLParser.InsertStmtLineContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#SelectStmtLine.
    def enterSelectStmtLine(self, ctx:Punto1SQLParser.SelectStmtLineContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#SelectStmtLine.
    def exitSelectStmtLine(self, ctx:Punto1SQLParser.SelectStmtLineContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#UpdateStmtLine.
    def enterUpdateStmtLine(self, ctx:Punto1SQLParser.UpdateStmtLineContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#UpdateStmtLine.
    def exitUpdateStmtLine(self, ctx:Punto1SQLParser.UpdateStmtLineContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#DeleteStmtLine.
    def enterDeleteStmtLine(self, ctx:Punto1SQLParser.DeleteStmtLineContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#DeleteStmtLine.
    def exitDeleteStmtLine(self, ctx:Punto1SQLParser.DeleteStmtLineContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#createStmt.
    def enterCreateStmt(self, ctx:Punto1SQLParser.CreateStmtContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#createStmt.
    def exitCreateStmt(self, ctx:Punto1SQLParser.CreateStmtContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#colDef.
    def enterColDef(self, ctx:Punto1SQLParser.ColDefContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#colDef.
    def exitColDef(self, ctx:Punto1SQLParser.ColDefContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#type.
    def enterType(self, ctx:Punto1SQLParser.TypeContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#type.
    def exitType(self, ctx:Punto1SQLParser.TypeContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#insertStmt.
    def enterInsertStmt(self, ctx:Punto1SQLParser.InsertStmtContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#insertStmt.
    def exitInsertStmt(self, ctx:Punto1SQLParser.InsertStmtContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#selectStmt.
    def enterSelectStmt(self, ctx:Punto1SQLParser.SelectStmtContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#selectStmt.
    def exitSelectStmt(self, ctx:Punto1SQLParser.SelectStmtContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#selectList.
    def enterSelectList(self, ctx:Punto1SQLParser.SelectListContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#selectList.
    def exitSelectList(self, ctx:Punto1SQLParser.SelectListContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#updateStmt.
    def enterUpdateStmt(self, ctx:Punto1SQLParser.UpdateStmtContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#updateStmt.
    def exitUpdateStmt(self, ctx:Punto1SQLParser.UpdateStmtContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#assignList.
    def enterAssignList(self, ctx:Punto1SQLParser.AssignListContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#assignList.
    def exitAssignList(self, ctx:Punto1SQLParser.AssignListContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#assign.
    def enterAssign(self, ctx:Punto1SQLParser.AssignContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#assign.
    def exitAssign(self, ctx:Punto1SQLParser.AssignContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#deleteStmt.
    def enterDeleteStmt(self, ctx:Punto1SQLParser.DeleteStmtContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#deleteStmt.
    def exitDeleteStmt(self, ctx:Punto1SQLParser.DeleteStmtContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#whereClause.
    def enterWhereClause(self, ctx:Punto1SQLParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#whereClause.
    def exitWhereClause(self, ctx:Punto1SQLParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#idList.
    def enterIdList(self, ctx:Punto1SQLParser.IdListContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#idList.
    def exitIdList(self, ctx:Punto1SQLParser.IdListContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#literalList.
    def enterLiteralList(self, ctx:Punto1SQLParser.LiteralListContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#literalList.
    def exitLiteralList(self, ctx:Punto1SQLParser.LiteralListContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#AndExpr.
    def enterAndExpr(self, ctx:Punto1SQLParser.AndExprContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#AndExpr.
    def exitAndExpr(self, ctx:Punto1SQLParser.AndExprContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#EqExpr.
    def enterEqExpr(self, ctx:Punto1SQLParser.EqExprContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#EqExpr.
    def exitEqExpr(self, ctx:Punto1SQLParser.EqExprContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#ParenExpr.
    def enterParenExpr(self, ctx:Punto1SQLParser.ParenExprContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#ParenExpr.
    def exitParenExpr(self, ctx:Punto1SQLParser.ParenExprContext):
        pass


    # Enter a parse tree produced by Punto1SQLParser#literal.
    def enterLiteral(self, ctx:Punto1SQLParser.LiteralContext):
        pass

    # Exit a parse tree produced by Punto1SQLParser#literal.
    def exitLiteral(self, ctx:Punto1SQLParser.LiteralContext):
        pass



del Punto1SQLParser