parser grammar SASParser;

options { tokenVocab = SASLexer; }

program
    : (preprocessor | statement)* EOF
    ;

preprocessor
    : PREPROCESSOR_DIRECTIVE IDENTIFIER
    ;

statement
    : varDecl
    | ifStatement
    | loopStatement
    | funcDecl
    | classDecl
    | exprStatement
    ;

varDecl
    : (INT | FLOAT | DOUBLE | CHAR | BOOL | STRING_K) IDENTIFIER (ASSIGN expr)? SEMICOLON
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
    : (INT | FLOAT | DOUBLE | CHAR | BOOL | STRING_K ) IDENTIFIER LPAREN paramList? RPAREN
    ;

paramList
    : param (COMMA param)*
    ;

param
    : (INT | FLOAT | DOUBLE | CHAR | BOOL | STRING_K) IDENTIFIER
    ;

classDecl
    : CLASS IDENTIFIER LBRACE classBody RBRACE
    ;

classBody
    : (varDecl | funcDecl)*
    ;

exprStatement
    : expr SEMICOLON
    ;

expr
    : expr (PLUS | MINUS | MULT | DIV | MOD) expr    #mathExpr
    | LPAREN expr RPAREN                             #parenExpr
    | funcCall                                       #funcCallExpr
    | IDENTIFIER                                     #idExpr
    | literal                                        #literalExpr
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
    ;

block
    : LBRACE statement* RBRACE
    ;
