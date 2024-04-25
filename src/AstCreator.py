# import decimal
# import socket
# import struct
# from math import floor
#
# from colorama import Fore
# import copy
import copy

import antlr4.tree
from AST import *
from SymbolTable import *
from out.FileParser import FileParser
from out.FileVisitor import FileVisitor
from decimal import Decimal
import re

class AstCreator(FileVisitor):

    def __init__(self, filename: str = None) -> None:
        """
        Initializer function
        """
        super().__init__()
        self.base_ast: AST = AST()
        self.symbol_table: SymbolTable = SymbolTable()
        self.warnings: list = []
        self.file_name: str = filename

    def visit_child(self, ctx):
        """
        visit the right visit function for the give context
        :param ctx: the context to know what to visit
        :return: the given output given by every visit function (AST or Node)
        """
        if isinstance(ctx, FileParser.InstrContext):
            return self.visitInstr(ctx)
        elif isinstance(ctx, FileParser.ExprContext):
            return self.visitExpr(ctx)
        elif isinstance(ctx, FileParser.RvarContext):
            return self.visitRvar(ctx)
        elif isinstance(ctx, FileParser.RtypeContext):
            return self.visitRtype(ctx)
        elif isinstance(ctx, FileParser.AssignContext):
            return self.visitAssign(ctx)
        elif isinstance(ctx, FileParser.LvarContext):
            return self.visitLvar(ctx)
        elif isinstance(ctx, FileParser.DerefContext):
            return self.visitDeref(ctx)
        elif isinstance(ctx, FileParser.PrintfContext):
            return self.visitPrintf(ctx)
        elif isinstance(ctx, FileParser.Var_declContext):
            return self.visitVar_decl(ctx)
        elif isinstance(ctx, FileParser.DeclrContext):
            return self.visitDeclr(ctx)
        elif isinstance(ctx, FileParser.TermContext):
            return self.visitTerm(ctx)
        elif isinstance(ctx, FileParser.FactorContext):
            return self.visitFactor(ctx)
        elif isinstance(ctx, FileParser.PrimaryContext):
            return self.visitPrimary(ctx)
        elif isinstance(ctx, FileParser.ScopeContext):
            return self.visitScope(ctx)
        elif isinstance(ctx, FileParser.For_loopContext):
            return self.visitFor_loop(ctx)
        elif isinstance(ctx, FileParser.While_loopContext):
            return self.visitWhile_loop(ctx)
        elif isinstance(ctx, FileParser.If_condContext):
            return self.visitIf_cond(ctx)
        elif isinstance(ctx, FileParser.Else_condContext):
            return self.visitElse_cond(ctx)
        elif isinstance(ctx, FileParser.InitContext):
            return self.visitInit(ctx)
        elif isinstance(ctx, FileParser.CondContext):
            return self.visitCond(ctx)
        elif isinstance(ctx, FileParser.IncrContext):
            return self.visitIncr(ctx)
        elif isinstance(ctx, FileParser.Cont_instrContext):
            return self.visitCont_instr(ctx)
        elif isinstance(ctx, FileParser.Break_instrContext):
            return self.visitBreak_instr(ctx)
        elif isinstance(ctx, FileParser.Func_defnContext):
            return self.visitFunc_defn(ctx)
        elif isinstance(ctx, FileParser.Func_declContext):
            return self.visitFunc_decl(ctx)
        elif isinstance(ctx, FileParser.Arg_listContext):
            return self.visitArg_list(ctx)
        elif isinstance(ctx, FileParser.Func_callContext):
            return self.visitFunc_call(ctx)
        elif isinstance(ctx, FileParser.Func_scopeContext):
            return self.visitFunc_scope(ctx)
        elif isinstance(ctx, FileParser.Func_argContext):
            return self.visitFunc_arg(ctx)
        elif isinstance(ctx, FileParser.Param_declrContext):
            return self.visitParam_declr(ctx)
        elif isinstance(ctx, FileParser.Param_listContext):
            return self.visitParam_list(ctx)
        elif isinstance(ctx, FileParser.Return_instrContext):
            return self.visitReturn_instr(ctx)
        elif isinstance(ctx, FileParser.Array_declContext):
            return self.visitArray_decl(ctx)
        elif isinstance(ctx, FileParser.Array_elContext):
            return self.visitArray_el(ctx)
        elif isinstance(ctx, FileParser.Incl_statContext):
            return self.visitIncl_stat(ctx)
        elif isinstance(ctx, FileParser.ScanfContext):
            return self.visitScanf(ctx)
        elif isinstance(ctx, FileParser.CompContext):
            return self.visitComp(ctx)
        elif isinstance(ctx, FileParser.Switch_instrContext):
            return self.visitSwitch_instr(ctx)
        elif isinstance(ctx, FileParser.Case_instrContext):
            return self.visitCase_instr(ctx)
        elif isinstance(ctx, FileParser.Default_instrContext):
            return self.visitDefault_instr(ctx)
        elif isinstance(ctx, FileParser.Switch_scopeContext):
            return self.visitSwitch_scope(ctx)
        elif isinstance(ctx, FileParser.CommentContext):
            return self.visitComment(ctx)
        elif isinstance(ctx, antlr4.TerminalNode):
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
                isinstance(in_list[i], FuncDeclAST) or isinstance(in_list[i], FuncDefnAST) or \
                isinstance(in_list[i], ScanfAST) or isinstance(in_list[i], PrintfAST) or \
                isinstance(in_list[i], SwitchAST) or isinstance(in_list[i], CommentAST):
                return i
        return -1

    @staticmethod
    def lastDeclaration(index: int, in_list, token: str = '}'):
        for i in reversed(range(index)):
            if isinstance(in_list[i], PrintfAST) or \
                    isinstance(in_list[i], AssignAST) or isinstance(in_list[i], InstrAST) or \
                    (isinstance(in_list[i], Node) and in_list[i].key == token) or \
                    isinstance(in_list[i], FuncDeclAST) or isinstance(in_list[i], FuncDefnAST) or \
                    isinstance(in_list[i], DeclrAST) or isinstance(in_list[i], Scope_AST)\
                    or isinstance(in_list[i], ScanfAST) or isinstance(in_list[i], PrintfAST)\
                    or isinstance(in_list[i], SwitchAST) or isinstance(in_list[i], CommentAST):
                return i
        return -1

    @staticmethod
    def lastInit(index: int, in_list):
        for i in reversed(range(index)):
            if isinstance(in_list[i], CondAST):
                return i
        return -1

    @staticmethod
    def lastElse(index: int, in_list):
        for i in reversed(range(index)):
            if isinstance(in_list[i], Else_CondAST):
                return i
        return -1

    @staticmethod
    def lastFuncScope(index: int, in_list):
        for i in reversed(range(index)):
            if isinstance(in_list[i], FuncScopeAST):
                return i
        return -1

    @staticmethod
    def lastDefaultOrCase(index: int, in_list):
        for i in reversed(range(index)):
            if isinstance(in_list[i], CaseAST) or isinstance(in_list[i], DefaultAST):
                return i
            # elif isinstance(in_list[i], BreakAST):
            #     return i - 1
        return -1

    @staticmethod
    def lastSwitchScope(index: int, in_list):
        for i in reversed(range(index)):
            if isinstance(in_list[i], SwitchScopeAST):
                return i
        return -1

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
                if isinstance(v, antlr4.TerminalNode):
                    continue
                for child in v.getChildren():
                    s.append(child)
            else:
                v = self.visit_child(v)
                if v is None:
                    continue
                a.add_child(v)
        return a

    def visitFile(self, ctx: FileParser.FileContext):
        """
        Math visit function
        :param ctx: context
        :return: AST
        """
        math_ast = AST()
        math_ast.symbolTable = SymbolTable()
        math_ast.symbolTable.owner = math_ast
        return math_ast

    def visitInstr(self, ctx: FileParser.InstrContext):
        """
        Instruction visit
        :param ctx: context
        :return: AST
        """
        instr_ast = InstrAST()
        instr_ast.root = Node("instr", None)
        instr_ast.column = ctx.start.column
        instr_ast.line = ctx.start.line
        return instr_ast

    def visitExpr(self, ctx: FileParser.ExprContext):
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
        expr_ast.column = ctx.start.column
        expr_ast.line = ctx.start.line
        return expr_ast

    def visitPrintf(self, ctx: FileParser.PrintfContext):
        """
        Creates the node for printf function
        :param ctx: context
        :return: Node
        """

        out = PrintfAST(Node("printf", None))
        out.column = ctx.start.column
        out.line = ctx.start.line
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

    def visitRvar(self, ctx: FileParser.RvarContext):
        """
        Right-hand side variable visit function
        :param ctx: context
        :return: Node
        """
        root = Node(keywords[0], ctx.children[0].getText())
        return root

    def visitRtype(self, ctx: FileParser.RtypeContext):
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

    def visitAssign(self, ctx: FileParser.AssignContext):
        """
        Assign operand visit function
        :param ctx: context
        :return: Node
        """
        root = AssignAST(Node("assign", None))
        root.column = ctx.start.column
        root.line = ctx.start.line
        return root

    def visitDeclr(self, ctx: FileParser.DeclrContext):
        """
        Declaration visit function
        :param ctx: context
        :return: AST
        """
        out = DeclrAST(Node("declr", None))
        out.column = ctx.start.column
        out.line = ctx.start.line
        index = 0
        if ctx.children[index].getText() == "const":
            out.const = True
            index += 1
        if ctx.children[index].getText() in keywords_datatype:
            out.type = ctx.children[index].getText()
        else:
            raise TypeError(f"Variable declared with invalid type {ctx.children[0].getText()}")
        return out

    def visitVar_decl(self, ctx: FileParser.Var_declContext):
        """
        Variable declaration visit function
        :param ctx: context
        :return: VarNode || AST
        """
        if len(ctx.children) == 3:
            out = VarDeclrAST(Node("assign", None))
            out.column = ctx.start.column
            out.line = ctx.start.line
            return out
        else:
            out = VarDeclrAST(Node("var_declr", None))
            out.column = ctx.start.column
            out.line = ctx.start.line
            return out

    def visitLvar(self, ctx: FileParser.LvarContext):
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

    def visitDeref(self, ctx: FileParser.DerefContext):
        """
        Dereference visit function
        :param ctx: context
        :return: VarNode
        """
        # STR rvar
        # STR deref
        out = DerefAST(Node("deref", None))
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitTerm(self, ctx: FileParser.TermContext):
        ast = TermAST()
        ast.column = ctx.start.column
        ast.line = ctx.start.line
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

    def visitFactor(self, ctx: FileParser.FactorContext):
        ast = FactorAST()
        ast.column = ctx.start.column
        ast.line = ctx.start.line
        if len(ctx.children) == 2:
            ast.root = Node("factor", ctx.children[0].getText())
        else:
            return None
        return ast

    def visitPrimary(self, ctx: FileParser.PrimaryContext):
        ast = PrimaryAST()
        ast.column = ctx.start.column
        ast.line = ctx.start.line
        if len(ctx.children) == 2:
            ast.root = Node("primary", ctx.children[0].getText())
        else:
            return None
        return ast

    def visitScope(self, ctx: FileParser.ScopeContext):
        out = Scope_AST(Node("unnamed", None))
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitIf_cond(self, ctx: FileParser.If_condContext):
        out = If_CondAST(Node("If_cond", None))
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitElse_cond(self, ctx: FileParser.Else_condContext):
        out = Else_CondAST(Node("Else_cond", None))
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitWhile_loop(self, ctx: FileParser.While_loopContext):
        out = While_loopAST(Node("While_loop", None))
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitFor_loop(self, ctx: FileParser.For_loopContext):
        out =  For_loopAST(Node("For_loop", None))
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitInit(self, ctx: FileParser.InitContext):
        if len(ctx.children) == 1:
            return
        else:
            out = InitAST(Node("init", None))
            out.column = ctx.start.column
            out.line = ctx.start.line
            index = 0
            if ctx.children[index].getText() in keywords_datatype:
                out.type = ctx.children[index].getText()
            else:
                raise TypeError(f"Variable declared with invalid type {ctx.children[0].getText()}")
            return out

    def visitCond(self, ctx: FileParser.CondContext):
        ast = CondAST()
        ast.column = ctx.start.column
        ast.line = ctx.start.line
        # cond : comp | expr
        if len(ctx.children) != 1:
            raise TypeError("Invalid condition")
        if isinstance(ctx.children[0], FileParser.CompContext):
            ast.root = Node("cond", None)
        elif isinstance(ctx.children[0], FileParser.ExprContext):
            ast.root = Node("expr", "const")
        return ast

    def visitIncr(self, ctx: FileParser.IncrContext):
        if isinstance(ctx.children[0], antlr4.tree.Tree.TerminalNodeImpl):
            # case for rvar INCR and rvar DECR
            out = TermAST(Node("factor", ctx.children[0].getText()))
        else:
            # case for INCR rvar and DECR rvar
            out = FactorAST(Node("term", ctx.children[1].getText()))
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitCont_instr(self, ctx: FileParser.Cont_instrContext):
        out = ContAST(Node("cont", None))
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitBreak_instr(self, ctx: FileParser.Break_instrContext):
        out = BreakAST(Node("break", None))
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitParam_list(self, ctx: FileParser.Param_listContext):
        out = FuncParametersAST(Node("parameter", None), parameters=[None for _ in ctx.params])
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitParam_declr(self, ctx: FileParser.Param_declrContext):
        raise NotImplementedError("Parameter declaration not implemented")

    def visitFunc_defn(self, ctx: FileParser.Func_defnContext):
        out = FuncDefnAST(root=Node(ctx.name.text, None), const=(ctx.const is not None), return_type=ctx.type_.text,
                           ptr=(len(ctx.ptr) > 0), ptr_level=(len(ctx.ptr)),
                           symbolTable=SymbolTable())
        out.symbolTable.owner = out
        out.root = VarNode(out.root.key, out.root.value, out.type, out.const, out.ptr, total_deref=out.ptr_level,
                           const_ptr=out.ptr and out.const)
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitFunc_decl(self, ctx: FileParser.Func_declContext):
        out = FuncDeclAST(root=Node(ctx.name.text, None), const=(ctx.const is not None), return_type=ctx.type_.text,
                           ptr=(len(ctx.ptr) > 0), ptr_level=(len(ctx.ptr)),
                           symbolTable=SymbolTable())
        out.symbolTable.owner = out
        out.root = VarNode(out.root.key, out.root.value, out.type, out.const, out.ptr, total_deref=out.ptr_level,
                           const_ptr=out.ptr and out.const)
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out
    def visitFunc_arg(self, ctx: FileParser.Func_argContext):
        return

    def visitArg_list(self, ctx: FileParser.Arg_listContext):
        """
        :return: Node with name args_list and value the number of arguments
        """
        # return Node("args_list", len(ctx.args))
        return

    def visitFunc_call(self, ctx: FileParser.Func_callContext):
        """
        :return: A FuncCallAST.
        Key is the name of the function being called and value is None.
        Args is an empty initialized list with the size of the number of arguments
        """
        out = FuncCallAST(Node(ctx.name.text, None))
        if ctx.args is not None:
            out.args = [None for _ in ctx.args.args]
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitFunc_scope(self, ctx: FileParser.Func_scopeContext):
        """
        :return: A FuncScopeAST.
        The key is the name of the function it belongs to.
        The value is None.
        """
        out = FuncScopeAST(Node(ctx.parentCtx.name.text, None), symbolTable=SymbolTable())
        out.symbolTable.owner = out
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitReturn_instr(self, ctx: FileParser.Return_instrContext):
        out = ReturnInstr(Node("return", None))
        if ctx.ret_val is None:
            out.root.value = "void"
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out


    def visitScanf(self, ctx: FileParser.ScanfContext):
        ast = ScanfAST(Node("scanf", None))
        ast.column = ctx.start.column
        ast.line = ctx.start.line
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

    def visitArray_decl(self, ctx: FileParser.Array_declContext):
        ast = ArrayDeclAST(
            VarNode(ctx.name.text + '[]', None, ctx.type_.text, const=(ctx.const is not None), ptr=(len(ctx.ptr) > 0),
                    deref_level=0, total_deref=(len(ctx.ptr) if ctx.ptr is not None else 0),
                    const_ptr=(ctx.const is not None and len(ctx.ptr) > 0), is_array=True),
            arr_type=ctx.type_.text
        )
        ast.column = ctx.start.column
        ast.line = ctx.start.line
        ast.root.parent = ast
        ast.values = [self.visit_child(value) for value in ctx.values]
        if ctx.size is not None:
            ast.size = int(ctx.size.text)
        else:
            ast.size = len(ast.values)
        if len(ast.values) > ast.size:
            raise RuntimeError(f"Too many values for array {ast.root.key} of size {ast.size} given in line "
                               f"{ctx.start.line} column {ctx.start.column}")
        # if len(ast.values) == 0:
        #     ast.values = [None for i in range(ast.size)]
        else:
            for value in ast.values:
                if value.key != ast.type:
                    self.warnings.append(f"Implicit cast from {value.key} to {ast.type} in line {ctx.start.line} for "
                                         f"array element '{value.value}' of array '{ast.root.key}' with index "
                                         f"{ast.values.index(value)}. This element will be casted to {self.convert(value.value, ast.type)}")
                value.parent = ast
        return ast

    def visitArray_el(self, ctx: FileParser.Array_elContext):
        element = ArrayElementAST(Node("array_element", None))
        element.column = ctx.start.column
        element.line = ctx.start.line
        # get index
        if ctx.index is not None:
            element.root.value = int(ctx.index.text)
        return element

    def visitIncl_stat(self, ctx: FileParser.Incl_statContext):
        if ctx.library.text != "stdio":
            raise RuntimeError("Unsupported Library")
        out = IncludeAST(Node(f"{ctx.library.text}.h", None))
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitComp(self, ctx: FileParser.CompContext):
        # this is just an in-between node for an expression
        # check the operation
        if ctx.op.text in ["&&", "||"]:
            out = ExprAST(Node("expr", ctx.op.text))
        else:
            out = TermAST(Node("term" , ctx.op.text))
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitSwitch_instr(self, ctx: FileParser.Switch_instrContext):
        out = SwitchAST(Node("switch", None))
        out.column = ctx.start.column
        out.line = ctx.start.line
        out.cases = [None] * len(ctx.case_list)
        out.has_default = ctx.default is not None
        return out

    def visitCase_instr(self, ctx: FileParser.Case_instrContext):
        out = CaseAST(Node("case", None))
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitDefault_instr(self, ctx: FileParser.Default_instrContext):
        out = DefaultAST(Node("default", None))
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitSwitch_scope(self, ctx: FileParser.Switch_scopeContext):
        out = SwitchScopeAST(Node("switch_scope", None))
        out.column = ctx.start.column
        out.line = ctx.start.line
        return out

    def visitComment(self, ctx: FileParser.CommentContext):
        out = CommentAST(Node("comment", ctx.com.text))
        if ctx.com.text.startswith("//"):
            out.root.value = "singleline"
            out.comment = ctx.com.text[2:]
        elif ctx.com.text.startswith("/*"):
            out.root.value = "multiline"
            out.comment = ctx.com.text[2:-2]
        # out.comment = ctx.com.text
        return out

    @staticmethod
    def convert(value, d_type):
        """
        help function for casting
        :param value: input_value
        :param d_type: cast type
        :return: cast value
        """
        try:
            if value is None:
                return value
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
                elif value == 0:
                    # return utf-8 null character
                    return value
                return chr(value)
        except Exception:
            raise RuntimeError("Bad Cast")

    def warn(self):
        """
        print all warnings on console
        :return: None
        """
        for warn in self.warnings:
            print(warn)