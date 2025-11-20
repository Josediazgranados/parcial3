grammar MatrixLang;

prog : expr EOF ;

expr : matrix '*' matrix ;

matrix
    : '[' row (',' row)* ']'
    ;

row
    : '[' NUMBER (',' NUMBER)* ']'
    ;

NUMBER : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;
