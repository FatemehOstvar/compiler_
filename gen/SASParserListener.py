# Generated from D:/pycharm/Parser/SASParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from parser.gen.SASParser import SASParser
else:
    from parser.gen.SASParser import SASParser

# This class defines a complete listener for a parse tree produced by SASParser.
class SASParserListener(ParseTreeListener):

    # Enter a parse tree produced by SASParser#program.
    def enterProgram(self, ctx:SASParser.ProgramContext):
        pass

    # Exit a parse tree produced by SASParser#program.
    def exitProgram(self, ctx:SASParser.ProgramContext):
        pass


    # Enter a parse tree produced by SASParser#preprocessor.
    def enterPreprocessor(self, ctx:SASParser.PreprocessorContext):
        pass

    # Exit a parse tree produced by SASParser#preprocessor.
    def exitPreprocessor(self, ctx:SASParser.PreprocessorContext):
        pass


    # Enter a parse tree produced by SASParser#statement.
    def enterStatement(self, ctx:SASParser.StatementContext):
        pass

    # Exit a parse tree produced by SASParser#statement.
    def exitStatement(self, ctx:SASParser.StatementContext):
        pass


    # Enter a parse tree produced by SASParser#varDecl.
    def enterVarDecl(self, ctx:SASParser.VarDeclContext):
        pass

    # Exit a parse tree produced by SASParser#varDecl.
    def exitVarDecl(self, ctx:SASParser.VarDeclContext):
        pass


    # Enter a parse tree produced by SASParser#ifStatement.
    def enterIfStatement(self, ctx:SASParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SASParser#ifStatement.
    def exitIfStatement(self, ctx:SASParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SASParser#ifBlock.
    def enterIfBlock(self, ctx:SASParser.IfBlockContext):
        pass

    # Exit a parse tree produced by SASParser#ifBlock.
    def exitIfBlock(self, ctx:SASParser.IfBlockContext):
        pass


    # Enter a parse tree produced by SASParser#elseIfBlock.
    def enterElseIfBlock(self, ctx:SASParser.ElseIfBlockContext):
        pass

    # Exit a parse tree produced by SASParser#elseIfBlock.
    def exitElseIfBlock(self, ctx:SASParser.ElseIfBlockContext):
        pass


    # Enter a parse tree produced by SASParser#elseBlock.
    def enterElseBlock(self, ctx:SASParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by SASParser#elseBlock.
    def exitElseBlock(self, ctx:SASParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by SASParser#loopStatement.
    def enterLoopStatement(self, ctx:SASParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by SASParser#loopStatement.
    def exitLoopStatement(self, ctx:SASParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by SASParser#forLoop.
    def enterForLoop(self, ctx:SASParser.ForLoopContext):
        pass

    # Exit a parse tree produced by SASParser#forLoop.
    def exitForLoop(self, ctx:SASParser.ForLoopContext):
        pass


    # Enter a parse tree produced by SASParser#whileLoop.
    def enterWhileLoop(self, ctx:SASParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by SASParser#whileLoop.
    def exitWhileLoop(self, ctx:SASParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by SASParser#funcDecl.
    def enterFuncDecl(self, ctx:SASParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by SASParser#funcDecl.
    def exitFuncDecl(self, ctx:SASParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by SASParser#funcHeader.
    def enterFuncHeader(self, ctx:SASParser.FuncHeaderContext):
        pass

    # Exit a parse tree produced by SASParser#funcHeader.
    def exitFuncHeader(self, ctx:SASParser.FuncHeaderContext):
        pass


    # Enter a parse tree produced by SASParser#paramList.
    def enterParamList(self, ctx:SASParser.ParamListContext):
        pass

    # Exit a parse tree produced by SASParser#paramList.
    def exitParamList(self, ctx:SASParser.ParamListContext):
        pass


    # Enter a parse tree produced by SASParser#param.
    def enterParam(self, ctx:SASParser.ParamContext):
        pass

    # Exit a parse tree produced by SASParser#param.
    def exitParam(self, ctx:SASParser.ParamContext):
        pass


    # Enter a parse tree produced by SASParser#classDecl.
    def enterClassDecl(self, ctx:SASParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by SASParser#classDecl.
    def exitClassDecl(self, ctx:SASParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by SASParser#classBody.
    def enterClassBody(self, ctx:SASParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by SASParser#classBody.
    def exitClassBody(self, ctx:SASParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by SASParser#exprStatement.
    def enterExprStatement(self, ctx:SASParser.ExprStatementContext):
        pass

    # Exit a parse tree produced by SASParser#exprStatement.
    def exitExprStatement(self, ctx:SASParser.ExprStatementContext):
        pass


    # Enter a parse tree produced by SASParser#mathExpr.
    def enterMathExpr(self, ctx:SASParser.MathExprContext):
        pass

    # Exit a parse tree produced by SASParser#mathExpr.
    def exitMathExpr(self, ctx:SASParser.MathExprContext):
        pass


    # Enter a parse tree produced by SASParser#literalExpr.
    def enterLiteralExpr(self, ctx:SASParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by SASParser#literalExpr.
    def exitLiteralExpr(self, ctx:SASParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by SASParser#funcCallExpr.
    def enterFuncCallExpr(self, ctx:SASParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by SASParser#funcCallExpr.
    def exitFuncCallExpr(self, ctx:SASParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by SASParser#parenExpr.
    def enterParenExpr(self, ctx:SASParser.ParenExprContext):
        pass

    # Exit a parse tree produced by SASParser#parenExpr.
    def exitParenExpr(self, ctx:SASParser.ParenExprContext):
        pass


    # Enter a parse tree produced by SASParser#idExpr.
    def enterIdExpr(self, ctx:SASParser.IdExprContext):
        pass

    # Exit a parse tree produced by SASParser#idExpr.
    def exitIdExpr(self, ctx:SASParser.IdExprContext):
        pass


    # Enter a parse tree produced by SASParser#funcCall.
    def enterFuncCall(self, ctx:SASParser.FuncCallContext):
        pass

    # Exit a parse tree produced by SASParser#funcCall.
    def exitFuncCall(self, ctx:SASParser.FuncCallContext):
        pass


    # Enter a parse tree produced by SASParser#argList.
    def enterArgList(self, ctx:SASParser.ArgListContext):
        pass

    # Exit a parse tree produced by SASParser#argList.
    def exitArgList(self, ctx:SASParser.ArgListContext):
        pass


    # Enter a parse tree produced by SASParser#literal.
    def enterLiteral(self, ctx:SASParser.LiteralContext):
        pass

    # Exit a parse tree produced by SASParser#literal.
    def exitLiteral(self, ctx:SASParser.LiteralContext):
        pass


    # Enter a parse tree produced by SASParser#block.
    def enterBlock(self, ctx:SASParser.BlockContext):
        pass

    # Exit a parse tree produced by SASParser#block.
    def exitBlock(self, ctx:SASParser.BlockContext):
        pass



del SASParser