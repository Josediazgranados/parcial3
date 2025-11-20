# Generated from MatrixLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,74,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,41,8,2,
        10,2,12,2,44,9,2,1,2,1,2,1,3,1,3,1,3,1,3,5,3,52,8,3,10,3,12,3,55,
        9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,67,8,5,1,6,1,6,1,
        6,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,0,72,0,17,1,0,0,0,2,31,1,0,
        0,0,4,33,1,0,0,0,6,47,1,0,0,0,8,58,1,0,0,0,10,66,1,0,0,0,12,68,1,
        0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,
        18,1,0,0,0,18,20,1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,0,0,
        0,22,23,3,4,2,0,23,24,5,1,0,0,24,32,1,0,0,0,25,26,3,8,4,0,26,27,
        5,1,0,0,27,32,1,0,0,0,28,29,3,12,6,0,29,30,5,1,0,0,30,32,1,0,0,0,
        31,22,1,0,0,0,31,25,1,0,0,0,31,28,1,0,0,0,32,3,1,0,0,0,33,34,5,2,
        0,0,34,35,5,11,0,0,35,36,5,3,0,0,36,37,5,4,0,0,37,42,3,6,3,0,38,
        39,5,5,0,0,39,41,3,6,3,0,40,38,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,
        0,42,43,1,0,0,0,43,45,1,0,0,0,44,42,1,0,0,0,45,46,5,6,0,0,46,5,1,
        0,0,0,47,48,5,4,0,0,48,53,5,12,0,0,49,50,5,5,0,0,50,52,5,12,0,0,
        51,49,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,1,
        0,0,0,55,53,1,0,0,0,56,57,5,6,0,0,57,7,1,0,0,0,58,59,5,11,0,0,59,
        60,5,3,0,0,60,61,3,10,5,0,61,9,1,0,0,0,62,63,5,11,0,0,63,64,5,7,
        0,0,64,67,5,11,0,0,65,67,5,11,0,0,66,62,1,0,0,0,66,65,1,0,0,0,67,
        11,1,0,0,0,68,69,5,8,0,0,69,70,5,9,0,0,70,71,5,11,0,0,71,72,5,10,
        0,0,72,13,1,0,0,0,5,17,31,42,53,66
    ]

class MatrixLangParser ( Parser ):

    grammarFileName = "MatrixLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'matrix'", "'='", "'['", "','", 
                     "']'", "'*'", "'print'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUMBER", 
                      "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_matrixDecl = 2
    RULE_row = 3
    RULE_assignStmt = 4
    RULE_expr = 5
    RULE_printStmt = 6

    ruleNames =  [ "program", "statement", "matrixDecl", "row", "assignStmt", 
                   "expr", "printStmt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    ID=11
    NUMBER=12
    WS=13
    COMMENT=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MatrixLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatrixLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MatrixLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MatrixLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MatrixLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2308) != 0):
                self.state = 14
                self.statement()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(MatrixLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MatrixLangParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StmtMatrixDeclContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatrixLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def matrixDecl(self):
            return self.getTypedRuleContext(MatrixLangParser.MatrixDeclContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtMatrixDecl" ):
                listener.enterStmtMatrixDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtMatrixDecl" ):
                listener.exitStmtMatrixDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtMatrixDecl" ):
                return visitor.visitStmtMatrixDecl(self)
            else:
                return visitor.visitChildren(self)


    class StmtPrintContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatrixLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def printStmt(self):
            return self.getTypedRuleContext(MatrixLangParser.PrintStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtPrint" ):
                listener.enterStmtPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtPrint" ):
                listener.exitStmtPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtPrint" ):
                return visitor.visitStmtPrint(self)
            else:
                return visitor.visitChildren(self)


    class StmtAssignContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatrixLangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignStmt(self):
            return self.getTypedRuleContext(MatrixLangParser.AssignStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtAssign" ):
                listener.enterStmtAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtAssign" ):
                listener.exitStmtAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtAssign" ):
                return visitor.visitStmtAssign(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = MatrixLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = MatrixLangParser.StmtMatrixDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.matrixDecl()
                self.state = 23
                self.match(MatrixLangParser.T__0)
                pass
            elif token in [11]:
                localctx = MatrixLangParser.StmtAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.assignStmt()
                self.state = 26
                self.match(MatrixLangParser.T__0)
                pass
            elif token in [8]:
                localctx = MatrixLangParser.StmtPrintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.printStmt()
                self.state = 29
                self.match(MatrixLangParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MatrixLangParser.ID, 0)

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatrixLangParser.RowContext)
            else:
                return self.getTypedRuleContext(MatrixLangParser.RowContext,i)


        def getRuleIndex(self):
            return MatrixLangParser.RULE_matrixDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixDecl" ):
                listener.enterMatrixDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixDecl" ):
                listener.exitMatrixDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixDecl" ):
                return visitor.visitMatrixDecl(self)
            else:
                return visitor.visitChildren(self)




    def matrixDecl(self):

        localctx = MatrixLangParser.MatrixDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_matrixDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(MatrixLangParser.T__1)
            self.state = 34
            self.match(MatrixLangParser.ID)
            self.state = 35
            self.match(MatrixLangParser.T__2)
            self.state = 36
            self.match(MatrixLangParser.T__3)
            self.state = 37
            self.row()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 38
                self.match(MatrixLangParser.T__4)
                self.state = 39
                self.row()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(MatrixLangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(MatrixLangParser.NUMBER)
            else:
                return self.getToken(MatrixLangParser.NUMBER, i)

        def getRuleIndex(self):
            return MatrixLangParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRow" ):
                return visitor.visitRow(self)
            else:
                return visitor.visitChildren(self)




    def row(self):

        localctx = MatrixLangParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(MatrixLangParser.T__3)
            self.state = 48
            self.match(MatrixLangParser.NUMBER)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 49
                self.match(MatrixLangParser.T__4)
                self.state = 50
                self.match(MatrixLangParser.NUMBER)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(MatrixLangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MatrixLangParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MatrixLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MatrixLangParser.RULE_assignStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = MatrixLangParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MatrixLangParser.ID)
            self.state = 59
            self.match(MatrixLangParser.T__2)
            self.state = 60
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MatrixLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprMatrixMulContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatrixLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MatrixLangParser.ID)
            else:
                return self.getToken(MatrixLangParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMatrixMul" ):
                listener.enterExprMatrixMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMatrixMul" ):
                listener.exitExprMatrixMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMatrixMul" ):
                return visitor.visitExprMatrixMul(self)
            else:
                return visitor.visitChildren(self)


    class ExprVarRefContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatrixLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MatrixLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprVarRef" ):
                listener.enterExprVarRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprVarRef" ):
                listener.exitExprVarRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprVarRef" ):
                return visitor.visitExprVarRef(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = MatrixLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = MatrixLangParser.ExprMatrixMulContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(MatrixLangParser.ID)
                self.state = 63
                self.match(MatrixLangParser.T__6)
                self.state = 64
                self.match(MatrixLangParser.ID)
                pass

            elif la_ == 2:
                localctx = MatrixLangParser.ExprVarRefContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(MatrixLangParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MatrixLangParser.ID, 0)

        def getRuleIndex(self):
            return MatrixLangParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = MatrixLangParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(MatrixLangParser.T__7)
            self.state = 69
            self.match(MatrixLangParser.T__8)
            self.state = 70
            self.match(MatrixLangParser.ID)
            self.state = 71
            self.match(MatrixLangParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





