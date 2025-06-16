parser grammar SASParser;

options { tokenVocab = SASLexer; }

program
    : (preprocessor | statement)* EOF
    ;
returnStatement
    : RETURN expr SEMI
    ;

preprocessor
    : PREPROCESSOR_DIRECTIVE IDENTIFIER
    ;

statement
    : returnStatement
    | varDecl
    | ifStatement
    | loopStatement
    | funcDecl
    | classDecl
    | exprStatement
    ;

varDecl
    : (INT | FLOAT | DOUBLE | CHAR | BOOL | STRING) IDENTIFIER (ASSIGN expr)? SEMI
    ;

ifStatement
    : ifBlock elseIfBlock* elseBlock?
    ;

ifBlock
    : IF LPAREN expr RPAREN block
    ;

elseIfBlock
    : ELSE IF LPAREN expr RPAREN block
    ;

elseBlock
    : ELSE block
    ;

loopStatement
    : forLoop
    | whileLoop
    ;

forLoop
    : FOR LPAREN exprStatement exprStatement expr RPAREN block
    ;

whileLoop
    : WHILE LPAREN expr RPAREN block
    ;

funcDecl
    : funcHeader block
    ;

funcHeader
    : (INT | FLOAT | DOUBLE | CHAR | BOOL | STRING ) IDENTIFIER LPAREN paramList? RPAREN
    ;

paramList
    : param (COMMA param)*
    ;

param
    : (INT | FLOAT | DOUBLE | CHAR | BOOL | STRING) IDENTIFIER
    ;

classDecl
    : CLASS IDENTIFIER LBRACE classBody RBRACE
    ;

classBody
    : (varDecl | funcDecl)*
    ;

exprStatement
    : { self._input.LA(1) != SASLexer.RETURN }? expr SEMI
    ;

expr
    : IDENTIFIER (ASSIGN | ASSIGNMENT_OPERATOR) expr     #assignExpr
    | logicOrExpr                                         #logicOrPass
    ;

logicOrExpr
    : logicAndExpr (LOGICAL_OPERATOR logicAndExpr)*      #logicalExpr
    ;

logicAndExpr
    : bitwiseExpr                                         #bitwisePass
    ;

bitwiseExpr
    : compareExpr (BITWISE_OPERATOR compareExpr)*
    ;

compareExpr
    : additiveExpr ((EQ | NEQ | GT | LT | GEQ | LEQ) additiveExpr)*
    ;

additiveExpr
    : multiplicativeExpr ((PLUS | MINUS) multiplicativeExpr)* #addSub
    ;

multiplicativeExpr
    : unaryExpr ((MULT | DIV | MOD) unaryExpr)*               #mulDivMod
    ;

unaryExpr
    : (PLUS | MINUS | LOGICAL_OPERATOR | BITWISE_OPERATOR)? primary #unaryOpExpr
    | primary                                                      #noUnary
    ;


primary
    : LPAREN expr RPAREN             #parenExpr
    | funcCall                       #funcCallExpr
    | IDENTIFIER                     #idExpr
    | literal                        #literalExpr
    ;

funcCall
    : IDENTIFIER LPAREN argList? RPAREN
    ;

argList
    : expr (COMMA expr)*
    ;

literal
    : INTEGER_LITERAL
    | FLOAT_LITERAL
    | STRING_LITERAL
    | CHAR_LITERAL
    | HEX_LITERAL
    | BINARY_LITERAL
    | OCTAL_LITERAL
    | SCIENTIFIC_LITERAL
    | TRUE
    | FALSE
    ;


block
    : LBRACE statement* RBRACE
    ;
