grammar Math;
math        :   expr EOF
            |   expr ';'
            ;
expr        :   '(' expr ')'
            |   expr op expr
            |   expr unop expr
            |   expr comp_op expr
            |   expr comp_eq expr
            |   expr logop expr
            |   INT
            |   NEGINT
            |   ID
            |   ID ASSIGN ID
            |   ID ASSIGN INT
            ;
op          :   (MUL  | DIV | MOD );
unop        :   (SUM | DIF);
comp_op     :   (GT | LT | EQ);
comp_eq     :    (GEQ | LEQ | NEQ);
logop       :   (AND_OP | OR_OP | NOT_OP) ;
// Identifiers and data types
ID          :   ([a-z] | [A-Z])+ ;             // match lower-case identifiers
INT         :   [0-9]+;
NEGINT      :   '-'INT;
// Operations
MUL         :   '*';
DIV         :   '/';
MOD         :   '%';
SUM         :   '+';
DIF         :   '-';
LT          :   '<';
LEQ         :   '<=';
GT          :   '>';
GEQ         :   '>=';
EQ          :   '==';
NEQ         :   '!=';
OR_OP       :   '||';
AND_OP      :   '&&';
NOT_OP      :   '!';
ASSIGN      :   '=';
// Redundant characters to be removed
SP          :   [ ]+ -> skip;
NEWLINE     :   [\r\n]+ -> skip;
WS          :   [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
LN          :   [ \t\n]+ -> skip ; // skip spaces, tabs, newlines

/*
(mandatory) Unary operators + and -.
(mandatory) Binary operations +, -, *, and /.
(mandatory) Binary operations >, <, and ==.
(optional) Comparison operators >=, <=, and !=.
(mandatory) Brackets to overwrite the order of operations.
(mandatory) Logical operators &&, ||, and !.
(optional) Binary operator %.
*/