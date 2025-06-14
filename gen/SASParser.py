# Generated from D:/pycharm/Parser/parser/SASParser.g4 by ANTLR 4.13.2
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
        4,1,47,269,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,5,0,67,
        8,0,10,0,12,0,70,9,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,84,8,2,1,3,1,3,1,3,1,3,3,3,90,8,3,1,3,1,3,1,4,1,4,5,4,96,
        8,4,10,4,12,4,99,9,4,1,4,3,4,102,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,3,8,122,8,8,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,
        1,11,1,12,1,12,1,12,1,12,3,12,145,8,12,1,12,1,12,1,13,1,13,1,13,
        5,13,152,8,13,10,13,12,13,155,9,13,1,14,1,14,1,14,1,15,1,15,1,15,
        1,15,1,15,1,15,1,16,1,16,5,16,168,8,16,10,16,12,16,171,9,16,1,17,
        1,17,1,17,1,17,1,18,1,18,1,18,1,18,3,18,181,8,18,1,19,1,19,1,19,
        5,19,186,8,19,10,19,12,19,189,9,19,1,20,1,20,1,21,1,21,1,21,5,21,
        196,8,21,10,21,12,21,199,9,21,1,22,1,22,1,22,5,22,204,8,22,10,22,
        12,22,207,9,22,1,23,1,23,1,23,5,23,212,8,23,10,23,12,23,215,9,23,
        1,24,1,24,1,24,5,24,220,8,24,10,24,12,24,223,9,24,1,25,3,25,226,
        8,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,237,8,26,
        1,27,1,27,1,27,3,27,242,8,27,1,27,1,27,1,28,1,28,1,28,5,28,249,8,
        28,10,28,12,28,252,9,28,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,
        5,31,262,8,31,10,31,12,31,265,9,31,1,31,1,31,1,31,0,0,32,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,60,62,0,7,1,0,1,6,2,0,13,13,24,24,1,0,14,19,1,0,25,26,
        2,0,22,23,33,33,2,0,20,21,34,34,1,0,37,44,265,0,68,1,0,0,0,2,73,
        1,0,0,0,4,83,1,0,0,0,6,85,1,0,0,0,8,93,1,0,0,0,10,103,1,0,0,0,12,
        109,1,0,0,0,14,116,1,0,0,0,16,121,1,0,0,0,18,123,1,0,0,0,20,131,
        1,0,0,0,22,137,1,0,0,0,24,140,1,0,0,0,26,148,1,0,0,0,28,156,1,0,
        0,0,30,159,1,0,0,0,32,169,1,0,0,0,34,172,1,0,0,0,36,180,1,0,0,0,
        38,182,1,0,0,0,40,190,1,0,0,0,42,192,1,0,0,0,44,200,1,0,0,0,46,208,
        1,0,0,0,48,216,1,0,0,0,50,225,1,0,0,0,52,236,1,0,0,0,54,238,1,0,
        0,0,56,245,1,0,0,0,58,253,1,0,0,0,60,255,1,0,0,0,62,259,1,0,0,0,
        64,67,3,2,1,0,65,67,3,4,2,0,66,64,1,0,0,0,66,65,1,0,0,0,67,70,1,
        0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,71,1,0,0,0,70,68,1,0,0,0,71,
        72,5,0,0,1,72,1,1,0,0,0,73,74,5,36,0,0,74,75,5,35,0,0,75,3,1,0,0,
        0,76,84,3,60,30,0,77,84,3,6,3,0,78,84,3,8,4,0,79,84,3,16,8,0,80,
        84,3,22,11,0,81,84,3,30,15,0,82,84,3,34,17,0,83,76,1,0,0,0,83,77,
        1,0,0,0,83,78,1,0,0,0,83,79,1,0,0,0,83,80,1,0,0,0,83,81,1,0,0,0,
        83,82,1,0,0,0,84,5,1,0,0,0,85,86,7,0,0,0,86,89,5,35,0,0,87,88,5,
        24,0,0,88,90,3,36,18,0,89,87,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,
        91,92,5,27,0,0,92,7,1,0,0,0,93,97,3,10,5,0,94,96,3,12,6,0,95,94,
        1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,101,1,0,0,0,
        99,97,1,0,0,0,100,102,3,14,7,0,101,100,1,0,0,0,101,102,1,0,0,0,102,
        9,1,0,0,0,103,104,5,7,0,0,104,105,5,29,0,0,105,106,3,36,18,0,106,
        107,5,30,0,0,107,108,3,62,31,0,108,11,1,0,0,0,109,110,5,8,0,0,110,
        111,5,7,0,0,111,112,5,29,0,0,112,113,3,36,18,0,113,114,5,30,0,0,
        114,115,3,62,31,0,115,13,1,0,0,0,116,117,5,8,0,0,117,118,3,62,31,
        0,118,15,1,0,0,0,119,122,3,18,9,0,120,122,3,20,10,0,121,119,1,0,
        0,0,121,120,1,0,0,0,122,17,1,0,0,0,123,124,5,9,0,0,124,125,5,29,
        0,0,125,126,3,34,17,0,126,127,3,34,17,0,127,128,3,36,18,0,128,129,
        5,30,0,0,129,130,3,62,31,0,130,19,1,0,0,0,131,132,5,10,0,0,132,133,
        5,29,0,0,133,134,3,36,18,0,134,135,5,30,0,0,135,136,3,62,31,0,136,
        21,1,0,0,0,137,138,3,24,12,0,138,139,3,62,31,0,139,23,1,0,0,0,140,
        141,7,0,0,0,141,142,5,35,0,0,142,144,5,29,0,0,143,145,3,26,13,0,
        144,143,1,0,0,0,144,145,1,0,0,0,145,146,1,0,0,0,146,147,5,30,0,0,
        147,25,1,0,0,0,148,153,3,28,14,0,149,150,5,28,0,0,150,152,3,28,14,
        0,151,149,1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,
        0,154,27,1,0,0,0,155,153,1,0,0,0,156,157,7,0,0,0,157,158,5,35,0,
        0,158,29,1,0,0,0,159,160,5,12,0,0,160,161,5,35,0,0,161,162,5,31,
        0,0,162,163,3,32,16,0,163,164,5,32,0,0,164,31,1,0,0,0,165,168,3,
        6,3,0,166,168,3,22,11,0,167,165,1,0,0,0,167,166,1,0,0,0,168,171,
        1,0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,33,1,0,0,0,171,169,1,
        0,0,0,172,173,4,17,0,0,173,174,3,36,18,0,174,175,5,27,0,0,175,35,
        1,0,0,0,176,177,5,35,0,0,177,178,7,1,0,0,178,181,3,36,18,0,179,181,
        3,38,19,0,180,176,1,0,0,0,180,179,1,0,0,0,181,37,1,0,0,0,182,187,
        3,40,20,0,183,184,5,20,0,0,184,186,3,40,20,0,185,183,1,0,0,0,186,
        189,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,39,1,0,0,0,189,187,
        1,0,0,0,190,191,3,42,21,0,191,41,1,0,0,0,192,197,3,44,22,0,193,194,
        5,34,0,0,194,196,3,44,22,0,195,193,1,0,0,0,196,199,1,0,0,0,197,195,
        1,0,0,0,197,198,1,0,0,0,198,43,1,0,0,0,199,197,1,0,0,0,200,205,3,
        46,23,0,201,202,7,2,0,0,202,204,3,46,23,0,203,201,1,0,0,0,204,207,
        1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,45,1,0,0,0,207,205,1,
        0,0,0,208,213,3,48,24,0,209,210,7,3,0,0,210,212,3,48,24,0,211,209,
        1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,47,1,
        0,0,0,215,213,1,0,0,0,216,221,3,50,25,0,217,218,7,4,0,0,218,220,
        3,50,25,0,219,217,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,222,
        1,0,0,0,222,49,1,0,0,0,223,221,1,0,0,0,224,226,7,5,0,0,225,224,1,
        0,0,0,225,226,1,0,0,0,226,227,1,0,0,0,227,228,3,52,26,0,228,51,1,
        0,0,0,229,230,5,29,0,0,230,231,3,36,18,0,231,232,5,30,0,0,232,237,
        1,0,0,0,233,237,3,54,27,0,234,237,5,35,0,0,235,237,3,58,29,0,236,
        229,1,0,0,0,236,233,1,0,0,0,236,234,1,0,0,0,236,235,1,0,0,0,237,
        53,1,0,0,0,238,239,5,35,0,0,239,241,5,29,0,0,240,242,3,56,28,0,241,
        240,1,0,0,0,241,242,1,0,0,0,242,243,1,0,0,0,243,244,5,30,0,0,244,
        55,1,0,0,0,245,250,3,36,18,0,246,247,5,28,0,0,247,249,3,36,18,0,
        248,246,1,0,0,0,249,252,1,0,0,0,250,248,1,0,0,0,250,251,1,0,0,0,
        251,57,1,0,0,0,252,250,1,0,0,0,253,254,7,6,0,0,254,59,1,0,0,0,255,
        256,5,11,0,0,256,257,3,36,18,0,257,258,5,27,0,0,258,61,1,0,0,0,259,
        263,5,31,0,0,260,262,3,4,2,0,261,260,1,0,0,0,262,265,1,0,0,0,263,
        261,1,0,0,0,263,264,1,0,0,0,264,266,1,0,0,0,265,263,1,0,0,0,266,
        267,5,32,0,0,267,63,1,0,0,0,22,66,68,83,89,97,101,121,144,153,167,
        169,180,187,197,205,213,221,225,236,241,250,263
    ]

class SASParser ( Parser ):

    grammarFileName = "SASParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'double'", "'char'", 
                     "'bool'", "'string'", "'if'", "'else'", "'for'", "'while'", 
                     "'return'", "'class'", "<INVALID>", "'>'", "'<'", "'=='", 
                     "'!='", "'>='", "'<='", "<INVALID>", "<INVALID>", "'*'", 
                     "'/'", "'='", "'+'", "'-'", "';'", "','", "'('", "')'", 
                     "'{'", "'}'", "'%'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "DOUBLE", "CHAR", "BOOL", 
                      "STRING", "IF", "ELSE", "FOR", "WHILE", "RETURN", 
                      "CLASS", "ASSIGNMENT_OPERATOR", "GT", "LT", "EQ", 
                      "NEQ", "GEQ", "LEQ", "LOGICAL_OPERATOR", "MATHEMATICAL_OPERATOR", 
                      "MULT", "DIV", "ASSIGN", "PLUS", "MINUS", "SEMI", 
                      "COMMA", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "MOD", 
                      "BITWISE_OPERATOR", "IDENTIFIER", "PREPROCESSOR_DIRECTIVE", 
                      "OCTAL_LITERAL", "SCIENTIFIC_LITERAL", "FLOAT_LITERAL", 
                      "INTEGER_LITERAL", "STRING_LITERAL", "CHAR_LITERAL", 
                      "HEX_LITERAL", "BINARY_LITERAL", "BLOCK_COMMENT", 
                      "LINE_COMMENT", "WS" ]

    RULE_program = 0
    RULE_preprocessor = 1
    RULE_statement = 2
    RULE_varDecl = 3
    RULE_ifStatement = 4
    RULE_ifBlock = 5
    RULE_elseIfBlock = 6
    RULE_elseBlock = 7
    RULE_loopStatement = 8
    RULE_forLoop = 9
    RULE_whileLoop = 10
    RULE_funcDecl = 11
    RULE_funcHeader = 12
    RULE_paramList = 13
    RULE_param = 14
    RULE_classDecl = 15
    RULE_classBody = 16
    RULE_exprStatement = 17
    RULE_expr = 18
    RULE_logicOrExpr = 19
    RULE_logicAndExpr = 20
    RULE_bitwiseExpr = 21
    RULE_compareExpr = 22
    RULE_additiveExpr = 23
    RULE_multiplicativeExpr = 24
    RULE_unaryExpr = 25
    RULE_primary = 26
    RULE_funcCall = 27
    RULE_argList = 28
    RULE_literal = 29
    RULE_returnStatement = 30
    RULE_block = 31

    ruleNames =  [ "program", "preprocessor", "statement", "varDecl", "ifStatement", 
                   "ifBlock", "elseIfBlock", "elseBlock", "loopStatement", 
                   "forLoop", "whileLoop", "funcDecl", "funcHeader", "paramList", 
                   "param", "classDecl", "classBody", "exprStatement", "expr", 
                   "logicOrExpr", "logicAndExpr", "bitwiseExpr", "compareExpr", 
                   "additiveExpr", "multiplicativeExpr", "unaryExpr", "primary", 
                   "funcCall", "argList", "literal", "returnStatement", 
                   "block" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    DOUBLE=3
    CHAR=4
    BOOL=5
    STRING=6
    IF=7
    ELSE=8
    FOR=9
    WHILE=10
    RETURN=11
    CLASS=12
    ASSIGNMENT_OPERATOR=13
    GT=14
    LT=15
    EQ=16
    NEQ=17
    GEQ=18
    LEQ=19
    LOGICAL_OPERATOR=20
    MATHEMATICAL_OPERATOR=21
    MULT=22
    DIV=23
    ASSIGN=24
    PLUS=25
    MINUS=26
    SEMI=27
    COMMA=28
    LPAREN=29
    RPAREN=30
    LBRACE=31
    RBRACE=32
    MOD=33
    BITWISE_OPERATOR=34
    IDENTIFIER=35
    PREPROCESSOR_DIRECTIVE=36
    OCTAL_LITERAL=37
    SCIENTIFIC_LITERAL=38
    FLOAT_LITERAL=39
    INTEGER_LITERAL=40
    STRING_LITERAL=41
    CHAR_LITERAL=42
    HEX_LITERAL=43
    BINARY_LITERAL=44
    BLOCK_COMMENT=45
    LINE_COMMENT=46
    WS=47

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
        self.enterRule(localctx, 2, self.RULE_preprocessor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(SASParser.PREPROCESSOR_DIRECTIVE)
            self.state = 74
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
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.returnStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.varDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.loopStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.funcDecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 81
                self.classDecl()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 82
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
        self.enterRule(localctx, 6, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 86
            self.match(SASParser.IDENTIFIER)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 87
                self.match(SASParser.ASSIGN)
                self.state = 88
                self.expr()


            self.state = 91
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
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.ifBlock()
            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 94
                    self.elseIfBlock() 
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 100
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
        self.enterRule(localctx, 10, self.RULE_ifBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(SASParser.IF)
            self.state = 104
            self.match(SASParser.LPAREN)
            self.state = 105
            self.expr()
            self.state = 106
            self.match(SASParser.RPAREN)
            self.state = 107
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
        self.enterRule(localctx, 12, self.RULE_elseIfBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(SASParser.ELSE)
            self.state = 110
            self.match(SASParser.IF)
            self.state = 111
            self.match(SASParser.LPAREN)
            self.state = 112
            self.expr()
            self.state = 113
            self.match(SASParser.RPAREN)
            self.state = 114
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
        self.enterRule(localctx, 14, self.RULE_elseBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(SASParser.ELSE)
            self.state = 117
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
        self.enterRule(localctx, 16, self.RULE_loopStatement)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.forLoop()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
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
        self.enterRule(localctx, 18, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(SASParser.FOR)
            self.state = 124
            self.match(SASParser.LPAREN)
            self.state = 125
            self.exprStatement()
            self.state = 126
            self.exprStatement()
            self.state = 127
            self.expr()
            self.state = 128
            self.match(SASParser.RPAREN)
            self.state = 129
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
        self.enterRule(localctx, 20, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(SASParser.WHILE)
            self.state = 132
            self.match(SASParser.LPAREN)
            self.state = 133
            self.expr()
            self.state = 134
            self.match(SASParser.RPAREN)
            self.state = 135
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
        self.enterRule(localctx, 22, self.RULE_funcDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.funcHeader()
            self.state = 138
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
        self.enterRule(localctx, 24, self.RULE_funcHeader)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 141
            self.match(SASParser.IDENTIFIER)
            self.state = 142
            self.match(SASParser.LPAREN)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0):
                self.state = 143
                self.paramList()


            self.state = 146
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
        self.enterRule(localctx, 26, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.param()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 149
                self.match(SASParser.COMMA)
                self.state = 150
                self.param()
                self.state = 155
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
        self.enterRule(localctx, 28, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 157
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
        self.enterRule(localctx, 30, self.RULE_classDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(SASParser.CLASS)
            self.state = 160
            self.match(SASParser.IDENTIFIER)
            self.state = 161
            self.match(SASParser.LBRACE)
            self.state = 162
            self.classBody()
            self.state = 163
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
        self.enterRule(localctx, 32, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0):
                self.state = 167
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 165
                    self.varDecl()
                    pass

                elif la_ == 2:
                    self.state = 166
                    self.funcDecl()
                    pass


                self.state = 171
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
        self.enterRule(localctx, 34, self.RULE_exprStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            if not  _input.LA(1) != SASLexer.RETURN :
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, " _input.LA(1) != SASLexer.RETURN ")
            self.state = 173
            self.expr()
            self.state = 174
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
        self.enterRule(localctx, 36, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = SASParser.AssignExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(SASParser.IDENTIFIER)
                self.state = 177
                _la = self._input.LA(1)
                if not(_la==13 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 178
                self.expr()
                pass

            elif la_ == 2:
                localctx = SASParser.LogicOrPassContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 179
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
        self.enterRule(localctx, 38, self.RULE_logicOrExpr)
        self._la = 0 # Token type
        try:
            localctx = SASParser.LogicalExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.logicAndExpr()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 183
                self.match(SASParser.LOGICAL_OPERATOR)
                self.state = 184
                self.logicAndExpr()
                self.state = 189
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
        self.enterRule(localctx, 40, self.RULE_logicAndExpr)
        try:
            localctx = SASParser.BitwisePassContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 190
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
        self.enterRule(localctx, 42, self.RULE_bitwiseExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.compareExpr()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 193
                self.match(SASParser.BITWISE_OPERATOR)
                self.state = 194
                self.compareExpr()
                self.state = 199
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
        self.enterRule(localctx, 44, self.RULE_compareExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.additiveExpr()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0):
                self.state = 201
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 202
                self.additiveExpr()
                self.state = 207
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
        self.enterRule(localctx, 46, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            localctx = SASParser.AddSubContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.multiplicativeExpr()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25 or _la==26:
                self.state = 209
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 210
                self.multiplicativeExpr()
                self.state = 215
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
        self.enterRule(localctx, 48, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            localctx = SASParser.MulDivModContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.unaryExpr()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8602517504) != 0):
                self.state = 217
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8602517504) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 218
                self.unaryExpr()
                self.state = 223
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

        def MATHEMATICAL_OPERATOR(self):
            return self.getToken(SASParser.MATHEMATICAL_OPERATOR, 0)
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



    def unaryExpr(self):

        localctx = SASParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            localctx = SASParser.UnaryOpExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 17183014912) != 0):
                self.state = 224
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17183014912) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 227
            self.primary()
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
        self.enterRule(localctx, 52, self.RULE_primary)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = SASParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(SASParser.LPAREN)
                self.state = 230
                self.expr()
                self.state = 231
                self.match(SASParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = SASParser.FuncCallExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.funcCall()
                pass

            elif la_ == 3:
                localctx = SASParser.IdExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.match(SASParser.IDENTIFIER)
                pass

            elif la_ == 4:
                localctx = SASParser.LiteralExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 235
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
        self.enterRule(localctx, 54, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(SASParser.IDENTIFIER)
            self.state = 239
            self.match(SASParser.LPAREN)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 35099012759552) != 0):
                self.state = 240
                self.argList()


            self.state = 243
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
        self.enterRule(localctx, 56, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.expr()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 246
                self.match(SASParser.COMMA)
                self.state = 247
                self.expr()
                self.state = 252
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
        self.enterRule(localctx, 58, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 35046933135360) != 0)):
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
        self.enterRule(localctx, 60, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(SASParser.RETURN)
            self.state = 256
            self.expr()
            self.state = 257
            self.match(SASParser.SEMI)
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
            self.state = 259
            self.match(SASParser.LBRACE)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 260
                    self.statement() 
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 266
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
        self._predicates[17] = self.exprStatement_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exprStatement_sempred(self, localctx:ExprStatementContext, predIndex:int):
            if predIndex == 0:
                return  _input.LA(1) != SASLexer.RETURN 
         




