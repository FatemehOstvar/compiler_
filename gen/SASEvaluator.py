from SASParserVisitor import SASParserVisitor
from SASParser import SASParser

class SASEvaluator(SASParserVisitor):
    def __init__(self):
        self.vars = {}

    def visitVarDecl(self, ctx: SASParser.VarDeclContext):
        type_name = ctx.getChild(0).getText()
        var_name = ctx.IDENTIFIER().getText()
        value = 0
        if ctx.expr():
            value = self.visit(ctx.expr())
        # Truncate float if declared as int
        if type_name == 'int':
            value = int(value)
        self.vars[var_name] = value
        return value

    def visitAssignExpr(self, ctx: SASParser.AssignExprContext):
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expr())
        self.vars[var_name] = value
        return value

    def visitAddSub(self, ctx):
        if ctx.getChildCount( ) == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText( )
        right = self.visit(ctx.getChild(2))
        return left + right if op == '+' else left - right

    def visitMulDivMod(self, ctx):
        if ctx.getChildCount( ) == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText( )
        right = self.visit(ctx.getChild(2))
        if op == '*':
            return left * right
        elif op == '/':
            return left / right
        elif op == '%':
            return left % right

    def visitIdExpr(self, ctx: SASParser.IdExprContext):
        name = ctx.IDENTIFIER().getText()
        return self.vars.get(name, 0)

    def visitLiteralExpr(self, ctx):
        text = ctx.getText( )
        if '.' in text or 'e' in text.lower( ):
            return float(text)
        return int(text)

    def visitExprStatement(self, ctx: SASParser.ExprStatementContext):
        return self.visit(ctx.expr())

    def visitProgram(self, ctx: SASParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return self.vars
