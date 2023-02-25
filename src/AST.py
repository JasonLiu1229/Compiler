# External libraries
from output.MathVisitor import MathVisitor
from output.MathParser import MathParser
import json
keywords = ["id", "int", "binary_op", "unary_op", "comp_op", "comp_eq", "log_op", "assign_op"]

class AST_CREATOR (MathVisitor):
    def __init__(self) -> None:
        super().__init__()

    def visit_child(self, ctx):
        if isinstance(ctx, MathParser.MathContext):
            return self.visitMath(ctx)
        elif isinstance(ctx, MathParser.InstrContext):
            return self.visitInstr(ctx)
        elif isinstance(ctx, MathParser.ExprContext):
            return self.visitExpr(ctx)
        elif isinstance(ctx, MathParser.IdContext):
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
        math_ast = AST()
        math_ast.root = Node("math", None)
        for c in ctx.getChildren():
            math_ast.children.insert(len(math_ast.children), self.visit_child(c))
        return math_ast

    def visitInstr(self, ctx: MathParser.InstrContext):
        instr_ast = AST()
        instr_ast.root = Node("instr", None)
        for c in ctx.getChildren():
            instr_ast.children.insert(len(instr_ast.children), self.visit_child(c))
        return instr_ast

    def visitExpr(self, ctx: MathParser.ExprContext):
        """
        '(' expr ')'
            |   expr binary_op expr
            |   expr unary_op expr
            |   expr comp_op expr
            |   expr comp_eq expr
            |   expr log_op expr
            |   unary_op expr
            |   int
            |   id
            |   id assign id
            |   id assign int
            |   id assign expr
        """
        # self.visitInstr(ctx.children[0])
        # print(list(ctx.getChildren()))
        expr_ast = AST()
        expr_ast.root = Node("expr" , None)
        for c in ctx.getChildren():
            expr_ast.children.insert(len(expr_ast.children) , self.visit_child(c))
        return expr_ast

    def visitId(self, ctx: MathParser.IdContext):
        root = Node(keywords[0], ctx.children[0].getText())
        return root

    def visitInt(self, ctx: MathParser.IntContext):
        root = Node(keywords[1], int(ctx.children[0].getText()))
        return root

    def visitBinary_op(self, ctx: MathParser.Binary_opContext):
        root = Node(keywords[2], ctx.children[0].getText())
        return root

    def visitUnary_op(self, ctx: MathParser.Unary_opContext):
        root = Node(keywords[3], ctx.children[0].getText())
        return root

    def visitComp_op(self, ctx: MathParser.Comp_opContext):
        root = Node(keywords[4], ctx.children[0].getText())
        return root

    def visitComp_eq(self, ctx: MathParser.Comp_eqContext):
        root = Node(keywords[5], ctx.children[0].getText())
        return root

    def visitLog_op(self, ctx: MathParser.Log_opContext):
        root = Node(keywords[6], ctx.children[0].getText())
        return root

    def visitAssign(self, ctx: MathParser.AssignContext):
        root = Node(keywords[7], ctx.children[0].getText())
        return root


class Node:
    def __init__(self, key, value) -> None:
        super().__init__()
        self.key = key
        self.value = value

    def print(self):
        print(self.get_str())

    def save(self):
        out = { self.key : self.value }
        return out
    def get_str(self):
        return self.key + '\t' + ':' + '\t' + str(self.value)

class AST:
    def __init__(self) -> None:
        super().__init__()
        self.root : Node | None = None
        self.children : list[Node] | [] = []

    def add_child(self, child):
        if not isinstance(child, AST):
            raise TypeError("child must be set to an AST")
        self.children.insert(len(self.children), child)

    def save(self):
        out = {self.root.key: self.root.value}
        if out[self.root.key] is None:
            out[self.root.key] = []
        for i in range(len(self.children)):
            if self.children[i] is not None and self.root.value is None:
                out[self.root.key].insert(len(out[self.root.key]) , self.children[i].save())
        return out

    def print(self):
        # out = self.save()
        # for child in self.children:
        #     if child is not None and isinstance(child , AST):
        #         child.print()
        #     elif child is not None:
        #         out += "\t" + child.get_str() + "\n"
        # out += "}"
        # out = json.dumps(self.save() , indent=4)
        # out = self.save()
        print(json.dumps(self.save() , indent=4))

    def get_str(self):
        return self.root.key + '\t' + ':' + '\t' + str(self.root.value)