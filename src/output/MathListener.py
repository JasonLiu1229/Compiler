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


    # Enter a parse tree produced by MathParser#scope.
    def enterScope(self, ctx:MathParser.ScopeContext):
        pass

    # Exit a parse tree produced by MathParser#scope.
    def exitScope(self, ctx:MathParser.ScopeContext):
        pass


    # Enter a parse tree produced by MathParser#cont_instr.
    def enterCont_instr(self, ctx:MathParser.Cont_instrContext):
        pass

    # Exit a parse tree produced by MathParser#cont_instr.
    def exitCont_instr(self, ctx:MathParser.Cont_instrContext):
        pass


    # Enter a parse tree produced by MathParser#break_instr.
    def enterBreak_instr(self, ctx:MathParser.Break_instrContext):
        pass

    # Exit a parse tree produced by MathParser#break_instr.
    def exitBreak_instr(self, ctx:MathParser.Break_instrContext):
        pass


    # Enter a parse tree produced by MathParser#if_cond.
    def enterIf_cond(self, ctx:MathParser.If_condContext):
        pass

    # Exit a parse tree produced by MathParser#if_cond.
    def exitIf_cond(self, ctx:MathParser.If_condContext):
        pass


    # Enter a parse tree produced by MathParser#else_cond.
    def enterElse_cond(self, ctx:MathParser.Else_condContext):
        pass

    # Exit a parse tree produced by MathParser#else_cond.
    def exitElse_cond(self, ctx:MathParser.Else_condContext):
        pass


    # Enter a parse tree produced by MathParser#while_loop.
    def enterWhile_loop(self, ctx:MathParser.While_loopContext):
        pass

    # Exit a parse tree produced by MathParser#while_loop.
    def exitWhile_loop(self, ctx:MathParser.While_loopContext):
        pass


    # Enter a parse tree produced by MathParser#for_loop.
    def enterFor_loop(self, ctx:MathParser.For_loopContext):
        pass

    # Exit a parse tree produced by MathParser#for_loop.
    def exitFor_loop(self, ctx:MathParser.For_loopContext):
        pass


    # Enter a parse tree produced by MathParser#init.
    def enterInit(self, ctx:MathParser.InitContext):
        pass

    # Exit a parse tree produced by MathParser#init.
    def exitInit(self, ctx:MathParser.InitContext):
        pass


    # Enter a parse tree produced by MathParser#cond.
    def enterCond(self, ctx:MathParser.CondContext):
        pass

    # Exit a parse tree produced by MathParser#cond.
    def exitCond(self, ctx:MathParser.CondContext):
        pass


    # Enter a parse tree produced by MathParser#incr.
    def enterIncr(self, ctx:MathParser.IncrContext):
        pass

    # Exit a parse tree produced by MathParser#incr.
    def exitIncr(self, ctx:MathParser.IncrContext):
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