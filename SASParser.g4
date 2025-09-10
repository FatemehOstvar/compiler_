parser grammar SASParser;

options { tokenVocab = SASLexer; }

program
    : preprocessor* statement* EOF
    ;
returnStatement
    : RETURN expr SEMI
    ;

preprocessor
    : PREPROCESSOR_DIRECTIVE
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

elseIfBlock
    : ELSIF LPAREN expr RPAREN block
    ;

ifBlock
    : IF LPAREN expr RPAREN block
    ;

elseBlock
    : ELSE block
    ;

ifStatement
    : ifBlock elseIfBlock* elseBlock?
    ;

loopStatement
    : forLoop
    | whileLoop
    ;

forLoop
    : FOR LPAREN (exprStatement|varDecl) exprStatement expr RPAREN block
    ;

whileLoop
    : WHILE LPAREN expr RPAREN block
    ;

funcDecl
    : funcHeader block
    ;

funcHeader
    : (INT | FLOAT | DOUBLE | CHAR | BOOL | STRING | VOID ) IDENTIFIER LPAREN paramList? RPAREN
    ;

paramList
    : param (COMMA param)*
    ;

param
    : (INT | FLOAT | DOUBLE | CHAR | BOOL | STRING) IDENTIFIER
    ;

classDecl : CLASS IDENTIFIER  LBRACE classBody RBRACE  SEMI;

classBody
    : (varDecl | funcDecl)*
    ;

exprStatement
    : expr SEMI
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
