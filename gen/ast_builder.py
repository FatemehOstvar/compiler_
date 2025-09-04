# ast_builder.py
from __future__ import annotations
from typing import List, Optional

from SASParserVisitor import SASParserVisitor
from SASParser import SASParser
from SASLexer import SASLexer as L

from ast_nodes import *

def span_of(ctx) -> Span:
    return (ctx.start.line, ctx.start.column)


class SASAstBuilder(SASParserVisitor):
    """
    Pure builder: converts the ANTLR parse tree into our AST nodes.
    No evaluation. No side effects. Safe to run anywhere.
    """

    # ---------- program & preprocessor ----------
    def visitProgram(self, ctx: SASParser.ProgramContext) -> Program:
        items: List[Node] = []
        # program : (preprocessor | funcDecl | classDecl | statement)* EOF
        for i in range(ctx.getChildCount() - 1):  # skip EOF
            child = ctx.getChild(i)
            if hasattr(child, "accept"):
                node = child.accept(self)
                if node is None:
                    continue
                if isinstance(node, list):
                    items.extend(node)
                else:
                    items.append(node)
        return Program(span_of(ctx), items)

    def visitPreprocessor(self, ctx: SASParser.PreprocessorContext) -> Preprocessor:
        return Preprocessor(span_of(ctx), ctx.PREPROCESSOR_DIRECTIVE().getText())

    # ---------- declarations ----------
    def visitVarDecl(self, ctx: SASParser.VarDeclContext) -> VarDecl:
        typ = ctx.getChild(0).getText()
        name = ctx.IDENTIFIER().getText()
        init = self.visit(ctx.expr()) if ctx.expr() else None
        return VarDecl(span_of(ctx), typ, name, init)

    def visitFuncDecl(self, ctx: SASParser.FuncDeclContext) -> FuncDecl:
        header = ctx.funcHeader()
        ret_type = header.getChild(0).getText()
        name = header.IDENTIFIER().getText()
        params: List[Param] = []
        if header.paramList():
            for p in header.paramList().param():
                ptype = p.getChild(0).getText()
                pname = p.IDENTIFIER().getText()
                params.append(Param(span_of(p), ptype, pname))
        body = self.visit(ctx.block())
        return FuncDecl(span_of(ctx), ret_type, name, params, body)

    def visitClassDecl(self, ctx: SASParser.ClassDeclContext) -> ClassDecl:
        # You currently have: classDecl : CLASS IDENTIFIER block
        # If you later switch to classMember*, this still works (we'll just collect from members).
        name = ctx.IDENTIFIER().getText()
        members: List[Union[VarDecl, FuncDecl]] = []

        # If you update grammar to classMember*, prefer walking those:
        if hasattr(ctx, "classMember"):
            for m in ctx.classMember():
                node = m.accept(self)
                if isinstance(node, (VarDecl, FuncDecl)):
                    members.append(node)
        else:
            # Current grammar: harvest only var/func from the block (ignore statements)
            blk = self.visit(ctx.block())
            for it in blk.items:
                if isinstance(it, (VarDecl, FuncDecl)):
                    members.append(it)

        return ClassDecl(span_of(ctx), name, members)

    # ---------- blocks & statements ----------
    def visitBlock(self, ctx: SASParser.BlockContext) -> Block:
        # block : LBRACE statement* RBRACE
        items: List[Union[VarDecl, Stmt]] = []
        for s in ctx.statement():
            node = s.accept(self)
            if isinstance(node, list):
                items.extend(node)
            else:
                items.append(node)
        return Block(span_of(ctx), items)

    def visitReturnStatement(self, ctx: SASParser.ReturnStatementContext) -> ReturnStmt:
        value = self.visit(ctx.expr()) if ctx.expr() else None
        return ReturnStmt(span_of(ctx), value)

    def visitIfStatement(self, ctx: SASParser.IfStatementContext) -> IfStmt:
        ifblk = ctx.ifBlock()
        cond = self.visit(ifblk.expr())
        then_blk = self.visit(ifblk.block())

        elifs: List[tuple[Expr, Block]] = []
        for e in ctx.elseIfBlock():
            econd = self.visit(e.expr())
            eblk = self.visit(e.block())
            elifs.append((econd, eblk))

        else_blk = self.visit(ctx.elseBlock().block()) if ctx.elseBlock() else None
        return IfStmt(span_of(ctx), cond, then_blk, elifs, else_blk)

    def visitForLoop(self, ctx: SASParser.ForLoopContext) -> ForStmt:
        init_stmt = self.visit(ctx.exprStatement(0))   # ExprStmt
        cond_expr = self.visit(ctx.exprStatement(1).expr())
        step_expr = self.visit(ctx.expr())
        body_blk = self.visit(ctx.block())
        return ForStmt(span_of(ctx), init_stmt, cond_expr, step_expr, body_blk)

    def visitWhileLoop(self, ctx: SASParser.WhileLoopContext) -> WhileStmt:
        return WhileStmt(span_of(ctx), self.visit(ctx.expr()), self.visit(ctx.block()))

    def visitExprStatement(self, ctx: SASParser.ExprStatementContext) -> ExprStmt:
        return ExprStmt(span_of(ctx), self.visit(ctx.expr()))

    # ---------- expressions ----------
    # expr : IDENTIFIER (ASSIGN | ASSIGNMENT_OPERATOR) expr #assignExpr
    #      | logicOrExpr                                    #logicOrPass
    def visitAssignExpr(self, ctx: SASParser.AssignExprContext) -> Assign:
        name = ctx.IDENTIFIER().getText()
        op = ctx.getChild(1).getText()
        rhs = self.visit(ctx.expr())
        return Assign(span_of(ctx), name, op, rhs)

    # pass-through to the real logic-or visitor
    def visitLogicOrPass(self, ctx: SASParser.LogicOrPassContext):
        return self.visit(ctx.getChild(0))

    # logicOrExpr : logicAndExpr (OR_OP logicAndExpr)* #logicalExpr
    def visitLogicalExpr(self, ctx: SASParser.LogicalExprContext) -> Expr:
        node = self.visit(ctx.getChild(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()       # '||'
            rhs = self.visit(ctx.getChild(i + 1))
            node = Binary(span_of(ctx), op, node, rhs)
        return node

    # logicAndExpr : bitwiseOrExpr (AND_OP bitwiseOrExpr)*
    def visitLogicAndExpr(self, ctx: SASParser.LogicAndExprContext) -> Expr:
        node = self.visit(ctx.getChild(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()       # '&&'
            rhs = self.visit(ctx.getChild(i + 1))
            node = Binary(span_of(ctx), op, node, rhs)
        return node

    # bitwiseOrExpr  : bitwiseXorExpr (BITOR  bitwiseXorExpr)* ;
    def visitBitwiseOrExpr(self, ctx: SASParser.BitwiseOrExprContext) -> Expr:
        node = self.visit(ctx.getChild(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()       # '|'
            rhs = self.visit(ctx.getChild(i + 1))
            node = Binary(span_of(ctx), op, node, rhs)
        return node

    # bitwiseXorExpr : bitwiseAndExpr (BITXOR bitwiseAndExpr)* ;
    def visitBitwiseXorExpr(self, ctx: SASParser.BitwiseXorExprContext) -> Expr:
        node = self.visit(ctx.getChild(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()       # '^'
            rhs = self.visit(ctx.getChild(i + 1))
            node = Binary(span_of(ctx), op, node, rhs)
        return node

    # bitwiseAndExpr : shiftExpr (BITAND shiftExpr)* ;
    def visitBitwiseAndExpr(self, ctx: SASParser.BitwiseAndExprContext) -> Expr:
        node = self.visit(ctx.getChild(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()       # '&'
            rhs = self.visit(ctx.getChild(i + 1))
            node = Binary(span_of(ctx), op, node, rhs)
        return node

    # shiftExpr : compareExpr ((SHL | SHR) compareExpr)* ;
    def visitShiftExpr(self, ctx: SASParser.ShiftExprContext) -> Expr:
        node = self.visit(ctx.getChild(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()       # '<<' or '>>'
            rhs = self.visit(ctx.getChild(i + 1))
            node = Binary(span_of(ctx), op, node, rhs)
        return node

    # compareExpr : additiveExpr ((== | != | < | <= | > | >=) additiveExpr)* ;
    def visitCompareExpr(self, ctx: SASParser.CompareExprContext) -> Expr:
        node = self.visit(ctx.getChild(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()
            rhs = self.visit(ctx.getChild(i + 1))
            node = Binary(span_of(ctx), op, node, rhs)
        return node

    # additiveExpr : multiplicativeExpr ((PLUS | MINUS) multiplicativeExpr)* #addSub
    def visitAddSub(self, ctx: SASParser.AddSubContext) -> Expr:
        node = self.visit(ctx.getChild(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()       # '+' or '-'
            rhs = self.visit(ctx.getChild(i + 1))
            node = Binary(span_of(ctx), op, node, rhs)
        return node

    # multiplicativeExpr : unaryExpr ((MULT | DIV | MOD) unaryExpr)* #mulDivMod
    def visitMulDivMod(self, ctx: SASParser.MulDivModContext) -> Expr:
        node = self.visit(ctx.getChild(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()       # '*', '/', '%'
            rhs = self.visit(ctx.getChild(i + 1))
            node = Binary(span_of(ctx), op, node, rhs)
        return node

    # unaryExpr : (INC_OP|DEC_OP) unaryExpr
    #           | (PLUS|MINUS|NOT_OP|BITNOT) unaryExpr
    #           | postfixExpr
    def visitUnaryExpr(self, ctx: SASParser.UnaryExprContext) -> Expr:
        if ctx.getChildCount() == 2 and hasattr(ctx.getChild(0), "symbol"):
            op = ctx.getChild(0).getText()       # '++','--','+','-','!','~'
            rhs = self.visit(ctx.getChild(1))
            return Unary(span_of(ctx), op, rhs, postfix=False)
        return self.visit(ctx.postfixExpr())

    # postfixExpr : primary (INC_OP | DEC_OP)*
    def visitPostfixExpr(self, ctx: SASParser.PostfixExprContext) -> Expr:
        node = self.visit(ctx.primary())
        # fold a chain like: (((id)++)++)
        for i in range(1, ctx.getChildCount()):
            op = ctx.getChild(i).getText()       # '++' or '--'
            node = Unary(span_of(ctx), op, node, postfix=True)
        return node

    # ---------- primaries ----------
    def visitParenExpr(self, ctx: SASParser.ParenExprContext) -> Expr:
        return self.visit(ctx.expr())

    def visitFuncCallExpr(self, ctx: SASParser.FuncCallExprContext) -> Call:
        f = ctx.funcCall()
        name = f.IDENTIFIER().getText()
        args: List[Expr] = []
        if f.argList():
            for e in f.argList().expr():
                args.append(self.visit(e))
        return Call(span_of(ctx), name, args)

    def visitIdExpr(self, ctx: SASParser.IdExprContext) -> Identifier:
        return Identifier(span_of(ctx), ctx.IDENTIFIER().getText())

    def visitLiteralExpr(self, ctx: SASParser.LiteralExprContext) -> Literal:
        tok = ctx.start
        text = ctx.getText()

        def parse_char(t: str) -> str:
            s = t.strip("'")
            return s  # you can unescape if you like

        if tok.type == L.TRUE:  return Literal(span_of(ctx), True)
        if tok.type == L.FALSE: return Literal(span_of(ctx), False)
        if tok.type == L.STRING_LITERAL: return Literal(span_of(ctx), text.strip('"'))
        if tok.type == L.CHAR_LITERAL:   return Literal(span_of(ctx), parse_char(text))
        if tok.type == L.SCIENTIFIC_LITERAL: return Literal(span_of(ctx), float(text))
        if tok.type == L.FLOAT_LITERAL:      return Literal(span_of(ctx), float(text))
        if tok.type == L.INTEGER_LITERAL:    return Literal(span_of(ctx), int(text))
        if tok.type == L.HEX_LITERAL:        return Literal(span_of(ctx), int(text, 16))
        if tok.type == L.BINARY_LITERAL:     return Literal(span_of(ctx), int(text, 2))
        if tok.type == L.OCTAL_LITERAL:      return Literal(span_of(ctx), int(text, 8))

        # Fallback: store raw text
        return Literal(span_of(ctx), text)
