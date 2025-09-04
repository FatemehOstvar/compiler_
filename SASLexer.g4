lexer grammar SASLexer;


TRUE  : 'true';
FALSE : 'false';
BOOL  : 'bool';
INT : 'int';
FLOAT : 'float';
DOUBLE : 'double';
CHAR : 'char';
STRING : 'string';
ELSIF: 'elsif';
IF : 'if';
ELSE : 'else';
FOR : 'for';
WHILE : 'while';
RETURN : 'return';
CLASS : 'class';
VOID : 'void';

// Assignment Operators
ASSIGNMENT_OPERATOR
    : '+='
    | '-='
    | '*='
    | '/='
    | '%='
    ;


// Comparison Operators
GT  : '>';
LT  : '<';
EQ  : '==';
NEQ : '!=';
GEQ : '>=';
LEQ : '<=';


// Logical Operators
LOGICAL_OPERATOR
    : '&&'
    | '||'
    | '!'
    ;
// Mathematical Operators
MATHEMATICAL_OPERATOR
    : '++'
    | '--'
    ;

MULT : '*';
DIV  : '/';
ASSIGN : '=';
PLUS : '+';
MINUS : '-';
SEMI : ';';
COMMA : ',';
LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
MOD : '%';


// Bitwise Operators
BITWISE_OPERATOR
    : '&'
    | '|'
    | '^'
    | '~'
    | '<<'
    | '>>'
    ;




IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]*;

PREPROCESSOR_DIRECTIVE : '#' ~[\r\n]* ;

OCTAL_LITERAL      : '0' [0-7]+;
SCIENTIFIC_LITERAL : [0-9]+ ('.' [0-9]*)? [eE] [+-]? [0-9]+;
FLOAT_LITERAL      : [0-9]+ '.' [0-9]* ([eE][+-]?[0-9]+)?;
INTEGER_LITERAL    : [0-9]+;
STRING_LITERAL     : '"' (~["\\] | '\\' .)* '"';
CHAR_LITERAL       : '\'' (~['\\] | '\\' .) '\'';
HEX_LITERAL        : '0x' [0-9a-fA-F]+;
BINARY_LITERAL     : '0b' [01]+;

BLOCK_COMMENT : '/*' .*? '*/' -> skip;
LINE_COMMENT : '//' ~[\r\n]* -> skip;

WS : [ \t\r\n]+ -> skip;
