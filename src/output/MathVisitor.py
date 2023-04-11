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


    # Visit a parse tree produced by MathParser#assign.
    def visitAssign(self, ctx:MathParser.AssignContext):
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