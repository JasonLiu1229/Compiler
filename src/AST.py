from math import floor
from pprint import pprint
from typing import Any
from Node import Node, VarNode, FunctionNode
import antlr4.error.ErrorListener
import json
# Standard Variables
keywords = ["var", "int", "binary_op", "unary_op", "comp_op", "comp_eq", "bin_log_op", "un_log_op", "assign_op",
            "const_var"]
keywords_datatype = ["int", "float", "char"]
keywords_binary = ["binary_op", "comp_op", "comp_eq", "bin_log_op", "un_log_op"]
keywords_unary = ["unary_op"]
keywords_indecr = ["incr", "decr"]
keywords_assign = ["assign_op"]
keywords_functions = ["printf"]
conversions = [("float", "int"), ("int", "char"), ("float", "char")]
conv_promotions = [("int", "float"), ("char", "int"), ("char", "float")]

#TODO: Make specific types of AST in the visit functions
#TODO: Replace code in the handle function of AstCreator with the handle functions


class ErrorListener(antlr4.error.ErrorListener.ErrorListener):
    def __init__(self):
        super(ErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Gives an error when there is a syntax error
        :return: a syntax error class
        """
        out = "Syntax error at line " + str(line) + ":" + str(column) + ": '"
        if offendingSymbol is not None:
            out += offendingSymbol.text
        out += "'" + "\n" + msg
        raise SyntaxError(out)

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

class AST:
    def __init__(self, root: Node = None, children: list = None, parent=None):
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
        out , name = self.getDict()
        if out[name] is None:
            out[name] = []
        else:
            out["children"] = []
        for i in range(len(self.children)):
            if self.children[i] is not None and self.root.value is None:
                out[name].insert(len(out[name]), self.children[i].save())
            elif self.children[i] is not None:
                out["children"].insert(len(out["children"]), self.children[i].save())
        return out

    def getDict(self):
        return {self.root.key: self.root.value} , self.root.key

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


class PrintfAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)


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
        return {self.root.key : [f"{'const ' if self.const else ''}{self.type}"]} , self.root.key


class VarDeclrAST(AST):
    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        return self


class TermAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        node = Node("",None)

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
        node.parent = self.parent
        return node


class FactorAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        if self.root.value == '-':
            return -self.children[0]
        elif self.root.value == '+':
            return self.children[0]
        elif self.children == '++':
            return self.children[0] + 1
        elif self.children == '--':
            return self.children[0] - 1

class PrimaryAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        return self
