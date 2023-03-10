# External libraries
import antlr4.error.ErrorListener
from output.MathVisitor import MathVisitor
from output.MathParser import MathParser
import json
import warnings
import copy
from colorama import Fore

# Standard Variables
keywords = ["var", "int", "binary_op", "unary_op", "comp_op", "comp_eq", "bin_log_op" , "un_log_op", "assign_op" , "const_var"]
keywords_datatype = ["int" , "float" , "char"]
keywords_binary = ["binary_op", "comp_op", "comp_eq", "bin_log_op" , "un_log_op"]
keywords_unary = ["unary_op"]
keywords_assign = ["assign_op"]
keywords_functions = ["printf"]
conversions = [("float" , "int") , ("int" , "char")]
conv_promotions = [("int" , "float") , ("char" , "int")]

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
        if isinstance(self.value , VarNode):
            return { self.key : self.value.save() }
        out = { self.key : self.value }
        return out
    def get_str(self):
        return self.key + '\t' + ':' + '\t' + str(self.value)

    def recursive_dot(self, dictionary, count, name):
        if self.key not in dictionary or count[self.key] == 1:
            dictionary[self.key] = set()
            name = self.key
        else:
            dictionary[name] = set()

        if isinstance(self.value, Node):
            dictionary[name].add(self.value.key)
            self.value.recursive_dot(dictionary, count,  self.value.key)
        else:
            dictionary[name].add(self.value)


class VarNode( Node ):

    def __init__(self, key: str, value , vtype: str , const : bool = False , ptr: bool = False , deref_level: int = 0 , total_deref: int = 0) -> None:
        super().__init__(key, value)
        self.type = vtype
        self.const = const
        self.ptr = ptr
        self.deref_level = deref_level
        self.total_deref = total_deref

    def print(self):
        return self.get_str()

    def save(self):
        out_key = ""
        if self.type != "":
            out_key += self.type
            if self.type != "":
                out_key += " "
        out_key += str('*'*self.deref_level) + self.key
        if self.const:
            out_key = "const " + out_key
        if isinstance(self.value , VarNode):
            # out_key = str('*'*(self.deref_level+1)) + out_key
            out = {out_key : self.value.save()}
        else:
            out = { out_key : self.value }
        return out

    def assign_type(self, vtype):
        self.type = vtype
        if isinstance(self.value , VarNode):
            self.value.assign_type(vtype)

    def get_str(self):
        return self.type + ' ' + self.key + '\t' + ':' + '\t' + str(self.value)

class FunctionNode(Node):

    def __init__(self, key: str, value : dict) -> None:
        super().__init__(key, value)
        self.body = None

    def print(self):
        print(self.get_str())

    def save(self):
        if isinstance(self.value, VarNode):
            return {self.key: self.value.save()}
        values = []
        for key,val in self.value.items():
            values.append(str(key) + "=" + str(val.value))
        out = {self.key: values}
        return out

    def get_str(self):
        out = self.key + '\t' + ':' + '\t'
        for key,val in self.value.items():
            if isinstance(val , Node):
                out += str(key) + "=" + str(val.value)
            else:
                out += str(key) + "=" + str(val)
        return out

    def recursive_dot(self, dictionary, count, name):
        super().recursive_dot(dictionary, count, name)


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

    def dot_language(self, file_name):
        """
        Create dot language format file

        :param file_name: string that determines the file name
        :return: None
        """
        # Create file
        file = open("./Output/" + file_name + ".txt", "w+")
        file.close()

        # Start of dot language
        new_dictionary = dict()
        count = dict()
        self.recursive_dot(new_dictionary, count)
        self.connect("./Output/" + file_name + ".txt", new_dictionary)

        # print dot language

        file = open("./Output/" + file_name + ".txt", "r")

        file_contents = file.read()

        print(file_contents)

        file.close()

    def recursive_dot(self, dictionary, count, name = None):
        if self.root.key not in dictionary or count[self.root.key] == 1:
            dictionary[self.root.key] = set()
            count[self.root.key] = 1
            name = self.root.key
        # elif self.root.key in dictionary and name is None:
        #     name = self.root.key + str(count[self.root.key])
        #     dictionary[name] = set()
        #     count[self.root.key] += 1
        else:
            dictionary[name] = set()

        for i in range(len(self.children)):
            if isinstance(self.children[i], Node):
                name_key = None
                if self.children[i].key not in dictionary:
                    dictionary[name].add(self.children[i].key)
                    count[self.children[i].key] = 1
                else:
                    name_key = self.children[i].key + str(count[self.children[i].key])
                    dictionary[name].add(name_key)
                    count[self.children[i].key] += 1
                self.children[i].recursive_dot(dictionary, count, name_key)
            else:
                name_key = None
                if self.children[i].root.key not in dictionary:
                    dictionary[name].add(self.children[i].root.key)
                    count[self.children[i].root.key] = 1
                else:
                    name_key = self.children[i].root.key + str(count[self.children[i].root.key])
                    dictionary[name].add(name_key)
                    count[self.children[i].root.key] += 1
                self.children[i].recursive_dot(dictionary, count, name_key)

    def connect(self, file_name, dictionary):
        with open(str(file_name), "w") as f:
            for key, value in dictionary.items():
                for v in value:
                    string = str(key) + "\t-->\t" + str(v) + "\n"
                    f.write(string)


    def get_str(self):
        return self.root.key + '\t' + ':' + '\t' + str(self.root.value)

class AstCreator (MathVisitor):

    # TODO: Add support for pointer and address operations
    # TODO: Finetune the error listener
    # TODO: Add a semantics error check

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
        elif isinstance(ctx, MathParser.RvarContext):
            return self.visitRvar(ctx)
        elif isinstance(ctx, MathParser.RtypeContext):
            return self.visitRtype(ctx)
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
        elif isinstance(ctx , MathParser.LvarContext):
            return self.visitLvar(ctx)
        elif isinstance(ctx , MathParser.DeclrContext):
            return self.visitDeclr(ctx)
        elif isinstance(ctx , MathParser.DerefContext):
            return self.visitDeref(ctx)
        elif isinstance(ctx , MathParser.Addr_opContext):
            return self.visitAddr_op(ctx)
        elif isinstance(ctx , MathParser.PrintfContext):
            return self.visitPrintf(ctx)


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

    def visitPrintf(self, ctx: MathParser.PrintfContext):
        out = FunctionNode(ctx.children[0].getText() , {"par0" : self.visit_child(ctx.children[2])})
        return out

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
        expr_ast = self.resolve_datatype(expr_ast)
        self.resolve_unary(expr_ast)
        self.resolve_binary(expr_ast)
        self.resolve_assign(expr_ast)
        return expr_ast

    def visitRvar(self, ctx: MathParser.RvarContext):
        root = Node(keywords[0], ctx.children[0].getText())
        return root

    def visitRtype(self, ctx: MathParser.RtypeContext):
        if ctx.children[0].getText().isdigit():
            return Node(keywords_datatype[0], int(ctx.children[0].getText()))
        elif self.isfloat(ctx.children[0].getText()):
            return Node(keywords_datatype[1], float(ctx.children[0].getText()))
        else:
            return Node(keywords_datatype[2], ctx.children[0].getText())

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

    def visitDeclr(self, ctx: MathParser.DeclrContext):
        # CONST? TYPE (var_decl ',')* var_decl
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
                self.optimise(root)
                new_ast = self.resolve_datatype(root)
                root = new_ast
                root.const = const
                if isinstance(root , VarNode):
                    root.assign_type(v_type)
                out.add_child(root)
                if not isinstance(root , AST):
                    self.symbol_table[root.key] = copy.copy(root)
        return out

    def visitVar_decl(self, ctx: MathParser.Var_declContext):
        # TYPE VAR_NAME
        # int x
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

    def visitAddr_op(self, ctx: MathParser.Addr_opContext):
        # resolve second child (rvar)
        r_var = self.visit_child(ctx.children[1])
        r_var = self.resolve_variables(r_var)
        # Search for variable in the symbol table

        root = r_var
        return root

    # Helper functions

    def isfloat(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    # Tree reduction methods

    def resolve_binary(self, expr_ast) -> AST | Node:
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
        if isinstance(expr_ast, Node):
            return expr_ast
        for i in range(len(expr_ast.children)):
            expr_ast.children[i] = self.resolve_unary(expr_ast.children[i])
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
        if isinstance(expr_ast , Node):
            return expr_ast
        for child in expr_ast.children:
            if child is None:
                expr_ast.children.remove(child)
            else:
                child = self.resolve_empty(child)

    def unnest(self, input_ast: AST | Node):
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

    def visitDeref(self, ctx: MathParser.DerefContext):
        # STR rvar
        # STR deref
        inp = ctx
        key = ""
        deref_count = 0
        # Get deref level
        while True:
            if isinstance(inp.children[1], MathParser.RvarContext):
                key = inp.children[1].getText()
                break
            else:
                inp = inp.children[1]

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
        if isinstance(first , Node):
            first = self.optimise_variables(first)
        if isinstance(second, Node):
            second = self.optimise_variables(second)
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
            else:
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
                elif new_el.ptr:
                    if new_el.deref_level > 0 and not isinstance(second , VarNode):
                        raise RuntimeError("Attempting to assign pointer of depth greater than 0 to a non-pointer value")
                    if new_el.total_deref > second.total_deref + 1:
                        raise RuntimeError("Pointer depth incompatible for pointer "
                                           + new_el.key + " with depth " + str(new_el.total_deref) + " and pointer "
                                           + second.key + " with depth " + str(second.total_deref))
                    new_el.value = self.symbol_table[second.key]
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
                        warnings.warn(Fore.YELLOW + "Implicit conversion from " + second.key + " to " + self.symbol_table[
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
                    second_entry = self.symbol_table[second.key]
                    raise AttributeError("Incompatible types when assigning to type ‘" + entry.type + str('*')*entry.total_deref +"’ from type ‘float’")
                else:
                    new_el.value = second.value
                self.symbol_table[new_el.key].value = new_el.value
        return new_el

    @staticmethod
    def convert(value, d_type):
        if d_type == "int":
            return int(value)
        elif d_type == "float":
            return float(value)
        elif d_type == "char":
            return chr(value)

    def optimise_variables(self, input_node : Node) -> Node :
        # Search for the variable name in the symbols table
        if input_node.key in self.symbol_table:
            if self.symbol_table[input_node.key] is None:
                if isinstance(input_node , VarNode):
                    new_node = VarNode(input_node.key , input_node.value , input_node.type , input_node.const)
                    self.symbol_table[new_node.key] = new_node
                return input_node
            if self.symbol_table[input_node.key] is not None and self.symbol_table[input_node.key].const:
                if input_node.value is not None and input_node.value != self.symbol_table[input_node.key].value:
                    raise RuntimeError("Attempting to modify a const variable " + input_node.key)
            input_node.value = self.symbol_table[input_node.key].value
        elif isinstance(input_node , FunctionNode) and input_node.key in keywords_functions:
            for i in range(len(input_node.value)):
                if input_node.value["par" + str(i)].key in keywords_datatype:
                    return input_node
                elif self.symbol_table[input_node.value["par" + str(i)].value] is None:
                    raise NameError("Variable " + input_node.value["par" + str(i)] + " doesn't exist")
                else:
                    input_node.value["par" + str(i)].key = self.symbol_table[input_node.value["par" + str(i)].value].type
                    input_node.value["par" + str(i)].value = self.symbol_table[input_node.value["par" + str(i)].value].value
                # input_node.value = self.symbol_table[input_node.value["par" + ]]
        return input_node

    def optimise(self, input_ast : AST | Node) -> AST | Node:
        if isinstance(input_ast , VarNode) or isinstance(input_ast, FunctionNode):
            return self.optimise_variables(input_ast)
        if isinstance(input_ast , Node):
            return self.optimise_variables(input_ast)
        for i in range(len(input_ast.children)):
            input_ast.children[i] = self.optimise(input_ast.children[i])
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
            return self.unnest(input_ast)
            return input_ast
