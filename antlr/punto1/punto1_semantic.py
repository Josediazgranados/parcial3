# punto1_semantic.py
from Punto1SQLParser import Punto1SQLParser
from Punto1SQLVisitor import Punto1SQLVisitor

class SemanticVisitor(Punto1SQLVisitor):
    def __init__(self):
        self.env = {}       # table_name -> {col_name: type}
        self.errors = []

    def error(self, msg):
        self.errors.append(msg)

    # CREATE TABLE
    def visitCreateStmt(self, ctx:Punto1SQLParser.CreateStmtContext):
        table = ctx.ID().getText()
        if table in self.env:
            self.error(f"CREATE: la tabla '{table}' ya existe")
            return None
        schema = {}
        for col in ctx.colDef():
            name = col.ID().getText()
            type_ = col.type_().getText()
            schema[name] = type_
        self.env[table] = schema
        return None

    # INSERT INTO
    def visitInsertStmt(self, ctx:Punto1SQLParser.InsertStmtContext):
        table = ctx.ID().getText()
        if table not in self.env:
            self.error(f"INSERT: tabla '{table}' no existe")
            return None
        cols = [t.getText() for t in ctx.idList().ID()]
        vals = ctx.literalList().literal()
        if len(cols) != len(vals):
            self.error(f"INSERT: columnas ({len(cols)}) y valores ({len(vals)}) no coinciden en '{table}'")
            return None
        # verificar columnas existen
        for c in cols:
            if c not in self.env[table]:
                self.error(f"INSERT: columna '{c}' no existe en '{table}'")
        return None

    # SELECT
    def visitSelectStmt(self, ctx:Punto1SQLParser.SelectStmtContext):
        table = ctx.ID().getText()
        if table not in self.env:
            self.error(f"SELECT: tabla '{table}' no existe")
            return None
        if ctx.selectList().getText() != '*':
            if ctx.selectList().idList():
                for c in ctx.selectList().idList().ID():
                    name = c.getText()
                    if name not in self.env[table]:
                        self.error(f"SELECT: columna '{name}' no existe en '{table}'")
        if ctx.whereClause():
            self.visit(ctx.whereClause())
        return None

    # UPDATE
    def visitUpdateStmt(self, ctx:Punto1SQLParser.UpdateStmtContext):
        table = ctx.ID().getText()
        if table not in self.env:
            self.error(f"UPDATE: tabla '{table}' no existe")
            return None
        for a in ctx.assignList().assign():
            col = a.ID().getText()
            if col not in self.env[table]:
                self.error(f"UPDATE: columna '{col}' no existe en '{table}'")
        if ctx.whereClause():
            self.visit(ctx.whereClause())
        return None

    # DELETE
    def visitDeleteStmt(self, ctx:Punto1SQLParser.DeleteStmtContext):
        table = ctx.ID().getText()
        if table not in self.env:
            self.error(f"DELETE: tabla '{table}' no existe")
            return None
        if ctx.whereClause():
            self.visit(ctx.whereClause())
        return None

    # WHERE expr
    def visitEqExpr(self, ctx:Punto1SQLParser.EqExprContext):
        # formato: ID '=' literal
        col = ctx.ID().getText()
        # intentamos deducir la tabla: we cannot know table here -> caller should check column membership
        # Aquí solo no provoca error; SELECT/UPDATE already verificado columnas.
        return None

    def visitAndExpr(self, ctx:Punto1SQLParser.AndExprContext):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        return None

    def visitParenExpr(self, ctx:Punto1SQLParser.ParenExprContext):
        self.visit(ctx.expr())
        return None

