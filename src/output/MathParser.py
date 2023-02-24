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
        4,1,25,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,0,1,0,1,0,3,0,
        29,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,47,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,69,8,1,10,1,12,1,72,9,1,1,2,
        1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,
        1,10,1,10,0,1,2,11,0,2,4,6,8,10,12,14,16,18,20,0,5,1,0,7,9,1,0,10,
        11,3,0,12,12,14,14,16,16,3,0,13,13,15,15,17,17,1,0,18,20,91,0,28,
        1,0,0,0,2,46,1,0,0,0,4,73,1,0,0,0,6,75,1,0,0,0,8,77,1,0,0,0,10,79,
        1,0,0,0,12,81,1,0,0,0,14,83,1,0,0,0,16,85,1,0,0,0,18,87,1,0,0,0,
        20,89,1,0,0,0,22,23,3,2,1,0,23,24,5,0,0,1,24,29,1,0,0,0,25,26,3,
        2,1,0,26,27,5,1,0,0,27,29,1,0,0,0,28,22,1,0,0,0,28,25,1,0,0,0,29,
        1,1,0,0,0,30,31,6,1,-1,0,31,32,5,2,0,0,32,33,3,2,1,0,33,34,5,3,0,
        0,34,47,1,0,0,0,35,47,3,6,3,0,36,47,3,8,4,0,37,47,3,4,2,0,38,39,
        3,4,2,0,39,40,3,20,10,0,40,41,3,4,2,0,41,47,1,0,0,0,42,43,3,4,2,
        0,43,44,3,20,10,0,44,45,3,6,3,0,45,47,1,0,0,0,46,30,1,0,0,0,46,35,
        1,0,0,0,46,36,1,0,0,0,46,37,1,0,0,0,46,38,1,0,0,0,46,42,1,0,0,0,
        47,70,1,0,0,0,48,49,10,10,0,0,49,50,3,10,5,0,50,51,3,2,1,11,51,69,
        1,0,0,0,52,53,10,9,0,0,53,54,3,12,6,0,54,55,3,2,1,10,55,69,1,0,0,
        0,56,57,10,8,0,0,57,58,3,14,7,0,58,59,3,2,1,9,59,69,1,0,0,0,60,61,
        10,7,0,0,61,62,3,16,8,0,62,63,3,2,1,8,63,69,1,0,0,0,64,65,10,6,0,
        0,65,66,3,18,9,0,66,67,3,2,1,7,67,69,1,0,0,0,68,48,1,0,0,0,68,52,
        1,0,0,0,68,56,1,0,0,0,68,60,1,0,0,0,68,64,1,0,0,0,69,72,1,0,0,0,
        70,68,1,0,0,0,70,71,1,0,0,0,71,3,1,0,0,0,72,70,1,0,0,0,73,74,5,4,
        0,0,74,5,1,0,0,0,75,76,5,5,0,0,76,7,1,0,0,0,77,78,5,6,0,0,78,9,1,
        0,0,0,79,80,7,0,0,0,80,11,1,0,0,0,81,82,7,1,0,0,82,13,1,0,0,0,83,
        84,7,2,0,0,84,15,1,0,0,0,85,86,7,3,0,0,86,17,1,0,0,0,87,88,7,4,0,
        0,88,19,1,0,0,0,89,90,5,21,0,0,90,21,1,0,0,0,4,28,46,68,70
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
    RULE_expr = 1
    RULE_id = 2
    RULE_int = 3
    RULE_negint = 4
    RULE_binary_op = 5
    RULE_unary_op = 6
    RULE_comp_op = 7
    RULE_comp_eq = 8
    RULE_log_op = 9
    RULE_assign = 10

    ruleNames =  [ "math", "expr", "id", "int", "negint", "binary_op", "unary_op", 
                   "comp_op", "comp_eq", "log_op", "assign" ]

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

        def expr(self):
            return self.getTypedRuleContext(MathParser.ExprContext,0)


        def EOF(self):
            return self.getToken(MathParser.EOF, 0)

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
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.expr(0)
                self.state = 23
                self.match(MathParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.expr(0)
                self.state = 26
                self.match(MathParser.T__0)
                pass


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
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 31
                self.match(MathParser.T__1)
                self.state = 32
                self.expr(0)
                self.state = 33
                self.match(MathParser.T__2)
                pass

            elif la_ == 2:
                self.state = 35
                self.int_()
                pass

            elif la_ == 3:
                self.state = 36
                self.negint()
                pass

            elif la_ == 4:
                self.state = 37
                self.id_()
                pass

            elif la_ == 5:
                self.state = 38
                self.id_()
                self.state = 39
                self.assign()
                self.state = 40
                self.id_()
                pass

            elif la_ == 6:
                self.state = 42
                self.id_()
                self.state = 43
                self.assign()
                self.state = 44
                self.int_()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 68
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 49
                        self.binary_op()
                        self.state = 50
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 53
                        self.unary_op()
                        self.state = 54
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 57
                        self.comp_op()
                        self.state = 58
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 60
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 61
                        self.comp_eq()
                        self.state = 62
                        self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = MathParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 64
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 65
                        self.log_op()
                        self.state = 66
                        self.expr(7)
                        pass

             
                self.state = 72
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
        self.enterRule(localctx, 4, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
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
        self.enterRule(localctx, 6, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
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
        self.enterRule(localctx, 8, self.RULE_negint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
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
        self.enterRule(localctx, 10, self.RULE_binary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
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
        self.enterRule(localctx, 12, self.RULE_unary_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
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
        self.enterRule(localctx, 14, self.RULE_comp_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
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
        self.enterRule(localctx, 16, self.RULE_comp_eq)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
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
        self.enterRule(localctx, 18, self.RULE_log_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
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
        self.enterRule(localctx, 20, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
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
        self._predicates[1] = self.expr_sempred
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
         




