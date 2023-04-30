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


class AstCreator(MathVisitor):

    def __init__(self) -> None:
        """
        Initializer function
        """
        super().__init__()
        self.base_ast: AST = AST()
        self.symbol_table: SymbolTable = SymbolTable()
        self.warnings: list = []

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
            return self.visitDeref(ctx)
        elif isinstance(ctx, MathParser.PrintfContext):
            return self.visitPrintf(ctx)
        elif isinstance(ctx, MathParser.Var_declContext):
            return self.visitVar_decl(ctx)
        elif isinstance(ctx, MathParser.DeclrContext):
            return self.visitDeclr(ctx)
        elif isinstance(ctx, MathParser.TermContext):
            return self.visitTerm(ctx)
        elif isinstance(ctx, MathParser.FactorContext):
            return self.visitFactor(ctx)
        elif isinstance(ctx, MathParser.PrimaryContext):
            return self.visitPrimary(ctx)
        elif isinstance(ctx, MathParser.ScopeContext):
            return self.visitScope(ctx)
        elif isinstance(ctx, MathParser.For_loopContext):
            return self.visitFor_loop(ctx)
        elif isinstance(ctx, MathParser.While_loopContext):
            return self.visitWhile_loop(ctx)
        elif isinstance(ctx, MathParser.If_condContext):
            return self.visitIf_cond(ctx)
        elif isinstance(ctx, MathParser.Else_condContext):
            return self.visitElse_cond(ctx)
        elif isinstance(ctx, MathParser.InitContext):
            return self.visitInit(ctx)
        elif isinstance(ctx, MathParser.CondContext):
            return self.visitCond(ctx)
        elif isinstance(ctx, MathParser.IncrContext):
            return self.visitIncr(ctx)
        elif isinstance(ctx, MathParser.Cont_instrContext):
            return self.visitCont_instr(ctx)
        elif isinstance(ctx, MathParser.Break_instrContext):
            return self.visitBreak_instr(ctx)
        elif isinstance(ctx, antlr4.tree.Tree.TerminalNodeImpl):
            if ctx.getText() in ["{", "}"]:
                return Node(ctx.getText(), None)

    @staticmethod
    def searchPrevToken(index: int, in_list, token: str = '}'):
        # index = len(in_list)
        for i in reversed(range(index)):
            if isinstance(in_list[i], Node) and in_list[i].key == token:
                return i
        return -1

    @staticmethod
    def lastInstruction(index: int, in_list, token: str = '}'):
        for i in reversed(range(index)):
            if isinstance(in_list[i], InstrAST) or (isinstance(in_list[i], Node) and in_list[i].key == token):
                return i
        return -1

    @staticmethod
    def lastDeclaration(index: int, in_list, token: str = '}'):
        for i in reversed(range(index)):
            if isinstance(in_list[i], InstrAST) or (
                    isinstance(in_list[i], Node) and in_list[i].key == token) or isinstance(in_list[i], DeclrAST):
                return i
        return -1

    @staticmethod
    def lastInit(index: int, in_list, token: str = '}'):
        for i in reversed(range(index)):
            if isinstance(in_list[i], CondAST):
                return i
        return -1

    @staticmethod
    def lastElse(index: int, in_list, token: str = '}'):
        for i in reversed(range(index)):
            if isinstance(in_list[i], Else_CondAST):
                return i
        return -1

    def resolveTree(self, base: AST):
        """
        visit the right visit function for the give context
        :param base: The base AST given to resolve
        :return: the given output given by every visit function (AST or Node)
        """
        # Terminals processing
        index = 0
        indexes = {"last_instr": 0, "last_declr": 0, "last_scope": [0], "last_scope_open": 0, "scope_depth": 0}
        last_else = None
        for child in base.children[:]:
            if isinstance(child, AST):
                if child.root.key in ["expr", "term"] and child.root.value is not None:
                    if child.root.value in ["++", "--", "!"]:
                        child.children = base.children[index - 1: index]
                        base.children[index - 1: index] = []
                        index -= 1
                    else:
                        child.children = base.children[index - 2: index]
                        base.children[index - 2: index] = []
                        index -= 2
                    child.children.reverse()
                elif child.root.key == "factor" and child.root.value is not None:
                    if child.root.value in ["++", "+", "--", "-"]:
                        child.children = base.children[index - 1: index]
                        base.children[index - 1: index] = []
                        index -= 1
                    child.children.reverse()
                elif child.root.key == "primary" and child.root.value is not None:
                    child.children = base.children[index - 1: index]
                    base.children[index - 1: index] = []
                    index -= 1
                elif isinstance(child, CondAST):
                    child.children = base.children[index - 2: index]
                    child.children.reverse()
                    base.children[index-2:index] = []
                    index = base.children.index(child)
                elif isinstance(child, InitAST):
                    last_decl = self.lastInit(index, base.children)
                    last_decl += 1
                    child.children = base.children[last_decl: index]
                    child.children.reverse()
                    base.children[last_decl: index] = []
                    index = base.children.index(child)
                    update_index = last_decl
                    update_index += 1
                elif isinstance(child, InstrAST):
                    # Parent of instr is base itself, if no parent is already found
                    if child.parent is None:
                        child.parent = base
                    if self.searchPrevToken(index=index, token="}", in_list=base.children) == -1:
                        child.children = base.children[indexes["last_instr"]: index]
                        base.children[indexes["last_instr"]: index] = []
                    else:
                        last_inst = self.lastInstruction(index, base.children)
                        child.children = base.children[last_inst + 1:index]
                        base.children[last_inst + 1: index] = []
                    child.children.reverse()
                    index = base.children.index(child)
                    indexes["last_instr"] = index + 1
                elif isinstance(child, If_CondAST) or isinstance(child, While_loopAST):
                    if child.parent is None:
                        child.parent = base
                    number = 2
                    else_child = None
                    if isinstance(base.children[index - 3], Else_CondAST):
                        number = 3
                        else_child = base.children[index - 3]
                    child.children = base.children[index - number: index]
                    base.children[index - number: index] = []
                    child.children.reverse()
                    # assign condition
                    child.condition = child.children[0]
                    child.condition.parent = child
                    child.children = child.children[1:]
                    index = base.children.index(child)
                elif isinstance(child, Else_CondAST):
                    if child.parent is None:
                        child.parent = base
                    child.children = base.children[index - 1: index]
                    base.children[index - 1: index] = []
                    child.children.reverse()
                    last_else = child
                    index = base.children.index(child)
                elif isinstance(child, For_loopAST):
                    if child.parent is None:
                        child.parent = base
                    child.children = base.children[index - 4: index]
                    base.children[index - 4: index] = []
                    child.children.reverse()
                    # assign initialization
                    child.initialization = child.children[0]
                    child.initialization.parent = child
                    # assign condition
                    child.condition = child.children[1]
                    child.condition.parent = child
                    # assign increment
                    child.incr = child.children[2]
                    child.incr.parent = child
                    child.children = child.children[3:]
                    index = base.children.index(child)
                elif isinstance(child, Scope_AST):
                    # Parent of scope is base itself, if no parent is already found
                    # indexes["scope_depth"] += 1
                    if len(indexes["last_scope"]) < indexes["scope_depth"]:
                        indexes["last_scope"].append(0)
                    if child.parent is None:
                        child.parent = base
                    new_index = self.searchPrevToken(index=index, token="}", in_list=base.children)
                    base.children[new_index:new_index + 1] = []
                    child.children = base.children[new_index: index - 1]
                    child.children.reverse()
                    base.children[new_index: index - 1] = []
                    index = base.children.index(child)
                    # indexes["last_scope"][(indexes["scope_depth"]-1)] += 1
                    indexes["last_instr"] = self.lastInstruction(index, base.children) + 1
                elif isinstance(child, DeclrAST):
                    last_decl = self.lastDeclaration(index, base.children)
                    last_decl += 1
                    child.children = base.children[last_decl: index]
                    child.children.reverse()
                    base.children[last_decl: index] = []
                    index = base.children.index(child)
                    update_index = last_decl
                    update_index += 1
                elif child.root.key == "assign":
                    child.children = base.children[index - 2: index]
                    child.children.reverse()
                    base.children[index - 2: index] = []
                    # # Add first child to symbol table if it isn't already in
                    # if not temp_symbol.exists(child.children[0].key):
                    #     # make one
                    #     new_object = child.children[0]
                    #     temp_symbol.insert(SymbolEntry(new_object))
                    # else:
                    #     raise AttributeError(f"Redeclaration of variable {child.children[0].key}")
                    index -= 2
                elif child.root.key == "printf":
                    child.children = base.children[index - 1: index]
                    base.children[index - 1: index] = []
                    index -= 1
                elif child.root.key == "deref":
                    child.children = base.children[index - 1: index]
                    base.children[index - 1: index] = []
                    index -= 1
                # connect children to this node
                child = base.children[index]
                for n in child.children:
                    n.parent = child
                    if child.root.key == "declr" and child.root.value is not None:
                        if isinstance(n, AST):
                            n.root.value = child.root.value
                        elif isinstance(n, VarNode):
                            n.type = child.root.value
            elif isinstance(child, Node):
                if child.key == "}":
                    indexes["scope_depth"] += 1
                    indexes["last_scope_open"] = index
                    # base.children[index:index+1] = []
                    # index -= 1
                if child.key == "{":
                    indexes["scope_depth"] -= 1
                    base.children[index:index + 1] = []
                    index -= 1
                if child.key == "term" and child.value is None:
                    child.value = base.children[index - 1].value
                if child.key == "assign_op":
                    base.children[index] = AssignAST(Node("assign", None))
                    base.children[index].children = base.children[index - 2:index]
                    base.children[index].children.reverse()
                    base.children[index - 2:index] = []
                    index -= 2
                if isinstance(base.children[index], AST):
                    child = base.children[index]
                    # connect children to this node
                    for n in child.children:
                        n.parent = child
                        if child.root.key == "declr" and child.root.value is not None:
                            if isinstance(n, AST):
                                n.root.value = child.root.value
                            elif isinstance(n, VarNode):
                                n.type = child.root.value
            index += 1
        base.children.reverse()
        return base

    def DFS(self, visited, ctx, root_name: str = "math"):
        if visited is None:
            visited = []
        s = list()
        a = AST(root=Node(root_name, None))
        s.append(ctx)
        # while there are still nodes to visit in the tree
        while len(s) > 0:
            v = s.pop()
            if v not in visited:
                visited.append(v)
                s.append(v)
                if isinstance(v, antlr4.tree.Tree.TerminalNodeImpl):
                    continue
                for child in v.getChildren():
                    s.append(child)
            else:
                v = self.visit_child(v)
                if v is None:
                    continue
                a.add_child(v)
        a = self.resolveTree(a)
        return a

    def resolve(self, ast_in: AST):
        visited = list()
        not_visited = list()
        not_visited.append(ast_in)
        while len(not_visited) > 0:
            temp = not_visited.pop()
            if temp not in visited or isinstance(temp, CondAST):
                # if a scope, skip
                if not (isinstance(temp, Scope_AST) and temp is ast_in or temp.parent is ast_in):
                    visited.append(temp)
                if not isinstance(temp, Scope_AST) or temp is ast_in or temp.parent is ast_in:
                    for i in temp.children:
                        if isinstance(i, AST) and not isinstance(i, Else_CondAST):
                            not_visited.append(i)
                else:
                    if temp.condition is not None and not isinstance(temp.condition, Node):
                        not_visited.append(temp.condition)
        visited.reverse()
        self.handle(visited)
        return ast_in

    def handle(self, list_ast: list):
        # initialize queues
        updates_queue = []
        incr_queue = []
        decr_queue = []
        # flags
        conditional = False
        # initialize symbol table from root
        symbol_table = list_ast[-1].symbolTable
        temp_symbol = symbol_table
        temp_parent = list_ast[-1].parent
        while symbol_table is None and temp_parent is not None:
            temp_parent = list_ast[-1].parent
            symbol_table = temp_parent.symbolTable
        if symbol_table is None:
            raise RuntimeError("No symbol table found")
        # handle
        for ast in list_ast:
            if len(ast.children) == 0:
                continue
            if len(ast.children) > 0:
                handle = True
                for child in ast.children:
                    # unhandled trees
                    if isinstance(child, AST) and not isinstance(ast, Scope_AST):
                        handle = False
                        break
                    # unreplaced rvars
                    elif isinstance(child, Node) and child.key == "var":
                        # search in symbol table
                        exists_state = symbol_table.exists(child.value)
                        temp_ast = ast
                        # search in parent scopes if not found
                        old_symbol = symbol_table
                        while not exists_state and temp_ast is not None and temp_parent is not None:
                            temp_symbol = temp_ast.parent.symbolTable
                            temp_ast = temp_ast.parent
                            if temp_symbol is not None:
                                exists_state = temp_symbol.exists(child.value)
                        if not temp_symbol.exists(child.value):
                            raise ReferenceError(f"Variable {child.value} was not declared in this scope")
                        else:
                            index = ast.children.index(child)
                            matches = temp_symbol.lookup(child.value)
                            if len(matches) == 0:
                                raise ReferenceError(f"Variable {ast.children[0].key} undeclared")
                            if len(matches) > 1:
                                raise ReferenceError(f"Multiple matches for variable {ast.children[0].key}")
                            ast.children[index] = copy.copy(matches[0].object)
                            temp_symbol = old_symbol
                if not handle:
                    continue
            # conditional cases
            if isinstance(ast, If_CondAST) or isinstance(ast, Else_CondAST):
                # handle for condition true
                if ast.condition.value:
                    self.resolve(ast)
                    ast.symbolTable = ast.children[0].symbolTable
                # handle for else
                elif not ast.condition.value and isinstance(ast.children[-1], Else_CondAST):
                    self.resolve(ast.children[-1])
                    ast.symbolTable = ast.children[-1].children[0].symbolTable
                # update symbol table
                for update in updates_queue:
                    temp_symbol.update(update)
                updates_queue = []
                for entry in ast.symbolTable.table:
                    if temp_symbol.exists(entry.object):
                        updates_queue.append(entry.object)
                    else:
                        temp_symbol.insert(entry.object)

            # Variable assignment handling
            if ast.root.key == "assign" and ast.root.value is not None:
                if not isinstance(ast.children[0], VarNode):
                    raise AttributeError(f"Attempting to assign to a non variable type object")
                # assign the value to the variable if it is not constant
                if not ast.children[0].const:
                    ast.children[0].value = ast.children[1].value
                    # get type
                    if isinstance(ast.children[1].value, int):
                        ast.children[0].type = "int"
                    elif isinstance(ast.children[1].value, float):
                        ast.children[0].type = "float"
                    elif isinstance(ast.children[1].value, str) and len(ast.children[1].value) == 1:
                        ast.children[0].type = "char"
                    else:
                        raise TypeError(f"Wrong type assigned to {ast.children[0]}")
                    # Pointer depth check
                    if isinstance(ast.children[0], VarNode) and isinstance(ast.children[1], VarNode) \
                            and ast.children[0].ptr and ast.children[1].ptr:
                        if ast.children[0].total_deref != ast.children[1].total_deref + 1:
                            raise AttributeError(
                                f"Incompatible types for {ast.children[0].key} and {ast.children[1].key}.")
                    updates_queue.append(ast.children[0])
                    node = ast.children[0]
                    # refresh symbol table
                    # self.symbol_table.refresh()
                else:
                    raise AttributeError(f"Attempting to modify a const variable {ast.children[0]}")
            # declaration handling
            elif isinstance(ast, DeclrAST):
                if len(ast.children) != 1 or not isinstance(ast.children[0], VarNode):
                    raise RuntimeError("Faulty declaration")
                if symbol_table.exists(ast.children[0].key):
                    matches = temp_symbol.lookup(ast.children[0].key)
                    if len(matches) != 1:
                        raise ReferenceError(f"Multiple matches for variable {ast.children[0].key}")
                    match = matches[0]
                    if match.initialized():
                        raise AttributeError(f"Redeclaration of variable {ast.children[0].key}")

                if ast.type != ast.children[0].type and ast.children[0].value is not None and not ast.children[0].cast:
                    if (ast.children[0].type, ast.type) not in conversions:
                        raise AttributeError("Variable assigned to wrong type")
                    elif (ast.children[0].type, ast.type) not in conv_promotions:
                        self.warnings.append(
                            f"Implicit conversion from {ast.children[0].type} to {ast.type} for variable {ast.children[0].key}")
                node = ast.children[0]
                node.type = ast.type
                # node.const = (ast.const is True)
                if node.ptr and ast.const:
                    node.const_ptr = True
                else:
                    node.const = (ast.const is True)
                if not temp_symbol.exists(node):
                    temp_symbol.insert(SymbolEntry(node))
                updates_queue.append(node)
                # self.symbol_table.refresh()

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
                if rtype != assignee.type and not ast.children[1].cast:
                    if (assignee.type, rtype) not in conversions:
                        raise AttributeError("Variable assigned to wrong type")
                    elif (rtype, assignee.type) not in conv_promotions:
                        self.warnings.append(
                            f"Implicit conversion from {ast.root.value} to {ast.children[0].type} for variable {ast.children[0].key}")
                if isinstance(ast.children[0], VarNode) and isinstance(ast.children[1], VarNode) and ast.children[
                    0].ptr and ast.children[1].ptr and ast.children[0].total_deref != ast.children[1].total_deref + 1:
                    raise AttributeError(
                        f"Incompatible types for {ast.children[0].key} and {ast.children[1].key}.")
                if isinstance(ast.children[0], VarNode) and not isinstance(ast.children[1], VarNode):
                    if ast.children[0].total_deref - ast.children[0].deref_level != 0:
                        raise AttributeError(
                            f"Incompatible types for {ast.children[0].key} and {ast.children[1].key}.")
                assignee.value = ast.children[1].value
                assignee.type = getType(assignee.value)
                updates_queue.append(assignee)
                # refresh symbol table
                # self.symbol_table.refresh()
                node = assignee
            elif isinstance(ast, PrintfAST):
                # insert function into symbol table
                # hard code the parameters for this particular function
                if not isinstance(ast.children[0], VarNode):
                    continue
                new_param = FunctionParameter(getType(ast.children[0].value), None, "print_val")
                new_entry = FuncSymbolEntry(ast.root, in_parameters=[new_param])
                ast.root.type = new_param.type
                temp_symbol.insert(new_entry)
                temp_symbol.refresh()
                node = ast
            elif isinstance(ast, InstrAST):
                node = ast.handle()
                updates_queue.reverse()
                for instance in incr_queue:
                    instance = symbol_table.lookup(instance)[0].object
                    instance.value += 1
                    temp_symbol.update(instance)
                for instance in decr_queue:
                    instance = symbol_table.lookup(instance)[0].object
                    instance.value -= 1
                    temp_symbol.update(instance)
                for instance in updates_queue:
                    if not temp_symbol.exists(instance):
                        temp_symbol.insert(SymbolEntry(instance))
                    else:
                        temp_symbol.update(instance)

                temp_symbol.refresh()
                updates_queue = []
                incr_queue = []
                decr_queue = []
            elif isinstance(ast, TermAST) and ast.root.value in ["++", "--"]:
                node = ast.children[0]
                if ast.root.value == "++":
                    incr_queue.append(node)
                if ast.root.value == "--":
                    decr_queue.append(node)
                pass
            elif ast is not None:
                node = ast.handle()
            else:
                continue
            # Replace node
            if not isinstance(ast, CondAST):
                index = ast.parent.children.index(ast)
                ast.parent.children[index] = node
            else:
                ast.parent.condition = node
                if isinstance(ast.parent, Else_CondAST):
                    node.value = not node.value
        for instance in updates_queue:
            temp_symbol.update(instance)
        temp_symbol.refresh()
        symbol_table = temp_symbol

    def visitMath(self, ctx: MathParser.MathContext):
        """
        Math visit function
        :param ctx: context
        :return: AST
        """
        math_ast = self.DFS(None, ctx)
        math_ast.symbolTable = SymbolTable()
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
        expr_ast.root = Node("expr", None)
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

        out = PrintfAST(FunctionNode(key="printf"))
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
            root = VarNode(ctx.children[-1].getText(), None, "")
            return root
        # If more than 1 element: it's a pointer
        root = VarNode(ctx.children[-1].getText(), None, "", ptr=(len(ctx.children) - 1 > 0),
                       total_deref=len(ctx.children) - 1)
        return root

    def visitDeref(self, ctx: MathParser.DerefContext):
        """
        Dereference visit function
        :param ctx: context
        :return: VarNode
        """
        # STR rvar
        # STR deref
        out = DerefAST(Node("deref", None))
        return out

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

    def visitScope(self, ctx: MathParser.ScopeContext):
        return Scope_AST(Node("unnamed", None))

    def visitIf_cond(self, ctx: MathParser.If_condContext):
        return If_CondAST(Node("If_cond", None))

    def visitElse_cond(self, ctx: MathParser.Else_condContext):
        return Else_CondAST(Node("Else_cond", None))

    def visitWhile_loop(self, ctx: MathParser.While_loopContext):
        return While_loopAST(Node("While_loop", None))

    def visitFor_loop(self, ctx: MathParser.For_loopContext):
        return For_loopAST(Node("For_loop", None))

    def visitInit(self, ctx: MathParser.InitContext):
        if len(ctx.children) == 1:
            return Node(keywords[8], ctx.children[0].getText())
        else:
            out = InitAST(Node("init", None))
            index = 0
            if ctx.children[index].getText() in keywords_datatype:
                out.type = ctx.children[index].getText()
            else:
                raise TypeError(f"Variable declared with invalid type {ctx.children[0].getText()}")
            return out

    def visitCond(self, ctx: MathParser.CondContext):
        ast = CondAST()
        if len(ctx.children) == 3:
            ast.root = Node("cond", ctx.children[1].getText())
        return ast

    def visitIncr(self, ctx: MathParser.IncrContext):
        if isinstance(ctx.children[0], antlr4.tree.Tree.TerminalNodeImpl):
            # case for rvar INCR and rvar DECR
            return TermAST(Node("term", ctx.children[0].getText()))
        else:
            # case for INCR rvar and DECR rvar
            return FactorAST(Node("factor", ctx.children[1].getText()))

    def visitCont_instr(self, ctx: MathParser.Cont_instrContext):
        return ContAST(Node("cont", None))

    def visitBreak_instr(self, ctx: MathParser.Break_instrContext):
        return BreakAST(Node("break", None))

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
                if isinstance(value, int):
                    return value
                if isinstance(value, str):
                    return ord(value)
                else:
                    return int(value)
            elif d_type == "float":
                if isinstance(value, float):
                    return value
                if isinstance(value, str):
                    return float(ord(value))
                else:
                    return float(value)
            elif d_type == "char":
                if isinstance(value, str):
                    return value
                return chr(value)
        except Exception as e:
            raise RuntimeError("Bad Cast")

    def warn(self):
        """
        print all warnings on console
        :return: None
        """
        for warn in self.warnings:
            print(warn)
