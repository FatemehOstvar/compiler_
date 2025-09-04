from SASParserVisitor import SASParserVisitor
from SASParser import SASParser
from SASLexer import SASLexer as L
from semantics import TypeMismatchError, SemanticError, UnsupportedOperationError

class SASEvaluator(SASParserVisitor):
    def __init__(self):
        self.vars = {}
        self.types = {}
        self.decl_lines = {}
        self.in_conditional_block = False
        self.functions = {}
        self.output_lines = []

    def _log(self, line):
        self.output_lines.append(line)
        print(line)

    def _log_event(self, category, line=None, **fields):
        self._log("│")
        line_label = f"[LINE {line}] " if line is not None else ""
        self._log(f"└─{line_label}{category}")
        items = list(fields.items( ))
        for i, (key, val) in enumerate(items):
            branch = "└─" if i == len(items) - 1 else "├─"
            self._log(f"│   {branch} {key:<10} {val}")

    def write_output(self, filename="output.txt"):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("\n".join(self.output_lines))
    def visitVarDecl(self, ctx):
        declared_type = self._extract_declared_type(ctx)
        var_name = self._extract_var_name(ctx)
        value = self._extract_value(ctx)
        line = ctx.start.line
        actual_type = self._determine_actual_type(declared_type)

        self._validate_declared_type(declared_type, value, var_name, line)
        self._register_variable(var_name, value, actual_type, line)
        self._log_event("VAR", line, name=var_name, value=value, type=actual_type)

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

    def visitUnaryOpExpr(self, ctx: SASParser.UnaryOpExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        op_token = ctx.getChild(0).getSymbol().type
        value = self.visit(ctx.getChild(1))

        if op_token == L.MINUS:
            return -value
        elif op_token == L.PLUS:
            return +value
        elif op_token == L.LOGICAL_OPERATOR and ctx.getChild(0).getText() == '!':
            return not value
        elif op_token == L.BITWISE_OPERATOR and ctx.getChild(0).getText() == '~':
            return ~value
        else:
            raise SemanticError(f"Line {ctx.start.line}: Unsupported unary operator: {ctx.getChild(0).getText()}", ctx.start.line)


    def visitAssignExpr(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expr())

        if var_name in self.types:
            expected = self.types[var_name]
            if expected == L.INT and isinstance(value, float):
                raise TypeError(f"Type error: cannot assign float '{value}' to int '{var_name}'")
        else:
            raise NameError(f"Undeclared variable '{var_name}'")

        self.vars[var_name] = value
        return value

    def visitAddSub(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        op_token = ctx.getChild(1).symbol.type
        right = self.visit(ctx.getChild(2))
        if op_token == L.PLUS:
            return left + right
        elif op_token == L.MINUS:
            return left - right
    def visitMulDivMod(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        op_token = ctx.getChild(1).symbol.type
        right = self.visit(ctx.getChild(2))

        operations = {
            L.MULT: lambda l, r: l * r,
            L.DIV: lambda l, r: l / r,
            L.MOD: lambda l, r: l % r
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
        line = ctx.start.line

        self._log_event("COMPARE", line=line, left=left, operator=op_text, right=right)

        return self._evaluate_comparison(op_token, op_text, left, right, ctx)

    def _evaluate_comparison(self, token_type, token_text, left, right, ctx):
        ops = {
            L.EQ: lambda l, r: l == r,
            L.NEQ: lambda l, r: l != r,
            L.LT: lambda l, r: l < r,
            L.LEQ: lambda l, r: l <= r,
            L.GT: lambda l, r: l > r,
            L.GEQ: lambda l, r: l >= r,
        }
        op_func = ops.get(token_type)
        if op_func:
            return op_func(left, right)

        raise UnsupportedOperationError(token_text, type(left).__name__, ctx.start.line)

    def visitIdExpr(self, ctx: SASParser.IdExprContext):
        name = ctx.IDENTIFIER().getText()
        return self.vars.get(name, 0)

    def visitFuncCallExpr(self, ctx):
        func_call = ctx.funcCall()
        func_name = func_call.IDENTIFIER().getText()
        args = [self.visit(arg) for arg in func_call.argList().expr()] if func_call.argList() else []
        arg_str = ", ".join(repr(a) for a in args)
        line = ctx.start.line

        self._log_event("CALL", line, expression=f"{func_name}({arg_str})")

        if func_name not in self.functions:
            raise SemanticError(f"Undefined function: {func_name}", line)

        expected_params = self.functions[func_name]['param_types']
        if len(args) != len(expected_params):
            raise SemanticError(f"Argument count mismatch for '{func_name}' (expected {len(expected_params)}, got {len(args)})", line)

        for i, (arg_val, expected_type) in enumerate(zip(args, expected_params)):
            if not self._matches_type(expected_type, arg_val):
                raise TypeMismatchError(expected_type, type(arg_val).__name__, f"arg{i+1}", line)

        return None

    def _matches_type(self, expected_type, value):
        type_checks = {
            L.INT: int,
            L.FLOAT: float,
            L.STRING: str,
            L.CHAR: str,
            L.BOOL: bool
        }
        if expected_type == L.CHAR:
            return isinstance(value, str) and len(value) == 1
        return isinstance(value, type_checks.get(expected_type, object))


    def visitLiteralExpr(self, ctx):
        text = ctx.getText()
        token_type = ctx.start.type

        parser = self._get_literal_parser(token_type, ctx)
        if parser:
            return parser(text)

        raise SemanticError(f"Unsupported literal: {text}", ctx.start.line)

    def _get_literal_parser(self, token_type, ctx):
        return {
            L.TRUE: lambda _: True,
            L.FALSE: lambda _: False,
            L.STRING_LITERAL: lambda t: t.strip('"'),
            L.CHAR_LITERAL: lambda t: self._parse_char_literal(t, ctx),
            L.FLOAT_LITERAL: float,
            L.SCIENTIFIC_LITERAL: float,
            L.INTEGER_LITERAL: int,
            L.HEX_LITERAL: lambda t: int(t, 16),
            L.BINARY_LITERAL: lambda t: int(t, 2),
            L.OCTAL_LITERAL: lambda t: int(t, 8),
        }.get(token_type)

    def _parse_char_literal(self, t, ctx):
        stripped = t.strip("'")
        if len(stripped) != 1:
            raise SemanticError(f"Invalid char literal: {t}", ctx.start.line)
        return stripped

    def visitFuncDecl(self, ctx):
        header = ctx.funcHeader()
        return_type = header.getChild(0).getText()
        name = header.IDENTIFIER().getText()
        params = header.paramList()
        line = ctx.start.line
        param_types = []

        if params:
            for param in params.param():
                ptype = param.getChild(0).getText()
                param_types.append(ptype)

        self.functions[name] = {
            'return_type': return_type,
            'param_types': param_types
        }

        if param_types:
            param_str = [f"{param.getChild(1).getText()}: {param.getChild(0).getText()}" for param in params.param()]
            self._log_event("FUNCTION", line, name=name, returns=return_type)
            self._log("│   └─ params:")
            for p in param_str:
                self._log(f"│       ├─ {p}")
        else:
            self._log_event("FUNCTION", line, name=name, returns=return_type, params="(none)")

    def visitIfStatement(self, ctx):
        matched = self._handle_branch(ctx.ifBlock(), L.IF)

        for elif_ctx in ctx.elseIfBlock( ):
            if not matched:
                matched = self._handle_branch(elif_ctx, L.ELSIF)
            else:
                self._print_branch_info_only(elif_ctx, L.ELSIF)

        if ctx.elseBlock() :
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

    def _print_branch_info_only(self, branch_ctx, label) -> bool:
        line = self._get_branch_line(branch_ctx)
        expr_text = self._get_expr_text(branch_ctx)

        self._log_event(
            category=label,
            line=line,
            condition=expr_text,
            result="False",
            type="conditional"
        )
        return True

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
        self._log_event(label, line, condition=expr_text, result=result, type=result_type)
    def _validate_condition_type(self, value, value_type, label, line):
        if not isinstance(value, bool):
            raise TypeMismatchError('bool', value_type, f'<{label.lower()} condition>', line)

    def _handle_else(self, else_ctx, was_matched):
        line = else_ctx.start.line
        self._log_event("ELSE", line, type="conditional")

        if  not was_matched:
            self._execute_conditional_block(else_ctx.block())

    def _execute_conditional_block(self, block_ctx):
        self.in_conditional_block = True
        for stmt in block_ctx.statement():
            result = self.visit(stmt)
            if result is not None:
                self.log_none_type(stmt,result)
        self.in_conditional_block = False


    def log_none_type(self,stmt,result):
        assign_text = stmt.getText( )
        self._log_event("EXEC", stmt.start.line, statement=assign_text, result=result, type=type(result).__name__)

    def visitWhileLoop(self, ctx):
        line = ctx.start.line
        self._log_event("WHILE", line, condition=ctx.expr().getText())

        self.in_conditional_block = True
        while self.visit(ctx.expr()):
            for stmt in ctx.block().statement():
                result = self.visit(stmt)
                if result is not None:
                    self.log_none_type(stmt,result)

        self.in_conditional_block = False

    def visitForLoop(self, ctx):
        line = ctx.start.line
        self._log_event("FOR", line)

        self.visit(ctx.exprStatement(0))  # init
        self.in_conditional_block = True
        while self.visit(ctx.exprStatement(1)):
            for stmt in ctx.block().statement():
                result = self.visit(stmt)
                if result is not None:
                    self.log_none_type(stmt,result)

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
        self.write_output()