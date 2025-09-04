# ast_nodes.py
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Union, Tuple

Span = Tuple[int, int]  # (line, column)


# ---------- base ----------
@dataclass
class Node:
    span: Span


# ---------- top level ----------
@dataclass
class Program(Node):
    items: List[Node]  # Preprocessor | ClassDecl | FuncDecl | Stmt | VarDecl


@dataclass
class Preprocessor(Node):
    text: str


# ---------- declarations ----------
@dataclass
class VarDecl(Node):
    typ: str
    name: str
    init: Optional["Expr"]


@dataclass
class Param(Node):
    typ: str
    name: str


@dataclass
class FuncDecl(Node):
    ret_type: str
    name: str
    params: List[Param]
    body: "Block"


@dataclass
class ClassDecl(Node):
    name: str
    # Allow both styles: either members already filtered (var/func),
    # or a generic list when you still use `block` as class body.
    members: List[Union[VarDecl, FuncDecl]]


# ---------- statements ----------
class Stmt(Node):
    pass


@dataclass
class Block(Stmt):
    items: List[Union[VarDecl, Stmt]]


@dataclass
class ReturnStmt(Stmt):
    value: Optional["Expr"]


@dataclass
class IfStmt(Stmt):
    cond: "Expr"
    then_block: Block
    elifs: List[tuple["Expr", Block]]
    else_block: Optional[Block]


@dataclass
class ForStmt(Stmt):
    init: Stmt                # usually ExprStmt (you can extend to allow VarDecl)
    cond: "Expr"
    step: "Expr"
    body: Block


@dataclass
class WhileStmt(Stmt):
    cond: "Expr"
    body: Block


@dataclass
class ExprStmt(Stmt):
    expr: "Expr"


# ---------- expressions ----------
class Expr(Node):
    pass


@dataclass
class Assign(Expr):
    name: str
    op: str             # '=', '+=', '-=', '*=', '/=', '%='
    value: Expr


@dataclass
class Binary(Expr):
    op: str             # '||','&&','|','^','&','<<','>>','==','!=','<','<=','>','>=','+','-','*','/','%'
    left: Expr
    right: Expr


@dataclass
class Unary(Expr):
    op: str             # '+','-','!','~','++','--'
    expr: Expr
    postfix: bool = False  # True for i++/i--


@dataclass
class Call(Expr):
    callee: str
    args: List[Expr]


@dataclass
class Identifier(Expr):
    name: str


@dataclass
class Literal(Expr):
    value: Union[int, float, str, bool]
