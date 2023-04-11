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


    # Visit a parse tree produced by MathParser#var_decl.
    def visitVar_decl(self, ctx:MathParser.Var_declContext):
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


    # Visit a parse tree produced by MathParser#expr.
    def visitExpr(self, ctx:MathParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#cast.
    def visitCast(self, ctx:MathParser.CastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#rtype.
    def visitRtype(self, ctx:MathParser.RtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#addr_op.
    def visitAddr_op(self, ctx:MathParser.Addr_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#binary_op.
    def visitBinary_op(self, ctx:MathParser.Binary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#unary_op.
    def visitUnary_op(self, ctx:MathParser.Unary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#incr.
    def visitIncr(self, ctx:MathParser.IncrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#decr.
    def visitDecr(self, ctx:MathParser.DecrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#comp_op.
    def visitComp_op(self, ctx:MathParser.Comp_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#comp_eq.
    def visitComp_eq(self, ctx:MathParser.Comp_eqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#bin_log_op.
    def visitBin_log_op(self, ctx:MathParser.Bin_log_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#un_log_op.
    def visitUn_log_op(self, ctx:MathParser.Un_log_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#assign.
    def visitAssign(self, ctx:MathParser.AssignContext):
        return self.visitChildren(ctx)



del MathParser