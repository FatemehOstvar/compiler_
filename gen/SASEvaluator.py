from SASParserVisitor import SASParserVisitor
from SASParser import SASParser
from SASLexer import SASLexer
from semantics import TypeMismatchError, SemanticError


class SASEvaluator(SASParserVisitor):
    def __init__(self):
        self.vars = {}
        self.types = {}

    def visitVarDecl(self, ctx):
        declared_type = ctx.getChild(0).getText( )
        var_name = ctx.IDENTIFIER( ).getText( )
        value = self.visit(ctx.expr( )) if ctx.expr( ) else None

        # semantic type checks
        if declared_type == 'int' and not isinstance(value, int):
            raise TypeMismatchError('int', type(value).__name__, var_name, ctx.start.line)
        if declared_type == 'float' and not isinstance(value, float):
            raise TypeMismatchError('float', type(value).__name__, var_name, ctx.start.line)
        if declared_type == 'string' and not isinstance(value, str):
            raise TypeMismatchError('string', type(value).__name__, var_name, ctx.start.line)
        if declared_type == 'char' and (not isinstance(value, str) or len(value) != 1):
            raise TypeMismatchError('char', type(value).__name__, var_name, ctx.start.line)
        if declared_type == 'bool' and not isinstance(value, bool):
            raise TypeMismatchError('bool', type(value).__name__, var_name, ctx.start.line)

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
        token_type = ctx.start.type

        if token_type == SASLexer.TRUE:
            return True
        elif token_type == SASLexer.FALSE:
            return False
        elif token_type == SASLexer.STRING_LITERAL:
            return text.strip('"')
        elif token_type == SASLexer.CHAR_LITERAL:
            return text.strip("'")
        elif token_type == SASLexer.FLOAT_LITERAL or token_type == SASLexer.SCIENTIFIC_LITERAL:
            return float(text)
        elif token_type == SASLexer.INTEGER_LITERAL:
            return int(text)
        elif token_type == SASLexer.HEX_LITERAL:
            return int(text, 16)
        elif token_type == SASLexer.BINARY_LITERAL:
            return int(text, 2)
        elif token_type == SASLexer.OCTAL_LITERAL:
            return int(text, 8)
        else:
            raise SemanticError(f"Unsupported literal: {text}", ctx.start.line)

    def visitExprStatement(self, ctx: SASParser.ExprStatementContext):
        return self.visit(ctx.expr())

    def visitProgram(self, ctx: SASParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return self.vars
