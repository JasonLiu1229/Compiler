# Generated from Math.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,134,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,5,0,
        28,8,0,10,0,12,0,31,9,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,84,8,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,
        2,106,8,2,10,2,12,2,109,9,2,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,
        12,0,1,4,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,5,1,0,9,11,1,0,12,
        13,3,0,14,14,16,16,18,18,3,0,15,15,17,17,19,19,1,0,20,22,138,0,29,
        1,0,0,0,2,34,1,0,0,0,4,83,1,0,0,0,6,110,1,0,0,0,8,112,1,0,0,0,10,
        116,1,0,0,0,12,119,1,0,0,0,14,121,1,0,0,0,16,123,1,0,0,0,18,125,
        1,0,0,0,20,127,1,0,0,0,22,129,1,0,0,0,24,131,1,0,0,0,26,28,3,2,1,
        0,27,26,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,32,
        1,0,0,0,31,29,1,0,0,0,32,33,5,0,0,1,33,1,1,0,0,0,34,35,3,4,2,0,35,
        36,5,1,0,0,36,3,1,0,0,0,37,38,6,2,-1,0,38,39,5,2,0,0,39,40,3,4,2,
        0,40,41,5,3,0,0,41,84,1,0,0,0,42,43,3,16,8,0,43,44,3,4,2,12,44,84,
        1,0,0,0,45,84,3,12,6,0,46,84,3,6,3,0,47,48,3,6,3,0,48,49,3,24,12,
        0,49,50,3,4,2,9,50,84,1,0,0,0,51,52,3,6,3,0,52,53,3,24,12,0,53,54,
        3,6,3,0,54,84,1,0,0,0,55,56,3,6,3,0,56,57,3,24,12,0,57,58,3,12,6,
        0,58,84,1,0,0,0,59,60,3,8,4,0,60,61,3,24,12,0,61,62,3,4,2,6,62,84,
        1,0,0,0,63,64,3,8,4,0,64,65,3,24,12,0,65,66,3,6,3,0,66,84,1,0,0,
        0,67,68,3,8,4,0,68,69,3,24,12,0,69,70,3,12,6,0,70,84,1,0,0,0,71,
        72,3,10,5,0,72,73,3,24,12,0,73,74,3,4,2,3,74,84,1,0,0,0,75,76,3,
        10,5,0,76,77,3,24,12,0,77,78,3,6,3,0,78,84,1,0,0,0,79,80,3,10,5,
        0,80,81,3,24,12,0,81,82,3,12,6,0,82,84,1,0,0,0,83,37,1,0,0,0,83,
        42,1,0,0,0,83,45,1,0,0,0,83,46,1,0,0,0,83,47,1,0,0,0,83,51,1,0,0,
        0,83,55,1,0,0,0,83,59,1,0,0,0,83,63,1,0,0,0,83,67,1,0,0,0,83,71,
        1,0,0,0,83,75,1,0,0,0,83,79,1,0,0,0,84,107,1,0,0,0,85,86,10,17,0,
        0,86,87,3,14,7,0,87,88,3,4,2,18,88,106,1,0,0,0,89,90,10,16,0,0,90,
        91,3,16,8,0,91,92,3,4,2,17,92,106,1,0,0,0,93,94,10,15,0,0,94,95,
        3,18,9,0,95,96,3,4,2,16,96,106,1,0,0,0,97,98,10,14,0,0,98,99,3,20,
        10,0,99,100,3,4,2,15,100,106,1,0,0,0,101,102,10,13,0,0,102,103,3,
        22,11,0,103,104,3,4,2,14,104,106,1,0,0,0,105,85,1,0,0,0,105,89,1,
        0,0,0,105,93,1,0,0,0,105,97,1,0,0,0,105,101,1,0,0,0,106,109,1,0,
        0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,5,1,0,0,0,109,107,1,0,0,
        0,110,111,5,6,0,0,111,7,1,0,0,0,112,113,5,4,0,0,113,114,5,5,0,0,
        114,115,5,6,0,0,115,9,1,0,0,0,116,117,5,5,0,0,117,118,5,6,0,0,118,
        11,1,0,0,0,119,120,5,7,0,0,120,13,1,0,0,0,121,122,7,0,0,0,122,15,
        1,0,0,0,123,124,7,1,0,0,124,17,1,0,0,0,125,126,7,2,0,0,126,19,1,
        0,0,0,127,128,7,3,0,0,128,21,1,0,0,0,129,130,7,4,0,0,130,23,1,0,
        0,0,131,132,5,23,0,0,132,25,1,0,0,0,4,29,83,105,107
    ]

class MathParser ( Parser ):

    grammarFileName = "Math.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "')'", "'const'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'*'", "'/'", 
                     "'%'", "'+'", "'-'", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'!='", "'||'", "'&&'", "'!'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "CONST", "TYPE", "VAR_NAME", "INT", "FLOAT", "MUL", 
                      "DIV", "MOD", "SUM", "DIF", "LT", "LEQ", "GT", "GEQ", 
                      "EQ", "NEQ", "OR_OP", "AND_OP", "NOT_OP", "ASSIGN", 
                      "SP", "NEWLINE", "WS", "LN", "COMMENT", "LCOMMENT" ]

    RULE_math = 0
    RULE_instr = 1
    RULE_expr = 2
    RULE_var = 3
    RULE_cvar_decl = 4
    RULE_var_decl = 5
    RULE_int = 6
    RULE_binary_op = 7
    RULE_unary_op = 8
    RULE_comp_op = 9
    RULE_comp_eq = 10
    RULE_log_op = 11
    RULE_assign = 12

    ruleNames =  [ "math", "instr", "expr", "var", "cvar_decl", "var_decl", 
                   "int", "binary_op", "unary_op", "comp_op", "comp_eq", 
                   "log_op", "assign" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    CONST=4
    TYPE=5
    VAR_NAME=6
    INT=7
    FLOAT=8
    MUL=9
    DIV=10
    MOD=11
    SUM=12
    DIF=13
    LT=14
    LEQ=15
    GT=16
    GEQ=17
    EQ=18
    NEQ=19
    OR_OP=20
    AND_OP=21
    NOT_OP=22
    ASSIGN=23
    SP=24
    NEWLINE=25
    WS=26
    LN=27
    COMMENT=28
    LCOMMENT=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MathParser.EOF, 0)

        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.InstrContext)
            else:
                return self.getTypedRuleContext(MathParser.InstrContext,i)


        def getRuleIndex(self):
            return MathParser.RULE_math

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath" ):
                listener.enterMath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath" ):
                listener.exitMath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath" ):
                return visitor.visitMath(self)
            else:
                return visitor.visitChildren(self)




    def math(self):

        localctx = MathParser.MathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_math)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 12532) != 0):
                self.state = 26
                self.instr()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(MathParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MathParser.ExprContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_instr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstr" ):
                listener.enterInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstr" ):
                listener.exitInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstr" ):
                return visitor.visitInstr(self)
            else:
                return visitor.visitChildren(self)




    def instr(self):

        localctx = MathParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.expr(0)
            self.state = 35
            self.match(MathParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.ExprContext)
            else:
                return self.getTypedRuleContext(MathParser.ExprContext,i)


        def unary_op(self):
            return self.getTypedRuleContext(MathParser.Unary_opContext,0)


        def int_(self):
            return self.getTypedRuleContext(MathParser.IntContext,0)


        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.VarContext)
            else:
                return self.getTypedRuleContext(MathParser.VarContext,i)


        def assign(self):
            return self.getTypedRuleContext(MathParser.AssignContext,0)


        def cvar_decl(self):
            return self.getTypedRuleContext(MathParser.Cvar_declContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MathParser.Var_declContext,0)


        def binary_op(self):
            return self.getTypedRuleContext(MathParser.Binary_opContext,0)


        def comp_op(self):
            return self.getTypedRuleContext(MathParser.Comp_opContext,0)


        def comp_eq(self):
            return self.getTypedRuleContext(MathParser.Comp_eqContext,0)


        def log_op(self):
            return self.getTypedRuleContext(MathParser.Log_opContext,0)


        def getRuleIndex(self):
            return MathParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MathParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 38
                self.match(MathParser.T__1)
                self.state = 39
                self.expr(0)
                self.state = 40
                self.match(MathParser.T__2)
                pass

            elif la_ == 2:
                self.state = 42
                self.unary_op()
                self.state = 43
                self.expr(12)
                pass

            elif la_ == 3:
                self.state = 45
                self.int_()
                pass

            elif la_ == 4:
                self.state = 46
                self.var()
                pass

            elif la_ == 5:
                self.state = 47
                self.var()
                self.state = 48
                self.assign()
                self.state = 49
                self.expr(9)
                pass

            elif la_ == 6:
                self.state = 51
                self.var()
                self.state = 52
                self.assign()
                self.state = 53
                self.var()
                pass

            elif la_ == 7:
                self.state = 55
                self.var()
                self.state = 56
                self.assign()
                self.state = 57
                self.int_()
                pass

            elif la_ == 8:
                self.state = 59
                self.cvar_decl()
                self.state = 60
                self.assign()
                self.state = 61
                self.expr(6)
                pass

            elif la_ == 9:
                self.state = 63
                self.cvar_decl()
                self.state = 64
                self.assign()
                self.state = 65
                self.var()
                pass

            elif la_ == 10:
                self.state = 67
                self.cvar_decl()
                self.state = 68
                self.assign()
                self.state = 69
                self.int_()
                pass

            elif la_ == 11:
                self.state = 71
                self.var_decl()
                self.state = 72
                self.assign()
                self.state = 73
                self.expr(3)
                pass

            elif la_ == 12:
                self.state = 75
                self.var_decl()
                self.state = 76
                self.assign()
                self.state = 77
                self.var()
                pass

            elif la_ == 13:
                self.state = 79
                self.var_decl()
                self.state = 80
                self.assign()
                self.state = 81
                self.int_()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 105
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 86
                        self.binary_op()
                        self.state = 87
                        self.expr(18)
                        pass

                    elif la_ == 2:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 89
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 90
                        self.unary_op()
                        self.state = 91
                        self.expr(17)
                        pass

                    elif la_ == 3:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 93
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 94
                        self.comp_op()
                        self.state = 95
                        self.expr(16)
                        pass

                    elif la_ == 4:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 97
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 98
                        self.comp_eq()
                        self.state = 99
                        self.expr(15)
                        pass

                    elif la_ == 5:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 101
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 102
                        self.log_op()
                        self.state = 103
                        self.expr(14)
                        pass

             
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_NAME(self):
            return self.getToken(MathParser.VAR_NAME, 0)

        def getRuleIndex(self):
            return MathParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = MathParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(MathParser.VAR_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cvar_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MathParser.CONST, 0)

        def TYPE(self):
            return self.getToken(MathParser.TYPE, 0)

        def VAR_NAME(self):
            return self.getToken(MathParser.VAR_NAME, 0)

        def getRuleIndex(self):
            return MathParser.RULE_cvar_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCvar_decl" ):
                listener.enterCvar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCvar_decl" ):
                listener.exitCvar_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCvar_decl" ):
                return visitor.visitCvar_decl(self)
            else:
                return visitor.visitChildren(self)




    def cvar_decl(self):

        localctx = MathParser.Cvar_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_cvar_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(MathParser.CONST)
            self.state = 113
            self.match(MathParser.TYPE)
            self.state = 114
            self.match(MathParser.VAR_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MathParser.TYPE, 0)

        def VAR_NAME(self):
            return self.getToken(MathParser.VAR_NAME, 0)

        def getRuleIndex(self):
            return MathParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MathParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(MathParser.TYPE)
            self.state = 117
            self.match(MathParser.VAR_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MathParser.INT, 0)

        def getRuleIndex(self):
            return MathParser.RULE_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)




    def int_(self):

        localctx = MathParser.IntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MathParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Binary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(MathParser.MUL, 0)

        def DIV(self):
            return self.getToken(MathParser.DIV, 0)

        def MOD(self):
            return self.getToken(MathParser.MOD, 0)

        def getRuleIndex(self):
            return MathParser.RULE_binary_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_op" ):
                listener.enterBinary_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_op" ):
                listener.exitBinary_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_op" ):
                return visitor.visitBinary_op(self)
            else:
                return visitor.visitChildren(self)




    def binary_op(self):

        localctx = MathParser.Binary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_binary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUM(self):
            return self.getToken(MathParser.SUM, 0)

        def DIF(self):
            return self.getToken(MathParser.DIF, 0)

        def getRuleIndex(self):
            return MathParser.RULE_unary_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_op" ):
                listener.enterUnary_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_op" ):
                listener.exitUnary_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_op" ):
                return visitor.visitUnary_op(self)
            else:
                return visitor.visitChildren(self)




    def unary_op(self):

        localctx = MathParser.Unary_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_unary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(MathParser.GT, 0)

        def LT(self):
            return self.getToken(MathParser.LT, 0)

        def EQ(self):
            return self.getToken(MathParser.EQ, 0)

        def getRuleIndex(self):
            return MathParser.RULE_comp_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp_op" ):
                listener.enterComp_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp_op" ):
                listener.exitComp_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp_op" ):
                return visitor.visitComp_op(self)
            else:
                return visitor.visitChildren(self)




    def comp_op(self):

        localctx = MathParser.Comp_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comp_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 344064) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_eqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GEQ(self):
            return self.getToken(MathParser.GEQ, 0)

        def LEQ(self):
            return self.getToken(MathParser.LEQ, 0)

        def NEQ(self):
            return self.getToken(MathParser.NEQ, 0)

        def getRuleIndex(self):
            return MathParser.RULE_comp_eq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp_eq" ):
                listener.enterComp_eq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp_eq" ):
                listener.exitComp_eq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp_eq" ):
                return visitor.visitComp_eq(self)
            else:
                return visitor.visitChildren(self)




    def comp_eq(self):

        localctx = MathParser.Comp_eqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comp_eq)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 688128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Log_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND_OP(self):
            return self.getToken(MathParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(MathParser.OR_OP, 0)

        def NOT_OP(self):
            return self.getToken(MathParser.NOT_OP, 0)

        def getRuleIndex(self):
            return MathParser.RULE_log_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog_op" ):
                listener.enterLog_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog_op" ):
                listener.exitLog_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog_op" ):
                return visitor.visitLog_op(self)
            else:
                return visitor.visitChildren(self)




    def log_op(self):

        localctx = MathParser.Log_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_log_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MathParser.ASSIGN, 0)

        def getRuleIndex(self):
            return MathParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MathParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(MathParser.ASSIGN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 13)
         




