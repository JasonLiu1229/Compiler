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
import re

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
        elif isinstance(ctx, MathParser.Func_defnContext):
            return self.visitFunc_defn(ctx)
        elif isinstance(ctx, MathParser.Func_declContext):
            return self.visitFunc_decl(ctx)
        elif isinstance(ctx, MathParser.Arg_listContext):
            return self.visitArg_list(ctx)
        elif isinstance(ctx, MathParser.Func_callContext):
            return self.visitFunc_call(ctx)
        elif isinstance(ctx, MathParser.Func_scopeContext):
            return self.visitFunc_scope(ctx)
        elif isinstance(ctx, MathParser.Func_argContext):
            return self.visitFunc_arg(ctx)
        elif isinstance(ctx, MathParser.Param_declrContext):
            return self.visitParam_declr(ctx)
        elif isinstance(ctx, MathParser.Param_listContext):
            return self.visitParam_list(ctx)
        elif isinstance(ctx, MathParser.Return_instrContext):
            return self.visitReturn_instr(ctx)
        elif isinstance(ctx, MathParser.Array_declContext):
            return self.visitArray_decl(ctx)
        elif isinstance(ctx, MathParser.Incl_statContext):
            return self.visitIncl_stat(ctx)
        elif isinstance(ctx, MathParser.ScanfContext):
            return self.visitScanf(ctx)
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
            if isinstance(in_list[i], PrintfAST) or isinstance(in_list[i], VarDeclrAST) or \
                isinstance(in_list[i], AssignAST) or isinstance(in_list[i], InstrAST) or \
                isinstance(in_list[i], Scope_AST) or (isinstance(in_list[i], Node) and in_list[i].key == token) or \
                isinstance(in_list[i], FuncDeclAST) or isinstance(in_list[i], FuncDefnAST):
                return i
        return -1

    @staticmethod
    def lastDeclaration(index: int, in_list, token: str = '}'):
        for i in reversed(range(index)):
            if isinstance(in_list[i], PrintfAST) or \
                    isinstance(in_list[i], AssignAST) or isinstance(in_list[i], InstrAST) or \
                    (isinstance(in_list[i], Node) and in_list[i].key == token) or \
                    isinstance(in_list[i], FuncDeclAST) or isinstance(in_list[i], FuncDefnAST) or \
                    isinstance(in_list[i], DeclrAST) or isinstance(in_list[i], Scope_AST):
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

    @staticmethod
    def lastFuncScope(index: int, in_list, token: str = '}'):
        for i in reversed(range(index)):
            if isinstance(in_list[i], FuncScopeAST):
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

                elif isinstance(child, ScanfAST):
                    child.children = base.children[index - len(child.variables): index]
                    child.children.reverse()
                    base.children[index-len(child.variables):index] = []
                    index -= len(child.variables)

                elif isinstance(child, IncludeAST):
                    child.parent = base

                elif isinstance(child, ArrayDeclAST):
                    last_inst = self.lastInstruction(index=index, in_list=base.children)
                    child.children = base.children[last_inst + 1: index]
                    base.children[last_inst + 1: index] = []
                    child.children.reverse()
                    index = base.children.index(child)

                elif isinstance(child, FuncDeclAST):
                    if isinstance(base.children[index-1], FuncParametersAST):
                        child.children = base.children[index - 1: index]
                        base.children[index - 1: index] = []
                    child.children.reverse()
                    if len(child.children) > 0:
                        if isinstance(child.children[0], FuncParametersAST):
                            child.params = child.children[0].parameters
                        for param in child.params:
                            if param.value is not None:
                                child.has_defaults.append(param)
                    index = base.children.index(child)
                    child.parent = base

                elif isinstance(child, FuncCallAST):
                    amt = len(child.args)
                    for i in reversed(range(1, amt + 1)):
                        child.args[i - 1] = base.children[index - i]
                    base.children[index - amt:index] = []
                    child.children = child.args
                    index = base.children.index(child)

                elif isinstance(child, ReturnInstr):
                    if child.root.value is None:
                        last_token = self.searchPrevToken(index=index, token="}", in_list=base.children) + 1
                        child.children = base.children[index-1:index]
                        base.children[last_token : index] = []
                        index = base.children.index(child)

                elif isinstance(child, ContAST) or isinstance(child, BreakAST):
                    last_token = self.searchPrevToken(index=index, token="}", in_list=base.children) + 1
                    base.children[last_token: index] = []
                    index = base.children.index(child)

                elif isinstance(child, FuncDefnAST):
                    last_func = self.lastFuncScope(index=index, in_list=base.children)
                    child.children = base.children[last_func: index]
                    base.children[last_func: index] = []
                    child.children.reverse()
                    if isinstance(child.children[0], FuncParametersAST):
                        child.params = child.children[0].parameters
                    for param in child.params:
                        if param.value is not None:
                            child.has_defaults.append(param)
                    index = base.children.index(child)
                    child.parent = base

                elif isinstance(child, FuncParametersAST):
                    # last_inst = self.lastInstruction(index=index, in_list=base.children, token='}')
                    # last_func = self.lastFuncScope(index=index, in_list=base.children, token='}')
                    # last_det = max(last_inst, last_func)
                    child.parameters = base.children[index - len(child.parameters): index]
                    base.children[index - len(child.parameters): index] = []
                    child.parameters.reverse()
                    # check default parameters order
                    default_found = False
                    for param in child.parameters:
                        if param.value is not None:
                            default_found = True
                        elif param.value is None and default_found:
                            raise AttributeError("Default value in the middle")
                    index = base.children.index(child)

                elif isinstance(child, CondAST):
                    if child.root.value == "const":
                        child.children = base.children[index - 1: index]
                        base.children[index - 1:index] = []
                    else:
                        child.children = base.children[index - 2: index]
                        base.children[index - 2:index] = []
                    child.children.reverse()
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
                        last_inst = self.lastInstruction(index, base.children)
                        child.children = base.children[last_inst + 1: index]
                        base.children[last_inst + 1: index] = []
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
                    number = len(base.children[index-1].children)
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

                elif isinstance(child, Scope_AST) or isinstance(child, FuncScopeAST):
                    # Parent of scope is base itself, if no parent is already found
                    # indexes["scope_depth"] += 1
                    if child.parent is None:
                        child.parent = base
                    new_index = self.searchPrevToken(index=index, token="}", in_list=base.children)
                    base.children[new_index:new_index + 1] = []
                    index = base.children.index(child)
                    child.children = base.children[new_index: index - 1]
                    child.children.reverse()
                    base.children[new_index: index] = []
                    index = base.children.index(child)
                    # indexes["last_scope"][(indexes["scope_depth"]-1)] += 1
                    indexes["last_instr"] = self.lastInstruction(index, base.children) + 1

                elif isinstance(child, DeclrAST):
                    last_decl = self.lastDeclaration(index, base.children)
                    # last_decl += 1
                    child.children = base.children[last_decl + 1: index]
                    child.children.reverse()
                    base.children[last_decl + 1: index] = []
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

                elif isinstance(child, PrintfAST):
                    if child.root.value is None:
                        if len(child.children) > 0:
                            continue
                        child.args = base.children[index - len(child.args): index]
                        child.args.reverse()
                        child.children = base.children[index - len(child.args): index]
                        child.children.reverse()
                        base.children[index - len(child.args): index] = []
                        index -= len(child.args)
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
                    # indexes["last_scope_open"] = index
                    # base.children[index:index+1] = []
                    # index -= 1

                if child.key == "{":
                    indexes["scope_depth"] -= 1
                    # base.children[index:index + 1] = []
                    # index -= 1

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

                elif isinstance(child, FuncParameter):
                    if not isinstance(base.children[index - 1], FuncParameter) and isinstance(base.children[index - 1], Node):
                        child.value = base.children[index - 1].value
                        base.children[index-1: index] = []
                        index = base.children.index(child)

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
                if not (isinstance(temp, Scope_AST) or isinstance(temp, FuncScopeAST)):
                    visited.append(temp)
                if not (isinstance(temp, Scope_AST) or isinstance(temp, FuncScopeAST)) or \
                        temp is ast_in or isinstance(temp.parent, Scope_AST) or isinstance(temp.parent, FuncScopeAST):
                    for i in temp.children:
                        if isinstance(i, AST) and not isinstance(i, Else_CondAST):
                            not_visited.append(i)
                else:
                    if isinstance(temp, For_loopAST) and temp.initialization is not None:
                        not_visited.append(temp.initialization)
                    # if temp.condition is not None and not isinstance(temp.condition, Node):
                    #     not_visited.append(temp.condition)
        visited.reverse()
        ast_in.symbolTable = self.handle(visited)
        return ast_in

    def handle(self, list_ast: list):
        # TODO: handle function call
        # initialize queues
        updates_queue = []
        incr_queue = []
        decr_queue = []
        # flags
        conditional = False
        evaluate = True
        temp_symbol = None
        for ast in list_ast:
            temp_parent = ast.parent
            symbol_table = ast.symbolTable
            temp_symbol = ast.symbolTable
            while symbol_table is None and temp_parent is not None:
                symbol_table = temp_parent.symbolTable
                temp_parent = temp_parent.parent
            if symbol_table is None:
                raise RuntimeError("No symbol table found")
            temp_symbol = symbol_table
            if isinstance(ast, ReturnInstr):
                temp_parent = ast.parent
                while temp_parent is not None:
                    if isinstance(temp_parent, FuncDefnAST):
                        if temp_parent.type == "void" and ast.root.value != "void" :
                            raise AttributeError(f"void function '{temp_parent.root.key}' should not return a value")
                        if temp_parent.type != "void" and ast.root.value == "void":
                            raise AttributeError(f"non-void function '{temp_parent.root.key}' should return a value")
                        break
                    temp_parent = temp_parent.parent
            if isinstance(ast, FuncCallAST):
                # check whether function is in symbol table
                match = None
                temp_parent = ast
                while temp_parent.parent is not None:
                    temp_parent = temp_parent.parent
                # replace args
                for i in range(len(ast.args)):
                    if isinstance(ast.args[i], Node) and ast.args[i].key != "var":
                        continue
                    match = AST.getEntry(ast.args[i])
                    if match is None:
                        raise AttributeError(f"Variable {ast.args[i].value} not found in scope")
                    if match[0] is None:
                        raise AttributeError(f"Variable {ast.args[i].value} not found in scope")
                    ast.args[i] = match[0]
                if temp_parent.symbolTable is None:
                    raise RuntimeError("Symbol table not found")
                match_found = True
                for entry in temp_parent.symbolTable.table:
                    # name match
                    if entry.name == ast.root.key:
                        if len(entry.parameters) != len(ast.args):
                            continue
                        for i in range(len(entry.parameters)):
                            # name , const , ptr , ptr_level, array , type
                            # key , const , ptr , total_deref - deref_level , array, type
                            current_param = entry.parameters[i]
                            current_arg = ast.args[i]
                            if isinstance(current_arg, VarNode):
                                # check all attributes
                                if current_param.name != current_arg.key:
                                    match_found = False
                                    break
                                if current_param.const != current_arg.const:
                                    match_found = False
                                    break
                                if current_param.ptr != current_arg.ptr:
                                    match_found = False
                                    break
                                if current_param.ptr_level != (current_arg.total_deref - current_arg.deref_level):
                                    match_found = False
                                    break
                                if current_param.array != current_arg.array:
                                    match_found = False
                                    break
                                if current_param.type != current_arg.type:
                                    if (current_param.type, current_arg.type) not in conversions:
                                        match_found = False
                                        break
                                    if (current_arg.type, current_param.type) not in conv_promotions:
                                        self.warnings.append(f"Conversion from {current_arg.type} to {current_param.type} may cause loss of data")
                            else:
                                if current_param.type != getType(current_arg.value):
                                    if (getType(current_arg.value), current_param.type) not in conversions:
                                        match_found = False
                                        break
                if not match_found:
                    raise AttributeError(f"Function {ast.root.key} not found")

            if isinstance(ast, FuncDeclAST):
                # check function was previously declared
                if ast.parent.symbolTable.exists(ast.root):
                    raise AttributeError(f"Redefinition of function {ast.root.key}")
                else:
                    new_entry = FuncSymbolEntry(ast.root)
                    for param in ast.params:
                        new_entry.parameters.append(FunctionParameter(param))
                        ast.symbolTable.insert(SymbolEntry(param))
                    ast.parent.symbolTable.insert(new_entry)
                node = ast
                continue
            elif isinstance(ast, FuncScopeAST) or isinstance(ast, FuncDefnAST):
                temp_exists = False
                match = None
                if ast.parent.symbolTable.exists(ast.root):
                    temp_exists = True
                    matches = ast.parent.symbolTable.lookup(ast.root)
                    if len(matches) == 1:
                        if matches[0].defined:
                            raise AttributeError(f"Redefinition of function {ast.root.key}")
                        match = matches[0]
                if not temp_exists:
                    new_entry = FuncSymbolEntry(ast.root)
                    for param in ast.params:
                        new_entry.parameters.append(FunctionParameter(param))
                        ast.symbolTable.insert(SymbolEntry(param))
                    new_entry.defined = True
                    ast.parent.symbolTable.insert(new_entry)
                else:
                    new_entry = FuncSymbolEntry(ast.root)
                    for param in ast.params:
                        new_entry.parameters.append(FunctionParameter(param))
                        ast.symbolTable.insert(SymbolEntry(param))
                    if new_entry != match:
                        raise AttributeError(f"Redeclaration of function {ast.root.key} with different signature")
                    elif match.defined:
                        raise AttributeError(f"Redefinition of function {ast.root.key}")
                    match.defined = True
                    # ast.parent.symbolTable.refresh()

                    # check if entries match
                # declare each parameter in your scope
                # handle what's in the function scope
                ast.children[-1].symbolTable = ast.symbolTable
                symbol_table = self.resolve(ast.children[-1]).symbolTable
                # print symbol table
                # print(f"Symbol table for {ast.root.key}:")
                # symbol_table.print()
                # functions
            if isinstance(ast, IncludeAST):
                continue
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
                        # temp_parent = child.parent
                        # temp_symbol = child.parent.symbolTable
                        # symbol_table = child.parent.symbolTable
                        # search in symbol table
                        if temp_symbol is not None:
                            exists_state = temp_symbol.exists(child.value)
                        elif symbol_table is not None:
                            exists_state = symbol_table.exists(child.value)
                        else:
                            exists_state = False
                        temp_ast = ast
                        # search in parent scopes if not found
                        while not exists_state and temp_ast is not None and temp_ast.parent is not None:
                            temp_symbol = temp_ast.parent.symbolTable
                            temp_ast = temp_ast.parent
                            if temp_symbol is not None:
                                exists_state = temp_symbol.exists(child.value)
                        if temp_parent is not None:
                            evaluate = not (
                                        isinstance(temp_parent.parent, While_loopAST) or isinstance(temp_parent.parent,
                                                                                                    For_loopAST))
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
                if not handle:
                    continue
            if isinstance(ast, ScanfAST):
                for var in ast.variables:
                    match , total = AST.getEntry(var)
                    if total is -1:
                        raise ReferenceError(f"Variable {var.value} undeclared")
                    elif total > 1:
                        raise ReferenceError(f"Multiple matches for variable {var.value}")
                    ast.variables[ast.variables.index(var)] = match
                node = ast
            # conditional cases
            elif isinstance(ast, If_CondAST) or isinstance(ast, Else_CondAST):
                ast.symbolTable = temp_symbol
                self.resolve(ast.condition)
                # handle for condition true
                self.resolve(ast.children[0])
                self.resolve(ast.children[-1])
                node = ast

            elif isinstance(ast, While_loopAST):
                self.resolve(ast.condition)
                ast.symbolTable = temp_symbol
                self.resolve(ast.children[0])
                node = ast

            elif isinstance(ast, For_loopAST):
                self.resolve(ast.condition)
                entry = AST.getEntry(ast.incr.children[0])
                if entry is None:
                    raise ReferenceError(f"Variable {ast.incr.children[0].value} was not declared")
                ast.incr.children[0] = entry
                ast.children[0].children.append(InstrAST(Node("instr", None), [ast.incr]))
                ast.children[0].children[-1].parent = ast.children[0]
                # self.resolve(ast.initialization)
                temp = While_loopAST(Node("while", None), ast.children, ast.parent)
                temp.condition = ast.condition
                index = ast.parent.children.index(ast)
                ast.parent.children[index] = temp
                ast = temp
                for child in ast.children:
                    child.parent = ast
                node = ast
            # Variable assignment handling
            elif ast.root.key == "assign" and ast.root.value is not None:
                if not isinstance(ast.children[0], VarNode):
                    raise AttributeError(f"Attempting to assign to a non variable type object")
                if not evaluate:
                    node = ast
                    continue
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
            elif isinstance(ast, InitAST):
                # check if variable already exists
                if symbol_table.exists(ast.children[0]):
                    raise ReferenceError(f"Redeclaration of variable {ast.children[0].key}")
                new_entry = ast.children[0]
                new_entry.type = ast.type
                new_entry.const = ast.const
                new_entry.value = ast.children[1].value
                temp_symbol.insert(SymbolEntry(new_entry))
                updates_queue.append(new_entry)
                old_parent = ast.parent
                ast.parent = ast.parent.parent
                ast.parent.children.insert(ast.parent.children.index(old_parent), ast.children[0])
                node = InstrAST(Node("instr", None), [new_entry])
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
                    if not evaluate:
                        node = ast
                        continue
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
                    if not evaluate:
                        node.value = None
                    temp_symbol.insert(SymbolEntry(node))
                updates_queue.append(node)

            elif isinstance(ast, AssignAST):

                # check if assign value is of a valid type
                if not (isinstance(ast.children[1], Node) or isinstance(ast.children[1], VarNode)):
                    raise RuntimeError(f"\'Invalid assignment for variable {ast.children[0].key}\'")
                if isinstance(ast.children[1], VarNode):
                    rtype = ast.children[1].type
                else:
                    rtype = ast.children[1].key
                assignee = copy.copy(ast.children[0])
                if not evaluate:
                    node = ast
                    continue
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
                updates_queue.reverse()
                for instance in incr_queue:
                    instance = temp_symbol.lookup(instance)[0].object
                    instance.value += 1
                    temp_symbol.update(instance)
                for instance in decr_queue:
                    instance = temp_symbol.lookup(instance)[0].object
                    instance.value -= 1
                    temp_symbol.update(instance)
                for instance in updates_queue:
                    if not temp_symbol.exists(instance):
                        temp_symbol.insert(SymbolEntry(instance))
                    else:
                        temp_symbol.update(instance)
                temp_symbol.refresh()
                node = assignee
            elif isinstance(ast, InstrAST):
                node = ast.handle()
                updates_queue.reverse()
                for instance in incr_queue:
                    match, length = AST.getEntry(instance)
                    if length == 0:
                        raise ReferenceError(f"Variable {instance.key} not found")
                    if length > 1:
                        raise ReferenceError(f"Multiple matches for variable {instance.key}")
                    instance = match
                    instance.value += 1
                    temp_symbol.update(instance)
                for instance in decr_queue:
                    match, length = AST.getEntry(instance)
                    if length == 0:
                        raise ReferenceError(f"Variable {instance.key} not found")
                    if length > 1:
                        raise ReferenceError(f"Multiple matches for variable {instance.key}")
                    instance = match
                    instance.value -= 1
                    temp_symbol.update(instance)
                for instance in updates_queue:
                    if not temp_symbol.exists(instance):
                        temp_symbol.insert(SymbolEntry(instance))
                    else:
                        temp_symbol.update(instance)

                temp_symbol.refresh()
                # temp_symbol = old_symbol
                updates_queue = []
                incr_queue = []
                decr_queue = []
            elif isinstance(ast, TermAST) and ast.root.value in ["++", "--"]:
                node = ast
                if evaluate:
                    node = ast.children[0]
                    if ast.root.value == "++":
                        incr_queue.append(node)
                    if ast.root.value == "--":
                        decr_queue.append(node)
            elif isinstance(ast, CondAST):
                if evaluate:
                    ast.last_eval = copy.copy(ast).handle().value
            elif ast is not None:
                node = ast.handle()
            else:
                continue
            # Replace node
            if not isinstance(ast, CondAST) and not isinstance(ast, InitAST):
                index = ast.parent.children.index(ast)
                ast.parent.children[index] = node
            else:
                if isinstance(ast.parent, Else_CondAST):
                    ast.last_eval = not ast.last_eval
        if temp_symbol is not None:
            for instance in updates_queue:
                temp_symbol.update(instance)
            temp_symbol.refresh()
        symbol_table = temp_symbol
        return symbol_table

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

        out = PrintfAST(Node("printf", None))
        if ctx.print_val is not None:
            out.format_string = ctx.print_val.text[1:-1] # printf
        if ctx.format_string is not None:
            out.format_string = ctx.format_string.text[1:-1] # printf
        # split the format string into a list of strings and variables
        format_string = out.format_string
        format_string = format_string.replace("\\n", "\n")
        format_string = format_string.replace("\\t", "\t")
        format_string = format_string.replace("\\r", "\r")
        format_string = format_string.replace("\\v", "\v")
        format_string = format_string.replace("\\b", "\b")
        format_string = format_string.replace("\\a", "\a")
        format_string = format_string.replace("\\f", "\f")
        # format_string = format_string.replace("\\\\", "\\")
        # format_string = format_string.replace("\\\'", "\'")
        # format_string = format_string.replace("\\\"", "\"")
        # format_string = format_string.replace("\\\?", "\?")
        # format_string = format_string.replace("\\\0", "\0")
        format_string = format_string.replace(" ", "")
        out.format_specifiers += re.findall("%[0-9]*[discf]", format_string)
        # remove escape characters
        out.format_string = out.format_string.replace("\\n", "\\0A")
        out.format_string = out.format_string.replace("\\t", "\\09")
        out.format_string = out.format_string.replace("\\r", "\\0D")
        out.format_string = out.format_string.replace("\\v", "\\0B")
        out.format_string = out.format_string.replace("\\b", "\\08")
        out.format_string = out.format_string.replace("\\a", "\\07")
        out.format_string = out.format_string.replace("\\f", "\\0C")

        out.args = [None] * len(ctx.vars_) # printf
        if len(out.args) != len(out.format_specifiers):
            raise AttributeError("Wrong number of arguments for printf")
        for i in range(len(ctx.vars_)):
            if isinstance(ctx.vars_[i].children[0], antlr4.tree.Tree.TerminalNodeImpl):
                new_node = Node("string", ctx.vars_[i].children[0].getText()[1:-1])
                out.args[i] = new_node
                out.children.append(new_node)
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
        ptr_len = len(ctx.ptr) if ctx.ptr is not None else 0
        is_ptr = ptr_len > 0
        root = VarNode(ctx.name.text, None, "", ptr=is_ptr, total_deref=ptr_len)
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
        elif len(ctx.children) == 1:
            ast.root = Node("cond", "const")
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

    def visitParam_list(self, ctx: MathParser.Param_listContext):
        out = FuncParametersAST(Node("parameter", None), parameters=list(None for p in ctx.params))
        return out

    def visitParam_declr(self, ctx: MathParser.Param_declrContext):
        out = FuncParameter(key=ctx.var.text, value=None, vtype=ctx.type_.text, const=(ctx.const is not None),
                            ptr=(ctx.ptr is not None),
                            deref_level=(len(ctx.ptr) if ctx.ptr is not None else 0),
                            total_deref=(len(ctx.ptr) if ctx.ptr is not None else 0),
                            const_ptr=(ctx.const is not None and ctx.ptr is not None),
                            reference=(ctx.reference is not None))
        return out

    def visitFunc_defn(self, ctx: MathParser.Func_defnContext):
        out = FuncDefnAST(root=Node(ctx.name.text, None), const=(ctx.const is not None), return_type=ctx.type_.text,
                           ptr=(len(ctx.ptr) > 0), ptr_level=(len(ctx.ptr)),
                           symbolTable=SymbolTable())
        out.root = VarNode(out.root.key, out.root.value, out.type, out.const, out.ptr, total_deref=out.ptr_level,
                           const_ptr=out.ptr and out.const)
        return out

    def visitFunc_decl(self, ctx: MathParser.Func_declContext):
        out = FuncDeclAST(root=Node(ctx.name.text, None), const=(ctx.const is not None), return_type=ctx.type_.text,
                           ptr=(len(ctx.ptr) > 0), ptr_level=(len(ctx.ptr)),
                           symbolTable=SymbolTable())
        out.root = VarNode(out.root.key, out.root.value, out.type, out.const, out.ptr, total_deref=out.ptr_level,
                           const_ptr=out.ptr and out.const)
        return out
    def visitFunc_arg(self, ctx: MathParser.Func_argContext):
        return

    def visitArg_list(self, ctx: MathParser.Arg_listContext):
        """
        :return: Node with name args_list and value the number of arguments
        """
        # return Node("args_list", len(ctx.args))

    def visitFunc_call(self, ctx: MathParser.Func_callContext):
        """
        :return: A FuncCallAST.
        Key is the name of the function being called and value is None.
        Args is an empty initialized list with the size of the number of arguments
        """
        out = FuncCallAST(Node(ctx.name.text, None))
        if ctx.args is not None:
            out.args = [None for arg in ctx.args.args]
        return out

    def visitFunc_scope(self, ctx: MathParser.Func_scopeContext):
        """
        :return: A FuncScopeAST.
        The key is the name of the function it belongs to.
        The value is None.
        """
        return FuncScopeAST(Node(ctx.parentCtx.name.text, None))

    def visitReturn_instr(self, ctx: MathParser.Return_instrContext):
        out = ReturnInstr(Node("return", None))
        if ctx.ret_val is None:
            out.root.value = "void"
        return out


    def visitScanf(self, ctx: MathParser.ScanfContext):
        ast = ScanfAST(Node("scanf", None))
        # ast.variables = ctx.vars_
        ast.variables = [Node] * len(ctx.vars_)
        ast.format_string = ctx.format_string.text
        # split the format string into a list of strings and variables
        format_string = ast.format_string
        format_string = format_string.replace("\\n", "\n")
        format_string = format_string.replace("\\t", "\t")
        format_string = format_string.replace("\\r", "\r")
        format_string = format_string.replace("\\v", "\v")
        format_string = format_string.replace("\\b", "\b")
        format_string = format_string.replace("\\a", "\a")
        format_string = format_string.replace("\\f", "\f")
        format_string = format_string.replace("\\\\", "\\")
        format_string = format_string.replace("\\\'", "\'")
        format_string = format_string.replace("\\\"", "\"")
        format_string = format_string.replace("\\\?", "\?")
        format_string = format_string.replace("\\\0", "\0")
        format_string = format_string.replace(" ", "")
        ast.format_specifiers += re.findall("%[0-9]*[disc]", format_string) # find all format specifiers
        ast.variables = [self.visit_child(var.children[0]) for var in ctx.vars_]  # scanf can have multiple variables
        for var in ast.variables:
            var.parent = ast
        return ast

    def visitArray_decl(self, ctx: MathParser.Array_declContext):
        ast = ArrayDeclAST(VarNode(vtype=ctx.type_.text, key=ctx.name.text, const=True if ctx.const is not None else False, value="", is_array=True))
        ast.values = [self.visit_child(value) for value in ctx.values]
        if ctx.size is not None:
            ast.size = int(ctx.size.text)
        else:
            ast.size = len(ast.values)
        return ast

    def visitIncl_stat(self, ctx: MathParser.Incl_statContext):
        if ctx.library.text != "stdio":
            raise RuntimeError("Unsupported Library")
        return IncludeAST(Node(f"{ctx.library.text}.h", None))

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
