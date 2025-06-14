grammar Expr;

prog: statement* EOF ;

statement: varDecl
         | otherStatements
         ;

varDecl: type ID ('=' expr)? ';' ;  // Variable declaration (optional initialization)

type: 'int' | 'float' | 'double' | 'char' | 'bool' | 'string' ;

expr: INT                           # Int
    | ID                            # Var
    ;

INT : [0-9]+ ;
ID : [a-zA-Z_][a-zA-Z0-9_]* ;
WS  : [ \t\r\n]+ -> skip ;  // Ignore whitespace
