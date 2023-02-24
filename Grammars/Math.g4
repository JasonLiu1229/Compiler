grammar Math;
math        :   instr* EOF
            ;
instr       :   expr ';'
            ;
expr        :   '(' expr ')'
            |   expr binary_op expr
            |   expr unary_op expr
            |   expr comp_op expr
            |   expr comp_eq expr
            |   expr log_op expr
            |   unary_op expr
            |   int
            |   id
            |   id assign id
            |   id assign int
            |   id assign expr
            ;
id          :   ID;
int         :   INT;
binary_op   :   (MUL  | DIV | MOD);
unary_op    :   (SUM | DIF);
comp_op     :   (GT | LT | EQ);
comp_eq     :   (GEQ | LEQ | NEQ);
log_op      :   (AND_OP | OR_OP | NOT_OP);
assign      :   ASSIGN;
// Identifiers and data types
ID          :   ([a-z] | [A-Z])+ ;             // match lower-case identifiers
INT         :   [0-9]+;
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