grammar Math;
math        :   instr* EOF
            ;
instr       :   declr ';'
            |   expr ';'
            ;
declr       :   CONST? TYPE (var_decl ',')* var_decl
            ;

// Right-hand side variable use
var_decl    :   lvar
            |   lvar assign expr
            ;

deref       :   STR+ rvar;
rvar        :   VAR_NAME;
lvar        :   STR* VAR_NAME;

expr        :   '(' expr ')'
            |   expr binary_op expr
            |   expr unary_op expr
            |   expr comp_op expr
            |   expr comp_eq expr
            |   expr bin_log_op expr
            |   un_log_op expr
            |   unary_op expr
            |   int
            |   rvar
            |   rvar assign expr
            |   rvar assign rvar
            |   rvar assign int
            ;

int         :   INT;
float       :   FLOAT;
char        :   CHAR;
addr_op     :   ADDR rvar;
binary_op   :   (STR  | DIV | MOD);
unary_op    :   (SUM | DIF);
comp_op     :   (GT | LT | EQ);
comp_eq     :   (GEQ | LEQ | NEQ);
bin_log_op  :   (AND_OP | OR_OP);
un_log_op   :   (NOT_OP);
assign      :   ASSIGN;
// Keywords
CONST       :   'const';
// Identifiers and data types
TYPE        :   'char'
            |   'float'
            |   'int'
            ;
VAR_NAME    :   ([a-z] | [A-Z] | '_')([a-z] | [A-Z] | [0-9] | '_')*;             // match lower-case identifiers
INT         :   [0-9]+;
FLOAT       :   INT '.' INT;
CHAR        :   '\'' . '\'';
// Operations
STR         :   '*';
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
ADDR     :   '&';
// Redundant characters to be removed
SP          :   [ ]+ -> skip;
NEWLINE     :   [\r\n]+ -> skip;
WS          :   [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
LN          :   [ \t\n]+ -> skip ; // skip spaces, tabs, newlines
// Comments
// Ref : https://stackoverflow.com/a/23414078
COMMENT     : '/*' .*? '*/' -> channel(HIDDEN);
LCOMMENT    : '//' ~[\r\n]* -> channel(HIDDEN);
/*
(mandatory) Unary operators + and -.
(mandatory) Binary operations +, -, *, and /.
(mandatory) Binary operations >, <, and ==.
(optional) Comparison operators >=, <=, and !=.
(mandatory) Brackets to overwrite the order of operations.
(mandatory) Logical operators &&, ||, and !.
(optional) Binary operator %.
*/