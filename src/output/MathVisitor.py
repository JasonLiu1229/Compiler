# Generated from Math.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MathParser import MathParser
else:
    from MathParser import MathParser

# This class defines a complete generic visitor for a parse tree produced by MathParser.

class MathVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MathParser#math.
    def visitMath(self, ctx:MathParser.MathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#instr.
    def visitInstr(self, ctx:MathParser.InstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#declr.
    def visitDeclr(self, ctx:MathParser.DeclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#printf.
    def visitPrintf(self, ctx:MathParser.PrintfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#printf_arg.
    def visitPrintf_arg(self, ctx:MathParser.Printf_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#scanf.
    def visitScanf(self, ctx:MathParser.ScanfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#scanf_arg.
    def visitScanf_arg(self, ctx:MathParser.Scanf_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#param_list.
    def visitParam_list(self, ctx:MathParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#param_declr.
    def visitParam_declr(self, ctx:MathParser.Param_declrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#func_defn.
    def visitFunc_defn(self, ctx:MathParser.Func_defnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#func_decl.
    def visitFunc_decl(self, ctx:MathParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#arg_list.
    def visitArg_list(self, ctx:MathParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#func_arg.
    def visitFunc_arg(self, ctx:MathParser.Func_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#func_call.
    def visitFunc_call(self, ctx:MathParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#func_scope.
    def visitFunc_scope(self, ctx:MathParser.Func_scopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#return_instr.
    def visitReturn_instr(self, ctx:MathParser.Return_instrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#scope.
    def visitScope(self, ctx:MathParser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#cont_instr.
    def visitCont_instr(self, ctx:MathParser.Cont_instrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#break_instr.
    def visitBreak_instr(self, ctx:MathParser.Break_instrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#array_decl.
    def visitArray_decl(self, ctx:MathParser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#incl_stat.
    def visitIncl_stat(self, ctx:MathParser.Incl_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#if_cond.
    def visitIf_cond(self, ctx:MathParser.If_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#else_cond.
    def visitElse_cond(self, ctx:MathParser.Else_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#while_loop.
    def visitWhile_loop(self, ctx:MathParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#for_loop.
    def visitFor_loop(self, ctx:MathParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#init.
    def visitInit(self, ctx:MathParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#cond.
    def visitCond(self, ctx:MathParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#incr.
    def visitIncr(self, ctx:MathParser.IncrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#var_decl.
    def visitVar_decl(self, ctx:MathParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#assign.
    def visitAssign(self, ctx:MathParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#array_el.
    def visitArray_el(self, ctx:MathParser.Array_elContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#deref.
    def visitDeref(self, ctx:MathParser.DerefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#lvar.
    def visitLvar(self, ctx:MathParser.LvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#rvar.
    def visitRvar(self, ctx:MathParser.RvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#comp.
    def visitComp(self, ctx:MathParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#expr.
    def visitExpr(self, ctx:MathParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#term.
    def visitTerm(self, ctx:MathParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#factor.
    def visitFactor(self, ctx:MathParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#primary.
    def visitPrimary(self, ctx:MathParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#rtype.
    def visitRtype(self, ctx:MathParser.RtypeContext):
        return self.visitChildren(ctx)



del MathParser