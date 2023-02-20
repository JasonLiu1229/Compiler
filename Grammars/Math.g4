grammar Math;
math    :   expr EOF ;
expr    :
;
INT     :   [0-9] ;
UNOP    :   ('+' | '-') ;
BINOP1  :   (UNOP | '*') ;
BINOP2  :   ('<' | '>' | '==') ;
LOGOP   :   ('&&' | '||') ;
WS      :   [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines