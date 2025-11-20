from MatrixLangVisitor import MatrixLangVisitor
from MatrixLangParser import MatrixLangParser


class EvalVisitor(MatrixLangVisitor):

    def __init__(self):
        super().__init__()
        self.memory = {}   # almacena matrices y variables

    # ----------------------------
    #  PROGRAM
    # ----------------------------
    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    # ----------------------------
    #  STMT: DECLARACIÓN de MATRIZ
    # ----------------------------
    def visitStmtMatrixDecl(self, ctx: MatrixLangParser.StmtMatrixDeclContext):
        name = ctx.matrixDecl().ID().getText()
        rows = ctx.matrixDecl().row()

        matrix = []
        for r in rows:
            nums = [float(n.getText()) for n in r.NUMBER()]
            matrix.append(nums)

        self.memory[name] = matrix
        return matrix

    # ----------------------------
    #  STMT: ASIGNACIÓN
    # ----------------------------
    def visitStmtAssign(self, ctx: MatrixLangParser.StmtAssignContext):
        var = ctx.assignStmt().ID().getText()
        val = self.visit(ctx.assignStmt().expr())
        self.memory[var] = val
        return val

    # ----------------------------
    #  STMT: PRINT
    # ----------------------------
    def visitStmtPrint(self, ctx: MatrixLangParser.StmtPrintContext):
        var_name = ctx.printStmt().ID().getText()
        if var_name not in self.memory:
            raise Exception(f"Variable no definida: {var_name}")
        print(self.memory[var_name])
        return None

    # ----------------------------
    #  EXPR: VAR REF
    # ----------------------------
    def visitExprVarRef(self, ctx: MatrixLangParser.ExprVarRefContext):
        var = ctx.ID().getText()
        if var not in self.memory:
            raise Exception(f"Variable no definida: {var}")
        return self.memory[var]

    # ----------------------------
    #  EXPR: MATRIX MUL
    # ----------------------------
    def visitExprMatrixMul(self, ctx: MatrixLangParser.ExprMatrixMulContext):
        left = ctx.ID(0).getText()
        right = ctx.ID(1).getText()

        if left not in self.memory:
            raise Exception(f"Variable no definida: {left}")
        if right not in self.memory:
            raise Exception(f"Variable no definida: {right}")

        A = self.memory[left]
        B = self.memory[right]

        # Validar dimensiones
        if len(A[0]) != len(B):
            raise Exception("Dimensiones inválidas para producto punto")

        # Multiplicar matrices
        result = []
        for i in range(len(A)):
            fila = []
            for j in range(len(B[0])):
                suma = 0
                for k in range(len(B)):
                    suma += A[i][k] * B[k][j]
                fila.append(suma)
            result.append(fila)

        return result

