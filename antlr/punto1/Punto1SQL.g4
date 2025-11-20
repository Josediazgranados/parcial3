grammar Punto1SQL;

program
    : stmt* EOF
    ;

stmt
    : createStmt ';'            # CreateStmtLine
    | insertStmt ';'            # InsertStmtLine
    | selectStmt ';'            # SelectStmtLine
    | updateStmt ';'            # UpdateStmtLine
    | deleteStmt ';'            # DeleteStmtLine
    ;

createStmt
    : CREATE TABLE ID '(' colDef (',' colDef)* ')'
    ;

colDef
    : ID type_
    ;

type_
    : INT
    | STRING
    | BOOL
    ;

insertStmt
    : INSERT INTO ID '(' idList ')' VALUES '(' literalList ')'
    ;

selectStmt
    : SELECT selectList FROM ID whereClause?
    ;

selectList
    : '*'
    | idList
    ;

updateStmt
    : UPDATE ID SET assignList whereClause?
    ;

assignList
    : assign (',' assign)*
    ;

assign
    : ID '=' literal
    ;

deleteStmt
    : DELETE FROM ID whereClause?
    ;

whereClause
    : WHERE expr
    ;

idList
    : ID (',' ID)*
    ;

literalList
    : literal (',' literal)*
    ;

expr
    : expr AND expr            # AndExpr
    | ID '=' literal           # EqExpr
    | '(' expr ')'             # ParenExpr
    ;

literal
    : INTLIT
    | STRINGLIT
    | BOOLLIT
    ;

/////////////////////////////////////////////////////
// LEXER
/////////////////////////////////////////////////////
CREATE  : 'CREATE';
TABLE   : 'TABLE';
INSERT  : 'INSERT';
INTO    : 'INTO';
VALUES  : 'VALUES';
SELECT  : 'SELECT';
FROM    : 'FROM';
UPDATE  : 'UPDATE';
SET     : 'SET';
DELETE  : 'DELETE';
WHERE   : 'WHERE';
INT     : 'INT';
STRING  : 'STRING';
BOOL    : 'BOOL';
AND     : 'AND';

ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
INTLIT  : [0-9]+ ;
STRINGLIT : '"' (~["\r\n])* '"' ;
BOOLLIT : 'true' | 'false' ;

WS      : [ \t\r\n]+ -> skip ;
COMMENT : '--' ~[\r\n]* -> skip ;

