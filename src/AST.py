# External libraries
import antlr4.error.ErrorListener
from output.MathVisitor import MathVisitor
from output.MathParser import MathParser
import json
keywords = ["var", "int", "binary_op", "unary_op", "comp_op", "comp_eq", "bin_log_op" , "un_log_op", "assign_op" , "const_var"]
keywords_datatype = ["int" , "float" , "char"]
keywords_binary = ["binary_op", "comp_op", "comp_eq", "bin_log_op" , "un_log_op"]
keywords_unary = ["unary_op"]
keywords_assign = ["assign_op"]

class ErrorListener (antlr4.error.ErrorListener.ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        out = "Syntax error at line " + str(line) + ":" + str(column) + ": '" + offendingSymbol.text + "'" + "\n" + msg
        raise SyntaxError(out)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        super().reportAmbiguity(recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs)


class Node:
    def __init__(self, key : str, value) -> None:
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

class VarNode( Node ):

    def __init__(self, key: str, value , vtype: str , const : bool = False) -> None:
        super().__init__(key, value)
        self.type = vtype
        self.const = const

    def print(self):
        return self.get_str()

    def save(self):
        out_key = self.type + " " + self.key
        if self.const:
            out_key = "const " + out_key
        out = { out_key : self.value }
        return out

    def get_str(self):
        return self.type + ' ' + self.key + '\t' + ':' + '\t' + str(self.value)


class AST:
    def __init__(self, root : Node = None, children : list[Node] = None) -> None:
        super().__init__()
        if children is None:
            children = []
        self.root : Node | None = root
        self.children : list[Node] | [] = children

    def add_child(self, child):
        if child is None:
            return
        if not isinstance(child, AST) and not isinstance(child , Node):
            if not isinstance(child , AST):
                raise TypeError("child must be set to an AST")
            if not isinstance(child , Node):
                raise TypeError("child must be set to a Node")
        self.children.insert(len(self.children), child)

    def save(self):
        out = {self.root.key: self.root.value}
        if out[self.root.key] is None:
            out[self.root.key] = []
        else:
            out["children"] = []
        for i in range(len(self.children)):
            if self.children[i] is not None and self.root.value is None:
                out[self.root.key].insert(len(out[self.root.key]) , self.children[i].save())
            elif self.children[i] is not None:
                out["children"].insert(len(out["children"]) , self.children[i].save())
        return out

    def print(self , indent : int = 4):
        print(json.dumps(self.save() , indent=indent))

    def get_str(self):
        return self.root.key + '\t' + ':' + '\t' + str(self.root.value)

class AstCreator (MathVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.base_ast : AST = AST()
        self.symbol_table : dict = dict()

    def visit_child(self, ctx):
        if isinstance(ctx, MathParser.MathContext):
            return self.visitMath(ctx)
        elif isinstance(ctx, MathParser.InstrContext):
            return self.visitInstr(ctx)
        elif isinstance(ctx, MathParser.ExprContext):
            return self.visitExpr(ctx)
        elif isinstance(ctx, MathParser.VarContext):
            return self.visitVar(ctx)
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
        elif isinstance(ctx, MathParser.Bin_log_opContext):
            return self.visitBin_log_op(ctx)
        elif isinstance(ctx, MathParser.Un_log_opContext):
            return self.visitUn_log_op(ctx)
        elif isinstance(ctx, MathParser.AssignContext):
            return self.visitAssign(ctx)
        elif isinstance(ctx, MathParser.Var_declContext):
            return self.visitVar_decl(ctx)
        elif isinstance(ctx, MathParser.Cvar_declContext):
            return self.visitCvar_decl(ctx)


    def visitMath(self, ctx: MathParser.MathContext):
        math_ast = AST()
        math_ast.root = Node("math", None)
        for c in ctx.getChildren():
            math_ast.add_child(self.visit_child(c))
        self.resolve_empty(math_ast)
        self.base_ast = math_ast
        return math_ast

    def visitInstr(self, ctx: MathParser.InstrContext):
        instr_ast = AST()
        instr_ast.root = Node("instr", None)
        for c in ctx.getChildren():
            instr_ast.add_child(self.visit_child(c))
        self.resolve_empty(instr_ast)
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
        expr_ast = AST()
        expr_ast.root = Node("expr" , None)
        for c in ctx.getChildren():
            expr_ast.add_child(self.visit_child(c))
        self.resolve_empty(expr_ast)
        # Resolve the operations order
        self.resolve_unary(expr_ast)
        self.resolve_binary(expr_ast)
        self.resolve_assign(expr_ast)
        new_ast = self.resolve_datatype(expr_ast)
        return new_ast

    def visitVar(self, ctx: MathParser.VarContext):
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

    def visitBin_log_op(self, ctx: MathParser.Bin_log_opContext):
        root = Node(keywords[6], ctx.children[0].getText())
        return root

    def visitUn_log_op(self, ctx: MathParser.Un_log_opContext):
        root = Node(keywords[7], ctx.children[0].getText())
        return root

    def visitAssign(self, ctx: MathParser.AssignContext):
        root = Node(keywords[8], ctx.children[0].getText())
        return root

    def visitCvar_decl(self, ctx: MathParser.Cvar_declContext):
        # CONST TYPE VAR_NAME
        # const int x
        # check if type is in allowed types
        if ctx.children[1].getText() not in keywords_datatype:
            raise TypeError(ctx.children[1].getText() + " is not a valid type")
        root = VarNode(const= bool(ctx.children[0].getText()) , vtype= ctx.children[1].getText() , key= ctx.children[2].getText() , value= None)
        return root

    def visitVar_decl(self, ctx: MathParser.Var_declContext):
        # TYPE VAR_NAME
        # int x
        root = VarNode(vtype=ctx.children[0].getText(), key=ctx.children[1].getText(), value=None)
        return root

        # Tree reduction methods

    def resolve_binary(self, expr_ast) -> AST | Node:
        if isinstance(expr_ast, Node):
            return expr_ast
        for i in range(len(expr_ast.children)):
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
        if isinstance(expr_ast, Node):
            return expr_ast
        for i in range(len(expr_ast.children)):
            if expr_ast.children[i] is not None and isinstance(expr_ast.children[i], Node) and expr_ast.children[
                i].key in keywords_unary:
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
            elif expr_ast.children[i] is not None and isinstance(expr_ast.children[i], AST):
                expr_ast.children[i] = self.resolve_unary(expr_ast.children[i])
        return expr_ast

    def resolve_assign(self, expr_ast: AST | Node) -> AST | Node:
        for i in range(len(expr_ast.children)):
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
        if not isinstance(expr_ast , AST) or expr_ast.root.value is not None :
            return expr_ast
        if len(expr_ast.children) == 1:
            if isinstance(expr_ast.children[0], AST):
                expr_ast = expr_ast.children[0]
            elif isinstance(expr_ast.children[0], Node):
                if expr_ast.children[0].key == "var":
                    expr_ast = expr_ast.children[0]
                    expr_ast.key = expr_ast.value
                    expr_ast.value = None
                elif isinstance(expr_ast.children[0] , VarNode):
                    expr_ast = expr_ast.children[0]
                    # Add the variable declaration to the symbols table
                    if expr_ast.key not in self.symbol_table:
                        self.symbol_table[expr_ast.key] = None
                else:
                    expr_ast = expr_ast.children[0]
        return expr_ast

    def resolve_variables(self , input_ast : AST | Node) -> AST | Node:
        if not isinstance(input_ast , Node):
            return input_ast
        if input_ast.key == "var":
            input_ast.key = input_ast.value
            input_ast.value = None
        elif isinstance(input_ast, VarNode):
            # Add the variable declaration to the symbols table
            if input_ast.key not in self.symbol_table:
                self.symbol_table[input_ast.key] = None
        return input_ast

    @staticmethod
    def resolve_empty(expr_ast):
        for child in expr_ast.children:
            if child is None:
                expr_ast.children.remove(child)

    # Optimising tree by reducing operations with literals to their result

    def optimise_unary(self, input_ast: AST) -> AST | Node:
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
        new_el = Node("", None)
        first = input_ast.children[0]
        second = input_ast.children[1]
        # check if they are both literals
        if first is not None and isinstance(first, AST):
            first = self.optimise(first)
        if second is not None and isinstance(second, AST):
            second = self.optimise(second)
        # Resolve variables if they need to be
        if isinstance(first , Node) and first.value is None:
            self.optimise_variables(first)
        if isinstance(second, Node) and second.value is None:
            self.optimise_variables(second)
        if first is not None and first.value is not None and second is not None and second.value is not None:
            if input_ast.root.value == '*':
                new_el.value = first.value * second.value
            elif input_ast.root.value == '/':
                new_el.value = first.value / second.value
            elif input_ast.root.value == "%":
                new_el.value = first.value % second.value
            if isinstance(new_el.value, float):
                new_el.key = "float"
            elif isinstance(new_el.value, int):
                new_el.key = "int"
        return new_el

    def optimise_comp_op(self, input_ast: AST) -> AST | Node:
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
        new_el = Node("" , None)
        # Get the ID
        first = input_ast.children[0]
        # Get the rvalue to assign to the ID
        second = input_ast.children[1]
        # Check if condition is a literal
        if first is not None and not (isinstance(first, Node)):
            return input_ast
        if first is not None and isinstance(first , VarNode):
            first = self.optimise_variables(first)
            new_el = first
        if second is not None and isinstance(second, AST):
            second = self.optimise(second)
        if input_ast.root.value == "=":
            if isinstance(first , VarNode):
                if new_el.key not in self.symbol_table:
                    raise SyntaxError("Variable " + new_el.key + " not declared in this scope" )
                new_el.value = second.value
                self.symbol_table[new_el.key] = new_el.value
                return new_el
            else:
                new_el.key = first.value
                new_el.value = second.value
        return new_el

    def optimise_variables(self, input_node : Node) -> Node :
        # Search for the variable name in the symbols table
        if input_node.key in self.symbol_table:
            input_node.value = self.symbol_table[input_node.key]
        return input_node

    def optimise(self, input_ast : AST | Node) -> AST | Node:
        if isinstance(input_ast , VarNode):
            return self.optimise_variables(input_ast)
        if isinstance(input_ast , Node):
            return self.optimise_variables(input_ast)
        # Unary operation node replacements
        if input_ast.root.key == "assign_op":
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
        else:
            for i in range(len(input_ast.children)):
                input_ast.children[i] = self.optimise(input_ast.children[i])
        return input_ast