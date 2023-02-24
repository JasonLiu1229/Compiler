# External libraries
from output.MathVisitor import MathVisitor
from output.MathParser import MathParser

class AST (MathVisitor):
    def __init__(self) -> None:
        super().__init__()

    def visitMath(self, ctx: MathParser.MathContext):
        return super().visitMath(ctx)

    def visitInstr(self, ctx: MathParser.InstrContext):
        return super().visitInstr(ctx)

    def visitExpr(self, ctx: MathParser.ExprContext):
        return super().visitExpr(ctx)

    def visitId(self, ctx: MathParser.IdContext):
        return super().visitId(ctx)

    def visitInt(self, ctx: MathParser.IntContext):
        return super().visitInt(ctx)

    def visitNegint(self, ctx: MathParser.NegintContext):
        return super().visitNegint(ctx)

    def visitBinary_op(self, ctx: MathParser.Binary_opContext):
        return super().visitBinary_op(ctx)

    def visitUnary_op(self, ctx: MathParser.Unary_opContext):
        return super().visitUnary_op(ctx)

    def visitComp_op(self, ctx: MathParser.Comp_opContext):
        return super().visitComp_op(ctx)

    def visitComp_eq(self, ctx: MathParser.Comp_eqContext):
        return super().visitComp_eq(ctx)

    def visitLog_op(self, ctx: MathParser.Log_opContext):
        return super().visitLog_op(ctx)

    def visitAssign(self, ctx: MathParser.AssignContext):
        return super().visitAssign(ctx)

    def print(self):
        pass