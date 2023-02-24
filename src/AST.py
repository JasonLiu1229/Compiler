# External libraries
from output.MathVisitor import MathVisitor
from output.MathParser import MathParser

class AST_CREATOR (MathVisitor):
    def __init__(self) -> None:
        super().__init__()

    def visitMath(self, ctx: MathParser.MathContext):
        # self.visitInstr(ctx.children[0])
        return super().visitMath(ctx)

    def visitInstr(self, ctx: MathParser.InstrContext):
        return super().visitInstr(ctx)

    def visitExpr(self, ctx: MathParser.ExprContext):
        return super().visitExpr(ctx)

    def visitId(self, ctx: MathParser.IdContext):
        root = Node("id" ,ctx.children[0].symbol.text)
        return root

    def visitInt(self, ctx: MathParser.IntContext):
        root = Node("int", int(ctx.children[0].symbol.text))
        return root

    def visitBinary_op(self, ctx: MathParser.Binary_opContext):
        root = Node("binary_op", ctx.children[0].symbol.text)
        return root

    def visitUnary_op(self, ctx: MathParser.Unary_opContext):
        root = Node("unary_op", ctx.children[0].symbol.text)
        return root

    def visitComp_op(self, ctx: MathParser.Comp_opContext):
        root = Node("comp_op", ctx.children[0].symbol.text)
        return root

    def visitComp_eq(self, ctx: MathParser.Comp_eqContext):
        root = Node("comp_eq", ctx.children[0].symbol.text)
        return root

    def visitLog_op(self, ctx: MathParser.Log_opContext):
        root = Node("log_op", ctx.children[0].symbol.text)
        return root

    def visitAssign(self, ctx: MathParser.AssignContext):
        root = Node("assign_op", ctx.children[0].symbol.text)
        return root

    def create(self):
        pass



class Node:
    def __init__(self, key, value) -> None:
        super().__init__()
        self.key = key
        self.value = value

class AST:
    def __init__(self) -> None:
        super().__init__()
        self.root = None
        self.children = []

    def add_child(self, child):
        if not isinstance(child, AST):
            raise TypeError("child must be set to an AST")
        self.children.insert(len(self.children), child)

    def print(self):
        pass