# External libraries
from output.MathVisitor import MathVisitor
from output.MathParser import MathParser

keywords = ["id", "int", "binary_op", "unary_op", "comp_op", "comp_eq", "log_op", "assign_op"]

class AST_CREATOR (MathVisitor):
    def __init__(self) -> None:
        super().__init__()

    def visit_child(self, ctx):
        if isinstance(ctx, MathParser.IdContext):
            return self.visitId(ctx)
        elif isinstance(ctx, MathParser.IntContext):
            return self.visitInt(ctx)
        elif isinstance(ctx, MathParser.Binary_opContext):
            return self.visitBinary_op(ctx)
        elif isinstance(ctx, MathParser.Unary_opContext):
            return self.visitUnary_op(ctx)
        elif isinstance(ctx, MathParser.Comp_eqContext):
            return self.visitComp_eq(ctx)
        elif isinstance(ctx, MathParser.Comp_opContext):
            return self.visitComp_op(ctx)
        elif isinstance(ctx, MathParser.Log_opContext):
            return self.visitLog_op(ctx)
        elif isinstance(ctx, MathParser.AssignContext):
            return self.visitAssign(ctx)


    def visitMath(self, ctx: MathParser.MathContext):
        # self.visitInstr(ctx.children[0])
        return super().visitMath(ctx)

    def visitInstr(self, ctx: MathParser.InstrContext):
        return super().visitInstr(ctx)

    def visitExpr(self, ctx: MathParser.ExprContext):
        return super().visitExpr(ctx)

    def visitId(self, ctx: MathParser.IdContext):
        root = Node(keywords[0], ctx.children[0].symbol.text)
        return root

    def visitInt(self, ctx: MathParser.IntContext):
        root = Node(keywords[1], int(ctx.children[0].symbol.text))
        return root

    def visitBinary_op(self, ctx: MathParser.Binary_opContext):
        root = Node(keywords[2], ctx.children[0].symbol.text)
        return root

    def visitUnary_op(self, ctx: MathParser.Unary_opContext):
        root = Node(keywords[3], ctx.children[0].symbol.text)
        return root

    def visitComp_op(self, ctx: MathParser.Comp_opContext):
        root = Node(keywords[4], ctx.children[0].symbol.text)
        return root

    def visitComp_eq(self, ctx: MathParser.Comp_eqContext):
        root = Node(keywords[5], ctx.children[0].symbol.text)
        return root

    def visitLog_op(self, ctx: MathParser.Log_opContext):
        root = Node(keywords[6], ctx.children[0].symbol.text)
        return root

    def visitAssign(self, ctx: MathParser.AssignContext):
        root = Node(keywords[7], ctx.children[0].symbol.text)
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
        if self.root.key in keywords:
            print("idk yet")
        print(self.root.key + '\t' + ':' + '\t')