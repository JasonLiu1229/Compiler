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
            |   expr bin_log_op expr
            |   un_log_op expr
            |   unary_op expr
            |   int
            |   var
            |   var assign expr
            |   var assign var
            |   var assign int
            |   cvar_decl assign expr
            |   cvar_decl assign var
            |   cvar_decl assign int
            |   cvar_decl assign float
            |   cvar_decl assign char
            |   cvar_decl
            |   pvar_decl
            |   pvar_decl assign addr_op
            |   var_decl assign expr
            |   var_decl assign var
            |   var_decl assign int
            |   var_decl assign float
            |   var_decl assign char
            |   var_decl
            ;

var         :   VAR_NAME;
cvar_decl   :   CONST TYPE VAR_NAME;
pvar_decl   :   TYPE '*' VAR_NAME;
var_decl    :   TYPE VAR_NAME;
int         :   INT;
float       :   FLOAT;
char        :   CHAR;
addr_op     :   ADDR_OP var;
binary_op   :   (MUL  | DIV | MOD);
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
ADDR_OP     :   '&';
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