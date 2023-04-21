import decimal
import socket
import struct
from math import floor

from colorama import Fore
import copy

import antlr4.tree.Tree
from AST import *
from SymbolTable import *
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
        self.symbol_table : SymbolTable = SymbolTable()
        self.warnings : list = []

    def visit_child(self, ctx):
        """
        visit the right visit function for the give context
        :param ctx: the context to know what to visit
        :return: the given output given by every visit function (AST or Node)
        """
        if isinstance(ctx, MathParser.InstrContext):
            return self.visitInstr(ctx)
        elif isinstance(ctx, MathParser.ExprContext):
            return self.visitExpr(ctx)
        elif isinstance(ctx, MathParser.RvarContext):
            return self.visitRvar(ctx)
        elif isinstance(ctx, MathParser.RtypeContext):
            return self.visitRtype(ctx)
        elif isinstance(ctx, MathParser.AssignContext):
            return self.visitAssign(ctx)
        elif isinstance(ctx, MathParser.LvarContext):
            return self.visitLvar(ctx)
        elif isinstance(ctx, MathParser.DerefContext):
            return Node("deref", None)
        elif isinstance(ctx, MathParser.PrintfContext):
            return Node("printf", None)
        elif isinstance(ctx, MathParser.Var_declContext):
            return self.visitVar_decl(ctx)
        elif isinstance(ctx , MathParser.DeclrContext):
            return self.visitDeclr(ctx)
        elif isinstance(ctx, MathParser.TermContext):
            return self.visitTerm(ctx)
        elif isinstance(ctx, MathParser.FactorContext):
            return self.visitFactor(ctx)
        elif isinstance(ctx, MathParser.PrimaryContext):
            return self.visitPrimary(ctx)


    def resolveTree(self, base: AST):
        """
        visit the right visit function for the give context
        :param base: The base AST given to resolve
        :return: the given output given by every visit function (AST or Node)
        """
        # Terminals processing
        index = 0
        indexes = {"last_instr": 0 , "last_declr": 0}
        for child in base.children[:]:
            if isinstance(child, AST):
                if child.root.key in ["expr" , "term"] and child.root.value is not None:
                    child.children = base.children[index-2 : index]
                    child.children.reverse()
                    base.children[index - 2: index] = []
                    index -= 2
                elif child.root.key == "primary" and child.root.value is not None:
                    child.children = base.children[index-1 : index]
                    base.children[index - 1: index] = []
                    index -= 1
                elif child.root.key == "instr":
                    # Parent of instr is base itself, if no parent is already found
                    if child.parent is None:
                        child.parent = base
                    child.children = base.children[indexes["last_instr"] : index]
                    child.children.reverse()
                    base.children[indexes["last_instr"] : index] = []
                    index = base.children.index(child)
                    indexes["last_instr"] += 1
                elif child.root.key == "declr":
                    child.children = base.children[indexes["last_declr"]: index]
                    child.children.reverse()
                    base.children[indexes["last_declr"]: index] = []
                    index = base.children.index(child)
                    indexes["last_declr"] += 1
                elif child.root.key == "assign":
                    child.children = base.children[index - 2: index]
                    child.children.reverse()
                    base.children[index - 2: index] = []
                    # Add first child to symbol table if it isn't already in
                    if not self.symbol_table.exists(base.children[0]):
                        # make one
                        new_object = child.children[0]
                        self.symbol_table.insert(SymbolEntry(new_object))
                    else:
                        pass
                    index -= 2
                # connect children to this node
                for n in child.children:
                    n.parent = child
                    if child.root.key == "declr" and child.root.value is not None:
                        if isinstance(n , AST):
                            n.root.value = child.root.value
                        elif isinstance(n, VarNode):
                            n.type = child.root.value
            elif isinstance(child, Node):
                if child.key == "term" and child.value is None:
                    child.value = base.children[index-1].value

            index += 1
        base.children.reverse()
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
                v = self.visit_child(v)
                if v is None:
                    continue
                a.add_child(v)
        a = self.resolveTree(a)
        self.resolve(a)
        return a

    def resolve(self, ast_in : AST):
        visited = list()
        not_visited = list()
        not_visited.append(ast_in)
        while len(not_visited) > 0:
            temp = not_visited.pop()
            if temp not in visited:
                visited.append(temp)
                for i in temp.children:
                    if isinstance(i, AST):
                        not_visited.append(i)
        visited.reverse()
        self.handle(visited)
        return ast_in

    def handle(self, list_ast: list):
        for ast in list_ast:
            if len(ast.children) == 0:
                continue
            if len(ast.children) > 0:
                handle = True
                for child in ast.children:
                    if isinstance(child, AST):
                        handle = False
                        break
                if not handle:
                    continue
            # Variable assignment handling
            if ast.root.key == "assign" and ast.root.value is not None:
                if not isinstance(ast.children[0], VarNode):
                    raise AttributeError("Attempting to assign to a non variable type object")
                # check if variable is not in the symbol table
                if not self.symbol_table.exists(ast.children[0]):
                    raise ReferenceError(f"Variable {ast.children[0]} does was not declared in this scope")
                matches = self.symbol_table.lookup(ast.children[0])
                if len(matches) > 1:
                    raise ReferenceError(f"Multiple matches for variable {ast.children[0]}")
                # assign the value to the variable if it is not constant
                if not ast.children[0].const:
                    ast.children[0].value = ast.children[1].value
                    # get type
                    if isinstance(ast.children[1].value , int):
                        ast.children[0].type = "int"
                    elif isinstance(ast.children[1].value , float):
                        ast.children[0].type = "float"
                    elif isinstance(ast.children[1].value , str) and len(ast.children[1].value) == 1:
                        ast.children[0].type = "char"
                    else:
                        raise TypeError(f"Wrong type assigned to {ast.children[0]}")
                    self.symbol_table.update(ast.children[0])
                    # for i in range(len(ast.parent.children)):
                    #     if ast.parent.children[i] is ast:
                    node = ast.children[0]
            # Operations handling
            elif ast.root.value == '/':
                # Create node
                node = ast.children[0] / ast.children[1]
                if ast.children[0].key != "float" and ast.children[1].key != "float":
                    node.value = floor(node.value)
            elif ast.root.value == '+':
                # Check if one of the nodes is an unresolved variable
                if isinstance(ast.children[0].value , str) or isinstance(ast.children[1].value, str):
                    continue
                node = ast.children[0] + ast.children[1]
                node_type = self.checkType(str(node.value))
                node.key = node_type
            elif ast.root.value == '-':
                # Create node
                node = ast.children[0] - ast.children[1]
                node_type = self.checkType(str(node.value))
                node.key = node_type
            elif ast.root.value == '*':
                # Create node
                node = ast.children[0] * ast.children[1]
                node_type = self.checkType(str(node.value))
                node.key = node_type
            elif ast.root.value == '%':
                # Create node
                node = ast.children[0] % ast.children[1]
                node_type = self.checkType(str(node.value))
                node.key = node_type
            # declaration handling
            elif ast.root.key == "declr":
                if len(ast.children) != 1 or not isinstance(ast.children[0], VarNode):
                    raise RuntimeError("Faulty declaration")
                if ast.root.value != ast.children[0].type:
                    if (ast.root.value , ast.children[0].type) not in conversions:
                        raise AttributeError("Variable assigned to wrong type")
                    elif (ast.root.value , ast.children[0].type) not in conv_promotions:
                        self.warnings.append(f"Implicit conversion from {ast.root.value} to {ast.children[0].type}")
                node = ast.children[0]

            else:
                continue
            # Replace node
            index = ast.parent.children.index(ast)
            ast.parent.children[index] = node

    def visitMath(self, ctx: MathParser.MathContext):
        """
        Math visit function
        :param ctx: context
        :return: AST
        """
        math_ast = self.DFS(None, ctx)
        return math_ast

    def visitInstr(self, ctx: MathParser.InstrContext):
        """
        Instruction visit
        :param ctx: context
        :return: AST
        """
        instr_ast = AST()
        instr_ast.root = Node("instr", None)
        return instr_ast

    def visitExpr(self, ctx: MathParser.ExprContext):
        """
        Expression visit function
        :param ctx: context
        :return: AST
        """
        expr_ast = AST()
        expr_ast.root = Node("expr" , None)
        if len(ctx.children) == 3:
            expr_ast.root.value = ctx.children[1].getText()
        else:
            return None
        return expr_ast

    def visitPrintf(self, ctx: MathParser.PrintfContext):
        """
        Creates the node for printf function
        :param ctx: context
        :return: Node
        """
        out = FunctionNode(ctx.children[0].getText() ,
                           {"par0" : self.visit_child(ctx.children[2])}
                           )
        # if not out.key in self.symbol_table.keys():
        #     self.symbol_table[out.key] = [copy.copy(out)]
        # else:
        #     self.symbol_table[out.key].append(copy.copy(out))
        return out

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
        """
        Declaration visit function
        :param ctx: context
        :return: AST
        """
        out = AST(Node("declr", None))
        index = 0
        if ctx.children[index].getText() == "const":
            out.root.value = ctx.children[index].getText()
            index += 1
        if ctx.children[index].getText() in keywords_datatype:
            out.root.value = ctx.children[index].getText()
        else:
            raise TypeError(f"Variable declared with invalid type {ctx.children[0].getText()}")
        return out

    def visitVar_decl(self, ctx: MathParser.Var_declContext):
        """
        Variable declaration visit function
        :param ctx: context
        :return: VarNode || AST
        """
        # out = VarNode("" , None , "")
        # if len(ctx.children) == 1:
        #     out = self.visit_child(ctx.children[0])
        # else:
        #     out = AST()
        #     for c in ctx.children:
        #         out.add_child(self.visit_child(c))
        #     # return VarNode(vtype=ctx.children[0].getText(), key=ctx.children[1].getText(), value=None)
        #     out.root = Node("expr" , None)
        if len(ctx.children) == 3:
            return AST(Node("assign", None))
        else:
            return None

    def visitLvar(self, ctx: MathParser.LvarContext):
        """
        Left hand side variable
        :param ctx: context
        :return: VarNode
        """
        if len(ctx.children) == 1:
            root = VarNode(ctx.children[-1].getText() , None , "")
            return root
        # If more than 1 element: it's a pointer
        root = VarNode(ctx.children[-1].getText(), None , "" , ptr= (len(ctx.children) - 1 > 0), total_deref= len(ctx.children) - 1)

        # Make a length-1 chain on the symbol table for the pointer
        # current_node = root
        # for i in range(len(ctx.children) - 1):
        #     if current_node.key not in self.symbol_table.keys():
        #         self.symbol_table[current_node.key] = root
        #         root.value = current_node
        #         root.ptr = True
        #     current_node.value = VarNode(current_node.key , None , current_node.type , current_node.const , current_node.total_deref > 1 , i + 1 , current_node.total_deref - 1)
        #     current_node = current_node.value
        return root

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

    def visitTerm(self, ctx: MathParser.TermContext):
        ast = AST()
        if len(ctx.children) == 3:
            ast.root = Node("term", ctx.children[1].getText())
        elif len(ctx.children) == 2:
            if ctx.children[0].getText() == '!':
                ast.root = Node("term", ctx.children[0].getText())
            else:
                ast.root = Node("term", ctx.children[1].getText())
        else:
            return None
        return ast

    def visitFactor(self, ctx: MathParser.FactorContext):
        ast = AST()
        if len(ctx.children) == 2:
            ast.root = Node("factor", ctx.children[0].getText())
        else:
            return None
        return ast

    def visitPrimary(self, ctx: MathParser.PrimaryContext):
        ast = AST()
        if len(ctx.children) == 2:
            ast.root = Node("primary", ctx.children[0].getText())
        else:
            return None
        return ast

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

    def checkType(self, input: str):
        if input.isdigit():
            return "int"
        elif self.isfloat(input):
            return "float"
        else:
            return "char"
    @staticmethod
    def convert(value, d_type):
        """
        help function for casting
        :param value: input_value
        :param d_type: cast type
        :return: cast value
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

    def warn(self):
        """
        print all warnings on console
        :return: None
        """
        for warn in self.warnings:
            print(warn)
