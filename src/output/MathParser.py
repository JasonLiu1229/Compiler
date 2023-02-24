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
        4,1,25,97,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,52,8,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,
        74,8,2,10,2,12,2,77,9,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,
        1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,0,1,4,12,0,2,4,6,8,10,12,
        14,16,18,20,22,0,5,1,0,7,9,1,0,10,11,3,0,12,12,14,14,16,16,3,0,13,
        13,15,15,17,17,1,0,18,20,95,0,27,1,0,0,0,2,32,1,0,0,0,4,51,1,0,0,
        0,6,78,1,0,0,0,8,80,1,0,0,0,10,82,1,0,0,0,12,84,1,0,0,0,14,86,1,
        0,0,0,16,88,1,0,0,0,18,90,1,0,0,0,20,92,1,0,0,0,22,94,1,0,0,0,24,
        26,3,2,1,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,
        0,28,30,1,0,0,0,29,27,1,0,0,0,30,31,5,0,0,1,31,1,1,0,0,0,32,33,3,
        4,2,0,33,34,5,1,0,0,34,3,1,0,0,0,35,36,6,2,-1,0,36,37,5,2,0,0,37,
        38,3,4,2,0,38,39,5,3,0,0,39,52,1,0,0,0,40,52,3,8,4,0,41,52,3,10,
        5,0,42,52,3,6,3,0,43,44,3,6,3,0,44,45,3,22,11,0,45,46,3,6,3,0,46,
        52,1,0,0,0,47,48,3,6,3,0,48,49,3,22,11,0,49,50,3,8,4,0,50,52,1,0,
        0,0,51,35,1,0,0,0,51,40,1,0,0,0,51,41,1,0,0,0,51,42,1,0,0,0,51,43,
        1,0,0,0,51,47,1,0,0,0,52,75,1,0,0,0,53,54,10,10,0,0,54,55,3,12,6,
        0,55,56,3,4,2,11,56,74,1,0,0,0,57,58,10,9,0,0,58,59,3,14,7,0,59,
        60,3,4,2,10,60,74,1,0,0,0,61,62,10,8,0,0,62,63,3,16,8,0,63,64,3,
        4,2,9,64,74,1,0,0,0,65,66,10,7,0,0,66,67,3,18,9,0,67,68,3,4,2,8,
        68,74,1,0,0,0,69,70,10,6,0,0,70,71,3,20,10,0,71,72,3,4,2,7,72,74,
        1,0,0,0,73,53,1,0,0,0,73,57,1,0,0,0,73,61,1,0,0,0,73,65,1,0,0,0,
        73,69,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,5,1,0,
        0,0,77,75,1,0,0,0,78,79,5,4,0,0,79,7,1,0,0,0,80,81,5,5,0,0,81,9,
        1,0,0,0,82,83,5,6,0,0,83,11,1,0,0,0,84,85,7,0,0,0,85,13,1,0,0,0,
        86,87,7,1,0,0,87,15,1,0,0,0,88,89,7,2,0,0,89,17,1,0,0,0,90,91,7,
        3,0,0,91,19,1,0,0,0,92,93,7,4,0,0,93,21,1,0,0,0,94,95,5,21,0,0,95,
        23,1,0,0,0,4,27,51,73,75
    ]

class MathParser ( Parser ):

    grammarFileName = "Math.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'*'", "'/'", "'%'", "'+'", "'-'", "'<'", 
                     "'<='", "'>'", "'>='", "'=='", "'!='", "'||'", "'&&'", 
                     "'!'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "NEGINT", "MUL", "DIV", "MOD", "SUM", 
                      "DIF", "LT", "LEQ", "GT", "GEQ", "EQ", "NEQ", "OR_OP", 
                      "AND_OP", "NOT_OP", "ASSIGN", "SP", "NEWLINE", "WS", 
                      "LN" ]

    RULE_math = 0
    RULE_instr = 1
    RULE_expr = 2
    RULE_id = 3
    RULE_int = 4
    RULE_negint = 5
    RULE_binary_op = 6
    RULE_unary_op = 7
    RULE_comp_op = 8
    RULE_comp_eq = 9
    RULE_log_op = 10
    RULE_assign = 11

    ruleNames =  [ "math", "instr", "expr", "id", "int", "negint", "binary_op", 
                   "unary_op", "comp_op", "comp_eq", "log_op", "assign" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ID=4
    INT=5
    NEGINT=6
    MUL=7
    DIV=8
    MOD=9
    SUM=10
    DIF=11
    LT=12
    LEQ=13
    GT=14
    GEQ=15
    EQ=16
    NEQ=17
    OR_OP=18
    AND_OP=19
    NOT_OP=20
    ASSIGN=21
    SP=22
    NEWLINE=23
    WS=24
    LN=25

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
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 116) != 0):
                self.state = 24
                self.instr()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
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
            self.state = 32
            self.expr(0)
            self.state = 33
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


        def int_(self):
            return self.getTypedRuleContext(MathParser.IntContext,0)


        def negint(self):
            return self.getTypedRuleContext(MathParser.NegintContext,0)


        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MathParser.IdContext)
            else:
                return self.getTypedRuleContext(MathParser.IdContext,i)


        def assign(self):
            return self.getTypedRuleContext(MathParser.AssignContext,0)


        def binary_op(self):
            return self.getTypedRuleContext(MathParser.Binary_opContext,0)


        def unary_op(self):
            return self.getTypedRuleContext(MathParser.Unary_opContext,0)


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
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 36
                self.match(MathParser.T__1)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(MathParser.T__2)
                pass

            elif la_ == 2:
                self.state = 40
                self.int_()
                pass

            elif la_ == 3:
                self.state = 41
                self.negint()
                pass

            elif la_ == 4:
                self.state = 42
                self.id_()
                pass

            elif la_ == 5:
                self.state = 43
                self.id_()
                self.state = 44
                self.assign()
                self.state = 45
                self.id_()
                pass

            elif la_ == 6:
                self.state = 47
                self.id_()
                self.state = 48
                self.assign()
                self.state = 49
                self.int_()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 73
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 53
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 54
                        self.binary_op()
                        self.state = 55
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 57
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 58
                        self.unary_op()
                        self.state = 59
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 62
                        self.comp_op()
                        self.state = 63
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 65
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 66
                        self.comp_eq()
                        self.state = 67
                        self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 70
                        self.log_op()
                        self.state = 71
                        self.expr(7)
                        pass

             
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MathParser.ID, 0)

        def getRuleIndex(self):
            return MathParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)




    def id_(self):

        localctx = MathParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(MathParser.ID)
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
        self.enterRule(localctx, 8, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(MathParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NegintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEGINT(self):
            return self.getToken(MathParser.NEGINT, 0)

        def getRuleIndex(self):
            return MathParser.RULE_negint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegint" ):
                listener.enterNegint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegint" ):
                listener.exitNegint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegint" ):
                return visitor.visitNegint(self)
            else:
                return visitor.visitChildren(self)




    def negint(self):

        localctx = MathParser.NegintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_negint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(MathParser.NEGINT)
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
        self.enterRule(localctx, 12, self.RULE_binary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
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
        self.enterRule(localctx, 14, self.RULE_unary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
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
        self.enterRule(localctx, 16, self.RULE_comp_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 86016) != 0)):
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
        self.enterRule(localctx, 18, self.RULE_comp_eq)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 172032) != 0)):
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
        self.enterRule(localctx, 20, self.RULE_log_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1835008) != 0)):
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
        self.enterRule(localctx, 22, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
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
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         




