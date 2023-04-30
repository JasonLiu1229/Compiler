from math import floor
from pprint import pprint
from typing import Any
from Node import Node, VarNode, FunctionNode
import antlr4.error.ErrorListener
import antlr4.error.ErrorStrategy
import json
from SymbolTable import *
from antlr4.error.Errors import ParseCancellationException

# Standard Variables
keywords = ["var", "int", "binary_op", "unary_op", "comp_op", "comp_eq", "bin_log_op", "un_log_op", "assign_op",
            "const_var"]
keywords_datatype = ["int", "float", "char"]
keywords_binary = ["binary_op", "comp_op", "comp_eq", "bin_log_op", "un_log_op"]
keywords_unary = ["unary_op"]
keywords_indecr = ["incr", "decr"]
keywords_assign = ["assign_op"]
keywords_functions = ["printf"]
conversions = [("float", "int"), ("int", "char"), ("float", "char"),
               ("int", "float"), ("char", "int"), ("char", "float")]
conv_promotions = [("int", "float"), ("char", "int"), ("char", "float")]


# TODO: Make specific types of AST in the visit functions
# TODO: Replace code in the handle function of AstCreator with the handle functions


class ErrorListener(antlr4.error.ErrorListener.ErrorListener):
    def __init__(self):
        super(ErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Gives an error when there is a syntax error
        :return: a syntax error class
        """
        input_stream = recognizer.getInputStream()
        # Get all tokens in this line or the next one
        line_text = ""
        for token in input_stream.tokens[:input_stream.index]:
            if token.line in range(line-1 , line):
                line_text += token.text

        out = f"Error at line {str(line)}:{str(column)} : {msg}\nLine where it occurred: {line_text}"
        raise ParseCancellationException(out)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        """
        Gives an error when there is an ambiguity
        :return: None
        """
        # raise Exception("Ambiguity")
        super().reportAmbiguity(recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs)


def isfloat(string):
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


def checkType(inputStr: str):
    if inputStr.isdigit():
        return "int"
    elif isfloat(inputStr):
        return "float"
    else:
        return "char"


def getType(inputValue):
    if isinstance(inputValue, int):
        return "int"
    if isinstance(inputValue, float):
        return "float"
    if isinstance(inputValue, str):
        return "char"
    else:
        return None


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


class AST:
    def __init__(self, root: Node = None, children: list = None, parent=None, symbolTable: SymbolTable | None = None):
        """
        Initializer function
        :param root: assign root node
        :param children: assign children if given
        """
        super().__init__()
        if children is None:
            children = []
        self.root: Node | None = root
        self.children: list[Node] | list[AST] | [] = children
        self.parent: AST | None = parent
        self.dic_count = {"instr": 0, "expr": 0}
        self.symbolTable: SymbolTable | None = symbolTable

    # def __eq__(self, o: object) -> bool:
    #     return( self.root == o.root) and (self.children == o.children) and (self.parent == o.parent)
    #
    # def __ne__(self, o: object) -> bool:
    #     return not self.__eq__(o)

    def __repr__(self) -> str:
        return f"root: {{ {self.root} }} , children: {self.children}"

    def __sizeof__(self) -> int:
        return len(self.children)

    # def __getattr__(self, item):
    #     return

    def add_child(self, child):
        """
        Adds a child to the ast
        :param child: node
        :return: none
        """
        if child is None:
            return
        if not isinstance(child, AST) and not isinstance(child, Node):
            if not isinstance(child, AST):
                raise TypeError("child must be set to an AST")
            if not isinstance(child, Node):
                raise TypeError("child must be set to a Node")
        self.children.append(child)

    def save(self):
        """
        saves the ast in a dictionary
        :return: the dictionary
        """
        out, name = self.getDict()
        if out[name] is None:
            out[name] = []
        else:
            out["children"] = []
        if self.root.value is None:
            out[name] = [child.save() for child in self.children]
        else:
            out["children"] = [child.save() for child in self.children]
        return out

    def getDict(self):
        return {self.root.key: self.root.value}, self.root.key

    def save_dot(self, dictionary_function: dict = None):
        """
        saves the ast in a dot format in a dictionary
        :return: dot format dictionary
        """
        if self.root.key in self.dic_count:
            name = f"\"{self.root.key} {self.dic_count[self.root.key]}\""
            self.dic_count[self.root.key] += 1
        else:
            name = f"\"{self.root.key}\""

        out = {name: self.root.value}
        if out[name] is None:
            out[name] = []
        else:
            out["children"] = []

        # Check symbol table for functions
        try:
            for val in dictionary_function.values():
                function_dict = {}
                if isinstance(val, VarNode):
                    continue
                elif isinstance(val[0], FunctionNode):
                    function_dict[val[0].key] = []
                    for i in val:
                        parameter_array = []
                        count = 0
                        for j in i.value.values():
                            parameter_array.append("par" + str(count) + "=" + str(j.value))
                            count += 1
                        function_dict[val[0].key].append(parameter_array)
                out[name].append(function_dict)
        except Exception as e:
            raise e

        # The rest
        for i in range(len(self.children)):
            if self.children[i] is not None and self.root.value is None and not isinstance(self.children[i],
                                                                                           FunctionNode):
                out[name].append(self.children[i].save_dot())
            elif self.children[i] is not None and not isinstance(self.children[i], FunctionNode):
                out["children"].insert(len(out["children"]), self.children[i].save_dot())
        return out

    def print(self, indent: int = 4, save: bool = False, filename: str = ""):
        """
        prints a json format of ast
        :param filename: file to be saved into
        :param save: if True, it is saved to file
        :param indent: indent for json file
        :return:
        """
        output = self.save()
        if save:
            with open(f"../Output/{filename}.json", "w") as outfile:
                json.dump(output, outfile, indent=indent)
        print(json.dumps(output, indent=indent))

    def dot_language(self, file_name, symbol_table: dict = None):
        """
        Create dot language format file

        :param symbol_table:
        :param file_name: String that determines the file name
        :return: None
        """
        # Create file
        file = open("../Output/" + file_name + ".dot", "w+")
        file.close()

        # Start of dot language
        # self.recursive_dot(new_dictionary, count)
        self.connect("../Output/" + file_name + ".dot", self.save_dot(symbol_table))

        # print dot language

        file = open("../Output/" + file_name + ".dot", "r")

        file_contents = file.read()

        # print(file_contents)

        file.close()

    def connect(self, file_name: str, dictionary):
        """
        connects the dictionary items together, to form a completed dot format file
        :return: None
        """
        with open(str(file_name), "w") as f:
            # A = AGraph(dictionary , directed=True)
            # A.graph_attr["shape"] = "tree"
            # A.write(file_name)
            f.write("digraph { \n\tnode [shape=tree];\n\tgraph[smothing=avg_dist]\ncompound=true;\n")
            for key, value in dictionary.items():
                string = ""
                for v in value:
                    string += str(key) + "\t->\t"
                    if isinstance(v, dict):
                        for fk, fv in v.items():
                            string += fk + '\n'
                            string += f"subgraph {fk}" + '{\n'
                            mini_dict = {}
                            for i in range(len(fv)):
                                sub_string = ""
                                for j in fv[i]:
                                    sub_string += j
                                string += '\t' + f"{fk};"
                                mini_dict[fk + str(i)] = sub_string
                            string += "}\n"
                            for mk, mv in mini_dict.items():
                                string += f"\"{mk[:-1]}\"" + "\t->\t" + f"\"{mv}\"" + "\n"
                    else:
                        string += "\t" + str(v) + "\n"
                f.write(string)
            f.write("}")

    def get_str(self):
        """
        string version of the root
        :return: str
        """
        return self.root.key + '\t' + ':' + '\t' + str(self.root.value)

    def get_dot(self):
        """
        dot format version of the root
        :return: str
        """
        return '\"' + self.root.key + '\"' + '\t' + '->' + '\t' + str(self.root.value)

    def handle(self):
        return self


class ExprAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        node = Node("", None, self.parent)
        if self.root.value == '+':
            node = self.children[0] + self.children[1]
            node_type = checkType(str(node.value))
            node.key = node_type
        elif self.root.value == '-':
            node = self.children[0] - self.children[1]
            node_type = checkType(str(node.value))
            node.key = node_type
        node.parent = self.parent
        return node


class InstrAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        return self


class PrintfAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        return self


class DeclrAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None, in_const: bool = False,
                 var_type: str = None):
        super().__init__(root, children, parent)
        self.const = in_const
        self.type = var_type

    def handle(self):
        return self

    def __repr__(self) -> str:
        return f"{super().__repr__()} {'const' if self.const else ''} {self.type} "

    def getDict(self):
        return {self.root.key: [f"{'const ' if self.const else ''}{self.type}"]}, self.root.key


class VarDeclrAST(AST):
    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        if self.root.key == "assign":
            if not isinstance(self.children[0], VarNode):
                raise AttributeError(f"\'Attempting to assign to a non-variable type\'")
            # assign value
            if self.children[0].ptr:
                self.children[0].value = self.children[1]
            else:
                self.children[0].value = self.children[1].value
                self.children[0].cast = self.children[1].cast
            child = self.children[1].value
            while isinstance(child, VarNode):
                child = child.value
            self.children[0].type = getType(child)
            # if isinstance(self.children[0], VarNode) and isinstance(self.children[1], VarNode):
            #     if self.children[0].total_deref != self.children[1].total_deref + 1:
            #         raise AttributeError(f"Incompatible types for {self.children[0].key} and {self.children[1].key}.")
            return self.children[0]
        else:
            return self.children[0]


class AssignAST(AST):
    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        # check if there are conversions needed
        return self.children[0]


class TermAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        node = Node("", None)
        for child in self.children:
            if isinstance(child, AST):
                return self
        if self.root.value == '*':
            node = self.children[0] * self.children[1]
            node_type = checkType(str(node.value))
            node.key = node_type
        elif self.root.value == '%':
            node = self.children[0] % self.children[1]
            node_type = checkType(str(node.value))
            node.key = node_type
        elif self.root.value == '/':
            node = self.children[0] / self.children[1]
            if self.children[0].key != "float" and self.children[1].key != "float":
                node.value = floor(node.value)
        elif self.root.value == "++":
            if len(self.children) != 1:
                raise RuntimeError(f"\'Expected one variable for increment operation, got multiple\'")
            if not isinstance(self.children[0], VarNode):
                raise AttributeError(f"\'Attempting to increment a non-variable type object\'")
            node = self.children[0]
            if node.const:
                raise AttributeError(f"\'Attempting to modify a const variable {node.key}\'")
            node.value += 1
        elif self.root.value == "--":
            if len(self.children) != 1:
                raise RuntimeError(f"\'Expected one variable for increment operation, got multiple\'")
            if not isinstance(self.children[0], VarNode):
                raise AttributeError(f"\'Attempting to increment a non-variable type object\'")
            node = self.children[0]
            if node.const:
                raise AttributeError(f"\'Attempting to modify a const variable {node.key}\'")
            node.value -= 1
        elif self.root.value == '<=':
            node = self.children[0] <= self.children[1]
        elif self.root.value == '<':
            node = self.children[0] < self.children[1]
        elif self.root.value == '>=':
            node = self.children[0] >= self.children[1]
        elif self.root.value == '>':
            node = self.children[0] > self.children[1]
        elif self.root.value == '==':
            if type(self.children[0]) != type(self.children[1]):
                node.value = self.children[0].value == self.children[1].value
            else:
                node.value = self.children[0] == self.children[1]
            node.key = "int"
        elif self.root.value == '!=':
            if type(self.children[0]) != type(self.children[1]):
                node.value = self.children[0].value != self.children[1].value
            else:
                node.value = self.children[0] != self.children[1]
            node.key = "int"
        elif self.root.value == '&&':
            if self.children[0].key == 'char':
                return Node("int", ord(self.children[0].value) and ord(self.children[1].value))
            node = Node("int", self.children[0].value and self.children[1].value)
        elif self.root.value == '||':
            if self.children[0].key == 'char':
                return Node("int", ord(self.children[0].value) or ord(self.children[1].value))
            node = Node("int", self.children[0].value or self.children[1].value)
        elif self.root.value == '!':
            if self.children[0].key == 'char':
                node.value = int(not ord(self.children[0].value))
            node.value = int(not self.children[0].value)
            node.key = "int"
        node.parent = self.parent
        return node


class FactorAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        if self.root.value == '-':
            self.children[0].value = -self.children[0].value
            return self.children[0]
        elif self.root.value == '+':
            return self.children[0]
        elif self.root.value == "++":
            if len(self.children) != 1:
                raise RuntimeError(f"\'Expected one variable for increment operation, got multiple\'")
            if not isinstance(self.children[0], VarNode):
                raise AttributeError(f"\'Attempting to increment a non-variable type object\'")
            node = self.children[0]
            if node.const:
                raise AttributeError(f"\'Attempting to modify a const variable {node.key}\'")
            node.value += 1
            return node
        elif self.root.value == "--":
            if len(self.children) != 1:
                raise RuntimeError(f"\'Expected one variable for increment operation, got multiple\'")
            if not isinstance(self.children[0], VarNode):
                raise AttributeError(f"\'Attempting to increment a non-variable type object\'")
            node = self.children[0]
            if node.const:
                raise AttributeError(f"\'Attempting to modify a const variable {node.key}\'")
            node.value -= 1
            return node


class PrimaryAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        if self.root.value == "&":
            return self.children[0]
        elif self.root.value[0] + self.root.value[-1] == "()":
            ret = self.children[0]
            cast = self.root.value[1:-1]
            ret.value = convert(ret.value, cast)
            ret.cast = True
            return self.children[0]
        return self


class DerefAST(AST):
    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        child = self.children[0]
        if not isinstance(child, VarNode):
            raise ReferenceError(f"Attempting to dereference a non-variable type object")
        if not child.ptr:
            raise AttributeError(f"Attempting to dereference a non-pointer type variable")
        if child.deref_level > child.total_deref:
            raise AttributeError(f"Dereference depth reached for pointer {child.key}")
        child.deref_level += 1
        return child


class Scope_AST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None, condition: AST | None = None):
        super().__init__(root, children, parent, symbolTable=SymbolTable())
        self.condition: AST | Node | None = condition

    def handle(self):
        return self


class If_CondAST(Scope_AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        return self

    def getDict(self):
        return {"if" : self.condition.save()} , "if"

    def save(self):
        out, name = self.getDict()
        if out[name] is None:
            out[name] = []
        else:
            out["body"] = []
        if self.condition is None:
            out[name] = [child.save() for child in self.children]
        else:
            out["body"] = [child.save() for child in self.children]
        return out


class Else_CondAST(Scope_AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def getDict(self):
        return {"else" : None} , "else"

    def save(self):
        out, name = self.getDict()
        if out[name] is None:
            out[name] = [child.save() for child in self.children]
        return out

    def handle(self):
        return self


class For_loopAST(Scope_AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)
        self.initialization = None
        self.incr = None

    def handle(self):
        return self

    def getDict(self):
        return {"for" : [self.initialization.save() , self.condition.save() , self.incr.save()]} , "for"

    def save(self):
        out, name = self.getDict()
        if out[name] is None:
            out[name] = []
        if self.condition is None:
            out[name] = [child.save() for child in self.children]
        else:
            out[name].append({"body": [child.save() for child in self.children]})
            # out["body"] = [child.save() for child in self.children]
        return out


class While_loopAST(Scope_AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        return self

    def getDict(self):
        return {"while" : [self.condition.save()]} , "while"

    def save(self):
        out, name = self.getDict()
        if out[name] is None:
            out[name] = []
        if self.condition is None:
            out[name] = [child.save() for child in self.children]
        else:
            out[name].append({"body": [child.save() for child in self.children]})
        return out


class CondAST(TermAST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)


class InitAST(DeclrAST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

class BreakAST(InstrAST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)


class ContAST(InstrAST):
    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)
