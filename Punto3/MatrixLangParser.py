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
        4,1,6,38,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,2,1,2,1,2,1,2,5,2,20,8,2,10,2,12,2,23,9,2,1,2,1,2,1,3,1,3,
        1,3,1,3,5,3,31,8,3,10,3,12,3,34,9,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,
        0,35,0,8,1,0,0,0,2,11,1,0,0,0,4,15,1,0,0,0,6,26,1,0,0,0,8,9,3,2,
        1,0,9,10,5,0,0,1,10,1,1,0,0,0,11,12,3,4,2,0,12,13,5,1,0,0,13,14,
        3,4,2,0,14,3,1,0,0,0,15,16,5,2,0,0,16,21,3,6,3,0,17,18,5,3,0,0,18,
        20,3,6,3,0,19,17,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,
        0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,4,0,0,25,5,1,0,0,0,26,27,5,
        2,0,0,27,32,5,5,0,0,28,29,5,3,0,0,29,31,5,5,0,0,30,28,1,0,0,0,31,
        34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,32,1,0,0,
        0,35,36,5,4,0,0,36,7,1,0,0,0,2,21,32
    ]

class MatrixLangParser ( Parser ):

    grammarFileName = "MatrixLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'['", "','", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_matrix = 2
    RULE_row = 3

    ruleNames =  [ "prog", "expr", "matrix", "row" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NUMBER=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MatrixLangParser.ExprContext,0)


        def EOF(self):
            return self.getToken(MatrixLangParser.EOF, 0)

        def getRuleIndex(self):
            return MatrixLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MatrixLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr()
            self.state = 9
            self.match(MatrixLangParser.EOF)
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

        def matrix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatrixLangParser.MatrixContext)
            else:
                return self.getTypedRuleContext(MatrixLangParser.MatrixContext,i)


        def getRuleIndex(self):
            return MatrixLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MatrixLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.matrix()
            self.state = 12
            self.match(MatrixLangParser.T__0)
            self.state = 13
            self.matrix()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatrixLangParser.RowContext)
            else:
                return self.getTypedRuleContext(MatrixLangParser.RowContext,i)


        def getRuleIndex(self):
            return MatrixLangParser.RULE_matrix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrix" ):
                listener.enterMatrix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrix" ):
                listener.exitMatrix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrix" ):
                return visitor.visitMatrix(self)
            else:
                return visitor.visitChildren(self)




    def matrix(self):

        localctx = MatrixLangParser.MatrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_matrix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(MatrixLangParser.T__1)
            self.state = 16
            self.row()
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 17
                self.match(MatrixLangParser.T__2)
                self.state = 18
                self.row()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(MatrixLangParser.T__3)
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
            self.state = 26
            self.match(MatrixLangParser.T__1)
            self.state = 27
            self.match(MatrixLangParser.NUMBER)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 28
                self.match(MatrixLangParser.T__2)
                self.state = 29
                self.match(MatrixLangParser.NUMBER)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.match(MatrixLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





