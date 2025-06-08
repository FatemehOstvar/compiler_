lexer grammar SASLexer;

INT : 'int';
FLOAT : 'float';
DOUBLE : 'double';
CHAR : 'char';
BOOL : 'bool';
STRING : 'string';
IF : 'if';
ELSE : 'else';
FOR : 'for';
WHILE : 'while';
RETURN : 'return';
CLASS : 'class';

ASSIGN : '=';
PLUS : '+';
MINUS : '-';
STAR : '*';
SLASH : '/';
SEMI : ';';
COMMA : ',';
LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';

IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER : [0-9]+ ('.' [0-9]+)?;
WS : [ \t\r\n]+ -> skip;
