grammar Math;

math            :   incl_stat*  (instr | func_defn ((';')* | DELIM) | func_decl ((';')+ | DELIM) )* EOF
                ;

instr           :   declr ((';')+ | DELIM)
                |   array_decl ((';')+ | DELIM)
                |   expr ((';')+ | DELIM)
                |   assign ((';')+ | DELIM)
                |   scope
                ;

declr           :   CONST? TYPE (var_decl ',')* var_decl
                ;

// TODO: printf (modified) and scanf
printf          :   PRINTF '(' (rvar | rtype | print_val=STRING) ')'
                |   PRINTF '(' (format_string=SCANF_STRING | format_string=STRING) (',' (vars+=printf_arg ',')* vars+=printf_arg )? ')'
                ;

printf_arg      :   rvar
                |   rtype
                |   array_el
                |   deref
                |   STRING;

scanf           :   SCANF '(' (format_string=SCANF_STRING | format_string=STRING) ',' (ADDR? (vars+=scanf_arg) ',')* ADDR? vars+=scanf_arg ')'
                ;

scanf_arg       :   rvar
                |   deref
                |   array_el
                |   ADDR rvar
                |   ADDR deref
                ;

// Functions
param_list      :   params+=param_declr (',' params+=param_declr)*
                ;

param_declr     :   const=CONST? type=TYPE reference=ADDR? ptr+=STR* var=VAR_NAME (ASSIGN default=expr)?
                |   const=CONST? type=TYPE ptr+=STR* reference=ADDR? var=VAR_NAME (ASSIGN default=expr)?
                ;

func_defn       :   const=CONST? (type=TYPE | type=VOID) ptr+=STR* name=VAR_NAME '(' params=param_list? ')' func_scope
                ;

func_decl       :   const=CONST? (type=TYPE | type=VOID) ptr+=STR* name=VAR_NAME '(' params=param_list? ')'
                ;

arg_list        :   args+=func_arg (',' args+=func_arg)*?
                ;
func_arg        :   rvar
                |   deref
                |   func_call
                |   rtype
                ;

func_call       :   name=VAR_NAME '(' args=arg_list? ')'
                ;

func_scope      :   '{'(
                        printf ((';')+ | DELIM) | scanf ((';')+ | DELIM) | return_instr | if_cond ((';')* | DELIM)
                        | while_loop ((';')* | DELIM) | for_loop ((';')* | DELIM) | assign ((';')+ | DELIM) | instr
                           )* '}'
                ;

return_instr    :   RETURN (ret_val=expr)? ';' (instr | return_instr)*
                ;


scope           :   '{' (
                        printf ((';')+ | DELIM) | scanf ((';')+ | DELIM) | return_instr | if_cond ((';')* | DELIM)
                        | while_loop ((';')* | DELIM) | for_loop ((';')* | DELIM) | assign ((';')+ | DELIM)
                        | break_instr | cont_instr | instr
                        )* '}'
                ;

cont_instr      :   CONTINUE (';' | DELIM) instr*
                ;

break_instr     :   BREAK (';' | DELIM) instr*
                ;

array_decl      :   const=CONST? type=TYPE ptr+=STR* name=VAR_NAME '[' size=INT? ']' ASSIGN '{' (values+=rtype ',')* values+=rtype '}'
                |   const=CONST? type=TYPE ptr+=STR* name=VAR_NAME '[' size=INT ']'
                ;

incl_stat       :   INCLUDE LT library=VAR_NAME '.h' GT
                ;


// TODO: break and continue
// TODO: switch(case, break, default) -> translate switch to if

if_cond         :   IF '(' condition=cond ')' scope else_cond?
                ;

else_cond       :   ELSE scope
                ;

while_loop      :   WHILE '(' condition=cond ')' scope
                ;

for_loop        :   FOR '(' initialization=init ';' condition=cond ';' increment=incr ')' scope
                ;

init            :   TYPE lvar ASSIGN expr
                |   assign;

cond            :   term (GEQ | LEQ | NEQ) factor
                |   term (GT | LT | EQ) factor
                |   expr (AND_OP | OR_OP) term
                |   expr
                ;

incr            :   INCR rvar
                |   DECR rvar
                |   rvar INCR
                |   rvar DECR
                ;

// Right-hand side variable use
var_decl        :   lvar ASSIGN expr
                |   lvar
                ;

assign          :   rvar ASSIGN expr
                |   deref ASSIGN expr
                |   array_el ASSIGN expr
                ;

array_el        :   lvar '[' INT ']';

deref           :   STR deref
                |   STR rvar
                ;

lvar            :   ptr+=STR* name=VAR_NAME
                ;

rvar            :   VAR_NAME
                ;

expr            :   term
                |   expr SUM term
                |   expr DIF term
                |   expr (AND_OP | OR_OP) term
                ;

term            :   factor
                |   term (STR | DIV | MOD) factor
                |   term (GT | LT | EQ) factor
                |   term (GEQ | LEQ | NEQ) factor
                |   (NOT_OP) factor
                |   term (INCR | DECR)
                ;

factor          :   primary
                |   DIF factor
                |   SUM factor
                |   (INCR | DECR) factor
                ;

primary         :   rvar
                |   rtype
                |   ADDR rvar
                |   deref
                |   '(' expr ')'
                |   CAST primary
                |   func_call
                |   array_el
                ;

rtype           :   INT
                |   FLOAT
                |   CHAR
//                |   STRING
                ;


// Keywords
CAST            :   '(' TYPE ')';
CONST           :   'const';
IF              :   'if';
ELSE            :   'else';
FOR             :   'for';
WHILE           :   'while';
BREAK           :   'break';
CONTINUE        :   'continue';
SWITCH          :   'switch';
CASE            :   'case';
DEFAULT         :   'default';
PRINTF          :   'printf';
RETURN          :   'return';
SCANF           :   'scanf';
INCLUDE         :   '#include';
// Identifiers and data types
TYPE            :   'char'
                |   'float'
                |   'int'
                ;
VOID            :   'void' ;
VAR_NAME        :   ([a-z] | [A-Z] | '_')([a-z] | [A-Z] | [0-9] | '_')*;             // match lower-case identifiers
INT             :   ([1-9][0-9]*) | [0];
FLOAT           :   [0-9]+ '.' [0-9]+;
CHAR            :   ('\'' . '\'')
                |   ('\'\\' . '\'');
SCANF_STRING    :   '"' ('%' ('-' | '+')? (INT)? [disc])* '"';
STRING          :   '"' (.)*? '"';
// Operations
STR             :   '*';
DIV             :   '/';
MOD             :   '%';
SUM             :   '+';
DIF             :   '-';
LT              :   '<';
LEQ             :   '<=';
GT              :   '>';
GEQ             :   '>=';
EQ              :   '==';
NEQ             :   '!=';
OR_OP           :   '||';
AND_OP          :   '&&';
NOT_OP          :   '!';
ASSIGN          :   '=';
ADDR            :   '&';
INCR            :   '++';
DECR            :   '--';
// Redundant characters to be removed
SP              :   [ ]+ -> skip;
NEWLINE         :   [\r\n]+ -> skip;
WS              :   [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
UNICODE_WS      :   [\p{White_Space}] -> skip; // match all Unicode whitespace
LN              :   [ \t\n]+ -> skip ; // skip spaces, tabs, newlines
DELIM           :   [;]+;
// Comments
// Ref : https://stackoverflow.com/a/23414078
COMMENT         :   '/*' .*? '*/' -> channel(HIDDEN);
LCOMMENT        :   '//' ~[\r\n]* -> channel(HIDDEN);