import decimal
import struct
import pydot
from colorama import Fore
import copy

import antlr4.tree.Tree
from AST import *
from output.MathParser import MathParser
from output.MathVisitor import MathVisitor
from decimal import *

class AstCreator (MathVisitor):

    def __init__(self) -> None:
        """
        Initializer function
        """
        super().__init__()
        self.base_ast : AST = AST()
        self.symbol_table : dict = dict()
        self.warnings : list = []

    def visit_child(self, ctx):
        """
        visit the right visit function for the give context
        :param ctx: the context to know what to visit
        :return: the given output given by every visit function (AST or Node)
        """
        # Terminals processing
        # if isinstance(ctx, MathParser.InstrContext):
        #     return AST(Node("instr", None))
        # elif isinstance(ctx, MathParser.ExprContext):
        #     return AST(Node("expr", None))
        # elif isinstance(ctx, MathParser.MathContext):
        #     return AST(Node("math", None))
        if isinstance(ctx, MathParser.RvarContext):
            return self.visitRvar(ctx)
        elif isinstance(ctx, MathParser.RtypeContext):
            return self.visitRtype(ctx)
        # Operations processing
        elif isinstance(ctx, MathParser.AssignContext):
            return self.visitAssign(ctx)
        elif isinstance(ctx, MathParser.LvarContext):
            return self.visitLvar(ctx)
        elif isinstance(ctx, MathParser.DerefContext):
            return Node("deref", None)
        elif isinstance(ctx, MathParser.PrintfContext):
            return Node("printf", None)
        elif isinstance(ctx, MathParser.Var_declContext):
            return Node("var_declr", None)
        elif isinstance(ctx , MathParser.DeclrContext):
            return Node("declr", None)

    def resolveTree(self, base: AST):
        """
        visit the right visit function for the give context
        :param base: The base AST given to resolve
        :return: the given output given by every visit function (AST or Node)
        """
        # Terminals processing
        index = 0
        s = list()
        resolved = list()
        for child in base.children:
            # binary operation
            if isinstance(child, Node) and child.key in keywords_binary and len(base.children) > index + 1:
                # Promote operation
                child = AST(child, [base.children[index-1], base.children[index+1]])
                base.children[index] = child
                base.children.remove(base.children[index-1])
                base.children.remove(base.children[index])
                index -= 1
            elif isinstance(child, Node) and child.key == "cast" and len(base.children) > index + 1:
                base.children[index] = AST(child, [base.children[index+1]])
                base.children.remove(base.children[index+1])
            index += 1
        return base

    def DFS(self, visited, ctx):
        if visited is None:
            visited = []
        s = list()
        a = AST(root=Node("math", None))
        s.append(ctx)
        # while there are still nodes to visit in the tree
        while len(s) > 0:
            v = s.pop()
            if v not in visited:
                visited.append(v)
                s.append(v)
                if isinstance(v , antlr4.tree.Tree.TerminalNodeImpl):
                    continue
                for child in v.getChildren():
                    s.append(child)
            else:
                # Reverse the tree for processing
                # if not rev:
                #     s.append(v)
                #     s.reverse()
                #     v = s.pop()
                #     rev = True
                # print(f'Processing {v} with type {type(v)}')
                # process leaf nodes
                v = self.visit_child(v)
                # print(f'Processed node. Now it is {v} with type {type(v)}')
                # if v is None:
                #     continue
                # v = self.visit_child(v)
                a.add_child(v)
        return a


    def visitMath(self, ctx: MathParser.MathContext):
        """
        Math visit function
        :param ctx: context
        :return: AST
        """
        # stack for visited nodes
        s = []
        # create math node
        math_ast = AST()
        math_ast = self.DFS(None, ctx)
        # math_ast = Node("math", None)
        # s.append(math_ast)
        # math_ast.root = Node("math", None)
        # for c in ctx.getChildren():
        #     math_ast.add_child(self.visit_child(c))
        # self.resolve_empty(math_ast)
        # self.base_ast = math_ast
        return math_ast



    def visitInstr(self, ctx: MathParser.InstrContext):
        """
        Instruction visit
        :param ctx: context
        :return: AST
        """
        instr_ast = AST()
        instr_ast.root = Node("instr", None)
        for c in ctx.getChildren():
            instr_ast.add_child(self.visit_child(c))
        self.resolve_empty(instr_ast)
        return instr_ast

    def visitPrintf(self, ctx: MathParser.PrintfContext):
        """
        Creates the node for printf function
        :param ctx: context
        :return: Node
        """
        out = FunctionNode(ctx.children[0].getText() ,
                           {"par0" : self.visit_child(ctx.children[2])}
                           )
        if not out.key in self.symbol_table.keys():
            self.symbol_table[out.key] = [copy.copy(out)]
        else:
            self.symbol_table[out.key].append(copy.copy(out))
        return out

    def visitExpr(self, ctx: MathParser.ExprContext):
        """
        Expression visit function
        :param ctx: context
        :return: AST
        """
        expr_ast = AST()
        expr_ast.root = Node("expr" , None)
        for c in ctx.getChildren():
            expr_ast.add_child(self.visit_child(c))
        self.resolve_empty(expr_ast)
        # Resolve the operations order
        expr_ast = self.resolve_datatype(expr_ast)
        self.resolve_unary(expr_ast)
        self.resolve_binary(expr_ast)
        self.resolve_assign(expr_ast)
        # expr_ast = self.unnest(expr_ast)
        return expr_ast

    def visitRvar(self, ctx: MathParser.RvarContext):
        """
        Right hand side variable visit function
        :param ctx: context
        :return: Node
        """
        root = Node(keywords[0], ctx.children[0].getText())
        return root

    def visitRtype(self, ctx: MathParser.RtypeContext):
        """
        Right hand side type visit function
        :param ctx: context
        :return: Node
        """
        if ctx.children[0].getText().isdigit():
            return Node(keywords_datatype[0], int(ctx.children[0].getText()))
        elif self.isfloat(ctx.children[0].getText()):
            return Node(keywords_datatype[1], Decimal(ctx.children[0].getText()).__float__())
        else:
            return Node(keywords_datatype[2], ctx.children[0].getText()[1:-1])

    def visitAssign(self, ctx: MathParser.AssignContext):
        """
        Assign operand visit function
        :param ctx: context
        :return: Node
        """
        root = Node(keywords[8], ctx.children[0].getText())
        return root

    def visitDeclr(self, ctx: MathParser.DeclrContext):
        # CONST? TYPE (var_decl ',')* var_decl
        """
        Declaration visit function
        :param ctx: context
        :return: AST
        """
        out = AST()
        out.root = Node("declr" , None)
        const = False
        v_type = ""
        root = VarNode("", None, v_type, const)
        for i in range(len(ctx.children)):
            if ctx.children[i].getText() == "const":
                const = True
            elif ctx.children[i].getText() in keywords_datatype and v_type == "":
                v_type = ctx.children[i].getText()
            elif ctx.children[i].getText() == ",":
                root = VarNode("" , None , v_type , const)
            else:
                root = self.visit_child(ctx.children[i])
                self.resolve_unary(root)
                self.resolve_binary(root)
                self.resolve_variables(root)
                self.resolve_assign(root)
                self.resolve_empty(root)
                new_ast = self.resolve_datatype(root)
                # new_ast = self.unnest(new_ast)
                if isinstance(new_ast , VarNode):
                    new_ast.assign_type(v_type)
                elif isinstance(new_ast.children[0] , VarNode):
                    new_ast.children[0].assign_type(v_type)
                new_ast = self.optimise(new_ast)
                new_ast = new_ast
                new_ast.const = const

                out.add_child(new_ast)
                if not isinstance(new_ast , AST):
                    self.symbol_table[new_ast.key] = copy.copy(new_ast)
        return out

    def visitVar_decl(self, ctx: MathParser.Var_declContext):
        # TYPE VAR_NAME
        # int x
        """
        Variable declaration visit function
        :param ctx: context
        :return: VarNode || AST
        """
        out = VarNode("" , None , "")
        if len(ctx.children) == 1:
            out = self.visit_child(ctx.children[0])
        else:
            out = AST()
            for c in ctx.children:
                out.add_child(self.visit_child(c))
            # return VarNode(vtype=ctx.children[0].getText(), key=ctx.children[1].getText(), value=None)
            out.root = Node("expr" , None)
        return out

    def visitLvar(self, ctx: MathParser.LvarContext):
        """
        Left hand side variable
        :param ctx: context
        :return: VarNode
        """
        if ctx.children[-1].getText() in self.symbol_table.keys():
            raise AttributeError("Redeclaration of variable " + ctx.children[-1].getText())
        if len(ctx.children) == 1:
            root = VarNode(ctx.children[-1].getText() , None , "")
            return root
        # If more than 1 element: it's a pointer
        root = VarNode(ctx.children[-1].getText(), None , "" , total_deref= len(ctx.children) - 1)
        # Make a length-1 chain on the symbol table for the pointer
        current_node = root
        for i in range(len(ctx.children) - 1):
            # new_node = VarNode(current_node.key , None , current_node.type , current_node.const , i + 1)
            if current_node.key not in self.symbol_table.keys():
                self.symbol_table[current_node.key] = root
                root.value = current_node
                root.ptr = True
            current_node.value = VarNode(current_node.key , None , current_node.type , current_node.const , current_node.total_deref > 1 , i + 1 , current_node.total_deref - 1)
            current_node = current_node.value
        return root

    # Helper functions

    def visitDeref(self, ctx: MathParser.DerefContext):
        """
        Dereference visit function
        :param ctx: context
        :return: VarNode
        """
        # STR rvar
        # STR deref
        inp = ctx
        key = ""
        deref_count = 1
        # Get deref level
        while True:
            if isinstance(inp.children[1], MathParser.RvarContext):
                key = inp.children[1].getText()
                if self.symbol_table[key] is not None:
                    # Get pointer from symbol table
                    pointer = self.symbol_table[key]
                    if not isinstance(pointer , VarNode):
                        raise AttributeError("Variable " + key + " is not a pointer")
                    elif pointer.total_deref < deref_count:
                        raise RuntimeError("Trying to get pointer dereference depth" + str(deref_count)
                                           +" when pointer only has depth " + pointer.total_deref)
                    for i in range(deref_count):
                        pointer = pointer.value
                    out = copy.copy(pointer)
                    return out
            else:
                inp = inp.children[1]
                deref_count += 1

    # Tree reduction methods

    def isfloat(self, string):
        """
        Checks if inout is a float
        :param string: input variable
        :return: bool
        """
        try:
            float(string)
            return True
        except ValueError:
            return False

    def resolve_binary(self, expr_ast) -> AST | Node:
        """
        resolves binary operation,
        promotes operations to root and operands to their children
        :param expr_ast: input AST
        :return: AST | Node
        """
        if isinstance(expr_ast, Node):
            return expr_ast
        for i in range(len(expr_ast.children)):
            expr_ast.children[i] = self.resolve_binary(expr_ast.children[i])
            if expr_ast.children[i] is not None and isinstance(expr_ast.children[i], Node) and expr_ast.children[
                i].key in keywords_binary:
                new_el = AST()
                if i > 0:
                    new_el.add_child(expr_ast.children[i - 1])
                if i < len(expr_ast.children):
                    new_el.add_child(expr_ast.children[i + 1])
                new_el.root = expr_ast.children[i]
                expr_ast.children = [new_el]
                if len(expr_ast.children) == 1:
                    expr_ast.root = expr_ast.children[0].root
                    expr_ast.children = expr_ast.children[0].children
                    return expr_ast
                else:
                    for j in range(len(expr_ast.children)):
                        expr_ast.children[j] = self.resolve_binary(expr_ast.children[j])
                    return expr_ast
            elif expr_ast.children[i] is not None and isinstance(expr_ast.children[i], AST):
                expr_ast.children[i] = self.resolve_binary(expr_ast.children[i])
        return expr_ast

    def resolve_unary(self, expr_ast: AST | Node) -> AST | Node:
        """
        resolves unary operation,
        promotes operations to root and operands to their children
        :param expr_ast: input AST
        :return: AST | Node
        """
        if isinstance(expr_ast, Node):
            return expr_ast
        for i in range(len(expr_ast.children)):
            expr_ast.children[i] = self.resolve_unary(expr_ast.children[i])
            # Unary operations
            if expr_ast.children[i] is not None and isinstance(expr_ast.children[i], Node) and \
                    expr_ast.children[i].key in keywords_unary:
                new_el = AST()
                if i > 0:
                    new_el.add_child(expr_ast.children[i - 1])
                if i < len(expr_ast.children):
                    new_el.add_child(expr_ast.children[i + 1])
                new_el.root = expr_ast.children[i]
                expr_ast.root = new_el.root
                expr_ast.children = new_el.children
                if len(expr_ast.children) == 1:
                    return expr_ast
                else:
                    for j in range(len(expr_ast.children)):
                        expr_ast.children[j] = self.resolve_unary(expr_ast.children[j])
                    return expr_ast
            # Increment and decrement operations
            elif expr_ast.children[i] is not None and isinstance(expr_ast.children[i], Node) and \
                    expr_ast.children[i].key in keywords_indecr:
                # form rvar incr or rvar decr
                expr_ast.root = expr_ast.children[i]
                expr_ast.children.remove(expr_ast.children[i])
                expr_ast.children[0] = self.resolve_variables(expr_ast.children[0])
                return expr_ast
            # Casting operation
            elif expr_ast.children[i] is not None and isinstance(expr_ast.children[i], Node) and \
                    expr_ast.children[i].key == "cast":
                expr_ast.root = expr_ast.children[i]
                expr_ast.children.remove(expr_ast.children[i])
                expr_ast.children[0] = self.resolve_variables(expr_ast.children[0])
                return expr_ast
            elif expr_ast.children[i] is not None and isinstance(expr_ast.children[i], AST):
                expr_ast.children[i] = self.resolve_unary(expr_ast.children[i])
        return expr_ast

    def resolve_assign(self, expr_ast: AST | Node) -> AST | Node:
        """
        resolves assign operation,
        promotes operations to root and operands to their children
        :param expr_ast: input AST
        :return: AST | Node
        """
        if isinstance(expr_ast , Node):
            return expr_ast
        if len(expr_ast.children) < 3:
            return expr_ast
        for i in range(len(expr_ast.children)):
            expr_ast.children[i] = self.resolve_assign(expr_ast.children[i])
            if expr_ast.children[i] is not None and isinstance(expr_ast.children[i], Node) and expr_ast.children[i].key in keywords_assign:
                new_el = AST()
                if i > 0:
                    new_el.add_child(expr_ast.children[i - 1])
                if i < len(expr_ast.children):
                    new_el.add_child(expr_ast.children[i + 1])
                new_el.root = expr_ast.children[i]
                self.resolve_variables(new_el.children[0])
                self.resolve_variables(new_el.children[1])
                expr_ast.children = [new_el]
                return expr_ast

    def resolve_datatype(self , expr_ast: AST | Node) -> AST | Node:
        """
        resolves datatype operation,
        promotes operations to root and operands to their children
        :param expr_ast: input AST
        :return: AST | Node
        """
        if not isinstance(expr_ast , AST) or expr_ast.root.value is not None :
            return expr_ast
        if len(expr_ast.children) == 1:
            if isinstance(expr_ast.children[0], AST):
                expr_ast = expr_ast.children[0]
            elif isinstance(expr_ast.children[0], Node):
                if expr_ast.children[0].key == "var":
                    expr_ast = expr_ast.children[0]
                    expr_ast.key = expr_ast.value
                    if expr_ast.key in self.symbol_table.keys() and self.symbol_table[expr_ast.key] is not None:
                        expr_ast.value = self.symbol_table[expr_ast.key].value
                    else:
                        expr_ast.value = None
                elif isinstance(expr_ast.children[0] , VarNode):
                    expr_ast = expr_ast.children[0]
                    # Add the variable declaration to the symbols table
                    if expr_ast.key not in self.symbol_table:
                        self.symbol_table[expr_ast.key] = None
                    else:
                        expr_ast.value = self.symbol_table[expr_ast.key].value
                else:
                    expr_ast = expr_ast.children[0]
        return expr_ast

    def resolve_variables(self , input_ast : AST | Node) -> AST | Node:
        """
        resolves variable operation,
        promotes operations to root and operands to their children
        :param expr_ast: input AST
        :return: AST | Node
        """
        if not isinstance(input_ast , Node):
            return input_ast
        if input_ast.key == "var":
            input_ast.key = input_ast.value
            if input_ast.key in self.symbol_table.keys() and self.symbol_table[input_ast.key] is not None:
                input_ast.value = self.symbol_table[input_ast.key].value
        elif isinstance(input_ast, VarNode):
            # Add the variable declaration to the symbols table
            if input_ast.key not in self.symbol_table:
                self.symbol_table[input_ast.key] = None
        return input_ast

    def resolve_empty(self, expr_ast):
        """
        resolves empty operation,
        promotes operations to root and operands to their children
        :param expr_ast: input AST
        :return: AST | Node
        """
        if isinstance(expr_ast , Node):
            return expr_ast
        for child in expr_ast.children:
            if child is None:
                expr_ast.children.remove(child)
            else:
                self.resolve_empty(child)

    def unnest(self, input_ast: AST | Node):
        """
        unnest the operations
        :param input_ast: input AST or Node
        :return: AST
        """
        if isinstance(input_ast , Node):
            return input_ast
        if len(input_ast.children) == 1:
            return input_ast.children[0]
        else:
            for i in range(len(input_ast.children)):
                input_ast.children[i] = self.unnest(input_ast.children[i])
        return input_ast

    # Optimising tree by reducing operations with literals to their result
    def optimise_unary(self, input_ast: AST) -> AST | Node:
        """
        unary constant folding,
        replaces the AST --> Node with the result of the operation
        :param input_ast: Input AST
        :return: AST || Node
        """
        new_el = Node("", None)
        # check if they are both literals
        if len(input_ast.children) == 1:
            # unary sum
            if input_ast.root.value == "+":
                return input_ast.children[0]
            # unary dif
            elif input_ast.root.value == "-":
                new_el = input_ast.children[0]
                if not isinstance(new_el, Node):
                    return input_ast
                new_el.key = "int"
                new_el.value = - new_el.value
                return new_el
        elif len(input_ast.children) == 2:
            first = input_ast.children[0]
            second = input_ast.children[1]
            if first is not None and isinstance(first, AST):
                first = self.optimise(first)
            if second is not None and isinstance(second, AST):
                second = self.optimise(second)
            if first is not None and first.value is not None and second is not None and second.value is not None:
                if input_ast.root.value == "+":
                    new_el.value = first.value + second.value
                if input_ast.root.value == "-":
                    new_el.value = first.value - second.value
                if isinstance(new_el.value, float):
                    new_el.key = "float"
                elif isinstance(new_el.value, int):
                    new_el.key = "int"
            return new_el

    def optimise_binary(self, input_ast: AST) -> AST | Node:
        """
        binary constant folding,
        replaces the AST --> Node with the result of the operation
        :param input_ast: Input AST
        :return: AST || Node
        """
        new_el = Node("", None)
        first = input_ast.children[0]
        second = input_ast.children[1]
        # check if they are both literals
        if first is not None and isinstance(first, AST):
            first = self.optimise(first)
        if second is not None and isinstance(second, AST):
            second = self.optimise(second)
        # Resolve variables if they need to be
        if isinstance(first , Node):
            first = self.optimise_variables(first)
        if isinstance(second, Node):
            second = self.optimise_variables(second)
        if first is not None and first.value is not None and second is not None and second.value is not None:
            if input_ast.root.value == '*':
                new_el.value = first.value * second.value
            elif input_ast.root.value == '/':
                # check for implicit casting
                if first.key != "float" and second.key != "float":
                    new_el.value = int(first.value / second.value)
                else:
                    new_el.value = first.value / second.value
            elif input_ast.root.value == "%":
                new_el.value = int(first.value % second.value)
            if isinstance(new_el.value, float):
                new_el.key = "float"
            elif isinstance(new_el.value, int):
                new_el.key = "int"
        return new_el

    def optimise_comp_op(self, input_ast: AST) -> AST | Node:
        """
        compare operation constant folding,
        replaces the AST --> Node with the result of the operation
        :param input_ast: Input AST
        :return: AST || Node
        """
        new_el = Node("", None)
        first = input_ast.children[0]
        second = input_ast.children[1]
        # check if they are both literals
        if first is not None and isinstance(first, AST):
            first = self.optimise(first)
        if second is not None and isinstance(second, AST):
            second = self.optimise(second)
        if first is not None and first.key != "var" and second is not None and second.key != "var":
            if input_ast.root.value == '>':
                new_el.value = (first.value > second.value)
            elif input_ast.root.value == '<':
                new_el.value = (first.value < second.value)
            elif input_ast.root.value == "==":
                new_el.value = (first.value == second.value)
        if isinstance(new_el.value, bool):
            new_el.key = "bool"
        return new_el

    def optimise_comp_eq(self, input_ast: AST) -> AST | Node:
        """
        compare equal constant folding,
        replaces the AST --> Node with the result of the operation
        :param input_ast: Input AST
        :return: AST || Node
        """
        new_el = Node("", None)
        first = input_ast.children[0]
        second = input_ast.children[1]
        # check if they are both literals
        if first is not None and isinstance(first, AST):
            first = self.optimise(first)
        if second is not None and isinstance(second, AST):
            second = self.optimise(second)
        if first is not None and first.key != "var" and second is not None and second.key != "var":
            if input_ast.root.value == '>=':
                new_el.value = (first.value >= second.value)
            elif input_ast.root.value == '<=':
                new_el.value = (first.value <= second.value)
            elif input_ast.root.value == "!=":
                new_el.value = (first.value != second.value)
        if isinstance(new_el.value, bool):
            new_el.key = "bool"
        return new_el

    def optimise_bin_log(self, input_ast: AST) -> AST | Node:
        """
        binary logic constant folding,
        replaces the AST --> Node with the result of the operation
        :param input_ast: Input AST
        :return: AST || Node
        """
        new_el = Node("", None)
        first = input_ast.children[0]
        second = input_ast.children[1]
        # check if they are both literals
        if first is not None and isinstance(first, AST):
            first = self.optimise(first)
        if second is not None and isinstance(second, AST):
            second = self.optimise(second)
        if first is not None and first.key != "var" and second is not None and second.key != "var":
            if input_ast.root.value == '&&':
                new_el.value = (first.value and second.value)
            elif input_ast.root.value == '||':
                new_el.value = (first.value or second.value)
        if isinstance(new_el.value, bool):
            new_el.key = "bool"
        return new_el

    def optimise_un_log(self, input_ast: AST) -> AST | Node:
        """
        unary logic constant folding,
        replaces the AST --> Node with the result of the operation
        :param input_ast: Input AST
        :return: AST || Node
        """
        new_el = Node("", None)
        first = input_ast.children[0]
        # Check if condition is a literal
        if first is not None and isinstance(first, AST):
            first = self.optimise(first)
        if input_ast.root.value == "!":
            new_el.value = not first.value
        # Set the key name for the return node
        if isinstance(new_el.value, bool):
            new_el.key = "bool"
        return new_el

    def optimise_assign(self, input_ast: AST) -> AST | Node:
        """
        assign constant folding,
        replaces the AST --> Node with the result of the operation
        :param input_ast: Input AST
        :return: AST || Node
        """
        new_el = Node("" , None)
        # Get the ID
        first = input_ast.children[0]
        # Get the rvalue to assign to the ID
        second = input_ast.children[1]
        # Check if condition is a literal
        if first is None or not (isinstance(first, Node)):
            return input_ast
        if first is not None and isinstance(first , Node):
            first = self.optimise_variables(first)
            new_el = first
        if second is not None and isinstance(second, AST):
            second = self.optimise(second)
        if second is not None and isinstance(second , Node):
            if isinstance(first , VarNode) and first.ptr:
                if second.key in keywords_datatype:
                    raise AttributeError("Attempting to assign a non-variable to a pointer")
                val = self.symbol_table[second.key]
                second = VarNode(val.key , val.value , val.type , val.const , val.ptr , val.deref_level , val.total_deref)
            elif second.value is None:
                second = self.optimise_variables(second)
        if input_ast.root.value == "=":
            if new_el.key not in self.symbol_table:
                raise SyntaxError("Variable " + new_el.key + " not declared in this scope")
            if new_el.key in self.symbol_table and self.symbol_table[new_el.key] is not None:
                if self.symbol_table[new_el.key].value is not None and self.symbol_table[new_el.key].const:
                    raise RuntimeError("Attempting to modify a const variable " + new_el.key)
            if isinstance(first , VarNode):
                # Deref the required number of times
                if new_el.ptr and new_el.deref_level > 0 and not isinstance(second , VarNode):
                    raise RuntimeError("Attempting to assign value of pointer of depth " + new_el.deref_level + " to a non-pointer value")
                # Pointer assignment
                elif new_el.ptr:
                    if new_el.deref_level > 0 and not isinstance(second , VarNode):
                        raise RuntimeError("Attempting to assign pointer of depth greater than 0 to a non-pointer value")
                    if new_el.total_deref > second.total_deref + 1:
                        raise RuntimeError("Pointer depth incompatible for pointer "
                                           + new_el.key + " with depth " + str(new_el.total_deref) + " and pointer "
                                           + second.key + " with depth " + str(second.total_deref))
                    new_el.value = self.symbol_table[second.key]
                # Check if type matches
                elif second.key not in self.symbol_table.keys() and new_el.type != second.key:
                        # Check for any valid conversions
                        # Promoting conversions are good
                        if (self.symbol_table[new_el.key].type, second.key) in conv_promotions:
                            new_el.value = self.convert(second.value , self.symbol_table[new_el.key].type)
                        # Implicit demoting conversions
                        elif (self.symbol_table[new_el.key].type, second.key) in conversions:
                            self.warnings.append(
                                Fore.YELLOW + "Implicit conversion from " + second.key + " to " + self.symbol_table[
                                    new_el.key].type + " for variable " + new_el.key + ". Possible loss of information")
                            # print(Fore.YELLOW + "Implicit conversion from " + second.key + " to " + self.symbol_table[
                            #     new_el.key].type + " for variable " + new_el.key + ". Possible loss of information")
                            new_el.value = self.convert(second.value, self.symbol_table[new_el.key].type)
                        # No conversions
                        else:
                            raise TypeError("Assign value of invalid type. Should be " +
                                            self.symbol_table[new_el.key].type + " , but is " + second.key + "\n"
                                                                                                             "No valid conversion from " +
                                            self.symbol_table[new_el.key].type + " to " + second.key)
                elif second.key in self.symbol_table.keys() and self.symbol_table[second.key].type != new_el.type:
                    self.warnings.append(
                        Fore.YELLOW + "Implicit conversion from " + self.symbol_table[second.key].type + " to "
                        + self.symbol_table[new_el.key].type + " for variable " +
                        new_el.key + ". Possible loss of information")
                    new_el.value = self.convert(second.value , new_el.type)
                else:
                    new_el.value = second.value
                self.symbol_table[new_el.key].value = new_el.value
                return new_el
            else:
                new_el.key = first.key
                # Check that the assigned value is of correct type
                if self.symbol_table[new_el.key].type != second.key and second.key not in self.symbol_table.keys():
                    # Check for any valid conversions
                    # Promoting conversions are good
                    if (self.symbol_table[new_el.key].type , second.key) in conv_promotions:
                        new_el.value = second.value
                    # Implicit demoting conversions
                    elif (self.symbol_table[new_el.key].type , second.key) in conversions:
                        self.warnings.append(Fore.YELLOW + "Implicit conversion from " + second.key + " to " + self.symbol_table[
                            new_el.key].type + " for variable " + new_el.key + ". Possible loss of information")
                        # print(Fore.YELLOW + "Implicit conversion from " + second.key + " to " + self.symbol_table[
                        #     new_el.key].type + " for variable " + new_el.key + ". Possible loss of information")
                        new_el.value = self.convert(second.value, self.symbol_table[new_el.key].type)
                    # No conversions

                    elif second.key not in self.symbol_table.keys():
                        raise AttributeError("Variable " + second.key + " was not declared in this scope")
                    else:
                        raise TypeError("Assign value of invalid type. Should be " +
                                        self.symbol_table[new_el.key].type + " , but is " + second.key + "\n"
                                                                                                         "No valid conversion from " +
                                        self.symbol_table[new_el.key].type + " to " + second.key)
                elif isinstance(new_el.value, VarNode) and second.key in keywords_datatype:
                    raise AttributeError("Attempting to assign a pointer to a non-variable type")
                elif self.symbol_table[new_el.key].ptr and not self.symbol_table[second.key].ptr:
                    entry = self.symbol_table[new_el.key]
                    raise AttributeError("Incompatible types when assigning to type ‘" + entry.type + str('*')*entry.total_deref +"’ from type ‘float’")
                elif second.key in self.symbol_table.keys() and \
                        self.symbol_table[second.key].type != self.symbol_table[new_el.key].type:
                    second_type = self.symbol_table[second.key].type
                    # Check for any valid conversions
                    # Promoting conversions are good
                    if (second_type , self.symbol_table[new_el.key].type) in conv_promotions:
                        new_el.value = self.convert(second.value , self.symbol_table[new_el.key].type)
                    # Implicit demoting conversions
                    elif (self.symbol_table[new_el.key].type, second_type) in conversions:
                        self.warnings.append(
                            Fore.YELLOW + "Implicit conversion from " + second_type + " to " + self.symbol_table[
                                new_el.key].type + " for variable " + new_el.key + ". Possible loss of information")
                        # print(Fore.YELLOW + "Implicit conversion from " + second.key + " to " + self.symbol_table[
                        #     new_el.key].type + " for variable " + new_el.key + ". Possible loss of information")
                        new_el.value = self.convert(second.value, self.symbol_table[new_el.key].type)
                    # No conversions

                    elif second.key not in self.symbol_table.keys():
                        raise AttributeError("Variable " + second.key + " was not declared in this scope")
                    else:
                        raise TypeError("Assign value of invalid type. Should be " +
                                        self.symbol_table[new_el.key].type + " , but is " + second.key + "\n"
                                                                                                         "No valid conversion from " +
                                        self.symbol_table[new_el.key].type + " to " + second.key)
                else:
                    new_el.value = second.value
                self.symbol_table[new_el.key].value = new_el.value
        return new_el

    @staticmethod
    def convert(value, d_type):
        """
        help function for casting
        :param value: input_value
        :param d_type: cast type
        :return: casted value
        """
        try:
            if d_type == "int":
                if isinstance(value , int):
                    return value
                if isinstance(value , str):
                    return ord(value)
                else:
                    return int(value)
            elif d_type == "float":
                if isinstance(value , float):
                    return value
                if isinstance(value , str):
                    return float(ord(value))
                else:
                    return float(value)
            elif d_type == "char":
                if isinstance(value , str):
                    return value
                return chr(value)
        except:
            raise RuntimeError("Bad Cast")

    def optimise_variables(self, input_node : Node) -> Node :
        """
        variables constant folding,
        replaces the AST --> Node with the result of the operation
        :param input_ast: Input Node
        :return: Node
        """
        # Search for the variable name in the symbols table
        if input_node.key in self.symbol_table:
            if self.symbol_table[input_node.key] is None:
                if isinstance(input_node , VarNode):
                    new_node = VarNode(input_node.key , input_node.value , input_node.type , input_node.const)
                    self.symbol_table[new_node.key] = new_node
                    # check for usage of this variable in functions
                    for key , val in self.symbol_table.items():
                        if isinstance(val , FunctionNode):
                            for j in range(len(val.value)):
                                pass
                return input_node
            if self.symbol_table[input_node.key] is not None:
                if isinstance(input_node , VarNode) and self.symbol_table[input_node.key].const:
                    if input_node.value is not None and input_node.value != self.symbol_table[input_node.key].value:
                        raise RuntimeError("Attempting to modify a const variable " + input_node.key)
                else:
                    input_node.value = self.symbol_table[input_node.key].value
        return input_node

    def optimise_functions(self, input_node: Node) -> Node:
        """
        function constant folding,
        replaces the AST --> Node with the result of the operation
        :param input_ast: Input Node
        :return: Node
        """
        if isinstance(input_node, FunctionNode) and input_node.key in keywords_functions:
            for i in range(len(input_node.value)):
                if input_node.value["par" + str(i)].key in keywords_datatype:
                    return input_node
                elif isinstance(input_node.value["par" + str(i)] , Node) and input_node.value["par" + str(i)].value in self.symbol_table.keys():
                    input_node.value["par" + str(i)]= copy.copy(self.symbol_table[input_node.value["par" + str(i)].value])
                elif isinstance(input_node.value["par" + str(i)] , VarNode):
                    if self.symbol_table[input_node.value["par" + str(i)].key] is None:
                        raise NameError("Variable " + input_node.value["par" + str(i)] + " doesn't exist")
                    elif input_node.value["par" + str(i)].value is None:
                        raise NameError("Variable " + input_node.value["par" + str(i)] + " doesn't exist")
                    else:
                        input_node.value["par" + str(i)] = copy.copy(self.symbol_table[input_node.value["par" + str(i)].key])
                else:
                    pass
        return input_node

    def optimise_cast(self, input_node: AST) -> Node:
        """
        cast constant folding,
        replaces the AST --> Node with the result of the operation
        :param input_ast: Input AST
        :return: Node
        """
        # Check type of cast
        input_node.children[0].value = self.convert(input_node.children[0].value , input_node.root.value)
        input_node.children[0].key = input_node.root.value
        # if input_node.root.value == "int":
        #     input_node.children[0].value = int(input_node.children[0].value)
        # if input_node.root.value == "float":
        #     input_node.children[0].value = float(input_node.children[0].value)
        # if input_node.root.value == "char":
        #     input_node.children[0].value = chr(input_node.children[0].value)
        return input_node.children[0]

    def optimise_incr_decr(self, input_node: AST) -> Node:
        """
        increment or decrement constant folding,
        replaces the AST --> Node with the result of the operation
        :param input_ast: Input AST
        :return: Node
        """
        # Check which operation to perform
        if input_node.root.key == "incr":
            input_node.children[0].value += 1
        if input_node.root.key == "decr":
            input_node.children[0].value -= 1
        if input_node.children[0].key in self.symbol_table.keys():
            self.symbol_table[input_node.children[0].key].value = input_node.children[0].value
        return input_node.children[0]

    def optimise(self, input_ast : AST | Node) -> AST | Node:
        """
        constant folding,
        replaces the AST --> Node with the result of the operation
        :param input_ast: Input AST or Node
        :return: AST || Node
        """
        if isinstance(input_ast , AST):
            for i in range(len(input_ast.children)):
                input_ast.children[i] = self.optimise(input_ast.children[i])
            if input_ast.root.key == "cast":
                return self.optimise_cast(input_ast)
            elif input_ast.root.key == "assign_op":
                return self.optimise_assign(input_ast)
            elif input_ast.root.key == "unary_op":
                return self.optimise_unary(input_ast)
            elif input_ast.root.key == "binary_op":
                return self.optimise_binary(input_ast)
            # Comparison operations
            elif input_ast.root.key == "comp_op":
                return self.optimise_comp_op(input_ast)
            elif input_ast.root.key == "comp_eq":
                return self.optimise_comp_eq(input_ast)
            elif input_ast.root.key == "bin_log_op":
                return self.optimise_bin_log(input_ast)
            elif input_ast.root.key == "un_log_op":
                return self.optimise_un_log(input_ast)
            elif input_ast.root.key == "incr" or input_ast.root.key == "decr":
                return self.optimise_incr_decr(input_ast)
            else:
                return self.unnest(input_ast)
                # return input_ast
        elif isinstance(input_ast , FunctionNode):
            # return input_ast
            return self.optimise_functions(input_ast)
        elif isinstance(input_ast , VarNode):
            return self.optimise_variables(input_ast)
        elif isinstance(input_ast , Node):
            return self.optimise_variables(input_ast)
        # Unary operation node replacements

    def warn(self):
        """
        print all warnings on console
        :return: None
        """
        for warn in self.warnings:
            print(warn)
