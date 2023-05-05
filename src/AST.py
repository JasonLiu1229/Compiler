import random
import string
import uuid
from math import floor
from pprint import pprint
from typing import Any, Tuple
from Node import Node, VarNode, FunctionNode, FuncParameter
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
tokens = ['!=', '==', '>', '>=', '<', '<=', '||', '&&', '%', '/', '-', '+', '++', '--', '*']


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
        pass
        input_stream = recognizer.getInputStream()
        # Get all tokens in this line or the next one
        line_text = ""
        for token in input_stream.tokens[input_stream.index:]:
            if token.line in range(line - 1, line + 1):
                if input_stream.tokens.index(token) == input_stream.index:
                    line_text += "\u0332"
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


def getLLVMType(ObjectType: str) -> str | None:
    if ObjectType == 'int':
        return 'i32'
    elif ObjectType == 'float':
        return 'float'
    elif ObjectType == 'char':
        return 'i8'
    return None


def visited_list_DFS(ast) -> list:
    not_visited = [ast]
    visited = []
    while len(not_visited) > 0:
        v = not_visited.pop()
        if v not in visited:
            visited.append(v)
            if not isinstance(v, While_loopAST) or not isinstance(v, FuncDeclAST) \
                    or not isinstance(v, If_CondAST) \
                    or not isinstance(v, FuncDefnAST):
                for i in v.children:
                    not_visited.append(i)
    return visited


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

    def llvm_global(self, index: int = 1) -> tuple[str, int]:
        """
        Generates the LLVM code for the global variables
        :param index: index of the current variable
        :return: tuple of the LLVM code and the index
        """
        out = ""
        return out, index

    def visitLLVMOp(self, current, index: int) -> tuple[str, int]:
        out = ""
        indexL, indexR = 0, 0
        leftChild = current.children[0]
        rightChild = None
        rentry = None
        lentry = None
        if len(current.children) > 1:
            rightChild = current.children[1]

            if isinstance(rightChild, VarNode):
                rentry, length = self.getEntry(rightChild)
                if rentry is not None:
                    indexR = rentry.register
                    out += f"\t%{index} load {getLLVMType(rightChild.type)}, ptr %{indexR}, align 4\n"
                    index += 1
            else:
                indexR = rightChild.value

        if isinstance(leftChild, VarNode):
            lentry, length = self.getEntry(leftChild)
            if lentry is not None:
                indexL = lentry.register
                out += f"\t%{index} load {getLLVMType(leftChild.type)}, ptr %{indexL}, align 4\n"
                index += 1
        else:
            indexL = leftChild.value

        operand = current.root.value
        currenType = None
        if isinstance(leftChild, VarNode):
            currenType = leftChild.type
        elif isinstance(rightChild, VarNode):
            currenType = rightChild
        else:
            currenType = leftChild.key
        convertedType = getLLVMType(currenType)
        if operand == '<':
            out += f"\t%{index} = " + self.comp_lt(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
            current.parent.children[current.parent.children.index(current)] = Node(currenType, index)
            index += 1
        elif operand == '>':
            out += f"\t%{index} = " + self.comp_gt(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
            current.parent.children[current.parent.children.index(current)] = Node(currenType, index)
            index += 1
        elif operand == '==':
            out += f"\t%{index} = " + self.comp_eq(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
            current.parent.children[current.parent.children.index(current)] = Node(currenType, index)
            index += 1
        elif operand == '!=':
            out += f"\t%{index} = " + self.comp_neq(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
            current.parent.children[current.parent.children.index(current)] = Node(currenType, index)
            index += 1
        elif operand == '<=':
            out += f"\t%{index} = " + self.comp_leq(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
            current.parent.children[current.parent.children.index(current)] = Node(currenType, index)
            index += 1
        elif operand == '>=':
            out += f"\t%{index} = " + self.comp_geq(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
            current.parent.children[current.parent.children.index(current)] = Node(currenType, index)
            index += 1
        elif operand == '&&':
            out += f"\t%{index} = " + self.and_op(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
            current.parent.children[current.parent.children.index(current)] = Node(currenType, index)
            index += 1
        elif operand == '||':
            out += f"\t%{index} = " + self.or_op(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
            current.parent.children[current.parent.children.index(current)] = Node(currenType, index)
            index += 1
        elif operand == '+':
            out += f"\t%{index} = " + self.add(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
            current.parent.children[current.parent.children.index(current)] = Node(currenType, index)
            index += 1
        elif operand == '-':
            out += f"\t%{index} = " + self.sub(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
            current.parent.children[current.parent.children.index(current)] = Node(currenType, index)
            index += 1
        elif operand == '/':
            out += f"\t%{index} = " + self.div(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
            current.parent.children[current.parent.children.index(current)] = Node(currenType, index)
            index += 1
        elif operand == '*':
            out += f"\t%{index} = " + self.mul(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
            current.parent.children[current.parent.children.index(current)] = Node(currenType, index)
            index += 1
        elif operand == '%':
            out += f"\t%{index} = " + self.mod(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
            current.parent.children[current.parent.children.index(current)] = Node(currenType, index)
            index += 1
        elif operand == '++':
            out += f"\t%{index} = " + self.incr(convertedType, f"%{indexL}") + "\n"
            current.parent.children[current.parent.children.index(current)] = Node(currenType, index)
            index += 1
        elif operand == '--':
            out += f"\t%{index} = " + self.decr(convertedType, f"%{indexL}") + "\n"
            current.parent.children[current.parent.children.index(current)] = Node(currenType, index)
            index += 1
        return out, index

    @staticmethod
    def getEntry(entry):
        out = None
        temp_symbol = None if isinstance(entry, Node) else entry.symbolTable
        temp_parent = entry.parent
        found = False
        while not found and temp_parent is not None:
            temp_symbol = temp_parent.symbolTable if isinstance(temp_parent, AST) else None
            temp_parent = temp_parent.parent
            if temp_symbol is not None:
                if temp_symbol.exists(entry):
                    out = temp_symbol.lookup(entry)
                    return (out[0].object, len(out)) if out is not None else ([], None)
                elif temp_symbol.exists(entry.value):
                    out = temp_symbol.lookup(entry.value)
                    return (out[0].object, len(out)) if out is not None else ([], None)
        return out, -1

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

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        return f" ", index

    @staticmethod
    def sub(var_type: str, op1: str, op2: str):
        """
        Writes LLVM code for a subtract operation
        :param var_type: the type of return value
        :param op1: the first operand
        :param op2: the second operand
        """
        return f"sub nsw {var_type} {op1}, {op2}"

    @staticmethod
    def add(var_type: str, op1: str, op2: str):
        """
        Writes LLVM code for an addition operation
        :param var_type: the type of return value
        :param op1: the first operand
        :param op2: the second operand
        """
        return f"add nsw {var_type} {op1}, {op2}"

    @staticmethod
    def mul(var_type, op1, op2):
        """
        Writes LLVM code for a multiplication operation
        :param var_type: the type of return value
        :param op1: the first operand
        :param op2: the second operand
        """
        return f"mul nsw {var_type} {op1}, {op2}"

    @staticmethod
    def sdiv(var_type: str, op1: str, op2: str):
        """
        Writes LLVM code for a division operation (signed)
        :param var_type: the type of return value
        :param op1: the first operand
        :param op2: the second operand
        """
        return f"sdiv {var_type} {op1}, {op2}"

    @staticmethod
    def udiv(var_type: str, op1: str, op2: str):
        """
        Writes LLVM code for a division operation (unsigned)
        :param var_type: the type of return value
        :param op1: the first operand
        :param op2: the second operand
        """
        return f"udiv {var_type} {op1}, {op2}"

    @staticmethod
    def div(var_type: str, op1: str, op2: str):
        """
        Writes LLVM code for a division operation (unsigned)
        :param var_type: the type of return value
        :param op1: the first operand
        :param op2: the second operand
        """
        return AST.sdiv(var_type, op1, op2)

    @staticmethod
    def mod(var_type: str, op1: str, op2: str):
        """
        Writes LLVM code for a modulo operation (unsigned)
        :param var_type: the type of return value
        :param op1: the first operand
        :param op2: the second operand
        """
        return f"urem {var_type} {op1}, {op2}"

    @staticmethod
    def incr(var_type: str, op: str):
        """
        Writes LLVM code for an increment operation
        :param var_type: the type of return value
        :param op: the first operand
        """
        return AST.add(var_type, op, "1")

    @staticmethod
    def decr(var_type: str, op: str):
        """
        Writes LLVM code for a decrement operation
        :param var_type: the type of return value
        :param op: the first operand
        """
        return AST.sub(var_type, op, "1")

    @staticmethod
    def comp_gt(var_type: str, op1: str, op2: str):
        """
        Writes LLVM code for a greater than operation
        :param var_type: the type of return value
        :param op1: the first operand
        :param op2: the second operand
        """
        return f'icmp sgt {var_type} {op1}, {op2}'

    @staticmethod
    def comp_lt(var_type: str, op1: str, op2: str):
        """
        Writes LLVM code for a less than operation
        :param var_type: the type of return value
        :param op1: the first operand
        :param op2: the second operand
        """
        return f'icmp slt {var_type} {op1}, {op2}'

    @staticmethod
    def comp_eq(var_type: str, op1: str, op2: str):
        """
        Writes LLVM code for an is equal operation
        :param var_type: the type of return value
        :param op1: the first operand
        :param op2: the second operand
        """
        return f'icmp eq {var_type} {op1}, {op2}'

    @staticmethod
    def comp_geq(var_type: str, op1: str, op2: str):
        """
        Writes LLVM code for a greater than equals operation
        :param var_type: the type of return value
        :param op1: the first operand
        :param op2: the second operand
        """
        return f'icmp sge {var_type} {op1}, {op2}'

    @staticmethod
    def comp_leq(var_type: str, op1: str, op2: str):
        """
        Writes LLVM code for a less than equals operation
        :param var_type: the type of return value
        :param op1: the first operand
        :param op2: the second operand
        """
        return f'icmp sle {var_type} {op1}, {op2}'

    @staticmethod
    def comp_neq(var_type: str, op1: str, op2: str):
        """
        Writes LLVM code for a not equal operation
        :param var_type: the type of return value
        :param op1: the first operand
        :param op2: the second operand
        """
        return f'icmp ne {var_type} {op1}, {op2}'

    @staticmethod
    def and_op(var_type: str, op1: str, op2: str):
        """
        Writes LLVM code for an AND operation
        :param var_type: the type of return value
        :param op1: the first operand
        :param op2: the second operand
        """
        return f"and {var_type} {op1}, {op2}"

    @staticmethod
    def or_op(var_type: str, op1: str, op2: str):
        """
        Writes LLVM code for an OR operation
        :param var_type: the type of return value
        :param op1: the first operand
        :param op2: the second operand
        """
        return f"or {var_type} {op1}, {op2}"

    @staticmethod
    def not_op(var_type: str, op: str):
        """
        Writes LLVM code for an NOT operation
        :param var_type: the type of return value
        :param op: the first operand
        """
        return f"not {var_type} {op}"

    @staticmethod
    def assign(var_type: str, value, ptr):
        """
        Writes LLVM code for an assign operation
        :param var_type: the type of value to assign to the variable
        :param value: the value to store on the variable
        :param ptr: The register to store the value in
        """
        return f"store {var_type} {value}, {var_type}* {ptr}"


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

        # convert the value of first operand to int
        if self.children[0].key == 'char':
            temp_val1 = ord(self.children[0].value)
        else:
            temp_val1 = self.children[0].value

        # convert the value of second operand to int
        if self.children[1].key == 'char':
            temp_val2 = ord(self.children[1].value)
        else:
            temp_val2 = self.children[1].value

        # perform the operation
        if self.root.value == '&&':
            node = Node("int", int(temp_val1 != 0 and temp_val2 != 0))
        elif self.root.value == '||':
            node = Node("int", int(temp_val1 != 0 or temp_val2 != 0))
        node.parent = self.parent
        return node


class InstrAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        return self


class PrintfAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None, format_string: str = None, args=None,
                 format_specifiers: list = None):
        super().__init__(root, children, parent)
        if args is None:
            args = []
        self.format_string: str = format_string
        self.format_specifiers: list = []
        self.args: list = args

    def handle(self):
        for i in range(len(self.format_specifiers)):
            current_specifier = self.format_specifiers[i]
            current_child = self.children[i]
            length = int(current_specifier[1:-1]) if current_specifier[1:-1].isdigit() else 0
            # check the child's type
            if current_specifier[-1] == 'd':
                # check if the child is a node
                if isinstance(current_child, Node):
                    if not isinstance(current_child.value, int):
                        if isinstance(current_child.value, float):
                            current_child.value = int(current_child.value)
                        elif isinstance(current_child.value, str) and len(current_child.value) == 1:
                            current_child.value = ord(current_child.value)
                        elif current_child.value is None:
                            current_child.value = random.randint(0,10**length) if length > 0 else random.randint(0, 10)
                        else:
                            raise TypeError("Invalid type for printf")
                elif isinstance(current_child, VarNode):
                    if not current_child.type == 'int':
                        if current_child.type == 'float':
                            current_child.value = int(current_child.value)
                        elif current_child.type == 'char':
                            current_child.value = ord(current_child.value)
                        elif current_child.value is None:
                            current_child.value = random.randint(0, 10 ** length) if length > 0 else random.randint(0, 10)
                        else:
                            raise TypeError("Invalid type for printf")
                current_child.type = 'int'
            if current_specifier[-1] == 'i':
                # type can accept hexa, octal, decimal and binary
                if isinstance(current_child, Node):
                    if not isinstance(current_child.value, int):
                        if isinstance(current_child.value, float):
                            current_child.value = int(current_child.value)
                        elif isinstance(current_child.value, str) and len(current_child.value) == 1:
                            current_child.value = ord(current_child.value)
                        elif current_child.value is None:
                            current_child.value = random.randint(0,10**length)
                        else:
                            raise TypeError("Invalid type for printf")
                elif isinstance(current_child, VarNode):
                    if not current_child.type == 'int':
                        if current_child.type == 'float':
                            current_child.value = int(current_child.value)
                        elif current_child.type == 'char':
                            current_child.value = ord(current_child.value)
                        elif current_child.value is None:
                            current_child.value = random.randint(0, 10 ** length)
                        else:
                            raise TypeError("Invalid type for printf")
                current_child.type = 'int'
            if current_specifier[-1] == 'c':
                if isinstance(current_child, Node):
                    if not isinstance(current_child.value, str) or len(current_child.value) != 1:
                        if isinstance(current_child.value, float):
                            current_child.value = int(current_child.value)
                        elif current_child.value is None:
                            current_child.value = random.choice(string.ascii_letters)
                        else:
                            raise TypeError("Invalid type for printf")
                elif isinstance(current_child, VarNode):
                    if not current_child.type == 'char':
                        if current_child.type == 'float':
                            current_child.value = int(current_child.value)
                        elif current_child.value is None:
                            current_child.value = random.choice(string.ascii_letters)
                        else:
                            raise TypeError("Invalid type for printf")
                current_child.type = 'char'

            if current_specifier[-1] == 's':
                if isinstance(current_child, Node):
                    if current_child.value is None:
                        current_child.value = str(uuid.uuid1())
                    if not isinstance(current_child.value, str):
                        raise TypeError("Invalid type for printf")
                if not current_child.type == 'char' or not current_child.ptr or not current_child.array:
                    raise TypeError("Invalid type for printf")
            # check the length of format specifiers and child
            if length != 0:
                # convert child value to string
                if isinstance(current_child, Node):
                    if length > len(str(current_child.value)):
                        current_child.value = str(current_child.value).rjust(length, ' ')
        return self

    def llvm_global(self, index: int = 1) -> tuple[str, int]:
        out = ""
        out += f"@.str.{index} = private unnamed_addr constant [{len(self.format_string)} x i8] c\"{self.format_string}\\00\", align 1\n"
        entry, length = self.getEntry(self.root)
        entry.register = index
        index += 1
        return out, index

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        out = ""
        var_string = ""
        count = 0
        for var in self.variables:
            if isinstance(var, Node):
                var_string += f"{getLLVMType(getType(var.value))} noundef %{var.value}"
            else:
                entry, length = self.getEntry(var)
                var += f"{getLLVMType(entry.type)} noundef %{entry.register}"
            if count + 1 != len(self.variables):
                var_string += ', '
        out += f"call i32 (ptr, ...) @printf(ptr noundef @.str.{index}, {var_string})\n"
        return out, index


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

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        pass


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

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        pass


class AssignAST(AST):
    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        # check if there are conversions needed
        return self.children[0]

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        pass


class TermAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        node = Node("", None)
        for child in self.children:
            if isinstance(child, AST):
                return self
            if child.value is None:
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
            node.value = int(node.value)
        elif self.root.value == '<':
            node = self.children[0] < self.children[1]
            node.value = int(node.value)
        elif self.root.value == '>=':
            node = self.children[0] >= self.children[1]
            node.value = int(node.value)
        elif self.root.value == '>':
            node = self.children[0] > self.children[1]
            node.value = int(node.value)
        elif self.root.value == '==':
            if type(self.children[0]) != type(self.children[1]):
                node.value = self.children[0].value == self.children[1].value
            else:
                node.value = self.children[0] == self.children[1]
            node.value = int(node.value)
            node.key = "int"
        elif self.root.value == '!=':
            if type(self.children[0]) != type(self.children[1]):
                node.value = self.children[0].value != self.children[1].value
            else:
                node.value = self.children[0] != self.children[1]
            node.value = int(node.value)
            node.key = "int"
        elif self.root.value == '!':
            if self.children[0].key == 'char':
                node.value = not ord(self.children[0].value)
            node.value = not self.children[0].value
            node.value = int(node.value)
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
        child = child.value
        if isinstance(child, VarNode) and child.ptr:
            child.deref_level += 1
        return child


class Scope_AST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None, condition: AST | None = None):
        super().__init__(root, children, parent, symbolTable=SymbolTable())
        self.condition: AST | Node | None = condition
        self.symbolTable.owner = self.root.key

    def handle(self):
        return self

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        visited = visited_list_DFS(self)
        out = ""

        for current in visited:
            output = tuple
            if current.root.value in tokens:
                output = self.visitLLVMOp(current, index)
            else:
                output = current.llvm()
            out += output[0]
            index = output[1]
        return out, index


class If_CondAST(Scope_AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        return self

    def getDict(self):
        return {"if": self.condition.save()}, "if"

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

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        # condition first with branch
        out = ""
        visited = visited_list_DFS(self.condition)

        for current in visited:
            output_str, output_in = self.visitLLVMOp(current, index)
            out += output_str
            index = output_in

        # if block
        visited = visited_list_DFS(self)

        for current in visited:
            output = tuple
            if current.root.value in tokens:
                output = self.visitLLVMOp(current, index)
            else:
                output = current.llvm(True, index)
            out += output[0]
            index = output[1]

        # else block if else ast exist do 'else llvm' else do 'create block'
        else_bool = False
        for child in self.children:
            if isinstance(child, Else_CondAST):
                output = child.llvm(True, index)
                out += output[0]
                index = output[1]
                else_bool = True
                break
        # create new block if else llvm didn't pass
        if not else_bool:
            out += f"{index}:\n"
            index += 1

        return out, index


class Else_CondAST(Scope_AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def getDict(self):
        return {"else": None}, "else"

    def save(self):
        out, name = self.getDict()
        if out[name] is None:
            out[name] = [child.save() for child in self.children]
        return out

    def handle(self):
        return self

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        visited = visited_list_DFS(self)
        out = ""
        for current in visited:
            output = tuple
            if current.root.value in tokens:
                output = self.visitLLVMOp(current, index)
            else:
                output = current.llvm(True, index)
            out += output[0]
            index = output[1]
        return out, index


class For_loopAST(Scope_AST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)
        self.initialization = None
        self.incr = None

    def handle(self):
        return self

    def getDict(self):
        return {"for": [self.initialization.save(), self.condition.save(), self.incr.save()]}, "for"

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
        return {"while": [self.condition.save()]}, "while"

    def save(self):
        out, name = self.getDict()
        if out[name] is None:
            out[name] = []
        if self.condition is None:
            out[name] = [child.save() for child in self.children]
        else:
            out[name].append({"body": [child.save() for child in self.children]})
        return out

    def llvm_block1(self, out, index, blocks):
        name = blocks["1"]
        out += f"{name}:"
        index += 1

        # DFS the condition
        visited = []
        not_visited = [self.condition]
        while len(not_visited) > 0:
            current = not_visited.pop()
            if current not in visited:
                visited.append(current)
                for i in current.children:
                    if not isinstance(i, Node):
                        not_visited.append(i)

        # handle everything separately
        for current in visited:
            output = self.visitLLVMOp(current, index)

            out += output[0]
            index = output[1]
        index2 = blocks["2"]
        index3 = blocks["3"]
        out += f"br i1 %{index - 1}, label %{index2}, label %{index3}"
        return out, index

    def llvm_block2(self, out, index, blocks):
        name = blocks["2"]
        out += f"{name}:"

        # DFS
        visited = []
        not_visited = [self.children[0]]
        while len(not_visited) > 0:
            current = not_visited.pop()
            if current not in visited:
                visited.append(current)
                if not isinstance(current, While_loopAST) or not isinstance(current, FuncDeclAST) \
                        or not isinstance(current, If_CondAST) \
                        or not isinstance(current, FuncDefnAST):
                    for i in current.children:
                        not_visited.append(i)

        # Handle
        for current in visited:
            output = tuple
            if current.root.value in tokens:
                output = self.visitLLVMOp(current, index)
            else:
                output = current.llvm(True, index)
            out += output[0]
            index = output[1]

        index1 = blocks["1"]
        out += f"\tbr label %{index1}, !llvm.loop !6"
        return out, index

    @staticmethod
    def llvm_block3(out, index, blocks):
        name = blocks["3"]
        out += f"{name}:"
        out += f"\t%ret i32 0"
        index += 1
        return out, index

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[Any, Any]:
        blocks = {"1": index, "2": index + 1, "3": index + 2}
        index += 2
        out = f"\tbr label %{index}\n\n"
        out, index = self.llvm_block1(out, index, blocks)
        out, index = self.llvm_block2(out, index, blocks)
        out, index = self.llvm_block3(out, index, blocks)
        return out, index


class CondAST(TermAST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)
        self.last_eval = None

    def __repr__(self) -> str:
        return f"root: {{ {self.root} }}, last_eval: " \
               f"{self.last_eval.value if isinstance(self.last_eval, Node) else self.last_eval} , children: {self.children}"

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        pass


class InitAST(DeclrAST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        pass


class BreakAST(InstrAST):

    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)


class ContAST(InstrAST):
    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        pass


class FuncParametersAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None, symbolTable: SymbolTable | None = None,
                 parameters: list[FuncParameter] = None):
        super().__init__(root, children, parent, symbolTable)
        if parameters is None:
            parameters = []
        self.parameters = parameters

    def handle(self):
        return self

    def save(self):
        return [child.save() for child in self.children]


class FuncDeclAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None, symbolTable: SymbolTable | None = None,
                 return_type: str = None, const: bool = False, ptr: bool = False, ptr_level: int = 0,
                 params=None):
        super().__init__(root, children, parent, symbolTable)
        self.type: str = return_type
        self.const: bool = const
        self.ptr: bool = ptr
        self.ptr_level: int = ptr_level
        if params is None:
            params = []
        self.params = params
        self.has_defaults = []

    def handle(self):
        return self

    def save(self):
        out, name = self.getDict()
        if out[name] is None:
            out[name] = []
        for child in self.children:
            if isinstance(child, FuncParametersAST):
                out[name].append({"Parameters": child.save()})
        return out

    def getDict(self):
        return {f"{'const ' if self.const else ''}{self.type}{'*' * self.ptr_level} {self.root.key}": self.root.value}, \
            f"{'const ' if self.const else ''}{self.type}{'*' * self.ptr_level} {self.root.key}"

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        out = f""
        # Begin
        out += f"define dso_local {getLLVMType(self.type)} @{self.root.key}"
        # Parameters
        paramaters = self.params.parameters
        param_string = ""
        default_exist = False
        if len(paramaters) > 0:
            count = 0
            for i in paramaters:
                param_string += f"{getLLVMType(i.type)} noundef %{i.key}"
                if count + 1 != len(paramaters):
                    param_string += ', '
                count += 1
        out += f" ({param_string})"
        return out, index


class FuncDefnAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None, symbolTable: SymbolTable | None = None,
                 return_type: str = None, const: bool = False, ptr: bool = False, ptr_level: int = 0,
                 params=None):
        super().__init__(root, children, parent, symbolTable)
        self.type: str = return_type
        self.const: bool = const
        self.ptr: bool = ptr
        self.ptr_level: int = ptr_level
        if params is None:
            params = []
        self.params = params
        self.has_defaults = []

    def handle(self):
        return self

    def save(self):
        out, name = self.getDict()
        if out[name] is None:
            out[name] = []
        for child in self.children:
            if isinstance(child, FuncParametersAST):
                out[name].append({"Parameters": child.save()})
            else:
                out[name].append({"Body": child.save()})
        return out

    def getDict(self):
        return {f"{'const ' if self.const else ''}{self.type}{'*' * self.ptr_level} {self.root.key}": self.root.value}, \
            f"{'const ' if self.const else ''}{self.type}{'*' * self.ptr_level} {self.root.key}"

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        out = f""
        # Begin
        out += f"define dso_local {getLLVMType(self.type)} @{self.root.key}"
        # Parameters
        parameters = self.params.parameters
        param_string = ""
        default_exist = False
        if len(parameters) > 0:
            count = 0
            for i in parameters:
                param_string += f"{getLLVMType(i.type)} noundef %{i.key}"
                if count + 1 != len(parameters):
                    param_string += ', '
                count += 1
        out += f" ({param_string})"
        # the rest
        out += " #0 {\n"

        local_index = 1
        if len(parameters) > 0:
            for child in parameters:
                out += f"%{local_index} = alloca {getLLVMType(child.type)}, align {'4' if not child.ptr else '8'}\n"
                out += f"%store {getLLVMType(child.type)} %{child.key}, ptr %{local_index}, align {'4' if not child.ptr else '8'}\n"
                entry, length = self.getEntry(child)
                entry.register = local_index
                local_index += 1
        # Scope
        output = self.children[0].llvm(True, local_index)
        out += output[0]
        out += "}\n"
        return out, index


class FuncCallAST(AST):
    def __init__(self, root: Node = None, children: list = None, parent=None, symbolTable: SymbolTable | None = None,
                 args: list = None):
        super().__init__(root, children, parent, symbolTable)
        if args is None:
            args = []
        self.args = args

    def handle(self):
        return self

    def save(self):
        out, name = self.getDict()
        if out[name] is None:
            out[name] = []
        out[name].append({"parameters": [child.save() for child in self.children]})
        return out

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        # %result = call i32 @add(i32 3, i32 4)
        function, length = self.getEntry(self.root)
        # arguments
        arg_string = ""
        count = 0
        for arg in self.args:
            arg_string += f"{getLLVMType(getType(arg.value) if isinstance(arg, Node) else arg.type)} {str(arg.value)}"
            if count + 1 != len(arg):
                arg_string += ', '
        # end string
        out = f"call {getLLVMType(function.type)} @{self.root.key}({arg_string})\n"
        return out, index


class FuncScopeAST(AST):
    def __init__(self, root: Node = None, children: list = None, parent=None, symbolTable: SymbolTable | None = None):
        super().__init__(root, children, parent, SymbolTable())
        self.symbolTable.owner = self.root.key

    def handle(self):
        return self

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        # DFS the whole scope and llvm every part of them
        visited = []
        not_visited = [self]
        while len(not_visited) > 0:
            current = not_visited.pop()
            if current not in visited:
                visited.append(current)
                if not isinstance(current, While_loopAST) or not isinstance(current, FuncDeclAST) \
                        or not isinstance(current, If_CondAST) \
                        or not isinstance(current, FuncDefnAST):
                    for i in current.children:
                        not_visited.append(i)

        out = ""
        for current in visited:
            output = tuple
            if current.root.value in tokens:
                output = self.visitLLVMOp(current, index)
            else:
                output = current.llvm(True, index)
            out += output[0]
            index = output[1]
        out += "}\n"
        return out, index


class ReturnInstr(InstrAST):
    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        return self

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        out = ""
        if isinstance(self.root, Node):
            out += f"ret {getLLVMType(getType(self.root.value))} {self.root.value}\n"
        elif isinstance(self.root, VarNode):
            entry, length = self.getEntry(self.root)
            out += f"%{index} = load {getLLVMType(entry.type)}, ptr %{entry.register}, align {'4' if not entry.ptr else '8'}\n"
            out += f"ret {getLLVMType(self.root.type)} %{entry.register}\n"
        return out, index


class ScanfAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None, symbolTable: SymbolTable | None = None):
        super().__init__(root, children, parent, symbolTable)
        self.variables = []
        self.format_string = None
        self.format_specifiers = []

    def save(self):
        out, name = self.getDict()
        if out[name] is None:
            out[name] = []
        if self.root.value is None:
            out[name] = [child.save() for child in self.variables]
        return out

    def getDict(self):
        name = f"scanf({self.format_string})"
        return {name: self.variables}, name

    def handle(self):
        return self

    def llvm_global(self, index: int = 1) -> tuple[str, int]:
        out = ""
        out += f"@.str.{index} = private unnamed_addr constant [{len(self.format_string)} x i8] c\"{self.format_string}\\00\", align 1\n"
        entry, length = self.getEntry(self.root)
        entry.register = index
        index += 1
        return out, index

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        out = ""
        var_string = ""
        count = 0
        for var in self.variables:
            if isinstance(var, Node):
                var_string += f"{getLLVMType(getType(var.value))} noundef %{var.value}"
            else:
                entry, length = self.getEntry(var)
                var += f"{getLLVMType(entry.type)} noundef %{entry.register}"
            if count + 1 != len(self.variables):
                var_string += ', '
        out += f"call i32 (ptr, ...) @__isoc99_scanf(ptr noundef @.str.{index}, {var_string})\n"
        return out, index


class ArrayDeclAST(AST):
    def __init__(self, root: Node = None, children: list = None, parent=None, symbolTable: SymbolTable | None = None):
        super().__init__(root, children, parent, symbolTable)
        self.size = 0
        self.values = []

    def handle(self):
        return self

    def llvm_global(self, index: int = 1) -> tuple[str, int]:
        out = ""
        entry, length = self.getEntry(self.root)
        out += f"@__const.{entry.symbol_table.owner}.{entry.name} = private unnamed_addr constant " \
               f"[{self.size if self.size > 1 else 1} x {getLLVMType(getType(self.root.value))}] ["
        count = 0
        vals = ""
        for val in self.values:
            vals += f"{getLLVMType(entry.type)} {val.value} " \
                    f"{', ' if count + 1 != len(self.values) else ''}"
            count += 1
        if count < self.size != 0:
            for i in range(self.size - count):
                vals += f"{getLLVMType(entry.type)} 0 {', ' if count + 1 != len(self.values) else ''}"
        out += vals
        out += f"], align {4 if self.size < 4 else 16}\n"
        return out, index

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        out = ""
        entry, length = self.getEntry(self.root)
        if scope:
            # local
            out += f"%{index} = alloca [ {self.size} x {getLLVMType(entry.type)}], align {4 if self.size < 4 else 16}\n"
            entry.register = index
            out += f"call void @llvm.memcpy.p0.p0.i64(ptr allign {4 if self.size < 4 else 16} %{index}, " \
                   f"ptr align {4 if self.size < 4 else 16} " \
                   f"@__const.{entry.symbol_table.owner}.{entry.name}, i64 {self.size * 4}, i1 false)"
            out += f"\n"
            index += 1

        else:
            # global
            vals = "["
            count = 0
            for val in self.values:
                vals += f"{getLLVMType(getType(entry.type))} {val.value} {', ' if count + 1 != len(self.values) else ''}"
                count += 1
            if count < self.size != 0:
                for i in range(self.size - count):
                    vals += f"{getLLVMType(getType(entry.type))} 0 {', ' if count + 1 != len(self.values) else ''}"
            vals += "]"
            out += f"@{self.root.key} = dso_local global [ " \
                   f"{self.size if self.size > 1 else 1} x {getLLVMType(getType(entry.type))}] " \
                   f"{'zeroinitializer' if len(self.values) == 0 else vals}, align {4 if self.size < 4 else 16}\n"
        return out, index


class IncludeAST(AST):
    def __init__(self, root: Node = None, children: list = None, parent=None, symbolTable: SymbolTable | None = None):
        super().__init__(root, children, parent, symbolTable)

    def getDict(self):
        return {f"#include<{self.root.key}>": self.root.value}, f"#include<{self.root.key}>"

    def handle(self):
        return self

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        pass
