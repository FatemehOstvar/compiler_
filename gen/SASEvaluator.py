from SASParserVisitor import SASParserVisitor
from SASParser import SASParser

class SASEvaluator(SASParserVisitor):
    def __init__(self):
        self.vars = {}

    def visitVarDecl(self, ctx):
        declared_type = ctx.getChild(0).getText( )  # 'int', 'float', etc.
        var_name = ctx.IDENTIFIER( ).getText( )
        value = 0

        if ctx.expr( ):
            value = self.visit(ctx.expr( ))

            # Semantic check: catch type mismatches
            if declared_type == 'int' and isinstance(value, float):
                raise TypeError(f"Semantic error: cannot assign float '{value}' to int '{var_name}'")
            if declared_type == 'char' and not isinstance(value, str):
                raise TypeError(f"Semantic error: expected char for '{var_name}', got {type(value).__name__}")

        self.vars[var_name] = value
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
