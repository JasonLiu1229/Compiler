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


    # Enter a parse tree produced by MathParser#var.
    def enterVar(self, ctx:MathParser.VarContext):
        pass

    # Exit a parse tree produced by MathParser#var.
    def exitVar(self, ctx:MathParser.VarContext):
        pass


    # Enter a parse tree produced by MathParser#cvar_decl.
    def enterCvar_decl(self, ctx:MathParser.Cvar_declContext):
        pass

    # Exit a parse tree produced by MathParser#cvar_decl.
    def exitCvar_decl(self, ctx:MathParser.Cvar_declContext):
        pass


    # Enter a parse tree produced by MathParser#pvar_decl.
    def enterPvar_decl(self, ctx:MathParser.Pvar_declContext):
        pass

    # Exit a parse tree produced by MathParser#pvar_decl.
    def exitPvar_decl(self, ctx:MathParser.Pvar_declContext):
        pass


    # Enter a parse tree produced by MathParser#var_decl.
    def enterVar_decl(self, ctx:MathParser.Var_declContext):
        pass

    # Exit a parse tree produced by MathParser#var_decl.
    def exitVar_decl(self, ctx:MathParser.Var_declContext):
        pass


    # Enter a parse tree produced by MathParser#int.
    def enterInt(self, ctx:MathParser.IntContext):
        pass

    # Exit a parse tree produced by MathParser#int.
    def exitInt(self, ctx:MathParser.IntContext):
        pass


    # Enter a parse tree produced by MathParser#float.
    def enterFloat(self, ctx:MathParser.FloatContext):
        pass

    # Exit a parse tree produced by MathParser#float.
    def exitFloat(self, ctx:MathParser.FloatContext):
        pass


    # Enter a parse tree produced by MathParser#char.
    def enterChar(self, ctx:MathParser.CharContext):
        pass

    # Exit a parse tree produced by MathParser#char.
    def exitChar(self, ctx:MathParser.CharContext):
        pass


    # Enter a parse tree produced by MathParser#addr_op.
    def enterAddr_op(self, ctx:MathParser.Addr_opContext):
        pass

    # Exit a parse tree produced by MathParser#addr_op.
    def exitAddr_op(self, ctx:MathParser.Addr_opContext):
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


    # Enter a parse tree produced by MathParser#bin_log_op.
    def enterBin_log_op(self, ctx:MathParser.Bin_log_opContext):
        pass

    # Exit a parse tree produced by MathParser#bin_log_op.
    def exitBin_log_op(self, ctx:MathParser.Bin_log_opContext):
        pass


    # Enter a parse tree produced by MathParser#un_log_op.
    def enterUn_log_op(self, ctx:MathParser.Un_log_opContext):
        pass

    # Exit a parse tree produced by MathParser#un_log_op.
    def exitUn_log_op(self, ctx:MathParser.Un_log_opContext):
        pass


    # Enter a parse tree produced by MathParser#assign.
    def enterAssign(self, ctx:MathParser.AssignContext):
        pass

    # Exit a parse tree produced by MathParser#assign.
    def exitAssign(self, ctx:MathParser.AssignContext):
        pass



del MathParser