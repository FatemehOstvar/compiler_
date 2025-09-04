# Generated from D:/pycharm/Parser/parser/SASParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SASParser import SASParser
else:
    from SASParser import SASParser

# This class defines a complete generic visitor for a parse tree produced by SASParser.

class SASParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SASParser#program.
    def visitProgram(self, ctx:SASParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#returnStatement.
    def visitReturnStatement(self, ctx:SASParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#preprocessor.
    def visitPreprocessor(self, ctx:SASParser.PreprocessorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#statement.
    def visitStatement(self, ctx:SASParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#varDecl.
    def visitVarDecl(self, ctx:SASParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#elseIfBlock.
    def visitElseIfBlock(self, ctx:SASParser.ElseIfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#ifBlock.
    def visitIfBlock(self, ctx:SASParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#elseBlock.
    def visitElseBlock(self, ctx:SASParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#ifStatement.
    def visitIfStatement(self, ctx:SASParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#loopStatement.
    def visitLoopStatement(self, ctx:SASParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#forLoop.
    def visitForLoop(self, ctx:SASParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#whileLoop.
    def visitWhileLoop(self, ctx:SASParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#funcDecl.
    def visitFuncDecl(self, ctx:SASParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#funcHeader.
    def visitFuncHeader(self, ctx:SASParser.FuncHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#paramList.
    def visitParamList(self, ctx:SASParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#param.
    def visitParam(self, ctx:SASParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#classDecl.
    def visitClassDecl(self, ctx:SASParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#classBody.
    def visitClassBody(self, ctx:SASParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#exprStatement.
    def visitExprStatement(self, ctx:SASParser.ExprStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#assignExpr.
    def visitAssignExpr(self, ctx:SASParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#logicOrPass.
    def visitLogicOrPass(self, ctx:SASParser.LogicOrPassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#logicalExpr.
    def visitLogicalExpr(self, ctx:SASParser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#bitwisePass.
    def visitBitwisePass(self, ctx:SASParser.BitwisePassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#bitwiseExpr.
    def visitBitwiseExpr(self, ctx:SASParser.BitwiseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#compareExpr.
    def visitCompareExpr(self, ctx:SASParser.CompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#addSub.
    def visitAddSub(self, ctx:SASParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#mulDivMod.
    def visitMulDivMod(self, ctx:SASParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#unaryOpExpr.
    def visitUnaryOpExpr(self, ctx:SASParser.UnaryOpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#noUnary.
    def visitNoUnary(self, ctx:SASParser.NoUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#parenExpr.
    def visitParenExpr(self, ctx:SASParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#funcCallExpr.
    def visitFuncCallExpr(self, ctx:SASParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#idExpr.
    def visitIdExpr(self, ctx:SASParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#literalExpr.
    def visitLiteralExpr(self, ctx:SASParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#funcCall.
    def visitFuncCall(self, ctx:SASParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#argList.
    def visitArgList(self, ctx:SASParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#literal.
    def visitLiteral(self, ctx:SASParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SASParser#block.
    def visitBlock(self, ctx:SASParser.BlockContext):
        return self.visitChildren(ctx)



del SASParser