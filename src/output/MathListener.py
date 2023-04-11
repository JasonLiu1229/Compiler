# Generated from Math.g4 by ANTLR 4.11.1
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


    # Enter a parse tree produced by MathParser#declr.
    def enterDeclr(self, ctx:MathParser.DeclrContext):
        pass

    # Exit a parse tree produced by MathParser#declr.
    def exitDeclr(self, ctx:MathParser.DeclrContext):
        pass


    # Enter a parse tree produced by MathParser#printf.
    def enterPrintf(self, ctx:MathParser.PrintfContext):
        pass

    # Exit a parse tree produced by MathParser#printf.
    def exitPrintf(self, ctx:MathParser.PrintfContext):
        pass


    # Enter a parse tree produced by MathParser#var_decl.
    def enterVar_decl(self, ctx:MathParser.Var_declContext):
        pass

    # Exit a parse tree produced by MathParser#var_decl.
    def exitVar_decl(self, ctx:MathParser.Var_declContext):
        pass


    # Enter a parse tree produced by MathParser#assign.
    def enterAssign(self, ctx:MathParser.AssignContext):
        pass

    # Exit a parse tree produced by MathParser#assign.
    def exitAssign(self, ctx:MathParser.AssignContext):
        pass


    # Enter a parse tree produced by MathParser#deref.
    def enterDeref(self, ctx:MathParser.DerefContext):
        pass

    # Exit a parse tree produced by MathParser#deref.
    def exitDeref(self, ctx:MathParser.DerefContext):
        pass


    # Enter a parse tree produced by MathParser#lvar.
    def enterLvar(self, ctx:MathParser.LvarContext):
        pass

    # Exit a parse tree produced by MathParser#lvar.
    def exitLvar(self, ctx:MathParser.LvarContext):
        pass


    # Enter a parse tree produced by MathParser#rvar.
    def enterRvar(self, ctx:MathParser.RvarContext):
        pass

    # Exit a parse tree produced by MathParser#rvar.
    def exitRvar(self, ctx:MathParser.RvarContext):
        pass


    # Enter a parse tree produced by MathParser#expr.
    def enterExpr(self, ctx:MathParser.ExprContext):
        pass

    # Exit a parse tree produced by MathParser#expr.
    def exitExpr(self, ctx:MathParser.ExprContext):
        pass


    # Enter a parse tree produced by MathParser#term.
    def enterTerm(self, ctx:MathParser.TermContext):
        pass

    # Exit a parse tree produced by MathParser#term.
    def exitTerm(self, ctx:MathParser.TermContext):
        pass


    # Enter a parse tree produced by MathParser#factor.
    def enterFactor(self, ctx:MathParser.FactorContext):
        pass

    # Exit a parse tree produced by MathParser#factor.
    def exitFactor(self, ctx:MathParser.FactorContext):
        pass


    # Enter a parse tree produced by MathParser#primary.
    def enterPrimary(self, ctx:MathParser.PrimaryContext):
        pass

    # Exit a parse tree produced by MathParser#primary.
    def exitPrimary(self, ctx:MathParser.PrimaryContext):
        pass


    # Enter a parse tree produced by MathParser#rtype.
    def enterRtype(self, ctx:MathParser.RtypeContext):
        pass

    # Exit a parse tree produced by MathParser#rtype.
    def exitRtype(self, ctx:MathParser.RtypeContext):
        pass



del MathParser