# Generated from D:/pycharm/Parser/parser/SASParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys

from SASLexer import SASLexer

if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,271,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,5,0,67,
        8,0,10,0,12,0,70,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,3,3,88,8,3,1,4,1,4,1,4,1,4,3,4,94,8,4,1,4,1,
        4,1,5,1,5,5,5,100,8,5,10,5,12,5,103,9,5,1,5,3,5,106,8,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,
        3,9,126,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,
        11,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,3,13,149,8,
        13,1,13,1,13,1,14,1,14,1,14,5,14,156,8,14,10,14,12,14,159,9,14,1,
        15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,5,17,172,8,
        17,10,17,12,17,175,9,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,
        3,19,185,8,19,1,20,1,20,1,20,5,20,190,8,20,10,20,12,20,193,9,20,
        1,21,1,21,1,22,1,22,1,22,5,22,200,8,22,10,22,12,22,203,9,22,1,23,
        1,23,1,23,5,23,208,8,23,10,23,12,23,211,9,23,1,24,1,24,1,24,5,24,
        216,8,24,10,24,12,24,219,9,24,1,25,1,25,1,25,5,25,224,8,25,10,25,
        12,25,227,9,25,1,26,3,26,230,8,26,1,26,1,26,3,26,234,8,26,1,27,1,
        27,1,27,1,27,1,27,1,27,1,27,3,27,243,8,27,1,28,1,28,1,28,3,28,248,
        8,28,1,28,1,28,1,29,1,29,1,29,5,29,255,8,29,10,29,12,29,258,9,29,
        1,30,1,30,1,31,1,31,5,31,264,8,31,10,31,12,31,267,9,31,1,31,1,31,
        1,31,0,0,32,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,62,0,8,1,0,3,8,2,0,3,8,16,16,
        2,0,17,17,28,28,1,0,18,23,1,0,29,30,2,0,26,27,37,37,3,0,24,24,29,
        30,38,38,2,0,1,2,41,48,268,0,68,1,0,0,0,2,73,1,0,0,0,4,77,1,0,0,
        0,6,87,1,0,0,0,8,89,1,0,0,0,10,97,1,0,0,0,12,107,1,0,0,0,14,113,
        1,0,0,0,16,120,1,0,0,0,18,125,1,0,0,0,20,127,1,0,0,0,22,135,1,0,
        0,0,24,141,1,0,0,0,26,144,1,0,0,0,28,152,1,0,0,0,30,160,1,0,0,0,
        32,163,1,0,0,0,34,173,1,0,0,0,36,176,1,0,0,0,38,184,1,0,0,0,40,186,
        1,0,0,0,42,194,1,0,0,0,44,196,1,0,0,0,46,204,1,0,0,0,48,212,1,0,
        0,0,50,220,1,0,0,0,52,233,1,0,0,0,54,242,1,0,0,0,56,244,1,0,0,0,
        58,251,1,0,0,0,60,259,1,0,0,0,62,261,1,0,0,0,64,67,3,4,2,0,65,67,
        3,6,3,0,66,64,1,0,0,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,
        68,69,1,0,0,0,69,71,1,0,0,0,70,68,1,0,0,0,71,72,5,0,0,1,72,1,1,0,
        0,0,73,74,5,14,0,0,74,75,3,38,19,0,75,76,5,31,0,0,76,3,1,0,0,0,77,
        78,5,40,0,0,78,79,5,39,0,0,79,5,1,0,0,0,80,88,3,2,1,0,81,88,3,8,
        4,0,82,88,3,10,5,0,83,88,3,18,9,0,84,88,3,24,12,0,85,88,3,32,16,
        0,86,88,3,36,18,0,87,80,1,0,0,0,87,81,1,0,0,0,87,82,1,0,0,0,87,83,
        1,0,0,0,87,84,1,0,0,0,87,85,1,0,0,0,87,86,1,0,0,0,88,7,1,0,0,0,89,
        90,7,0,0,0,90,93,5,39,0,0,91,92,5,28,0,0,92,94,3,38,19,0,93,91,1,
        0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,95,96,5,31,0,0,96,9,1,0,0,0,97,
        101,3,12,6,0,98,100,3,14,7,0,99,98,1,0,0,0,100,103,1,0,0,0,101,99,
        1,0,0,0,101,102,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,104,106,
        3,16,8,0,105,104,1,0,0,0,105,106,1,0,0,0,106,11,1,0,0,0,107,108,
        5,9,0,0,108,109,5,33,0,0,109,110,3,38,19,0,110,111,5,34,0,0,111,
        112,3,62,31,0,112,13,1,0,0,0,113,114,5,10,0,0,114,115,5,9,0,0,115,
        116,5,33,0,0,116,117,3,38,19,0,117,118,5,34,0,0,118,119,3,62,31,
        0,119,15,1,0,0,0,120,121,5,10,0,0,121,122,3,62,31,0,122,17,1,0,0,
        0,123,126,3,20,10,0,124,126,3,22,11,0,125,123,1,0,0,0,125,124,1,
        0,0,0,126,19,1,0,0,0,127,128,5,12,0,0,128,129,5,33,0,0,129,130,3,
        36,18,0,130,131,3,36,18,0,131,132,3,38,19,0,132,133,5,34,0,0,133,
        134,3,62,31,0,134,21,1,0,0,0,135,136,5,13,0,0,136,137,5,33,0,0,137,
        138,3,38,19,0,138,139,5,34,0,0,139,140,3,62,31,0,140,23,1,0,0,0,
        141,142,3,26,13,0,142,143,3,62,31,0,143,25,1,0,0,0,144,145,7,1,0,
        0,145,146,5,39,0,0,146,148,5,33,0,0,147,149,3,28,14,0,148,147,1,
        0,0,0,148,149,1,0,0,0,149,150,1,0,0,0,150,151,5,34,0,0,151,27,1,
        0,0,0,152,157,3,30,15,0,153,154,5,32,0,0,154,156,3,30,15,0,155,153,
        1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,29,1,
        0,0,0,159,157,1,0,0,0,160,161,7,0,0,0,161,162,5,39,0,0,162,31,1,
        0,0,0,163,164,5,15,0,0,164,165,5,39,0,0,165,166,5,35,0,0,166,167,
        3,34,17,0,167,168,5,36,0,0,168,33,1,0,0,0,169,172,3,8,4,0,170,172,
        3,24,12,0,171,169,1,0,0,0,171,170,1,0,0,0,172,175,1,0,0,0,173,171,
        1,0,0,0,173,174,1,0,0,0,174,35,1,0,0,0,175,173,1,0,0,0,176,177,4,
        18,0,0,177,178,3,38,19,0,178,179,5,31,0,0,179,37,1,0,0,0,180,181,
        5,39,0,0,181,182,7,2,0,0,182,185,3,38,19,0,183,185,3,40,20,0,184,
        180,1,0,0,0,184,183,1,0,0,0,185,39,1,0,0,0,186,191,3,42,21,0,187,
        188,5,24,0,0,188,190,3,42,21,0,189,187,1,0,0,0,190,193,1,0,0,0,191,
        189,1,0,0,0,191,192,1,0,0,0,192,41,1,0,0,0,193,191,1,0,0,0,194,195,
        3,44,22,0,195,43,1,0,0,0,196,201,3,46,23,0,197,198,5,38,0,0,198,
        200,3,46,23,0,199,197,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,
        202,1,0,0,0,202,45,1,0,0,0,203,201,1,0,0,0,204,209,3,48,24,0,205,
        206,7,3,0,0,206,208,3,48,24,0,207,205,1,0,0,0,208,211,1,0,0,0,209,
        207,1,0,0,0,209,210,1,0,0,0,210,47,1,0,0,0,211,209,1,0,0,0,212,217,
        3,50,25,0,213,214,7,4,0,0,214,216,3,50,25,0,215,213,1,0,0,0,216,
        219,1,0,0,0,217,215,1,0,0,0,217,218,1,0,0,0,218,49,1,0,0,0,219,217,
        1,0,0,0,220,225,3,52,26,0,221,222,7,5,0,0,222,224,3,52,26,0,223,
        221,1,0,0,0,224,227,1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,
        51,1,0,0,0,227,225,1,0,0,0,228,230,7,6,0,0,229,228,1,0,0,0,229,230,
        1,0,0,0,230,231,1,0,0,0,231,234,3,54,27,0,232,234,3,54,27,0,233,
        229,1,0,0,0,233,232,1,0,0,0,234,53,1,0,0,0,235,236,5,33,0,0,236,
        237,3,38,19,0,237,238,5,34,0,0,238,243,1,0,0,0,239,243,3,56,28,0,
        240,243,5,39,0,0,241,243,3,60,30,0,242,235,1,0,0,0,242,239,1,0,0,
        0,242,240,1,0,0,0,242,241,1,0,0,0,243,55,1,0,0,0,244,245,5,39,0,
        0,245,247,5,33,0,0,246,248,3,58,29,0,247,246,1,0,0,0,247,248,1,0,
        0,0,248,249,1,0,0,0,249,250,5,34,0,0,250,57,1,0,0,0,251,256,3,38,
        19,0,252,253,5,32,0,0,253,255,3,38,19,0,254,252,1,0,0,0,255,258,
        1,0,0,0,256,254,1,0,0,0,256,257,1,0,0,0,257,59,1,0,0,0,258,256,1,
        0,0,0,259,260,7,7,0,0,260,61,1,0,0,0,261,265,5,35,0,0,262,264,3,
        6,3,0,263,262,1,0,0,0,264,267,1,0,0,0,265,263,1,0,0,0,265,266,1,
        0,0,0,266,268,1,0,0,0,267,265,1,0,0,0,268,269,5,36,0,0,269,63,1,
        0,0,0,23,66,68,87,93,101,105,125,148,157,171,173,184,191,201,209,
        217,225,229,233,242,247,256,265
    ]

class SASParser ( Parser ):

    grammarFileName = "SASParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'bool'", "'int'", 
                     "'float'", "'double'", "'char'", "'string'", "'if'", 
                     "'else'", "'else if'", "'for'", "'while'", "'return'", 
                     "'class'", "'void'", "<INVALID>", "'>'", "'<'", "'=='", 
                     "'!='", "'>='", "'<='", "<INVALID>", "<INVALID>", "'*'", 
                     "'/'", "'='", "'+'", "'-'", "';'", "','", "'('", "')'", 
                     "'{'", "'}'", "'%'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "BOOL", "INT", "FLOAT", 
                      "DOUBLE", "CHAR", "STRING", "IF", "ELSE", "ELSEIF", 
                      "FOR", "WHILE", "RETURN", "CLASS", "VOID", "ASSIGNMENT_OPERATOR", 
                      "GT", "LT", "EQ", "NEQ", "GEQ", "LEQ", "LOGICAL_OPERATOR", 
                      "MATHEMATICAL_OPERATOR", "MULT", "DIV", "ASSIGN", 
                      "PLUS", "MINUS", "SEMI", "COMMA", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "MOD", "BITWISE_OPERATOR", "IDENTIFIER", 
                      "PREPROCESSOR_DIRECTIVE", "OCTAL_LITERAL", "SCIENTIFIC_LITERAL", 
                      "FLOAT_LITERAL", "INTEGER_LITERAL", "STRING_LITERAL", 
                      "CHAR_LITERAL", "HEX_LITERAL", "BINARY_LITERAL", "BLOCK_COMMENT", 
                      "LINE_COMMENT", "WS" ]

    RULE_program = 0
    RULE_returnStatement = 1
    RULE_preprocessor = 2
    RULE_statement = 3
    RULE_varDecl = 4
    RULE_ifStatement = 5
    RULE_ifBlock = 6
    RULE_elseIfBlock = 7
    RULE_elseBlock = 8
    RULE_loopStatement = 9
    RULE_forLoop = 10
    RULE_whileLoop = 11
    RULE_funcDecl = 12
    RULE_funcHeader = 13
    RULE_paramList = 14
    RULE_param = 15
    RULE_classDecl = 16
    RULE_classBody = 17
    RULE_exprStatement = 18
    RULE_expr = 19
    RULE_logicOrExpr = 20
    RULE_logicAndExpr = 21
    RULE_bitwiseExpr = 22
    RULE_compareExpr = 23
    RULE_additiveExpr = 24
    RULE_multiplicativeExpr = 25
    RULE_unaryExpr = 26
    RULE_primary = 27
    RULE_funcCall = 28
    RULE_argList = 29
    RULE_literal = 30
    RULE_block = 31

    ruleNames =  [ "program", "returnStatement", "preprocessor", "statement", 
                   "varDecl", "ifStatement", "ifBlock", "elseIfBlock", "elseBlock", 
                   "loopStatement", "forLoop", "whileLoop", "funcDecl", 
                   "funcHeader", "paramList", "param", "classDecl", "classBody", 
                   "exprStatement", "expr", "logicOrExpr", "logicAndExpr", 
                   "bitwiseExpr", "compareExpr", "additiveExpr", "multiplicativeExpr", 
                   "unaryExpr", "primary", "funcCall", "argList", "literal", 
                   "block" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    BOOL=3
    INT=4
    FLOAT=5
    DOUBLE=6
    CHAR=7
    STRING=8
    IF=9
    ELSE=10
    ELSEIF=11
    FOR=12
    WHILE=13
    RETURN=14
    CLASS=15
    VOID=16
    ASSIGNMENT_OPERATOR=17
    GT=18
    LT=19
    EQ=20
    NEQ=21
    GEQ=22
    LEQ=23
    LOGICAL_OPERATOR=24
    MATHEMATICAL_OPERATOR=25
    MULT=26
    DIV=27
    ASSIGN=28
    PLUS=29
    MINUS=30
    SEMI=31
    COMMA=32
    LPAREN=33
    RPAREN=34
    LBRACE=35
    RBRACE=36
    MOD=37
    BITWISE_OPERATOR=38
    IDENTIFIER=39
    PREPROCESSOR_DIRECTIVE=40
    OCTAL_LITERAL=41
    SCIENTIFIC_LITERAL=42
    FLOAT_LITERAL=43
    INTEGER_LITERAL=44
    STRING_LITERAL=45
    CHAR_LITERAL=46
    HEX_LITERAL=47
    BINARY_LITERAL=48
    BLOCK_COMMENT=49
    LINE_COMMENT=50
    WS=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SASParser.EOF, 0)

        def preprocessor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SASParser.PreprocessorContext)
            else:
                return self.getTypedRuleContext(SASParser.PreprocessorContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SASParser.StatementContext)
            else:
                return self.getTypedRuleContext(SASParser.StatementContext,i)


        def getRuleIndex(self):
            return SASParser.RULE_program

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

        localctx = SASParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 66
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 64
                        self.preprocessor()
                        pass

                    elif la_ == 2:
                        self.state = 65
                        self.statement()
                        pass

             
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 71
            self.match(SASParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(SASParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(SASParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(SASParser.SEMI, 0)

        def getRuleIndex(self):
            return SASParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = SASParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(SASParser.RETURN)
            self.state = 74
            self.expr()
            self.state = 75
            self.match(SASParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreprocessorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREPROCESSOR_DIRECTIVE(self):
            return self.getToken(SASParser.PREPROCESSOR_DIRECTIVE, 0)

        def IDENTIFIER(self):
            return self.getToken(SASParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SASParser.RULE_preprocessor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessor" ):
                listener.enterPreprocessor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessor" ):
                listener.exitPreprocessor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessor" ):
                return visitor.visitPreprocessor(self)
            else:
                return visitor.visitChildren(self)




    def preprocessor(self):

        localctx = SASParser.PreprocessorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_preprocessor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(SASParser.PREPROCESSOR_DIRECTIVE)
            self.state = 78
            self.match(SASParser.IDENTIFIER)
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

        def returnStatement(self):
            return self.getTypedRuleContext(SASParser.ReturnStatementContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(SASParser.VarDeclContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(SASParser.IfStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(SASParser.LoopStatementContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(SASParser.FuncDeclContext,0)


        def classDecl(self):
            return self.getTypedRuleContext(SASParser.ClassDeclContext,0)


        def exprStatement(self):
            return self.getTypedRuleContext(SASParser.ExprStatementContext,0)


        def getRuleIndex(self):
            return SASParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SASParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.returnStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.varDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 83
                self.loopStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 84
                self.funcDecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 85
                self.classDecl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 86
                self.exprStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SASParser.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(SASParser.SEMI, 0)

        def INT(self):
            return self.getToken(SASParser.INT, 0)

        def FLOAT(self):
            return self.getToken(SASParser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(SASParser.DOUBLE, 0)

        def CHAR(self):
            return self.getToken(SASParser.CHAR, 0)

        def BOOL(self):
            return self.getToken(SASParser.BOOL, 0)

        def STRING(self):
            return self.getToken(SASParser.STRING, 0)

        def ASSIGN(self):
            return self.getToken(SASParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(SASParser.ExprContext,0)


        def getRuleIndex(self):
            return SASParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = SASParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 504) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 90
            self.match(SASParser.IDENTIFIER)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 91
                self.match(SASParser.ASSIGN)
                self.state = 92
                self.expr()


            self.state = 95
            self.match(SASParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifBlock(self):
            return self.getTypedRuleContext(SASParser.IfBlockContext,0)


        def elseIfBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SASParser.ElseIfBlockContext)
            else:
                return self.getTypedRuleContext(SASParser.ElseIfBlockContext,i)


        def elseBlock(self):
            return self.getTypedRuleContext(SASParser.ElseBlockContext,0)


        def getRuleIndex(self):
            return SASParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = SASParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.ifBlock()
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 98
                    self.elseIfBlock() 
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 104
                self.elseBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SASParser.IF, 0)

        def LPAREN(self):
            return self.getToken(SASParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(SASParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(SASParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(SASParser.BlockContext,0)


        def getRuleIndex(self):
            return SASParser.RULE_ifBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfBlock" ):
                listener.enterIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfBlock" ):
                listener.exitIfBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBlock" ):
                return visitor.visitIfBlock(self)
            else:
                return visitor.visitChildren(self)




    def ifBlock(self):

        localctx = SASParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(SASParser.IF)
            self.state = 108
            self.match(SASParser.LPAREN)
            self.state = 109
            self.expr()
            self.state = 110
            self.match(SASParser.RPAREN)
            self.state = 111
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(SASParser.ELSE, 0)

        def IF(self):
            return self.getToken(SASParser.IF, 0)

        def LPAREN(self):
            return self.getToken(SASParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(SASParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(SASParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(SASParser.BlockContext,0)


        def getRuleIndex(self):
            return SASParser.RULE_elseIfBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseIfBlock" ):
                listener.enterElseIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseIfBlock" ):
                listener.exitElseIfBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIfBlock" ):
                return visitor.visitElseIfBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseIfBlock(self):

        localctx = SASParser.ElseIfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elseIfBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(SASParser.ELSE)
            self.state = 114
            self.match(SASParser.IF)
            self.state = 115
            self.match(SASParser.LPAREN)
            self.state = 116
            self.expr()
            self.state = 117
            self.match(SASParser.RPAREN)
            self.state = 118
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(SASParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(SASParser.BlockContext,0)


        def getRuleIndex(self):
            return SASParser.RULE_elseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseBlock" ):
                listener.enterElseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseBlock" ):
                listener.exitElseBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseBlock" ):
                return visitor.visitElseBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseBlock(self):

        localctx = SASParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_elseBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(SASParser.ELSE)
            self.state = 121
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forLoop(self):
            return self.getTypedRuleContext(SASParser.ForLoopContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(SASParser.WhileLoopContext,0)


        def getRuleIndex(self):
            return SASParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = SASParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_loopStatement)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.forLoop()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.whileLoop()
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


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(SASParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(SASParser.LPAREN, 0)

        def exprStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SASParser.ExprStatementContext)
            else:
                return self.getTypedRuleContext(SASParser.ExprStatementContext,i)


        def expr(self):
            return self.getTypedRuleContext(SASParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(SASParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(SASParser.BlockContext,0)


        def getRuleIndex(self):
            return SASParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = SASParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(SASParser.FOR)
            self.state = 128
            self.match(SASParser.LPAREN)
            self.state = 129
            self.exprStatement()
            self.state = 130
            self.exprStatement()
            self.state = 131
            self.expr()
            self.state = 132
            self.match(SASParser.RPAREN)
            self.state = 133
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(SASParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(SASParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(SASParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(SASParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(SASParser.BlockContext,0)


        def getRuleIndex(self):
            return SASParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)




    def whileLoop(self):

        localctx = SASParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(SASParser.WHILE)
            self.state = 136
            self.match(SASParser.LPAREN)
            self.state = 137
            self.expr()
            self.state = 138
            self.match(SASParser.RPAREN)
            self.state = 139
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcHeader(self):
            return self.getTypedRuleContext(SASParser.FuncHeaderContext,0)


        def block(self):
            return self.getTypedRuleContext(SASParser.BlockContext,0)


        def getRuleIndex(self):
            return SASParser.RULE_funcDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDecl" ):
                listener.enterFuncDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDecl" ):
                listener.exitFuncDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = SASParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_funcDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.funcHeader()
            self.state = 142
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncHeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SASParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(SASParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SASParser.RPAREN, 0)

        def INT(self):
            return self.getToken(SASParser.INT, 0)

        def FLOAT(self):
            return self.getToken(SASParser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(SASParser.DOUBLE, 0)

        def CHAR(self):
            return self.getToken(SASParser.CHAR, 0)

        def BOOL(self):
            return self.getToken(SASParser.BOOL, 0)

        def STRING(self):
            return self.getToken(SASParser.STRING, 0)

        def VOID(self):
            return self.getToken(SASParser.VOID, 0)

        def paramList(self):
            return self.getTypedRuleContext(SASParser.ParamListContext,0)


        def getRuleIndex(self):
            return SASParser.RULE_funcHeader

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncHeader" ):
                listener.enterFuncHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncHeader" ):
                listener.exitFuncHeader(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncHeader" ):
                return visitor.visitFuncHeader(self)
            else:
                return visitor.visitChildren(self)




    def funcHeader(self):

        localctx = SASParser.FuncHeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_funcHeader)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66040) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 145
            self.match(SASParser.IDENTIFIER)
            self.state = 146
            self.match(SASParser.LPAREN)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 504) != 0):
                self.state = 147
                self.paramList()


            self.state = 150
            self.match(SASParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SASParser.ParamContext)
            else:
                return self.getTypedRuleContext(SASParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SASParser.COMMA)
            else:
                return self.getToken(SASParser.COMMA, i)

        def getRuleIndex(self):
            return SASParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = SASParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.param()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 153
                self.match(SASParser.COMMA)
                self.state = 154
                self.param()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SASParser.IDENTIFIER, 0)

        def INT(self):
            return self.getToken(SASParser.INT, 0)

        def FLOAT(self):
            return self.getToken(SASParser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(SASParser.DOUBLE, 0)

        def CHAR(self):
            return self.getToken(SASParser.CHAR, 0)

        def BOOL(self):
            return self.getToken(SASParser.BOOL, 0)

        def STRING(self):
            return self.getToken(SASParser.STRING, 0)

        def getRuleIndex(self):
            return SASParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = SASParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 504) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 161
            self.match(SASParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(SASParser.CLASS, 0)

        def IDENTIFIER(self):
            return self.getToken(SASParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(SASParser.LBRACE, 0)

        def classBody(self):
            return self.getTypedRuleContext(SASParser.ClassBodyContext,0)


        def RBRACE(self):
            return self.getToken(SASParser.RBRACE, 0)

        def getRuleIndex(self):
            return SASParser.RULE_classDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDecl" ):
                listener.enterClassDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDecl" ):
                listener.exitClassDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = SASParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_classDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(SASParser.CLASS)
            self.state = 164
            self.match(SASParser.IDENTIFIER)
            self.state = 165
            self.match(SASParser.LBRACE)
            self.state = 166
            self.classBody()
            self.state = 167
            self.match(SASParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SASParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(SASParser.VarDeclContext,i)


        def funcDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SASParser.FuncDeclContext)
            else:
                return self.getTypedRuleContext(SASParser.FuncDeclContext,i)


        def getRuleIndex(self):
            return SASParser.RULE_classBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBody" ):
                listener.enterClassBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBody" ):
                listener.exitClassBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBody" ):
                return visitor.visitClassBody(self)
            else:
                return visitor.visitChildren(self)




    def classBody(self):

        localctx = SASParser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 66040) != 0):
                self.state = 171
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 169
                    self.varDecl()
                    pass

                elif la_ == 2:
                    self.state = 170
                    self.funcDecl()
                    pass


                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SASParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(SASParser.SEMI, 0)

        def getRuleIndex(self):
            return SASParser.RULE_exprStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStatement" ):
                listener.enterExprStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStatement" ):
                listener.exitExprStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStatement" ):
                return visitor.visitExprStatement(self)
            else:
                return visitor.visitChildren(self)




    def exprStatement(self):

        localctx = SASParser.ExprStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exprStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            if not  self._input.LA(1) != SASLexer.RETURN :
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, " self._input.LA(1) != SASLexer.RETURN ")
            self.state = 177
            self.expr()
            self.state = 178
            self.match(SASParser.SEMI)
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
            return SASParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LogicOrPassContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logicOrExpr(self):
            return self.getTypedRuleContext(SASParser.LogicOrExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicOrPass" ):
                listener.enterLogicOrPass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicOrPass" ):
                listener.exitLogicOrPass(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOrPass" ):
                return visitor.visitLogicOrPass(self)
            else:
                return visitor.visitChildren(self)


    class AssignExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(SASParser.IDENTIFIER, 0)
        def expr(self):
            return self.getTypedRuleContext(SASParser.ExprContext,0)

        def ASSIGN(self):
            return self.getToken(SASParser.ASSIGN, 0)
        def ASSIGNMENT_OPERATOR(self):
            return self.getToken(SASParser.ASSIGNMENT_OPERATOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpr" ):
                listener.enterAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpr" ):
                listener.exitAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = SASParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = SASParser.AssignExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(SASParser.IDENTIFIER)
                self.state = 181
                _la = self._input.LA(1)
                if not(_la==17 or _la==28):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 182
                self.expr()
                pass

            elif la_ == 2:
                localctx = SASParser.LogicOrPassContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.logicOrExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicOrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SASParser.RULE_logicOrExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LogicalExprContext(LogicOrExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.LogicOrExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def logicAndExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SASParser.LogicAndExprContext)
            else:
                return self.getTypedRuleContext(SASParser.LogicAndExprContext,i)

        def LOGICAL_OPERATOR(self, i:int=None):
            if i is None:
                return self.getTokens(SASParser.LOGICAL_OPERATOR)
            else:
                return self.getToken(SASParser.LOGICAL_OPERATOR, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpr" ):
                listener.enterLogicalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpr" ):
                listener.exitLogicalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpr" ):
                return visitor.visitLogicalExpr(self)
            else:
                return visitor.visitChildren(self)



    def logicOrExpr(self):

        localctx = SASParser.LogicOrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_logicOrExpr)
        self._la = 0 # Token type
        try:
            localctx = SASParser.LogicalExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.logicAndExpr()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 187
                self.match(SASParser.LOGICAL_OPERATOR)
                self.state = 188
                self.logicAndExpr()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicAndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SASParser.RULE_logicAndExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BitwisePassContext(LogicAndExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.LogicAndExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bitwiseExpr(self):
            return self.getTypedRuleContext(SASParser.BitwiseExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitwisePass" ):
                listener.enterBitwisePass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitwisePass" ):
                listener.exitBitwisePass(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitwisePass" ):
                return visitor.visitBitwisePass(self)
            else:
                return visitor.visitChildren(self)



    def logicAndExpr(self):

        localctx = SASParser.LogicAndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_logicAndExpr)
        try:
            localctx = SASParser.BitwisePassContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.bitwiseExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BitwiseExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compareExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SASParser.CompareExprContext)
            else:
                return self.getTypedRuleContext(SASParser.CompareExprContext,i)


        def BITWISE_OPERATOR(self, i:int=None):
            if i is None:
                return self.getTokens(SASParser.BITWISE_OPERATOR)
            else:
                return self.getToken(SASParser.BITWISE_OPERATOR, i)

        def getRuleIndex(self):
            return SASParser.RULE_bitwiseExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitwiseExpr" ):
                listener.enterBitwiseExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitwiseExpr" ):
                listener.exitBitwiseExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitwiseExpr" ):
                return visitor.visitBitwiseExpr(self)
            else:
                return visitor.visitChildren(self)




    def bitwiseExpr(self):

        localctx = SASParser.BitwiseExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_bitwiseExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.compareExpr()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 197
                self.match(SASParser.BITWISE_OPERATOR)
                self.state = 198
                self.compareExpr()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SASParser.AdditiveExprContext)
            else:
                return self.getTypedRuleContext(SASParser.AdditiveExprContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(SASParser.EQ)
            else:
                return self.getToken(SASParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(SASParser.NEQ)
            else:
                return self.getToken(SASParser.NEQ, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(SASParser.GT)
            else:
                return self.getToken(SASParser.GT, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(SASParser.LT)
            else:
                return self.getToken(SASParser.LT, i)

        def GEQ(self, i:int=None):
            if i is None:
                return self.getTokens(SASParser.GEQ)
            else:
                return self.getToken(SASParser.GEQ, i)

        def LEQ(self, i:int=None):
            if i is None:
                return self.getTokens(SASParser.LEQ)
            else:
                return self.getToken(SASParser.LEQ, i)

        def getRuleIndex(self):
            return SASParser.RULE_compareExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompareExpr" ):
                listener.enterCompareExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareExpr" ):
                listener.exitCompareExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareExpr" ):
                return visitor.visitCompareExpr(self)
            else:
                return visitor.visitChildren(self)




    def compareExpr(self):

        localctx = SASParser.CompareExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_compareExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.additiveExpr()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0):
                self.state = 205
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 206
                self.additiveExpr()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SASParser.RULE_additiveExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddSubContext(AdditiveExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.AdditiveExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def multiplicativeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SASParser.MultiplicativeExprContext)
            else:
                return self.getTypedRuleContext(SASParser.MultiplicativeExprContext,i)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(SASParser.PLUS)
            else:
                return self.getToken(SASParser.PLUS, i)
        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(SASParser.MINUS)
            else:
                return self.getToken(SASParser.MINUS, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)



    def additiveExpr(self):

        localctx = SASParser.AdditiveExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            localctx = SASParser.AddSubContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.multiplicativeExpr()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29 or _la==30:
                self.state = 213
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 214
                self.multiplicativeExpr()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SASParser.RULE_multiplicativeExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MulDivModContext(MultiplicativeExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.MultiplicativeExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SASParser.UnaryExprContext)
            else:
                return self.getTypedRuleContext(SASParser.UnaryExprContext,i)

        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(SASParser.MULT)
            else:
                return self.getToken(SASParser.MULT, i)
        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(SASParser.DIV)
            else:
                return self.getToken(SASParser.DIV, i)
        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(SASParser.MOD)
            else:
                return self.getToken(SASParser.MOD, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivMod" ):
                listener.enterMulDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivMod" ):
                listener.exitMulDivMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivMod" ):
                return visitor.visitMulDivMod(self)
            else:
                return visitor.visitChildren(self)



    def multiplicativeExpr(self):

        localctx = SASParser.MultiplicativeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            localctx = SASParser.MulDivModContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.unaryExpr()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137640280064) != 0):
                self.state = 221
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 137640280064) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 222
                self.unaryExpr()
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SASParser.RULE_unaryExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class UnaryOpExprContext(UnaryExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.UnaryExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(SASParser.PrimaryContext,0)

        def PLUS(self):
            return self.getToken(SASParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(SASParser.MINUS, 0)
        def LOGICAL_OPERATOR(self):
            return self.getToken(SASParser.LOGICAL_OPERATOR, 0)
        def BITWISE_OPERATOR(self):
            return self.getToken(SASParser.BITWISE_OPERATOR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOpExpr" ):
                listener.enterUnaryOpExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOpExpr" ):
                listener.exitUnaryOpExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOpExpr" ):
                return visitor.visitUnaryOpExpr(self)
            else:
                return visitor.visitChildren(self)


    class NoUnaryContext(UnaryExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.UnaryExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(SASParser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoUnary" ):
                listener.enterNoUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoUnary" ):
                listener.exitNoUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoUnary" ):
                return visitor.visitNoUnary(self)
            else:
                return visitor.visitChildren(self)



    def unaryExpr(self):

        localctx = SASParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = SASParser.UnaryOpExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 276505296896) != 0):
                    self.state = 228
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 276505296896) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 231
                self.primary()
                pass

            elif la_ == 2:
                localctx = SASParser.NoUnaryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SASParser.RULE_primary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LiteralExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(SASParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpr" ):
                listener.enterLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpr" ):
                listener.exitLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralExpr" ):
                return visitor.visitLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcCall(self):
            return self.getTypedRuleContext(SASParser.FuncCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCallExpr" ):
                listener.enterFuncCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCallExpr" ):
                listener.exitFuncCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallExpr" ):
                return visitor.visitFuncCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(SASParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(SASParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(SASParser.RPAREN, 0)

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


    class IdExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(SASParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)



    def primary(self):

        localctx = SASParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_primary)
        try:
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                localctx = SASParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(SASParser.LPAREN)
                self.state = 236
                self.expr()
                self.state = 237
                self.match(SASParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = SASParser.FuncCallExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.funcCall()
                pass

            elif la_ == 3:
                localctx = SASParser.IdExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.match(SASParser.IDENTIFIER)
                pass

            elif la_ == 4:
                localctx = SASParser.LiteralExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 241
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SASParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(SASParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SASParser.RPAREN, 0)

        def argList(self):
            return self.getTypedRuleContext(SASParser.ArgListContext,0)


        def getRuleIndex(self):
            return SASParser.RULE_funcCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = SASParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(SASParser.IDENTIFIER)
            self.state = 245
            self.match(SASParser.LPAREN)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 561585781211142) != 0):
                self.state = 246
                self.argList()


            self.state = 249
            self.match(SASParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SASParser.ExprContext)
            else:
                return self.getTypedRuleContext(SASParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SASParser.COMMA)
            else:
                return self.getToken(SASParser.COMMA, i)

        def getRuleIndex(self):
            return SASParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = SASParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.expr()
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 252
                self.match(SASParser.COMMA)
                self.state = 253
                self.expr()
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(SASParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(SASParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(SASParser.STRING_LITERAL, 0)

        def CHAR_LITERAL(self):
            return self.getToken(SASParser.CHAR_LITERAL, 0)

        def HEX_LITERAL(self):
            return self.getToken(SASParser.HEX_LITERAL, 0)

        def BINARY_LITERAL(self):
            return self.getToken(SASParser.BINARY_LITERAL, 0)

        def OCTAL_LITERAL(self):
            return self.getToken(SASParser.OCTAL_LITERAL, 0)

        def SCIENTIFIC_LITERAL(self):
            return self.getToken(SASParser.SCIENTIFIC_LITERAL, 0)

        def TRUE(self):
            return self.getToken(SASParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SASParser.FALSE, 0)

        def getRuleIndex(self):
            return SASParser.RULE_literal

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

        localctx = SASParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 560750930165766) != 0)):
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


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(SASParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SASParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SASParser.StatementContext)
            else:
                return self.getTypedRuleContext(SASParser.StatementContext,i)


        def getRuleIndex(self):
            return SASParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = SASParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(SASParser.LBRACE)
            self.state = 265
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 262
                    self.statement() 
                self.state = 267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 268
            self.match(SASParser.RBRACE)
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
        self._predicates[18] = self.exprStatement_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exprStatement_sempred(self, localctx:ExprStatementContext, predIndex:int):
            if predIndex == 0:
                from SASLexer import SASLexer
                return  self._input.LA(1) != SASLexer.RETURN
         




