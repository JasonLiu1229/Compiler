grammar Math;

math        :   instr* EOF
            ;
instr       :   declr ';'
            |   expr ';'
            |   printf ';'
//            |   scope
//            |   if_cond
//            |   else_cond
//            |   while_loop
//            |   for_loop
            ;
declr       :   CONST? TYPE (var_decl ',')* var_decl
            ;

printf      :   PRINTF '(' (rvar | rtype | deref) ')';

// TODO: scopes (unnamed)
//scope       :   '{' instr* '}';

// TODO: if , else
//if_cond     :   IF expr scope;
//else_cond   :   ELSE scope;
//while_loop  :   WHILE expr scope;
//for_loop    :   FOR (expr ';' expr ';' (incr | decr) ) scope;

// TODO: for , while , break and continue -> translate while to for

// TODO: switch(case, break, default) -> translate switch to if

// Right-hand side variable use
var_decl    :   lvar assign addr_op
            |   lvar assign expr
            |   lvar
            ;

deref       :   STR deref
            |   STR rvar
            ;

lvar        :   STR* VAR_NAME;
rvar        :   VAR_NAME;

expr        :   '(' expr ')'
            |   cast expr
            |   expr binary_op expr
            |   expr unary_op expr
            |   expr comp_op expr
            |   expr comp_eq expr
            |   expr bin_log_op expr
            |   un_log_op expr
            |   unary_op expr
            |   decr rvar
            |   incr rvar
            |   rvar decr
            |   rvar incr
            |   rvar assign expr
            |   rvar assign rvar
            |   rvar assign rtype
            |   rvar assign addr_op
            |   rvar assign deref
            |   deref assign expr
            |   deref assign rvar
            |   deref assign rtype
            |   deref assign deref
            |   deref assign addr_op
            |   deref
            |   rtype
            |   rvar
            ;

cast        :   CAST;

rtype       :   INT
            |   FLOAT
            |   CHAR
            |   STRING
            ;
addr_op     :   ADDR rvar;
binary_op   :   (STR  | DIV | MOD);
unary_op    :   (SUM | DIF);
incr        :   INCR;
decr        :   DECR;
comp_op     :   (GT | LT | EQ);
comp_eq     :   (GEQ | LEQ | NEQ);
bin_log_op  :   (AND_OP | OR_OP);
un_log_op   :   (NOT_OP);
assign      :   ASSIGN;

// Keywords
CAST        :   '(' TYPE ')';
CONST       :   'const';
IF          :   'if';
ELSE        :   'else';
FOR         :   'for';
WHILE       :   'while';
BREAK       :   'break';
CONTINUE    :   'continue';
SWITCH      :   'switch';
CASE        :   'case';
DEFAULT     :   'default';
PRINTF      :   'printf';
// Identifiers and data types
TYPE        :   'char'
            |   'float'
            |   'int'
            ;
VAR_NAME    :   ([a-z] | [A-Z] | '_')([a-z] | [A-Z] | [0-9] | '_')*;             // match lower-case identifiers
INT         :   [0-9]+;
FLOAT       :   INT '.' INT;
CHAR        :   '\'' . '\'';
STRING      :   '"' (.)*? '"';
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
ADDR        :   '&';
INCR        :   '++';
DECR        :   '--';
// Redundant characters to be removed
SP          :   [ ]+ -> skip;
NEWLINE     :   [\r\n]+ -> skip;
WS          :   [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
LN          :   [ \t\n]+ -> skip ; // skip spaces, tabs, newlines

// Comments
// Ref : https://stackoverflow.com/a/23414078
COMMENT     : '/*' .*? '*/' -> channel(HIDDEN);
LCOMMENT    : '//' ~[\r\n]* -> channel(HIDDEN);