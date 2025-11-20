# Generated from Punto1/Punto1SQL.g4 by ANTLR 4.13.1
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
        4,1,27,165,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,58,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,67,8,2,10,2,12,2,70,
        9,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,95,8,6,1,7,1,7,3,7,99,8,7,1,
        8,1,8,1,8,1,8,1,8,3,8,106,8,8,1,9,1,9,1,9,5,9,111,8,9,10,9,12,9,
        114,9,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,3,11,124,8,11,1,
        12,1,12,1,12,1,13,1,13,1,13,5,13,132,8,13,10,13,12,13,135,9,13,1,
        14,1,14,1,14,5,14,140,8,14,10,14,12,14,143,9,14,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,3,15,153,8,15,1,15,1,15,1,15,5,15,158,8,15,
        10,15,12,15,161,9,15,1,16,1,16,1,16,0,1,30,17,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,0,2,1,0,18,20,1,0,23,25,162,0,37,1,0,
        0,0,2,57,1,0,0,0,4,59,1,0,0,0,6,73,1,0,0,0,8,76,1,0,0,0,10,78,1,
        0,0,0,12,89,1,0,0,0,14,98,1,0,0,0,16,100,1,0,0,0,18,107,1,0,0,0,
        20,115,1,0,0,0,22,119,1,0,0,0,24,125,1,0,0,0,26,128,1,0,0,0,28,136,
        1,0,0,0,30,152,1,0,0,0,32,162,1,0,0,0,34,36,3,2,1,0,35,34,1,0,0,
        0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,
        1,0,0,0,40,41,5,0,0,1,41,1,1,0,0,0,42,43,3,4,2,0,43,44,5,1,0,0,44,
        58,1,0,0,0,45,46,3,10,5,0,46,47,5,1,0,0,47,58,1,0,0,0,48,49,3,12,
        6,0,49,50,5,1,0,0,50,58,1,0,0,0,51,52,3,16,8,0,52,53,5,1,0,0,53,
        58,1,0,0,0,54,55,3,22,11,0,55,56,5,1,0,0,56,58,1,0,0,0,57,42,1,0,
        0,0,57,45,1,0,0,0,57,48,1,0,0,0,57,51,1,0,0,0,57,54,1,0,0,0,58,3,
        1,0,0,0,59,60,5,7,0,0,60,61,5,8,0,0,61,62,5,22,0,0,62,63,5,2,0,0,
        63,68,3,6,3,0,64,65,5,3,0,0,65,67,3,6,3,0,66,64,1,0,0,0,67,70,1,
        0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,71,1,0,0,0,70,68,1,0,0,0,71,
        72,5,4,0,0,72,5,1,0,0,0,73,74,5,22,0,0,74,75,3,8,4,0,75,7,1,0,0,
        0,76,77,7,0,0,0,77,9,1,0,0,0,78,79,5,9,0,0,79,80,5,10,0,0,80,81,
        5,22,0,0,81,82,5,2,0,0,82,83,3,26,13,0,83,84,5,4,0,0,84,85,5,11,
        0,0,85,86,5,2,0,0,86,87,3,28,14,0,87,88,5,4,0,0,88,11,1,0,0,0,89,
        90,5,12,0,0,90,91,3,14,7,0,91,92,5,13,0,0,92,94,5,22,0,0,93,95,3,
        24,12,0,94,93,1,0,0,0,94,95,1,0,0,0,95,13,1,0,0,0,96,99,5,5,0,0,
        97,99,3,26,13,0,98,96,1,0,0,0,98,97,1,0,0,0,99,15,1,0,0,0,100,101,
        5,14,0,0,101,102,5,22,0,0,102,103,5,15,0,0,103,105,3,18,9,0,104,
        106,3,24,12,0,105,104,1,0,0,0,105,106,1,0,0,0,106,17,1,0,0,0,107,
        112,3,20,10,0,108,109,5,3,0,0,109,111,3,20,10,0,110,108,1,0,0,0,
        111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,19,1,0,0,0,114,
        112,1,0,0,0,115,116,5,22,0,0,116,117,5,6,0,0,117,118,3,32,16,0,118,
        21,1,0,0,0,119,120,5,16,0,0,120,121,5,13,0,0,121,123,5,22,0,0,122,
        124,3,24,12,0,123,122,1,0,0,0,123,124,1,0,0,0,124,23,1,0,0,0,125,
        126,5,17,0,0,126,127,3,30,15,0,127,25,1,0,0,0,128,133,5,22,0,0,129,
        130,5,3,0,0,130,132,5,22,0,0,131,129,1,0,0,0,132,135,1,0,0,0,133,
        131,1,0,0,0,133,134,1,0,0,0,134,27,1,0,0,0,135,133,1,0,0,0,136,141,
        3,32,16,0,137,138,5,3,0,0,138,140,3,32,16,0,139,137,1,0,0,0,140,
        143,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,29,1,0,0,0,143,141,
        1,0,0,0,144,145,6,15,-1,0,145,146,5,22,0,0,146,147,5,6,0,0,147,153,
        3,32,16,0,148,149,5,2,0,0,149,150,3,30,15,0,150,151,5,4,0,0,151,
        153,1,0,0,0,152,144,1,0,0,0,152,148,1,0,0,0,153,159,1,0,0,0,154,
        155,10,3,0,0,155,156,5,21,0,0,156,158,3,30,15,4,157,154,1,0,0,0,
        158,161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,31,1,0,0,0,161,
        159,1,0,0,0,162,163,7,1,0,0,163,33,1,0,0,0,12,37,57,68,94,98,105,
        112,123,133,141,152,159
    ]

class Punto1SQLParser ( Parser ):

    grammarFileName = "Punto1SQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "','", "')'", "'*'", "'='", 
                     "'CREATE'", "'TABLE'", "'INSERT'", "'INTO'", "'VALUES'", 
                     "'SELECT'", "'FROM'", "'UPDATE'", "'SET'", "'DELETE'", 
                     "'WHERE'", "'INT'", "'STRING'", "'BOOL'", "'AND'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "CREATE", "TABLE", 
                      "INSERT", "INTO", "VALUES", "SELECT", "FROM", "UPDATE", 
                      "SET", "DELETE", "WHERE", "INT", "STRING", "BOOL", 
                      "AND", "ID", "INTLIT", "STRINGLIT", "BOOLLIT", "WS", 
                      "COMMENT" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_createStmt = 2
    RULE_colDef = 3
    RULE_type = 4
    RULE_insertStmt = 5
    RULE_selectStmt = 6
    RULE_selectList = 7
    RULE_updateStmt = 8
    RULE_assignList = 9
    RULE_assign = 10
    RULE_deleteStmt = 11
    RULE_whereClause = 12
    RULE_idList = 13
    RULE_literalList = 14
    RULE_expr = 15
    RULE_literal = 16

    ruleNames =  [ "program", "stmt", "createStmt", "colDef", "type", "insertStmt", 
                   "selectStmt", "selectList", "updateStmt", "assignList", 
                   "assign", "deleteStmt", "whereClause", "idList", "literalList", 
                   "expr", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    CREATE=7
    TABLE=8
    INSERT=9
    INTO=10
    VALUES=11
    SELECT=12
    FROM=13
    UPDATE=14
    SET=15
    DELETE=16
    WHERE=17
    INT=18
    STRING=19
    BOOL=20
    AND=21
    ID=22
    INTLIT=23
    STRINGLIT=24
    BOOLLIT=25
    WS=26
    COMMENT=27

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
            return self.getToken(Punto1SQLParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Punto1SQLParser.StmtContext)
            else:
                return self.getTypedRuleContext(Punto1SQLParser.StmtContext,i)


        def getRuleIndex(self):
            return Punto1SQLParser.RULE_program

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

        localctx = Punto1SQLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 86656) != 0):
                self.state = 34
                self.stmt()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(Punto1SQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Punto1SQLParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InsertStmtLineContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Punto1SQLParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def insertStmt(self):
            return self.getTypedRuleContext(Punto1SQLParser.InsertStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsertStmtLine" ):
                listener.enterInsertStmtLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsertStmtLine" ):
                listener.exitInsertStmtLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsertStmtLine" ):
                return visitor.visitInsertStmtLine(self)
            else:
                return visitor.visitChildren(self)


    class UpdateStmtLineContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Punto1SQLParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def updateStmt(self):
            return self.getTypedRuleContext(Punto1SQLParser.UpdateStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdateStmtLine" ):
                listener.enterUpdateStmtLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdateStmtLine" ):
                listener.exitUpdateStmtLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdateStmtLine" ):
                return visitor.visitUpdateStmtLine(self)
            else:
                return visitor.visitChildren(self)


    class SelectStmtLineContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Punto1SQLParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def selectStmt(self):
            return self.getTypedRuleContext(Punto1SQLParser.SelectStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectStmtLine" ):
                listener.enterSelectStmtLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectStmtLine" ):
                listener.exitSelectStmtLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectStmtLine" ):
                return visitor.visitSelectStmtLine(self)
            else:
                return visitor.visitChildren(self)


    class CreateStmtLineContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Punto1SQLParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def createStmt(self):
            return self.getTypedRuleContext(Punto1SQLParser.CreateStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateStmtLine" ):
                listener.enterCreateStmtLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateStmtLine" ):
                listener.exitCreateStmtLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateStmtLine" ):
                return visitor.visitCreateStmtLine(self)
            else:
                return visitor.visitChildren(self)


    class DeleteStmtLineContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Punto1SQLParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def deleteStmt(self):
            return self.getTypedRuleContext(Punto1SQLParser.DeleteStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteStmtLine" ):
                listener.enterDeleteStmtLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteStmtLine" ):
                listener.exitDeleteStmtLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeleteStmtLine" ):
                return visitor.visitDeleteStmtLine(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = Punto1SQLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = Punto1SQLParser.CreateStmtLineContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.createStmt()
                self.state = 43
                self.match(Punto1SQLParser.T__0)
                pass
            elif token in [9]:
                localctx = Punto1SQLParser.InsertStmtLineContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.insertStmt()
                self.state = 46
                self.match(Punto1SQLParser.T__0)
                pass
            elif token in [12]:
                localctx = Punto1SQLParser.SelectStmtLineContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.selectStmt()
                self.state = 49
                self.match(Punto1SQLParser.T__0)
                pass
            elif token in [14]:
                localctx = Punto1SQLParser.UpdateStmtLineContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.updateStmt()
                self.state = 52
                self.match(Punto1SQLParser.T__0)
                pass
            elif token in [16]:
                localctx = Punto1SQLParser.DeleteStmtLineContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.deleteStmt()
                self.state = 55
                self.match(Punto1SQLParser.T__0)
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


    class CreateStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(Punto1SQLParser.CREATE, 0)

        def TABLE(self):
            return self.getToken(Punto1SQLParser.TABLE, 0)

        def ID(self):
            return self.getToken(Punto1SQLParser.ID, 0)

        def colDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Punto1SQLParser.ColDefContext)
            else:
                return self.getTypedRuleContext(Punto1SQLParser.ColDefContext,i)


        def getRuleIndex(self):
            return Punto1SQLParser.RULE_createStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateStmt" ):
                listener.enterCreateStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateStmt" ):
                listener.exitCreateStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateStmt" ):
                return visitor.visitCreateStmt(self)
            else:
                return visitor.visitChildren(self)




    def createStmt(self):

        localctx = Punto1SQLParser.CreateStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_createStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(Punto1SQLParser.CREATE)
            self.state = 60
            self.match(Punto1SQLParser.TABLE)
            self.state = 61
            self.match(Punto1SQLParser.ID)
            self.state = 62
            self.match(Punto1SQLParser.T__1)
            self.state = 63
            self.colDef()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 64
                self.match(Punto1SQLParser.T__2)
                self.state = 65
                self.colDef()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(Punto1SQLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Punto1SQLParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(Punto1SQLParser.TypeContext,0)


        def getRuleIndex(self):
            return Punto1SQLParser.RULE_colDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColDef" ):
                listener.enterColDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColDef" ):
                listener.exitColDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColDef" ):
                return visitor.visitColDef(self)
            else:
                return visitor.visitChildren(self)




    def colDef(self):

        localctx = Punto1SQLParser.ColDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_colDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(Punto1SQLParser.ID)
            self.state = 74
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(Punto1SQLParser.INT, 0)

        def STRING(self):
            return self.getToken(Punto1SQLParser.STRING, 0)

        def BOOL(self):
            return self.getToken(Punto1SQLParser.BOOL, 0)

        def getRuleIndex(self):
            return Punto1SQLParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = Punto1SQLParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsertStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSERT(self):
            return self.getToken(Punto1SQLParser.INSERT, 0)

        def INTO(self):
            return self.getToken(Punto1SQLParser.INTO, 0)

        def ID(self):
            return self.getToken(Punto1SQLParser.ID, 0)

        def idList(self):
            return self.getTypedRuleContext(Punto1SQLParser.IdListContext,0)


        def VALUES(self):
            return self.getToken(Punto1SQLParser.VALUES, 0)

        def literalList(self):
            return self.getTypedRuleContext(Punto1SQLParser.LiteralListContext,0)


        def getRuleIndex(self):
            return Punto1SQLParser.RULE_insertStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsertStmt" ):
                listener.enterInsertStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsertStmt" ):
                listener.exitInsertStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsertStmt" ):
                return visitor.visitInsertStmt(self)
            else:
                return visitor.visitChildren(self)




    def insertStmt(self):

        localctx = Punto1SQLParser.InsertStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_insertStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(Punto1SQLParser.INSERT)
            self.state = 79
            self.match(Punto1SQLParser.INTO)
            self.state = 80
            self.match(Punto1SQLParser.ID)
            self.state = 81
            self.match(Punto1SQLParser.T__1)
            self.state = 82
            self.idList()
            self.state = 83
            self.match(Punto1SQLParser.T__3)
            self.state = 84
            self.match(Punto1SQLParser.VALUES)
            self.state = 85
            self.match(Punto1SQLParser.T__1)
            self.state = 86
            self.literalList()
            self.state = 87
            self.match(Punto1SQLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(Punto1SQLParser.SELECT, 0)

        def selectList(self):
            return self.getTypedRuleContext(Punto1SQLParser.SelectListContext,0)


        def FROM(self):
            return self.getToken(Punto1SQLParser.FROM, 0)

        def ID(self):
            return self.getToken(Punto1SQLParser.ID, 0)

        def whereClause(self):
            return self.getTypedRuleContext(Punto1SQLParser.WhereClauseContext,0)


        def getRuleIndex(self):
            return Punto1SQLParser.RULE_selectStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectStmt" ):
                listener.enterSelectStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectStmt" ):
                listener.exitSelectStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectStmt" ):
                return visitor.visitSelectStmt(self)
            else:
                return visitor.visitChildren(self)




    def selectStmt(self):

        localctx = Punto1SQLParser.SelectStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_selectStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(Punto1SQLParser.SELECT)
            self.state = 90
            self.selectList()
            self.state = 91
            self.match(Punto1SQLParser.FROM)
            self.state = 92
            self.match(Punto1SQLParser.ID)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 93
                self.whereClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idList(self):
            return self.getTypedRuleContext(Punto1SQLParser.IdListContext,0)


        def getRuleIndex(self):
            return Punto1SQLParser.RULE_selectList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectList" ):
                listener.enterSelectList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectList" ):
                listener.exitSelectList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectList" ):
                return visitor.visitSelectList(self)
            else:
                return visitor.visitChildren(self)




    def selectList(self):

        localctx = Punto1SQLParser.SelectListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_selectList)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(Punto1SQLParser.T__4)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.idList()
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


    class UpdateStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPDATE(self):
            return self.getToken(Punto1SQLParser.UPDATE, 0)

        def ID(self):
            return self.getToken(Punto1SQLParser.ID, 0)

        def SET(self):
            return self.getToken(Punto1SQLParser.SET, 0)

        def assignList(self):
            return self.getTypedRuleContext(Punto1SQLParser.AssignListContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(Punto1SQLParser.WhereClauseContext,0)


        def getRuleIndex(self):
            return Punto1SQLParser.RULE_updateStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdateStmt" ):
                listener.enterUpdateStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdateStmt" ):
                listener.exitUpdateStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdateStmt" ):
                return visitor.visitUpdateStmt(self)
            else:
                return visitor.visitChildren(self)




    def updateStmt(self):

        localctx = Punto1SQLParser.UpdateStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_updateStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(Punto1SQLParser.UPDATE)
            self.state = 101
            self.match(Punto1SQLParser.ID)
            self.state = 102
            self.match(Punto1SQLParser.SET)
            self.state = 103
            self.assignList()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 104
                self.whereClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Punto1SQLParser.AssignContext)
            else:
                return self.getTypedRuleContext(Punto1SQLParser.AssignContext,i)


        def getRuleIndex(self):
            return Punto1SQLParser.RULE_assignList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignList" ):
                listener.enterAssignList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignList" ):
                listener.exitAssignList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignList" ):
                return visitor.visitAssignList(self)
            else:
                return visitor.visitChildren(self)




    def assignList(self):

        localctx = Punto1SQLParser.AssignListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.assign()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 108
                self.match(Punto1SQLParser.T__2)
                self.state = 109
                self.assign()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Punto1SQLParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(Punto1SQLParser.LiteralContext,0)


        def getRuleIndex(self):
            return Punto1SQLParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = Punto1SQLParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(Punto1SQLParser.ID)
            self.state = 116
            self.match(Punto1SQLParser.T__5)
            self.state = 117
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(Punto1SQLParser.DELETE, 0)

        def FROM(self):
            return self.getToken(Punto1SQLParser.FROM, 0)

        def ID(self):
            return self.getToken(Punto1SQLParser.ID, 0)

        def whereClause(self):
            return self.getTypedRuleContext(Punto1SQLParser.WhereClauseContext,0)


        def getRuleIndex(self):
            return Punto1SQLParser.RULE_deleteStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteStmt" ):
                listener.enterDeleteStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteStmt" ):
                listener.exitDeleteStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeleteStmt" ):
                return visitor.visitDeleteStmt(self)
            else:
                return visitor.visitChildren(self)




    def deleteStmt(self):

        localctx = Punto1SQLParser.DeleteStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_deleteStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(Punto1SQLParser.DELETE)
            self.state = 120
            self.match(Punto1SQLParser.FROM)
            self.state = 121
            self.match(Punto1SQLParser.ID)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 122
                self.whereClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(Punto1SQLParser.WHERE, 0)

        def expr(self):
            return self.getTypedRuleContext(Punto1SQLParser.ExprContext,0)


        def getRuleIndex(self):
            return Punto1SQLParser.RULE_whereClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereClause" ):
                listener.enterWhereClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereClause" ):
                listener.exitWhereClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhereClause" ):
                return visitor.visitWhereClause(self)
            else:
                return visitor.visitChildren(self)




    def whereClause(self):

        localctx = Punto1SQLParser.WhereClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_whereClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(Punto1SQLParser.WHERE)
            self.state = 126
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Punto1SQLParser.ID)
            else:
                return self.getToken(Punto1SQLParser.ID, i)

        def getRuleIndex(self):
            return Punto1SQLParser.RULE_idList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdList" ):
                listener.enterIdList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdList" ):
                listener.exitIdList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdList" ):
                return visitor.visitIdList(self)
            else:
                return visitor.visitChildren(self)




    def idList(self):

        localctx = Punto1SQLParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(Punto1SQLParser.ID)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 129
                self.match(Punto1SQLParser.T__2)
                self.state = 130
                self.match(Punto1SQLParser.ID)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Punto1SQLParser.LiteralContext)
            else:
                return self.getTypedRuleContext(Punto1SQLParser.LiteralContext,i)


        def getRuleIndex(self):
            return Punto1SQLParser.RULE_literalList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralList" ):
                listener.enterLiteralList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralList" ):
                listener.exitLiteralList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralList" ):
                return visitor.visitLiteralList(self)
            else:
                return visitor.visitChildren(self)




    def literalList(self):

        localctx = Punto1SQLParser.LiteralListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_literalList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.literal()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 137
                self.match(Punto1SQLParser.T__2)
                self.state = 138
                self.literal()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return Punto1SQLParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Punto1SQLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Punto1SQLParser.ExprContext)
            else:
                return self.getTypedRuleContext(Punto1SQLParser.ExprContext,i)

        def AND(self):
            return self.getToken(Punto1SQLParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Punto1SQLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(Punto1SQLParser.ID, 0)
        def literal(self):
            return self.getTypedRuleContext(Punto1SQLParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqExpr" ):
                listener.enterEqExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqExpr" ):
                listener.exitEqExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqExpr" ):
                return visitor.visitEqExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Punto1SQLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(Punto1SQLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Punto1SQLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = Punto1SQLParser.EqExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 145
                self.match(Punto1SQLParser.ID)
                self.state = 146
                self.match(Punto1SQLParser.T__5)
                self.state = 147
                self.literal()
                pass
            elif token in [2]:
                localctx = Punto1SQLParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 148
                self.match(Punto1SQLParser.T__1)
                self.state = 149
                self.expr(0)
                self.state = 150
                self.match(Punto1SQLParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 159
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Punto1SQLParser.AndExprContext(self, Punto1SQLParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 154
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 155
                    self.match(Punto1SQLParser.AND)
                    self.state = 156
                    self.expr(4) 
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(Punto1SQLParser.INTLIT, 0)

        def STRINGLIT(self):
            return self.getToken(Punto1SQLParser.STRINGLIT, 0)

        def BOOLLIT(self):
            return self.getToken(Punto1SQLParser.BOOLLIT, 0)

        def getRuleIndex(self):
            return Punto1SQLParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = Punto1SQLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




