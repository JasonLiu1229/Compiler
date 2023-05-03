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


    # Enter a parse tree produced by MathParser#printf_arg.
    def enterPrintf_arg(self, ctx:MathParser.Printf_argContext):
        pass

    # Exit a parse tree produced by MathParser#printf_arg.
    def exitPrintf_arg(self, ctx:MathParser.Printf_argContext):
        pass


    # Enter a parse tree produced by MathParser#scanf.
    def enterScanf(self, ctx:MathParser.ScanfContext):
        pass

    # Exit a parse tree produced by MathParser#scanf.
    def exitScanf(self, ctx:MathParser.ScanfContext):
        pass


    # Enter a parse tree produced by MathParser#param_list.
    def enterParam_list(self, ctx:MathParser.Param_listContext):
        pass

    # Exit a parse tree produced by MathParser#param_list.
    def exitParam_list(self, ctx:MathParser.Param_listContext):
        pass


    # Enter a parse tree produced by MathParser#param_declr.
    def enterParam_declr(self, ctx:MathParser.Param_declrContext):
        pass

    # Exit a parse tree produced by MathParser#param_declr.
    def exitParam_declr(self, ctx:MathParser.Param_declrContext):
        pass


    # Enter a parse tree produced by MathParser#func_defn.
    def enterFunc_defn(self, ctx:MathParser.Func_defnContext):
        pass

    # Exit a parse tree produced by MathParser#func_defn.
    def exitFunc_defn(self, ctx:MathParser.Func_defnContext):
        pass


    # Enter a parse tree produced by MathParser#func_decl.
    def enterFunc_decl(self, ctx:MathParser.Func_declContext):
        pass

    # Exit a parse tree produced by MathParser#func_decl.
    def exitFunc_decl(self, ctx:MathParser.Func_declContext):
        pass


    # Enter a parse tree produced by MathParser#arg_list.
    def enterArg_list(self, ctx:MathParser.Arg_listContext):
        pass

    # Exit a parse tree produced by MathParser#arg_list.
    def exitArg_list(self, ctx:MathParser.Arg_listContext):
        pass


    # Enter a parse tree produced by MathParser#func_arg.
    def enterFunc_arg(self, ctx:MathParser.Func_argContext):
        pass

    # Exit a parse tree produced by MathParser#func_arg.
    def exitFunc_arg(self, ctx:MathParser.Func_argContext):
        pass


    # Enter a parse tree produced by MathParser#func_call.
    def enterFunc_call(self, ctx:MathParser.Func_callContext):
        pass

    # Exit a parse tree produced by MathParser#func_call.
    def exitFunc_call(self, ctx:MathParser.Func_callContext):
        pass


    # Enter a parse tree produced by MathParser#func_scope.
    def enterFunc_scope(self, ctx:MathParser.Func_scopeContext):
        pass

    # Exit a parse tree produced by MathParser#func_scope.
    def exitFunc_scope(self, ctx:MathParser.Func_scopeContext):
        pass


    # Enter a parse tree produced by MathParser#return_instr.
    def enterReturn_instr(self, ctx:MathParser.Return_instrContext):
        pass

    # Exit a parse tree produced by MathParser#return_instr.
    def exitReturn_instr(self, ctx:MathParser.Return_instrContext):
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


    # Enter a parse tree produced by MathParser#array_decl.
    def enterArray_decl(self, ctx:MathParser.Array_declContext):
        pass

    # Exit a parse tree produced by MathParser#array_decl.
    def exitArray_decl(self, ctx:MathParser.Array_declContext):
        pass


    # Enter a parse tree produced by MathParser#incl_stat.
    def enterIncl_stat(self, ctx:MathParser.Incl_statContext):
        pass

    # Exit a parse tree produced by MathParser#incl_stat.
    def exitIncl_stat(self, ctx:MathParser.Incl_statContext):
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


    # Enter a parse tree produced by MathParser#array_el.
    def enterArray_el(self, ctx:MathParser.Array_elContext):
        pass

    # Exit a parse tree produced by MathParser#array_el.
    def exitArray_el(self, ctx:MathParser.Array_elContext):
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