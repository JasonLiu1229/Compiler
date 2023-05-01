grammar Math;

math        :   instr* EOF
            ;
instr       :   declr ((';')+ | DELIM)
            |   expr ((';')+ | DELIM)
            |   printf ((';')+ | DELIM)
            |   assign ((';')+ | DELIM)
            |   scope (';')*
            |   if_cond (';')*
            |   while_loop (';')*
            |   for_loop (';')*
            |   func_defn ((';')* | DELIM)
            |   func_decl ((';')+ | DELIM)
            |   func_call ((';')+ | DELIM)
            ;
declr       :   CONST? TYPE (var_decl ',')* var_decl
            ;

printf      :   PRINTF '(' (rvar | rtype | deref) ')';

// Functions
param_list      :   param_declr (',' param_declr)*
                ;

param_declr     :   const=CONST? type=TYPE reference=ADDR? pointer=STR* var_decl
                |   const=CONST? type=TYPE pointer=STR* reference=ADDR? var_decl
                ;

func_defn       :   CONST? (TYPE | VOID) STR* VAR_NAME '(' params=param_list? ')' func_scope
                ;

func_decl       :   CONST? (TYPE | VOID) STR* VAR_NAME '(' params=param_list? ')'
                ;

arg_list        :   (lvar | func_call | rtype) (',' (lvar | func_call | rtype))+?
                ;

func_call       :   VAR_NAME '(' arg_list? ')'
                ;

func_scope      :   '{'(return_instr | instr)* '}'
                ;

return_instr    :   RETURN (expr) ';' (instr | return_instr)*
                ;


scope       :   '{' ( instr | break_instr | cont_instr )* '}'
            ;

cont_instr  :   CONTINUE (';' | DELIM) instr*
            ;

break_instr :   BREAK (';' | DELIM) instr*
            ;

// TODO: for , while , break and continue -> translate for to while
// TODO: switch(case, break, default) -> translate switch to if

if_cond     :   IF '(' condition=cond ')' scope else_cond?
            ;

else_cond   :   ELSE scope
            ;

while_loop  :   WHILE '(' condition=cond ')' scope
            ;

for_loop    :   FOR '(' initialization=init ';' condition=cond ';' increment=incr ')' scope
            ;

init        :   TYPE lvar ASSIGN expr
            |   assign;

cond        :   term (GEQ | LEQ | NEQ) factor
            |   term (GT | LT | EQ) factor
            |   term (AND_OP | OR_OP) factor
            ;

incr        :   INCR rvar
            |   DECR rvar
            |   rvar INCR
            |   rvar DECR
            ;

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
            | func_call
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
RETURN      :   'return';
// Identifiers and data types
TYPE        :   'char'
            |   'float'
            |   'int'
            ;
VOID        :   'void' ;
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
UNICODE_WS  :   [\p{White_Space}] -> skip; // match all Unicode whitespace
LN          :   [ \t\n]+ -> skip ; // skip spaces, tabs, newlines
DELIM       :   [;]+;
// Comments
// Ref : https://stackoverflow.com/a/23414078
COMMENT     : '/*' .*? '*/' -> channel(HIDDEN);
LCOMMENT    : '//' ~[\r\n]* -> channel(HIDDEN);