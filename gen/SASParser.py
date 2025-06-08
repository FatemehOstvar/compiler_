# Generated from D:/pycharm/Parser/SASParser.g4 by ANTLR 4.13.2
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
        4,1,73,201,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,5,0,49,8,0,10,0,12,0,52,9,0,1,0,
        1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,65,8,2,1,3,1,3,1,3,1,
        3,3,3,71,8,3,1,3,1,3,1,4,1,4,5,4,77,8,4,10,4,12,4,80,9,4,1,4,3,4,
        83,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,1,8,1,8,3,8,103,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,
        10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,12,3,12,126,
        8,12,1,12,1,12,1,13,1,13,1,13,5,13,133,8,13,10,13,12,13,136,9,13,
        1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,5,16,149,
        8,16,10,16,12,16,152,9,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,3,18,165,8,18,1,18,1,18,1,18,5,18,170,8,18,10,18,
        12,18,173,9,18,1,19,1,19,1,19,3,19,178,8,19,1,19,1,19,1,20,1,20,
        1,20,5,20,185,8,20,10,20,12,20,188,9,20,1,21,1,21,1,22,1,22,5,22,
        194,8,22,10,22,12,22,197,9,22,1,22,1,22,1,22,0,1,36,23,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,3,1,0,1,
        6,1,0,25,29,2,0,53,58,69,70,199,0,50,1,0,0,0,2,55,1,0,0,0,4,64,1,
        0,0,0,6,66,1,0,0,0,8,74,1,0,0,0,10,84,1,0,0,0,12,90,1,0,0,0,14,97,
        1,0,0,0,16,102,1,0,0,0,18,104,1,0,0,0,20,112,1,0,0,0,22,118,1,0,
        0,0,24,121,1,0,0,0,26,129,1,0,0,0,28,137,1,0,0,0,30,140,1,0,0,0,
        32,150,1,0,0,0,34,153,1,0,0,0,36,164,1,0,0,0,38,174,1,0,0,0,40,181,
        1,0,0,0,42,189,1,0,0,0,44,191,1,0,0,0,46,49,3,2,1,0,47,49,3,4,2,
        0,48,46,1,0,0,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,
        1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,0,53,54,5,0,0,1,54,1,1,0,0,0,55,
        56,5,68,0,0,56,57,5,59,0,0,57,3,1,0,0,0,58,65,3,6,3,0,59,65,3,8,
        4,0,60,65,3,16,8,0,61,65,3,22,11,0,62,65,3,30,15,0,63,65,3,34,17,
        0,64,58,1,0,0,0,64,59,1,0,0,0,64,60,1,0,0,0,64,61,1,0,0,0,64,62,
        1,0,0,0,64,63,1,0,0,0,65,5,1,0,0,0,66,67,7,0,0,0,67,70,5,59,0,0,
        68,69,5,47,0,0,69,71,3,36,18,0,70,68,1,0,0,0,70,71,1,0,0,0,71,72,
        1,0,0,0,72,73,5,64,0,0,73,7,1,0,0,0,74,78,3,10,5,0,75,77,3,12,6,
        0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,82,
        1,0,0,0,80,78,1,0,0,0,81,83,3,14,7,0,82,81,1,0,0,0,82,83,1,0,0,0,
        83,9,1,0,0,0,84,85,5,7,0,0,85,86,5,60,0,0,86,87,3,36,18,0,87,88,
        5,61,0,0,88,89,3,44,22,0,89,11,1,0,0,0,90,91,5,8,0,0,91,92,5,7,0,
        0,92,93,5,60,0,0,93,94,3,36,18,0,94,95,5,61,0,0,95,96,3,44,22,0,
        96,13,1,0,0,0,97,98,5,8,0,0,98,99,3,44,22,0,99,15,1,0,0,0,100,103,
        3,18,9,0,101,103,3,20,10,0,102,100,1,0,0,0,102,101,1,0,0,0,103,17,
        1,0,0,0,104,105,5,15,0,0,105,106,5,60,0,0,106,107,3,34,17,0,107,
        108,3,34,17,0,108,109,3,36,18,0,109,110,5,61,0,0,110,111,3,44,22,
        0,111,19,1,0,0,0,112,113,5,11,0,0,113,114,5,60,0,0,114,115,3,36,
        18,0,115,116,5,61,0,0,116,117,3,44,22,0,117,21,1,0,0,0,118,119,3,
        24,12,0,119,120,3,44,22,0,120,23,1,0,0,0,121,122,7,0,0,0,122,123,
        5,59,0,0,123,125,5,60,0,0,124,126,3,26,13,0,125,124,1,0,0,0,125,
        126,1,0,0,0,126,127,1,0,0,0,127,128,5,61,0,0,128,25,1,0,0,0,129,
        134,3,28,14,0,130,131,5,65,0,0,131,133,3,28,14,0,132,130,1,0,0,0,
        133,136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,27,1,0,0,0,136,
        134,1,0,0,0,137,138,7,0,0,0,138,139,5,59,0,0,139,29,1,0,0,0,140,
        141,5,18,0,0,141,142,5,59,0,0,142,143,5,62,0,0,143,144,3,32,16,0,
        144,145,5,63,0,0,145,31,1,0,0,0,146,149,3,6,3,0,147,149,3,22,11,
        0,148,146,1,0,0,0,148,147,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,
        0,150,151,1,0,0,0,151,33,1,0,0,0,152,150,1,0,0,0,153,154,3,36,18,
        0,154,155,5,64,0,0,155,35,1,0,0,0,156,157,6,18,-1,0,157,158,5,60,
        0,0,158,159,3,36,18,0,159,160,5,61,0,0,160,165,1,0,0,0,161,165,3,
        38,19,0,162,165,5,59,0,0,163,165,3,42,21,0,164,156,1,0,0,0,164,161,
        1,0,0,0,164,162,1,0,0,0,164,163,1,0,0,0,165,171,1,0,0,0,166,167,
        10,5,0,0,167,168,7,1,0,0,168,170,3,36,18,6,169,166,1,0,0,0,170,173,
        1,0,0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,37,1,0,0,0,173,171,1,
        0,0,0,174,175,5,59,0,0,175,177,5,60,0,0,176,178,3,40,20,0,177,176,
        1,0,0,0,177,178,1,0,0,0,178,179,1,0,0,0,179,180,5,61,0,0,180,39,
        1,0,0,0,181,186,3,36,18,0,182,183,5,65,0,0,183,185,3,36,18,0,184,
        182,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,
        41,1,0,0,0,188,186,1,0,0,0,189,190,7,2,0,0,190,43,1,0,0,0,191,195,
        5,62,0,0,192,194,3,4,2,0,193,192,1,0,0,0,194,197,1,0,0,0,195,193,
        1,0,0,0,195,196,1,0,0,0,196,198,1,0,0,0,197,195,1,0,0,0,198,199,
        5,63,0,0,199,45,1,0,0,0,16,48,50,64,70,78,82,102,125,134,148,150,
        164,171,177,186,195
    ]

class SASParser ( Parser ):

    grammarFileName = "SASParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'double'", "'char'", 
                     "'bool'", "'string'", "'if'", "'else'", "'switch'", 
                     "'case'", "'while'", "'continue'", "'break'", "'default'", 
                     "'for'", "'do'", "'return'", "'class'", "'const'", 
                     "'public'", "'private'", "'protected'", "'template'", 
                     "'static'", "'+'", "'-'", "'*'", "'/'", "'%'", "'++'", 
                     "'--'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'&&'", "'||'", "'!'", "'&'", "'|'", "'^'", "'~'", 
                     "'<<'", "'>>'", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "';'", "','", "':'", "'.'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "DOUBLE", "CHAR", "BOOL", 
                      "STRING_K", "IF", "ELSE", "SWITCH", "CASE", "WHILE", 
                      "CONTINUE", "BREAK", "DEFAULT", "FOR", "DO", "RETURN", 
                      "CLASS", "CONST", "PUBLIC", "PRIVATE", "PROTECTED", 
                      "TEMPLATE", "STATIC", "PLUS", "MINUS", "MULT", "DIV", 
                      "MOD", "INCREMENT", "DECREMENT", "EQ", "NEQ", "LT", 
                      "LTE", "GT", "GTE", "AND_AND", "OR_OR", "NOT", "BIT_AND", 
                      "BIT_OR", "BIT_XOR", "BIT_NOT", "LSHIFT", "RSHIFT", 
                      "ASSIGN", "PLUS_ASSIGN", "MINUS_ASSIGN", "MULT_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "INTEGER_LITERAL", "FLOAT_LITERAL", 
                      "HEX_LITERAL", "BINARY_LITERAL", "OCTAL_LITERAL", 
                      "SCIENTIFIC_LITERAL", "IDENTIFIER", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "SEMICOLON", "COMMA", "COLON", 
                      "DOT", "PREPROCESSOR_DIRECTIVE", "STRING_LITERAL", 
                      "CHAR_LITERAL", "LINE_COMMENT", "BLOCK_COMMENT", "WS" ]

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
    RULE_funcCall = 19
    RULE_argList = 20
    RULE_literal = 21
    RULE_block = 22

    ruleNames =  [ "program", "preprocessor", "statement", "varDecl", "ifStatement", 
                   "ifBlock", "elseIfBlock", "elseBlock", "loopStatement", 
                   "forLoop", "whileLoop", "funcDecl", "funcHeader", "paramList", 
                   "param", "classDecl", "classBody", "exprStatement", "expr", 
                   "funcCall", "argList", "literal", "block" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    DOUBLE=3
    CHAR=4
    BOOL=5
    STRING_K=6
    IF=7
    ELSE=8
    SWITCH=9
    CASE=10
    WHILE=11
    CONTINUE=12
    BREAK=13
    DEFAULT=14
    FOR=15
    DO=16
    RETURN=17
    CLASS=18
    CONST=19
    PUBLIC=20
    PRIVATE=21
    PROTECTED=22
    TEMPLATE=23
    STATIC=24
    PLUS=25
    MINUS=26
    MULT=27
    DIV=28
    MOD=29
    INCREMENT=30
    DECREMENT=31
    EQ=32
    NEQ=33
    LT=34
    LTE=35
    GT=36
    GTE=37
    AND_AND=38
    OR_OR=39
    NOT=40
    BIT_AND=41
    BIT_OR=42
    BIT_XOR=43
    BIT_NOT=44
    LSHIFT=45
    RSHIFT=46
    ASSIGN=47
    PLUS_ASSIGN=48
    MINUS_ASSIGN=49
    MULT_ASSIGN=50
    DIV_ASSIGN=51
    MOD_ASSIGN=52
    INTEGER_LITERAL=53
    FLOAT_LITERAL=54
    HEX_LITERAL=55
    BINARY_LITERAL=56
    OCTAL_LITERAL=57
    SCIENTIFIC_LITERAL=58
    IDENTIFIER=59
    LPAREN=60
    RPAREN=61
    LBRACE=62
    RBRACE=63
    SEMICOLON=64
    COMMA=65
    COLON=66
    DOT=67
    PREPROCESSOR_DIRECTIVE=68
    STRING_LITERAL=69
    CHAR_LITERAL=70
    LINE_COMMENT=71
    BLOCK_COMMENT=72
    WS=73

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2296835809959250174) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 7) != 0):
                self.state = 48
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [68]:
                    self.state = 46
                    self.preprocessor()
                    pass
                elif token in [1, 2, 3, 4, 5, 6, 7, 11, 15, 18, 53, 54, 55, 56, 57, 58, 59, 60, 69, 70]:
                    self.state = 47
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
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
            self.state = 55
            self.match(SASParser.PREPROCESSOR_DIRECTIVE)
            self.state = 56
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
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.ifStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.loopStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self.funcDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 62
                self.classDecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 63
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

        def SEMICOLON(self):
            return self.getToken(SASParser.SEMICOLON, 0)

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

        def STRING_K(self):
            return self.getToken(SASParser.STRING_K, 0)

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
            self.state = 66
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 67
            self.match(SASParser.IDENTIFIER)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 68
                self.match(SASParser.ASSIGN)
                self.state = 69
                self.expr(0)


            self.state = 72
            self.match(SASParser.SEMICOLON)
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.ifBlock()
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 75
                    self.elseIfBlock() 
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 81
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
            self.state = 84
            self.match(SASParser.IF)
            self.state = 85
            self.match(SASParser.LPAREN)
            self.state = 86
            self.expr(0)
            self.state = 87
            self.match(SASParser.RPAREN)
            self.state = 88
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
            self.state = 90
            self.match(SASParser.ELSE)
            self.state = 91
            self.match(SASParser.IF)
            self.state = 92
            self.match(SASParser.LPAREN)
            self.state = 93
            self.expr(0)
            self.state = 94
            self.match(SASParser.RPAREN)
            self.state = 95
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
            self.state = 97
            self.match(SASParser.ELSE)
            self.state = 98
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
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.forLoop()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
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
            self.state = 104
            self.match(SASParser.FOR)
            self.state = 105
            self.match(SASParser.LPAREN)
            self.state = 106
            self.exprStatement()
            self.state = 107
            self.exprStatement()
            self.state = 108
            self.expr(0)
            self.state = 109
            self.match(SASParser.RPAREN)
            self.state = 110
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
            self.state = 112
            self.match(SASParser.WHILE)
            self.state = 113
            self.match(SASParser.LPAREN)
            self.state = 114
            self.expr(0)
            self.state = 115
            self.match(SASParser.RPAREN)
            self.state = 116
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
            self.state = 118
            self.funcHeader()
            self.state = 119
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

        def STRING_K(self):
            return self.getToken(SASParser.STRING_K, 0)

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
            self.state = 121
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 122
            self.match(SASParser.IDENTIFIER)
            self.state = 123
            self.match(SASParser.LPAREN)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0):
                self.state = 124
                self.paramList()


            self.state = 127
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
            self.state = 129
            self.param()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==65:
                self.state = 130
                self.match(SASParser.COMMA)
                self.state = 131
                self.param()
                self.state = 136
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

        def STRING_K(self):
            return self.getToken(SASParser.STRING_K, 0)

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
            self.state = 137
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 138
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
            self.state = 140
            self.match(SASParser.CLASS)
            self.state = 141
            self.match(SASParser.IDENTIFIER)
            self.state = 142
            self.match(SASParser.LBRACE)
            self.state = 143
            self.classBody()
            self.state = 144
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
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0):
                self.state = 148
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 146
                    self.varDecl()
                    pass

                elif la_ == 2:
                    self.state = 147
                    self.funcDecl()
                    pass


                self.state = 152
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


        def SEMICOLON(self):
            return self.getToken(SASParser.SEMICOLON, 0)

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
            self.state = 153
            self.expr(0)
            self.state = 154
            self.match(SASParser.SEMICOLON)
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


    class MathExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SASParser.ExprContext)
            else:
                return self.getTypedRuleContext(SASParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(SASParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(SASParser.MINUS, 0)
        def MULT(self):
            return self.getToken(SASParser.MULT, 0)
        def DIV(self):
            return self.getToken(SASParser.DIV, 0)
        def MOD(self):
            return self.getToken(SASParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathExpr" ):
                listener.enterMathExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathExpr" ):
                listener.exitMathExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathExpr" ):
                return visitor.visitMathExpr(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.ExprContext
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


    class FuncCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.ExprContext
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


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.ExprContext
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


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SASParser.ExprContext
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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SASParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = SASParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 157
                self.match(SASParser.LPAREN)
                self.state = 158
                self.expr(0)
                self.state = 159
                self.match(SASParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = SASParser.FuncCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 161
                self.funcCall()
                pass

            elif la_ == 3:
                localctx = SASParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 162
                self.match(SASParser.IDENTIFIER)
                pass

            elif la_ == 4:
                localctx = SASParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 163
                self.literal()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SASParser.MathExprContext(self, SASParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 166
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 167
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1040187392) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 168
                    self.expr(6) 
                self.state = 173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 38, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(SASParser.IDENTIFIER)
            self.state = 175
            self.match(SASParser.LPAREN)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 53)) & ~0x3f) == 0 and ((1 << (_la - 53)) & 196863) != 0):
                self.state = 176
                self.argList()


            self.state = 179
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
        self.enterRule(localctx, 40, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.expr(0)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==65:
                self.state = 182
                self.match(SASParser.COMMA)
                self.state = 183
                self.expr(0)
                self.state = 188
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
        self.enterRule(localctx, 42, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            _la = self._input.LA(1)
            if not(((((_la - 53)) & ~0x3f) == 0 and ((1 << (_la - 53)) & 196671) != 0)):
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
        self.enterRule(localctx, 44, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(SASParser.LBRACE)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2296835809959250174) != 0) or _la==69 or _la==70:
                self.state = 192
                self.statement()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 198
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
        self._predicates[18] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         




