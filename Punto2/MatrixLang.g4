grammar MatrixLang;

program
    : statement* EOF
    ;

statement
    : matrixDecl ';'        # StmtMatrixDecl
    | assignStmt ';'        # StmtAssign
    | printStmt ';'         # StmtPrint
    ;

matrixDecl
    : 'matrix' ID '=' '[' row (',' row)* ']'
    ;

row
    : '[' NUMBER (',' NUMBER)* ']'
    ;

assignStmt
    : ID '=' expr
    ;

expr
    : ID '*' ID        # ExprMatrixMul
    | ID               # ExprVarRef
    ;

printStmt
    : 'print' '(' ID ')'
    ;

ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER  : [0-9]+ ('.' [0-9]+)? ;
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;

