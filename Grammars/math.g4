grammar math;
math    :   expr EOF ;
expr    :
;
UNOP    :   ('+' | '-') ;
BINOP1  :   (UNOP | '*') ;
BINOP2  :   ('<' | '>' | '==') ;
LOGOP   :   ('&&' | '||') ;
WS      :   [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines