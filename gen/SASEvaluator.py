from SASParserVisitor import SASParserVisitor
from SASParser import SASParser
from SASLexer import SASLexer
from semantics import TypeMismatchError, SemanticError, UnsupportedOperationError


class SASEvaluator(SASParserVisitor):
    def __init__(self):
        self.vars = {}
        self.types = {}
        self.decl_lines = {}
        self.in_conditional_block = False

    def visitVarDecl(self, ctx):
        declared_type = self._extract_declared_type(ctx)
        var_name = self._extract_var_name(ctx)
        value = self._extract_value(ctx)
        line = ctx.start.line
        actual_type = self._determine_actual_type(declared_type)

        self._validate_declared_type(declared_type, value, var_name, line)
        self._register_variable(var_name, value, actual_type, line)
        self._print_var_info(line, var_name, value, actual_type)

        return value

    def _extract_declared_type(self, ctx):
        return ctx.getChild(0).getText()

    def _extract_var_name(self, ctx):
        return ctx.IDENTIFIER().getText()

    def _extract_value(self, ctx):
        return self.visit(ctx.expr()) if ctx.expr() else None

    def _determine_actual_type(self, declared_type):
        return declared_type if not self.in_conditional_block else "conditional"

    def _register_variable(self, var_name, value, actual_type, line):
        self.vars[var_name] = value
        self.types[var_name] = actual_type
        self.decl_lines[var_name] = line

    def _validate_declared_type(self, declared_type, value, var_name, line):
        type_checks = {
            'int': lambda v: isinstance(v, int),
            'float': lambda v: isinstance(v, float),
            'string': lambda v: isinstance(v, str),
            'char': lambda v: isinstance(v, str) and len(v) == 1,
            'bool': lambda v: isinstance(v, bool)
        }

        check = type_checks.get(declared_type)
        if check and not check(value):
            raise TypeMismatchError(declared_type, type(value).__name__, var_name, line)

    def _print_var_info(self, line, var_name, value, actual_type):
        print(f"└─[LINE {line}] VAR")
        print(f"│   ├─ name:     {var_name}")
        print(f"│   ├─ value:    {value}")
        print(f"│   └─ type:     {actual_type}")

    def visitAssignExpr(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expr())

        if var_name in self.types:
            expected = self.types[var_name]
            if expected == 'int' and isinstance(value, float):
                raise TypeError(f"Type error: cannot assign float '{value}' to int '{var_name}'")
        else:
            raise NameError(f"Undeclared variable '{var_name}'")

        self.vars[var_name] = value
        return value

    def visitAddSub(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))
        return left + right if op == '+' else left - right

    def visitMulDivMod(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        op_token = ctx.getChild(1).symbol.type
        right = self.visit(ctx.getChild(2))

        operations = {
            SASLexer.MULT: lambda l, r: l * r,
            SASLexer.DIV: lambda l, r: l / r,
            SASLexer.MOD: lambda l, r: l % r
        }

        if op_token in operations:
            return operations[op_token](left, right)

        raise UnsupportedOperationError(ctx.getChild(1).getText(), type(left).__name__, ctx.start.line)

    def visitCompareExpr(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        op_node = ctx.getChild(1)
        op_token = op_node.symbol.type
        op_text = op_node.getText()

        print(f"└─[COMPARE] {left} {op_text} {right}")

        return self._evaluate_comparison(op_token, op_text, left, right, ctx)

    def _evaluate_comparison(self, token_type, token_text, left, right, ctx):
        ops = {
            SASLexer.EQ: lambda l, r: l == r,
            SASLexer.NEQ: lambda l, r: l != r,
            SASLexer.LT: lambda l, r: l < r,
            SASLexer.LEQ: lambda l, r: l <= r,
            SASLexer.GT: lambda l, r: l > r,
            SASLexer.GEQ: lambda l, r: l >= r,
        }
        op_func = ops.get(token_type)
        if op_func:
            return op_func(left, right)

        raise UnsupportedOperationError(token_text, type(left).__name__, ctx.start.line)

    def visitIdExpr(self, ctx: SASParser.IdExprContext):
        name = ctx.IDENTIFIER().getText()
        return self.vars.get(name, 0)

    def visitLiteralExpr(self, ctx):
        text = ctx.getText()
        token_type = ctx.start.type

        parser = self._get_literal_parser(token_type, ctx)
        if parser:
            return parser(text)

        raise SemanticError(f"Unsupported literal: {text}", ctx.start.line)

    def _get_literal_parser(self, token_type, ctx):
        return {
            SASLexer.TRUE: lambda _: True,
            SASLexer.FALSE: lambda _: False,
            SASLexer.STRING_LITERAL: lambda t: t.strip('"'),
            SASLexer.CHAR_LITERAL: lambda t: self._parse_char_literal(t, ctx),
            SASLexer.FLOAT_LITERAL: float,
            SASLexer.SCIENTIFIC_LITERAL: float,
            SASLexer.INTEGER_LITERAL: int,
            SASLexer.HEX_LITERAL: lambda t: int(t, 16),
            SASLexer.BINARY_LITERAL: lambda t: int(t, 2),
            SASLexer.OCTAL_LITERAL: lambda t: int(t, 8),
        }.get(token_type)

    def _parse_char_literal(self, t, ctx):
        stripped = t.strip("'")
        if len(stripped) != 1:
            raise SemanticError(f"Invalid char literal: {t}", ctx.start.line)
        return stripped

    def visitIfStatement(self, ctx):
        matched = self._handle_branch(ctx.ifBlock(), "IF")

        for elif_ctx in ctx.elseIfBlock():
            _ = self._handle_branch(elif_ctx, "ELSE IF") if not matched else self._print_branch_info_only(elif_ctx, "ELSE IF")

        if ctx.elseBlock():
            self._handle_else(ctx.elseBlock(), matched)

    def _handle_branch(self, branch_ctx, label):
        line = self._get_branch_line(branch_ctx)
        expr_text = self._get_expr_text(branch_ctx)
        condition_value, condition_type = self._evaluate_and_validate_condition(branch_ctx, label, line)

        self._print_condition_info(line, label, expr_text, condition_value, "conditional")

        if condition_value:
            self._execute_branch_block(branch_ctx)
            return True
        return False

    def _print_branch_info_only(self, branch_ctx, label):
        line = self._get_branch_line(branch_ctx)
        expr_text = self._get_expr_text(branch_ctx)
        print(f"└─[LINE {line}] {label}")
        print(f"│   ├─ condition:   {expr_text}")
        print(f"│   ├─ result:      False")
        print(f"│   └─ type:        conditional")

    def _get_branch_line(self, branch_ctx):
        return branch_ctx.start.line

    def _get_expr_text(self, branch_ctx):
        return branch_ctx.expr().getText()

    def _evaluate_and_validate_condition(self, branch_ctx, label, line):
        condition_value = self._evaluate_condition(branch_ctx)
        condition_type = type(condition_value).__name__
        self._validate_condition_type(condition_value, condition_type, label, line)
        return condition_value, condition_type

    def _execute_branch_block(self, branch_ctx):
        block = branch_ctx.block()
        self._execute_conditional_block(block)

    def _evaluate_condition(self, branch_ctx):
        return self.visit(branch_ctx.expr())

    def _print_condition_info(self, line, label, expr_text, result, result_type):
        print(f"└─[LINE {line}] {label}")
        print(f"│   ├─ condition:   {expr_text}")
        print(f"│   ├─ result:      {result}")
        print(f"│   └─ type:        {result_type}")

    def _validate_condition_type(self, value, value_type, label, line):
        if not isinstance(value, bool):
            raise TypeMismatchError('bool', value_type, f'<{label.lower()} condition>', line)

    def _handle_else(self, else_ctx, was_matched):
        line = else_ctx.start.line
        print(f"└─[LINE {line}] ELSE")
        print(f"│   └─ type:        conditional")
        if not was_matched:
            self._execute_conditional_block(else_ctx.block())

    def _execute_conditional_block(self, block_ctx):
        self.in_conditional_block = True
        for stmt in block_ctx.statement():
            result = self.visit(stmt)
            if result is not None:
                line = stmt.start.line
                print(f"[exec] Result at LINE {line}: {result} ({type(result).__name__})")
        self.in_conditional_block = False

    def visitWhileLoop(self, ctx):
        line = ctx.start.line
        print(f"└─[LINE {line}] WHILE")
        print(f"│   └─ condition:   {ctx.expr().getText()}")
        self.in_conditional_block = True
        while self.visit(ctx.expr()):
            for stmt in ctx.block().statement():
                result = self.visit(stmt)
                if result is not None:
                    print(f"[exec] Result at LINE {stmt.start.line}: {result} ({type(result).__name__})")
        self.in_conditional_block = False

    def visitForLoop(self, ctx):
        line = ctx.start.line
        print(f"└─[LINE {line}] FOR")
        self.visit(ctx.exprStatement(0))  # init
        self.in_conditional_block = True
        while self.visit(ctx.exprStatement(1)):
            for stmt in ctx.block().statement():
                result = self.visit(stmt)
                if result is not None:
                    print(f"[exec] Result at LINE {stmt.start.line}: {result} ({type(result).__name__})")
            self.visit(ctx.expr())  # increment
        self.in_conditional_block = False

    def visitBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitExprStatement(self, ctx: SASParser.ExprStatementContext):
        return self.visit(ctx.expr())

    def visitProgram(self, ctx: SASParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
