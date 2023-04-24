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
            return self.visitPrintf(ctx)
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
                    if child.root.value in ["++" , "--" , "!"]:
                        child.children = base.children[index-1 : index]
                        base.children[index - 1: index] = []
                        index -= 1
                    else:
                        child.children = base.children[index-2 : index]
                        base.children[index - 2: index] = []
                        index -= 2
                    child.children.reverse()
                elif child.root.key == "factor" and child.root.value is not None:
                    if child.root.value in ["++" , "+" , "--" , "-"]:
                        child.children = base.children[index-1 : index]
                        base.children[index - 1: index] = []
                        index -= 1
                    child.children.reverse()
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
                    child.children = base.children[max(indexes["last_declr"], indexes["last_instr"]): index]
                    child.children.reverse()
                    base.children[max(indexes["last_declr"], indexes["last_instr"]): index] = []
                    index = base.children.index(child)
                    update_index = max(indexes["last_declr"], indexes["last_instr"])
                    update_index += 1
                elif child.root.key == "assign":
                    child.children = base.children[index - 2: index]
                    child.children.reverse()
                    base.children[index - 2: index] = []
                    # Add first child to symbol table if it isn't already in
                    if not self.symbol_table.exists(child.children[0].key):
                        # make one
                        new_object = child.children[0]
                        self.symbol_table.insert(SymbolEntry(new_object))
                    else:
                        raise AttributeError(f"Redeclaration of variable {child.children[0].key}")
                    index -= 2
                elif child.root.key == "printf":
                    child.children = base.children[index-1 : index]
                    base.children[index - 1: index] = []
                    index -= 1

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
                if child.key == "assign_op":
                    base.children[index] = AssignAST(Node("assign",None))
                    base.children[index].children = base.children[index-2:index]
                    base.children[index].children.reverse()
                    base.children[index-2:index] = []
                    index -= 2
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
                    # unhandled trees
                    if isinstance(child, AST):
                        handle = False
                        break
                    # unreplaced rvars
                    elif isinstance(child, Node) and child.key == "var":
                        # search in symbol table
                        if not self.symbol_table.exists(child.value):
                            raise ReferenceError(f"Variable {child.value} does was not declared in this scope")
                        else:
                            index = ast.children.index(child)
                            matches = self.symbol_table.lookup(child.value)
                            if len(matches) > 1:
                                raise ReferenceError(f"Multiple matches for variable {ast.children[0].key}")
                            ast.children[index] = matches[0].object
                if not handle:
                    continue
            # Variable assignment handling
            if ast.root.key == "assign" and ast.root.value is not None:
                if not isinstance(ast.children[0], VarNode):
                    raise AttributeError(f"Attempting to assign to a non variable type object")
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
                    node = ast.children[0]
                    # refresh symbol table
                    self.symbol_table.refresh()
                else:
                    raise AttributeError(f"Attempting to modify a const variable {ast.children[0]}")
            # declaration handling
            elif ast.root.key == "declr":
                if len(ast.children) != 1 or not isinstance(ast.children[0], VarNode):
                    raise RuntimeError("Faulty declaration")
                if ast.type != ast.children[0].type and ast.children[0].value is not None:
                    if (ast.type , ast.children[0].type) not in conversions:
                        raise AttributeError("Variable assigned to wrong type")
                    elif (ast.type , ast.children[0].type) not in conv_promotions:
                        self.warnings.append(f"Implicit conversion from {ast.root.value} to {ast.children[0].type}")
                node = ast.children[0]
                if ast.const:
                    node.const = True
                self.symbol_table.update(node)
                self.symbol_table.refresh()

            elif isinstance(ast, AssignAST):
                # check if assign value is of a valid type
                if not (isinstance(ast.children[1], Node) or isinstance(ast.children[1], VarNode)):
                    raise RuntimeError(f"\'Invalid assignment for variable {ast.children[0].key}\'")
                if isinstance(ast.children[1], VarNode):
                    rtype = ast.children[1].type
                else:
                    rtype = ast.children[1].key
                assignee = copy.copy(ast.children[0])
                if not isinstance(assignee, VarNode):
                    raise AttributeError(f"Attempting to assign to a non-variable type")
                if assignee.const:
                    raise AttributeError(f"Attempting to modify a const variable {assignee.key}")
                if rtype is None:
                    raise AttributeError(f"Type {rtype} does not exist")
                if rtype != assignee.type:
                    if (assignee.type , rtype) not in conversions:
                        raise AttributeError("Variable assigned to wrong type")
                    elif (rtype, assignee.type) not in conv_promotions:
                        self.warnings.append(f"Implicit conversion from {ast.root.value} to {ast.children[0].type}")
                assignee.value = ast.children[1].value
                self.symbol_table.update(assignee)
                # refresh symbol table
                self.symbol_table.refresh()
                node = assignee
            elif isinstance(ast, PrintfAST):
                # insert function into symbol table
                # hard code the parameters for this particular function
                if not isinstance(ast.children[0], VarNode):
                    continue
                new_param = FunctionParameter(getType(ast.children[0].value), None, "print_val")
                new_entry = FuncSymbolEntry(ast.root, in_parameters=[new_param])
                ast.root.type = new_param.type
                self.symbol_table.insert(new_entry)
                self.symbol_table.refresh()
                node = ast
            elif isinstance(ast, InstrAST):
                node = ast.handle()
                self.symbol_table.refresh()
            elif ast is not None:
                node = ast.handle()
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
        instr_ast = InstrAST()
        instr_ast.root = Node("instr", None)
        return instr_ast

    def visitExpr(self, ctx: MathParser.ExprContext):
        """
        Expression visit function
        :param ctx: context
        :return: AST
        """
        expr_ast = ExprAST()
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

        out = PrintfAST(FunctionNode(key= "printf"))
        # PrintfAST root is the definition of the function
        # PrintfAST children are the parameters given to the function
        return out

    def visitRvar(self, ctx: MathParser.RvarContext):
        """
        Right-hand side variable visit function
        :param ctx: context
        :return: Node
        """
        root = Node(keywords[0], ctx.children[0].getText())
        return root

    def visitRtype(self, ctx: MathParser.RtypeContext):
        """
        Right-hand side type visit function
        :param ctx: context
        :return: Node
        """
        if ctx.children[0].getText().isdigit():
            return Node(keywords_datatype[0], int(ctx.children[0].getText()))
        elif isfloat(ctx.children[0].getText()):
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
        out = DeclrAST(Node("declr", None))
        index = 0
        if ctx.children[index].getText() == "const":
            out.const = True
            index += 1
        if ctx.children[index].getText() in keywords_datatype:
            out.type = ctx.children[index].getText()
        else:
            raise TypeError(f"Variable declared with invalid type {ctx.children[0].getText()}")
        return out

    def visitVar_decl(self, ctx: MathParser.Var_declContext):
        """
        Variable declaration visit function
        :param ctx: context
        :return: VarNode || AST
        """
        if len(ctx.children) == 3:
            return VarDeclrAST(Node("assign", None))
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
        deref_count = 1
        # Get deref level
        while True:
            if isinstance(inp.children[1], MathParser.RvarContext):
                key = inp.children[1].getText()
                if self.symbol_table[key] is not None:
                    # Get a pointer from symbol table
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
        ast = TermAST()
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
        ast = FactorAST()
        if len(ctx.children) == 2:
            ast.root = Node("factor", ctx.children[0].getText())
        else:
            return None
        return ast

    def visitPrimary(self, ctx: MathParser.PrimaryContext):
        ast = PrimaryAST()
        if len(ctx.children) == 2:
            ast.root = Node("primary", ctx.children[0].getText())
        else:
            return None
        return ast

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
