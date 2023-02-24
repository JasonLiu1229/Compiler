# Generated from Math.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MathParser import MathParser
else:
    from MathParser import MathParser

# This class defines a complete listener for a parse tree produced by MathParser.
class MathListener(ParseTreeListener):

    # Enter a parse tree produced by MathParser#math.
    def enterMath(self, ctx:MathParser.MathContext):
        pass

    # Exit a parse tree produced by MathParser#math.
    def exitMath(self, ctx:MathParser.MathContext):
        pass


    # Enter a parse tree produced by MathParser#instr.
    def enterInstr(self, ctx:MathParser.InstrContext):
        pass

    # Exit a parse tree produced by MathParser#instr.
    def exitInstr(self, ctx:MathParser.InstrContext):
        pass


    # Enter a parse tree produced by MathParser#expr.
    def enterExpr(self, ctx:MathParser.ExprContext):
        pass

    # Exit a parse tree produced by MathParser#expr.
    def exitExpr(self, ctx:MathParser.ExprContext):
        pass


    # Enter a parse tree produced by MathParser#id.
    def enterId(self, ctx:MathParser.IdContext):
        pass

    # Exit a parse tree produced by MathParser#id.
    def exitId(self, ctx:MathParser.IdContext):
        pass


    # Enter a parse tree produced by MathParser#int.
    def enterInt(self, ctx:MathParser.IntContext):
        pass

    # Exit a parse tree produced by MathParser#int.
    def exitInt(self, ctx:MathParser.IntContext):
        pass


    # Enter a parse tree produced by MathParser#negint.
    def enterNegint(self, ctx:MathParser.NegintContext):
        pass

    # Exit a parse tree produced by MathParser#negint.
    def exitNegint(self, ctx:MathParser.NegintContext):
        pass


    # Enter a parse tree produced by MathParser#binary_op.
    def enterBinary_op(self, ctx:MathParser.Binary_opContext):
        pass

    # Exit a parse tree produced by MathParser#binary_op.
    def exitBinary_op(self, ctx:MathParser.Binary_opContext):
        pass


    # Enter a parse tree produced by MathParser#unary_op.
    def enterUnary_op(self, ctx:MathParser.Unary_opContext):
        pass

    # Exit a parse tree produced by MathParser#unary_op.
    def exitUnary_op(self, ctx:MathParser.Unary_opContext):
        pass


    # Enter a parse tree produced by MathParser#comp_op.
    def enterComp_op(self, ctx:MathParser.Comp_opContext):
        pass

    # Exit a parse tree produced by MathParser#comp_op.
    def exitComp_op(self, ctx:MathParser.Comp_opContext):
        pass


    # Enter a parse tree produced by MathParser#comp_eq.
    def enterComp_eq(self, ctx:MathParser.Comp_eqContext):
        pass

    # Exit a parse tree produced by MathParser#comp_eq.
    def exitComp_eq(self, ctx:MathParser.Comp_eqContext):
        pass


    # Enter a parse tree produced by MathParser#log_op.
    def enterLog_op(self, ctx:MathParser.Log_opContext):
        pass

    # Exit a parse tree produced by MathParser#log_op.
    def exitLog_op(self, ctx:MathParser.Log_opContext):
        pass


    # Enter a parse tree produced by MathParser#assign.
    def enterAssign(self, ctx:MathParser.AssignContext):
        pass

    # Exit a parse tree produced by MathParser#assign.
    def exitAssign(self, ctx:MathParser.AssignContext):
        pass



del MathParser