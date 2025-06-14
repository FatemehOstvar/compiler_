from SASParserVisitor import SASParserVisitor
from SASParser import SASParser

class SASEvaluator(SASParserVisitor):
    def __init__(self):
        self.vars = {}
        self.types = {}

    def visitVarDecl(self, ctx):
        declared_type = ctx.getChild(0).getText( )
        var_name = ctx.IDENTIFIER( ).getText( )
        value = self.visit(ctx.expr( )) if ctx.expr( ) else 0

        # Type validation...

        self.vars[var_name] = value
        self.types[var_name] = declared_type
        return value

    def visitAssignExpr(self, ctx):
        var_name = ctx.IDENTIFIER( ).getText( )
        value = self.visit(ctx.expr( ))

        # Check if variable was declared
        if var_name in self.types:
            expected = self.types[var_name]
            if expected == 'int' and isinstance(value, float):
                raise TypeError(f"Type error: cannot assign float '{value}' to int '{var_name}'")
        else:
            raise NameError(f"Undeclared variable '{var_name}'")

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
