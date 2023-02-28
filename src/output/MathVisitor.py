# Generated from Math.g4 by ANTLR 4.12.0
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


    # Visit a parse tree produced by MathParser#expr.
    def visitExpr(self, ctx:MathParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#var.
    def visitVar(self, ctx:MathParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#cvar_decl.
    def visitCvar_decl(self, ctx:MathParser.Cvar_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#pvar_decl.
    def visitPvar_decl(self, ctx:MathParser.Pvar_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#var_decl.
    def visitVar_decl(self, ctx:MathParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#int.
    def visitInt(self, ctx:MathParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#binary_op.
    def visitBinary_op(self, ctx:MathParser.Binary_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#unary_op.
    def visitUnary_op(self, ctx:MathParser.Unary_opContext):
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