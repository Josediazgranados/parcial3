# Generated from Punto1/Punto1SQL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Punto1SQLParser import Punto1SQLParser
else:
    from Punto1SQLParser import Punto1SQLParser

# This class defines a complete generic visitor for a parse tree produced by Punto1SQLParser.

class Punto1SQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Punto1SQLParser#program.
    def visitProgram(self, ctx:Punto1SQLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#CreateStmtLine.
    def visitCreateStmtLine(self, ctx:Punto1SQLParser.CreateStmtLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#InsertStmtLine.
    def visitInsertStmtLine(self, ctx:Punto1SQLParser.InsertStmtLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#SelectStmtLine.
    def visitSelectStmtLine(self, ctx:Punto1SQLParser.SelectStmtLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#UpdateStmtLine.
    def visitUpdateStmtLine(self, ctx:Punto1SQLParser.UpdateStmtLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#DeleteStmtLine.
    def visitDeleteStmtLine(self, ctx:Punto1SQLParser.DeleteStmtLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#createStmt.
    def visitCreateStmt(self, ctx:Punto1SQLParser.CreateStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#colDef.
    def visitColDef(self, ctx:Punto1SQLParser.ColDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#type.
    def visitType(self, ctx:Punto1SQLParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#insertStmt.
    def visitInsertStmt(self, ctx:Punto1SQLParser.InsertStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#selectStmt.
    def visitSelectStmt(self, ctx:Punto1SQLParser.SelectStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#selectList.
    def visitSelectList(self, ctx:Punto1SQLParser.SelectListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#updateStmt.
    def visitUpdateStmt(self, ctx:Punto1SQLParser.UpdateStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#assignList.
    def visitAssignList(self, ctx:Punto1SQLParser.AssignListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#assign.
    def visitAssign(self, ctx:Punto1SQLParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#deleteStmt.
    def visitDeleteStmt(self, ctx:Punto1SQLParser.DeleteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#whereClause.
    def visitWhereClause(self, ctx:Punto1SQLParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#idList.
    def visitIdList(self, ctx:Punto1SQLParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#literalList.
    def visitLiteralList(self, ctx:Punto1SQLParser.LiteralListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#AndExpr.
    def visitAndExpr(self, ctx:Punto1SQLParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#EqExpr.
    def visitEqExpr(self, ctx:Punto1SQLParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#ParenExpr.
    def visitParenExpr(self, ctx:Punto1SQLParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Punto1SQLParser#literal.
    def visitLiteral(self, ctx:Punto1SQLParser.LiteralContext):
        return self.visitChildren(ctx)



del Punto1SQLParser