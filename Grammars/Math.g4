grammar Math;

math        :   instr* EOF
            ;
instr       :   declr (';')+
            |   expr (';')+
            |   printf (';')+
            |   assign (';')+
            |   scope
            |   if_cond
            |   else_cond
            |   while_loop
            |   for_loop
            ;
declr       :   CONST? TYPE (var_decl ',')* var_decl
            ;

printf      :   PRINTF '(' (rvar | rtype | deref) ')';

// TODO: scopes (unnamed)
scope       :   '{' instr* '}';

// TODO: if , else
if_cond     :   IF expr scope;
else_cond   :   ELSE scope;
while_loop  :   WHILE expr scope;
for_loop    :   FOR (expr ';' expr ';' (INCR rvar | DECR  | rvar INCR | rvar DECR) ) scope;

// TODO: for , while , break and continue -> translate while to for

// TODO: switch(case, break, default) -> translate switch to if

// Right-hand side variable use
var_decl    :   lvar ASSIGN expr
            |   lvar
            ;

assign      :   rvar ASSIGN expr
            |   deref ASSIGN expr
            ;

deref       :   STR deref
            |   STR rvar
            ;

lvar        :   STR* VAR_NAME;
rvar        :   VAR_NAME;

expr        : term
            | expr SUM term
            | expr DIF term
            ;

term        : factor
            | term (STR | DIV | MOD) factor
            | term (GT | LT | EQ) factor
            | term (GEQ | LEQ | NEQ) factor
            | term (AND_OP | OR_OP) factor
            | (NOT_OP) factor
            | term (INCR | DECR)
            ;

factor      : primary
            | DIF factor
            | SUM factor
            | (INCR | DECR) factor
            ;

primary     : rvar
            | rtype
            | ADDR rvar
            | deref
            | '(' expr ')'
            | CAST primary
            ;

rtype       :   INT
            |   FLOAT
            |   CHAR
            |   STRING
            ;


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
INT         :   ([1-9][0-9]*) | [0];
FLOAT       :   [0-9]+ '.' [0-9]+;
CHAR        :   ('\'' . '\'')
            |   ('\'\\' . '\'');
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
DELIM       :   (';')+;
// Comments
// Ref : https://stackoverflow.com/a/23414078
COMMENT     : '/*' .*? '*/' -> channel(HIDDEN);
LCOMMENT    : '//' ~[\r\n]* -> channel(HIDDEN);