import random
import re
import string
import uuid
from math import floor
from array import array
from pprint import pprint
from typing import Any, Tuple
from Node import Node, VarNode, FunctionNode, FuncParameter, ArrayNode
import antlr4.error.ErrorListener
import antlr4.error.ErrorStrategy
import json
from SymbolTable import *
from antlr4.error.Errors import ParseCancellationException
from MIPS import *

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

def getTypeFromFormat(inputValue):
    if inputValue == "d":
        return "int"
    if inputValue == "f":
        return "float"
    if inputValue == "c":
        return "char"
    if inputValue == "s":
        return "string"
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
            if not (isinstance(v, Node) or v is ast):
                visited.append(v)
            if not isinstance(v, While_loopAST) or not isinstance(v, FuncDeclAST) \
                    or not isinstance(v, If_CondAST) \
                    or not isinstance(v, FuncDefnAST) or not isinstance(v, For_loopAST):
                if isinstance(v, AST):
                    for i in v.children:
                        if i is not ast:
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
        self.register = None
        self.blocks = []
        self.column = None
        self.line = None
        self.in_loop = False
        self.in_func = False

    # def __eq__(self, o: object) -> bool:
    #     return( self.root == o.root) and (self.children == o.children) and (self.parent == o.parent)
    #
    # def __ne__(self, o: object) -> bool:
    #     return not self.__eq__(o)

    def mips(self, registers: Registers):
        out_global = ""
        out_local = ""
        return out_local, out_global

    def searchBlocks(self):
        if isinstance(self, While_loopAST):
            return self.blocks
        temp_parent = self.parent
        while self.parent is not None and isinstance(self.parent, Scope_AST):
            if isinstance(temp_parent, Scope_AST) and not isinstance(temp_parent, While_loopAST):
                temp_parent = temp_parent.parent
            else:
                return temp_parent.blocks
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
                    if rentry.register is None:
                        indexR = index
                        rentry.register = index
                        index += 1
                if rentry is not None:
                    indexR = rentry.register
                    out += f"\t%{index} load {getLLVMType(rightChild.type)}, ptr %{indexR}, align 4\n"
                    index += 1
            else:
                indexR = rightChild.value

        if isinstance(leftChild, VarNode):
            lentry, length = self.getEntry(leftChild)
            if lentry is not None:
                if lentry is not None:
                    if lentry.register is None:
                        indexL = index
                        lentry.register = index
                        index += 1
                out += f"\t%{index} = load {getLLVMType(leftChild.type)}, ptr %{indexL}, align 4\n"
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
        elif operand == '>':
            out += f"\t%{index} = " + self.comp_gt(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
        elif operand == '==':
            out += f"\t%{index} = " + self.comp_eq(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
        elif operand == '!=':
            out += f"\t%{index} = " + self.comp_neq(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
        elif operand == '<=':
            out += f"\t%{index} = " + self.comp_leq(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
        elif operand == '>=':
            out += f"\t%{index} = " + self.comp_geq(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
        elif operand == '&&':
            out += f"\t%{index} = " + self.and_op(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
        elif operand == '||':
            out += f"\t%{index} = " + self.or_op(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
        elif operand == '+':
            out += f"\t%{index} = " + self.add(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
        elif operand == '-':
            out += f"\t%{index} = " + self.sub(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
        elif operand == '/':
            out += f"\t%{index} = " + self.div(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
        elif operand == '*':
            out += f"\t%{index} = " + self.mul(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
        elif operand == '%':
            out += f"\t%{index} = " + self.mod(convertedType, f"%{indexL}", f"%{indexR}") + "\n"
        elif operand == '++':
            out += f"\t%{index} = " + self.incr(convertedType, f"%{indexL}") + "\n"
        elif operand == '--':
            out += f"\t%{index} = " + self.decr(convertedType, f"%{indexL}") + "\n"

        if isinstance(current, CondAST):
            pass
        else:
            current.parent.children[current.parent.children.index(current)] = Node(currenType, index)
            index += 1
        return out, index

    def visitMIPSOp(self, current, registers):
        out_local = ""
        out_global = ""
        # TODO: Implement MIPS operations
        # TODO: use $t0
        return out_local, out_global

    @staticmethod
    def getEntry(entry):
        if isinstance(entry, Node):
            if isinstance(entry.parent, ArrayNode):
                return entry.parent, 1
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
            out[name] = []
            for child in self.children:
                out[name].append(child.save())
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
        out = ""
        # if len(self.children) > 0:
        #     for child in self.children:
        #         out , index = child.llvm(scope, index)
        return out, index

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
        return f"add nsw ptr {op1}, {op2}"

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
        if self.children[0].key == "var" or self.children[1].key == "var":
            return self
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
        if self.children[1].key == 'char' and isinstance(self.children[1].value, str):
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
        self.width: int = 0

    def handle(self):
        warnings = []
        evaluate = True
        # replace all the arguments
        for i in range(len(self.args)):
            if isinstance(self.args[i], Node) and self.args[i].key == "string":
                continue
            last_register = self.children[i].register
            self.args[i] = self.children[i]
            self.args[i].register = last_register
        # if any children haven't been replaced yet
        for i in range(len(self.args)):
            if isinstance(self.args[i], Node) and self.args[i].key == "var":
                evaluate = False
                # search for the variable in the symbol table
                temp_symbol = self.symbolTable
                while temp_symbol is None:
                    temp_symbol = self.parent.symbolTable
                while not temp_symbol.exists(self.args[i].value) and temp_symbol.parent is not None:
                    temp_symbol = temp_symbol.parent
                if temp_symbol.exists(self.args[i].value):
                    matches = temp_symbol.lookup(self.args[i].value)
                    if len(matches) > 1:
                        raise Exception("Ambiguous variable name")
                    else:
                        self.args[i] = matches[0]
                        var_type = self.args[i].type
                        format_type = getTypeFromFormat(self.format_specifiers[i][-1])
                        if var_type == format_type:
                            continue
                        # check if the type of the variable matches
                        if (var_type, format_type) not in conversions:
                            raise Exception(f"No possible conversion from {var_type} to {format_type}")
                        if (var_type, format_type) not in conv_promotions:
                            # clang style warning
                            warnings.append(f"Format specifies type '{format_type}' but the argument has type '{var_type}'\n"
                                            f"Implicit conversion from '{var_type}' to '{format_type}'")
        if not evaluate:
            return self, warnings

        for i in range(len(self.format_specifiers)):
            current_specifier = self.format_specifiers[i]
            current_child = self.children[i]
            length = int(current_specifier[1:-1]) if current_specifier[1:-1].isdigit() else 0
            # check the child's type
            if current_specifier[-1] == 'd':
                # check if the child is a node
                if isinstance(current_child, VarNode):
                    if not current_child.type == 'int':
                        if current_child.type == 'float':
                            current_child.value = int(current_child.value)
                        elif current_child.type == 'char':
                            current_child.value = ord(current_child.value)
                        elif current_child.value is None:
                            current_child.value = random.randint(0, 10 ** length) if length > 0 else random.randint(0, 10)
                        else:
                            raise TypeError("Invalid type for printf")
                elif isinstance(current_child, Node):
                    if not isinstance(current_child.value, int):
                        if isinstance(current_child.value, float):
                            current_child.value = int(current_child.value)
                        elif isinstance(current_child.value, str) and len(current_child.value) == 1:
                            current_child.value = ord(current_child.value)
                        elif current_child.value is None:
                            current_child.value = random.randint(0,10**length) if length > 0 else random.randint(0, 10)
                        else:
                            raise TypeError("Invalid type for printf")
                if isinstance(current_child, VarNode):
                    current_child.type = "int"
                else:
                    current_child.key = "int"
            if current_specifier[-1] == 'i':
                # type can accept hexa, octal, decimal and binary
                if isinstance(current_child, VarNode):
                    if not current_child.type == 'int':
                        if current_child.type == 'float':
                            current_child.value = int(current_child.value)
                        elif current_child.type == 'char':
                            current_child.value = ord(current_child.value)
                        elif current_child.value is None:
                            current_child.value = random.randint(0, 10 ** length)
                        else:
                            raise TypeError("Invalid type for printf")
                elif isinstance(current_child, Node):
                    if not isinstance(current_child.value, int):
                        if isinstance(current_child.value, float):
                            current_child.value = int(current_child.value)
                        elif isinstance(current_child.value, str) and len(current_child.value) == 1:
                            current_child.value = ord(current_child.value)
                        elif current_child.value is None:
                            current_child.value = random.randint(0,10**length)
                        else:
                            raise TypeError("Invalid type for printf")

                if isinstance(current_child, VarNode):
                    current_child.type = "int"
                else:
                    current_child.key = "int"
            if current_specifier[-1] == 'c':
                if isinstance(current_child, VarNode):
                    if not current_child.type == 'char':
                        if current_child.type == 'float':
                            current_child.value = int(current_child.value)
                        elif current_child.value is None:
                            current_child.value = random.choice(string.ascii_letters)
                        else:
                            raise TypeError("Invalid type for printf")
                elif isinstance(current_child, Node):
                    if not isinstance(current_child.value, str) or len(current_child.value) != 1:
                        if isinstance(current_child.value, float):
                            current_child.value = int(current_child.value)
                        elif current_child.value is None:
                            current_child.value = random.choice(string.ascii_letters)
                        else:
                            raise TypeError("Invalid type for printf")

                if isinstance(current_child, VarNode):
                    if current_child.type == "char":
                        current_child.value = str(ord(current_child.value))
                else:
                    current_child.value = str(ord(current_child.value))
            if current_specifier[-1] == 'f':
                if isinstance(current_child, VarNode):
                    if not current_child.type == 'float':
                        if current_child.type == 'int':
                            current_child.value = array('f', [current_child.value])[0]
                        elif current_child.type == 'char':
                            current_child.value = array('f', [ord(current_child.value)])[0]
                        elif current_child.value is None:
                            current_child.value = random.uniform(0, 10 ** length)
                        else:
                            raise TypeError("Invalid type for printf")
                elif isinstance(current_child, Node):
                    if not isinstance(current_child.value, float):
                        if isinstance(current_child.value, int):
                            current_child.value = array('f', [current_child.value])[0]
                        elif isinstance(current_child.value, str) and len(current_child.value) == 1:
                            current_child.value = array('f', [ord(current_child.value)])[0]
                        elif current_child.value is None:
                            current_child.value = random.uniform(0, 10 ** length)
                        else:
                            raise TypeError("Invalid type for printf")

            if current_specifier[-1] == 's':
                if isinstance(current_child, VarNode):
                    if not current_child.type == 'char' or not current_child.array:
                        raise TypeError("Invalid type for printf")
                if isinstance(current_child, Node):
                    if current_child.value is None:
                        current_child.value = str(uuid.uuid1())
                    if not isinstance(current_child.value, str):
                        raise TypeError("Invalid type for printf")

            # check the length of format specifiers and child
            if length != 0:
                # convert child value to string
                if isinstance(current_child, Node):
                    if length > len(str(current_child.value)):
                        current_child.value = str(current_child.value).rjust(length, ' ')
        return self , warnings

    def llvm_global(self, index: int = 1) -> tuple[str, int]:
        out = ""
        extra_length = len(re.findall("\\\.*", self.format_string)) * 2
        out += f"@.str.{index} = private unnamed_addr constant [{len(self.format_string)+1 - extra_length} x i8] c\"{self.format_string}\\00\", align 1\n"
        # entry, length = self.getEntry(self.root)
        self.register = index
        index += 1
        for i in range(len(self.args)):
            if self.args[i].key == "string":
                extra_length = len(re.findall("\\\.*", self.args[i].value)) * 2
                out += f"@str.{index} = private unnamed_addr constant [{len(self.args[i].value)+1 - extra_length} x i8] c\"{self.args[i].value}\\00\", align 1\n"
                self.args[i].register = index
                self.children[i].register = index
                index += 1
        return out, index

    def updateRegisters(self):
        for i in range(len(self.args)):
            self.args[i].register = self.children[i].register

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        out = ""
        var_string = ""
        count = 0
        self.updateRegisters()
        for var in self.args:
            temp_type = getLLVMType(getType(var.value))

            if isinstance(var, Node):
                if var.key == "string":
                    temp_type = "ptr"
                var_string += f"{temp_type if temp_type != 'float' else 'double'} noundef {'@str.' if var.key == 'string' else ''}{var.register if var.register is not None else var.value}"
            else:
                entry, length = self.getEntry(var)
                var += f"{temp_type if temp_type != 'float' else 'double'} noundef %{entry.register}"
            if count + 1 != len(self.args):
                var_string += ', '
            count += 1
        out += f"call i32 (ptr, ...) @printf(ptr noundef @.str.{self.register if self.register is not None else ''}{', ' if len(var_string) > 0 else ''}{var_string})\n"
        return out, index

    def format(self):
        # Split the format string into a list of strings and format specifiers (e.g. "%s") but not \%[A-Za-z] but keep the string
        # so if \%s is found, it is not split
        # TODO: argument if variable -> take value of the variable else make string
        format_ = re.split(r'((?<!\\)%[A-Za-z])', self.format_string)
        # loop through list and check for valid format specifiers
        counter = -1
        for i in range(len(format_)):
            # if the string is a format specifier
            if format_[i].startswith('%'):
                counter += 1
                # remove the first character
                format_[i] = format_[i][1:]
                # if the first character is a number, it is the index of the argument to use
                # if the first character is a special character, it is a special format specifier
                # | Format Specifier | Output                                                       |
                # |------------------|--------------------------------------------------------------|
                # | `%10d`           | integer with a minimum width of 10 characters, right-aligned |
                # | `%-10s`          | string with a minimum width of 10 characters, left-aligned   |
                # | `%.2f`           | floating-point number with 2 decimal places of precision     |
                # | `%#x`            | hexadecimal integer with the `0x` prefix                     |
                # | `%+d`            | signed integer with a plus sign (+) for positive numbers     |
                # all valid specifiers
                left_align = False
                precision_valid = False
                precision = ""
                if format_[i][0] == '-':
                    left_align = True
                    format_[i] = format_[i][1:]
                elif format_[i][0] == '.':
                    # remove the dot
                    format_[i] = format_[i][1:]
                    # the next characters are the precision till the next character that is not a digit
                    for j in range(len(format_[i])):
                        if not format_[i][j].isdigit():
                            break
                        precision += format_[i][j]
                    # remove the precision from the format string
                    format_[i] = format_[i][len(precision):]
                    # convert the precision to an integer
                    precision = int(precision)
                    precision_valid = True
                if format_[i][0].isdigit():
                    # take the full integer as teh size
                    size_str = ""
                    for j in range(len(format_[i])):
                        if not format_[i][j].isdigit():
                            break
                        size_str += format_[i][j]
                    # remove the size from the format string
                    format_[i] = format_[i][len(size_str):]
                    # convert the size to an integer
                    self.width = int(size_str)
                # replace the format specifier with the argument
                # check first if the format specifier is in the list of valid specifiers
                if format_[i][0] in ['d', 'i', 'u', 'o', 'x', 'X', 'f', 'F', 'e', 'E', 'g', 'G', 'a', 'A', 'c', 's',
                                     'p',
                                     'n']:
                    # if the format specifier is a string
                    arg = self.args[counter]
                    # if the format specifier is an integer
                    if format_[i][0] in ['d', 'i', 'u', 'o', 'x', 'X']:
                        # if the precision is valid
                        if precision_valid:
                            format_[i] = arg
                            continue
                        # if the integer is shorter than the size
                        if len(str(arg)) < self.width:
                            # if the integer is left-aligned
                            if left_align:
                                # add spaces to the right of the integer
                                arg = str(arg) + " " * (self.width - len(str(arg)))
                            # if the integer is right-aligned
                            else:
                                # add spaces to the left of the integer
                                arg = " " * (self.width - len(str(arg))) + str(arg)
                        format_[i] = arg
                    # if the format specifier is a floating-point number
                    elif format_[i][0] in ['f', 'F', 'e', 'E', 'g', 'G', 'a', 'A']:
                        # if the precision is valid
                        if precision_valid:
                            # if the number after the dot is longer than the precision
                            if len(str(arg).split('.')[1]) > precision:
                                # truncate the number
                                arg = str(arg)[:precision]
                            format_[i] = arg
                            continue
                        # if the number is shorter than the size
                        if len(str(arg)) < self.width:
                            # if the number is left-aligned
                            if left_align:
                                # add spaces to the right of the number
                                arg = str(arg) + " " * (self.width - len(str(arg)))
                            # if the number is right-aligned
                            else:
                                # add spaces to the left of the number
                                arg = " " * (self.width - len(str(arg))) + str(arg)
                        format_[i] = arg
                    # if the format specifier is a character
                    elif format_[i][0] == 'c':
                        # if the precision is valid but is not float than continue
                        if precision_valid:
                            format_[i] = arg
                            continue
                        # if the character is shorter than the size
                        if len(str(arg)) < self.width:
                            # if the character is left-aligned
                            if left_align:
                                # add spaces to the right of the character
                                arg = str(arg) + " " * (self.width - len(str(arg)))
                            # if the character is right-aligned
                            else:
                                # add spaces to the left of the character
                                arg = " " * (self.width - len(str(arg))) + str(arg)
                        format_[i] = arg
                    # if the format specifier is a string
                    elif format_[i][0] == 's':
                        # if the precision is valid
                        if precision_valid:
                            format_[i] = arg
                            continue
                        # if the string is shorter than the size
                        if len(str(arg)) < self.width:
                            # if the string is left-aligned
                            if left_align:
                                # add spaces to the right of the string
                                arg = str(arg) + " " * (self.width - len(str(arg)))
                            # if the string is right-aligned
                            else:
                                # add spaces to the left of the string
                                arg = " " * (self.width - len(str(arg))) + str(arg)
                        format_[i] = arg
        return format_

    @staticmethod
    def getType(input):
        if type(input) == int:
            return 0
        elif type(input) == float:
            return 1
        elif type(input) == str:
            return 2

    def mips(self, registers: Registers):
        out_local = ""
        out_global = ""
        list_format = self.format()
        # check all strings in list_format and if they are not in the global objects add them
        for i in list_format:
            if i in registers.globalObjects.data[0].values():
                continue
            else:
                registers.globalObjects.data[0][i] = f"str_{len(registers.globalObjects.data[0])}"
        # now syscall the list format in the right order with the right names
        for i in range(len(list_format)):
            # load the right variable in $a0
            # out_local += f"la $a0, {registers.globalObjects.data[0][i]}\n"
            # out_local += "li $v0, 4\n"
            # out_local += "syscall\n"
            # change so it call the right print function
            if self.getType(i) == 0:
                out_local += f"li $a0, {i}\n"
                out_local += f"jal print_int\n"
            elif self.getType(i) == 1:
                out_local += f"li $a0, {i}\n"
                out_local += f"jal print_float\n"
            elif self.getType(i) == 2:
                out_local += f"la $a0, {registers.globalObjects.data[0][i]}\n"
                out_local += f"jal print_string\n"
        return out_local, out_global



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
                self.children[1].parent = self.children[0]
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
        out = ""
        return out, index


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
            if child.key == "var":
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
                if not self.children[0].parent.array:
                    raise AttributeError(f"\'Attempting to decrement a non-variable type object\'")
            node = self.children[0]
            if isinstance(node, VarNode):
                if node.const:
                    raise AttributeError(f"\'Attempting to modify a const variable {node.key}\'")
            else:
                if node.parent.const:
                    raise AttributeError(f"\'Attempting to modify a const variable {node.key}\'")
            node.value += 1
        elif self.root.value == "--":
            if len(self.children) != 1:
                raise RuntimeError(f"\'Expected one variable for increment operation, got multiple\'")
            if not isinstance(self.children[0], VarNode):
                if not self.children[0].parent.array:
                    raise AttributeError(f"\'Attempting to decrement a non-variable type object\'")
            node = self.children[0]
            if isinstance(node, VarNode):
                if node.const:
                    raise AttributeError(f"\'Attempting to modify a const variable {node.key}\'")
            else:
                if node.parent.const:
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
                if not self.children[0].parent.array:
                    raise AttributeError(f"\'Attempting to decrement a non-variable type object\'")
            node = self.children[0]
            if isinstance(node, VarNode):
                if node.const:
                    raise AttributeError(f"\'Attempting to modify a const variable {node.key}\'")
            else:
                if node.parent.const:
                    raise AttributeError(f"\'Attempting to modify a const variable {node.key}\'")
            node.value += 1
            return node
        elif self.root.value == "--":
            if len(self.children) != 1:
                raise RuntimeError(f"\'Expected one variable for increment operation, got multiple\'")
            if not isinstance(self.children[0], VarNode):
                if not self.children[0].parent.array:
                    raise AttributeError(f"\'Attempting to decrement a non-variable type object\'")
            node = self.children[0]
            if isinstance(node, VarNode):
                if node.const:
                    raise AttributeError(f"\'Attempting to modify a const variable {node.key}\'")
            else:
                if node.parent.const:
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
        if not isinstance(self.children[0], FuncParameter):
            child.parent = self.children[0]
        if isinstance(child, VarNode) and child.ptr and not isinstance(self.children[0], FuncParameter):
            child.deref_level += 1
        return child

class ArrayElementAST(AST):
    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)
        self.array: ArrayNode | None = None

    def handle(self):
        # update root value
        if len(self.children) == 2:
            if isinstance(self.children[1], Node):
                self.root.value = self.children[1].value
        # get nearest symbol table
        temp_symbol = self.symbolTable
        temp_parent = self.parent
        while temp_symbol is None and temp_parent is not None:
            temp_symbol = temp_parent.symbolTable
            temp_parent = temp_parent.parent
        if temp_symbol is None:
            raise AttributeError(f"Array {self.root.key} not found in symbol table")
        while not temp_symbol.exists(self.root.key):
            temp_symbol = temp_symbol.parent
            if temp_symbol is None:
                raise AttributeError(f"Array {self.root.key} not found in symbol table")
        matches = temp_symbol.lookup(self.root.key)
        if len(matches) != 1:
            raise AttributeError(f"Multiple definitions of array {self.root.key}")
        temp_symbol = matches[0]
        if self.root.value < 0 or self.root.value >= temp_symbol.size:
            raise AttributeError(f"Array index {self.root.value} out of bounds for array {self.root.key}")
        return temp_symbol.object.values[self.root.value]

    def save(self):
        # for printing purposes
        out = f"{self.root.key}[{self.root.value}]"
        return out


class Scope_AST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None, condition: AST | None = None):
        super().__init__(root, children, parent, symbolTable=SymbolTable())
        self.condition: AST | Node | None = condition
        self.symbolTable.owner = self

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
    def calculateStacksize(self):
        size = 0
        # calculate the size of the stack of the function
        for entry in self.symbolTable.table:
            if isinstance(entry.object, VarNode):
                if entry.object.ptr:
                    size += 4
                if entry.object.array:
                    size += 4 * entry.size
                else:
                    size += 4

        # calculate the size of the stack of the function parameters
        for entry in self.parent.symbolTable.table:
            if isinstance(entry.object, VarNode):
                if entry.object.ptr:
                    size += 4
                if entry.object.array:
                    size += 4 * entry.size
                else:
                    size += 4
        return size

    def mips(self, registers: Registers):
        visited = []
        not_visited = [self.children[0]]
        # DFS
        while len(not_visited) != 0:
            current = not_visited.pop()
            if current not in visited:
                visited.append(current)
                if not (isinstance(current, Scope_AST) or isinstance(current, FuncDefnAST) or isinstance(current, FuncCallAST)\
                        or isinstance(current, If_CondAST) or isinstance(current, While_loopAST) or isinstance(current, For_loopAST)\
                        or isinstance(current, FuncDeclAST)):
                    for i in current.children:
                        not_visited.append(i)
        out_local = out_global = ""
        size = self.calculateStacksize()
        size += 4
        # begin
        out_local += f"addi $sp, $sp, -{size}\n"
        out_local += f"sw $ra, {4}($sp)\n"

        # middle
        for current in visited:
            output = tuple
            if current.root.value in tokens:
                output = self.visitMIPSOp(current, registers)
            else:
                output = current.mips(registers)

        # end
        out_local += f"lw $ra, {4}($sp)\n"
        out_local += f"addi $sp, $sp, {size}\n"
        return out_local, out_global





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
        visited = visited_list_DFS(self.children[0])

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
    def mips(self, registers: Registers):
        out = ""
        # condition first
        visited = []
        not_visited = [self.condition]
        # DFS
        while len(not_visited) != 0:
            current = not_visited.pop()
            if current not in visited:
                visited.append(current)
                if not (isinstance(current, Scope_AST) or isinstance(current, FuncDefnAST) or isinstance(current, FuncCallAST)\
                        or isinstance(current, If_CondAST) or isinstance(current, While_loopAST) or isinstance(current, For_loopAST)\
                        or isinstance(current, FuncDeclAST)):
                    for i in current.children:
                        not_visited.append(i)
        out = f"if_{registers.globalObjects.index}: \n"
        self.register = registers.globalObjects.index
        registers.globalObjects.index += 1
        # TODO: stack size
        # TODO: condition
        for current in visited:
            output = tuple
            if current.root.value in tokens:
                output = self.visitMIPSOp(current, registers)
            else:
                output = current.mips(registers)
            out += output[0]
        # TODO: if block
        output = self.children[0].mips(registers)
        out += output[0]
        # TODO: add else block if exist
        # else block if exist
        # otherwise go back to the main block
        return out, ""


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
        visited = visited_list_DFS(self.children[0])
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

    def mips(self, registers: Registers):
        # # DFS
        # visited = []
        # not_visited = [self.children[0]]
        # while len(not_visited) > 0:
        #     current = not_visited.pop()
        #     visited.append(current)
        #     if not (isinstance(current, Scope_AST) or isinstance(current, FuncDeclAST) or isinstance(current, FuncCallAST)
        #             or isinstance(current, If_CondAST) or isinstance(current, Else_CondAST) or isinstance(current, For_loopAST)
        #             or isinstance(current, While_loopAST)):
        #         for i in current.children:
        #             not_visited.append(i)
        # # begin
        # # TODO: allocate space in stack for local variables
        # out = ""
        # for current in visited:
        #     output = current.mips(registers)
        #     out += output[0]
        # # end
        # # TODO: deallocate space in stack for local variables
        out = f"else_{self.register}: \n"
        output = self.children[0].mips(registers)
        out += output[0]
        return out, ""



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
        out += f"{name}: ; preds = %{blocks['2']}, %0\n"
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
        out += f"br i1 %{index}, label %{index2}, label %{index3}\n"
        return out, index

    def llvm_block2(self, out, index, blocks):
        name = blocks["2"]
        out += f"{name}: ; preds = %{blocks['1']}\n"

        # DFS
        visited = visited_list_DFS(self.children[0])

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
        out += f"br label %{index1}\n"
        return out, index

    @staticmethod
    def llvm_block3(out, index, blocks):
        name = blocks["3"]
        out += f"{name}: ; preds = %{blocks['1']}\n"
        # out += f"\t%ret i32 0\n"
        index += 1
        return out, index

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[Any, Any]:
        self.blocks = {"1": index, "2": index + 1, "3": index + 2}
        index += 2
        out = f"\tbr label %{index}\n\n"
        out, index = self.llvm_block1(out, index, self.blocks)
        out, index = self.llvm_block2(out, index, self.blocks)
        out, index = self.llvm_block3(out, index, self.blocks)
        return out, index

    def mips(self, registers: Registers):
        out = f"while_{registers.globalObjects.index}: \n"
        self.register = registers.globalObjects.index
        registers.globalObjects.index += 1
        # TODO: add the condition
        # TODO: add the body
        output = self.children[0].mips(registers)
        out += output[0]
        pass


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

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        blocks = self.searchBlocks()
        name = blocks["3"]
        out = f"br label %{name}"
        return out, index

    def mips(self, registers: Registers):
        pass


class ContAST(InstrAST):
    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        blocks = self.searchBlocks()
        name = blocks["1"]
        out = f"br label %{name}"
        return out, index

    def mips(self, registers: Registers):
        # get the name of it's block
        pass

class FuncParametersAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None, symbolTable: SymbolTable | None = None,
                 parameters: list[FuncParameter : None] = None):
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
        super().__init__(root, children, parent, symbolTable=SymbolTable() if symbolTable is None else symbolTable)
        self.symbolTable.owner = self
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

    def save_dot(self, dictionary_function: dict = None):
        return f"{'const ' if self.const else ''}{self.type}{'*'*self.ptr_level} {self.root.key} [label=\"{self.root.key}\"]\n"

    def getDict(self):
        return {f"{'const ' if self.const else ''}{self.type}{'*' * self.ptr_level} {self.root.key}": self.root.value}, \
            f"{'const ' if self.const else ''}{self.type}{'*' * self.ptr_level} {self.root.key}"

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        out = f""
        # Begin
        out += f"define dso_local {getLLVMType(self.type)} @{self.root.key}"
        # Parameters
        paramaters = self.params
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

    def mips(self, registers: Registers):
        return f"{self.root.key}:\n", f".globl {self.root.key}\n" if self.root.key == "main" else ""


class FuncDefnAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None, symbolTable: SymbolTable | None = None,
                 return_type: str = None, const: bool = False, ptr: bool = False, ptr_level: int = 0,
                 params=None):
        super().__init__(root, children, parent, symbolTable=SymbolTable() if symbolTable is None else symbolTable)
        self.symbolTable.owner = self
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
        out += f"\ndefine dso_local {getLLVMType(self.type)} @{self.root.key}"
        # Parameters
        parameters = self.params
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
        out += "\n"
        return out, index

    def mips(self, registers: Registers):
        out_local = f"{self.root.key}:\n"
        out_global = f".globl {self.root.key}\n" if self.root.key == "main" else ""
        # Begin
        # Parameters
        # TODO: Parameters
        # Body
        out_l, out_g = self.children[0].mips(registers)
        out_local += out_l
        out_global += out_g
        return out_local, out_global

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

    def mips(self, registers: Registers):
        out = ""
        # arguments
        arg_string = ""
        count = 0
        for arg in self.args:
            # TODO: add support for arguments
            pass
        # end string
        out += f"jal {self.root.key}\n"
        return out, ""



class FuncScopeAST(AST):
    def __init__(self, root: Node = None, children: list = None, parent=None, symbolTable: SymbolTable | None = None):
        super().__init__(root, children, parent, SymbolTable())
        self.symbolTable.owner = self.root.key

    def handle(self):
        return self

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        # DFS the whole scope and llvm every part of them
        visited = []
        has_return = False
        not_visited = [self]
        while len(not_visited) > 0:
            current = not_visited.pop()
            if current not in visited:
                if current is not self:
                    visited.append(current)
                if not isinstance(current, While_loopAST) or not isinstance(current, FuncDeclAST) \
                        or not isinstance(current, If_CondAST) \
                        or not isinstance(current, FuncDefnAST) and not isinstance(current, FuncScopeAST):
                    for i in current.children:
                        if not isinstance(i, Node):
                            not_visited.append(i)

        out = ""
        visited.reverse()
        for current in visited:
            if isinstance(current, ReturnInstr):
                has_return = True
            output = tuple
            if current.root.value in tokens:
                output = self.visitLLVMOp(current, index)
            else:
                output = current.llvm(True, index)
            out += output[0]
            index = output[1]
        if not has_return:
            ret_type = getLLVMType(self.parent.type)
            out += f"ret {ret_type if self.parent.type != 'void' else ''} {0 if self.parent.type != 'void' else '' } \n"
        out += "}\n"
        return out, index

    def calculateStackSize(self):
        size = 0
        # calculate the size of the stack of the function
        for entry in self.symbolTable.table:
            if isinstance(entry.object, VarNode):
                if entry.object.ptr:
                    size += 4
                if entry.object.array:
                    size += 4 * entry.size
                else:
                    size += 4

        # calculate the size of the stack of the function parameters
        for entry in self.parent.symbolTable.table:
            if isinstance(entry.object, VarNode):
                if entry.object.ptr:
                    size += 4
                if entry.object.array:
                    size += 4 * entry.size
                else:
                    size += 4
        return size
    def mips(self, registers: Registers):
        size = self.calculateStackSize()
        size += 4 # for the return address
        # Begin
        out_global = ""
        out_local = f"\taddi $sp, $sp, -{size}\n"
        out_local += "\tsw $ra, 4($sp)\n"
        # TODO: add the function body
        # DFS
        visited = []
        not_visited = [self]
        while len(not_visited) > 0:
            current = not_visited.pop()
            if current not in visited:
                if current is not self:
                    visited.append(current)
                if not isinstance(current, While_loopAST) or not isinstance(current, FuncDeclAST) \
                    or not isinstance(current, If_CondAST) \
                    or not isinstance(current, FuncDefnAST) and not isinstance(current, FuncScopeAST):
                    for i in current.children:
                        if not isinstance(i, Node):
                            not_visited.append(i)

        for current in visited:
            output = tuple
            if current.root.value in tokens:
                output = self.visitMIPSOp(current, registers)
            else:
                output = current.mips(registers)
            out_local += output[0]
            out_global += output[1]

        # End
        out_local += "\tlw $ra, -4($sp)\n"
        out_local += f"\taddi $sp, $sp, {size}\n"
        out_local += "\tjr $ra\n"
        return out_local, out_global

class ReturnInstr(InstrAST):
    def __init__(self, root: Node = None, children: list = None, parent=None):
        super().__init__(root, children, parent)

    def handle(self):
        return self

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        out = ""
        temp_type = ""
        child = self.children[0]
        if isinstance(child, Node):
            temp_type = getLLVMType(child.key)
            if temp_type == "float":
                temp_type = "double"
            out += f"ret {temp_type if child.key is not None else 'i32'} {child.value if child.value is not Node else 0}\n"
        elif isinstance(child, VarNode):
            temp_type = getLLVMType(child.key)
            entry, length = self.getEntry(child)
            out += f"%{index} = load {temp_type}, {temp_type} %{entry.register}, align {'4' if not child.ptr else '8'}\n"
            out += f"ret {temp_type} %{entry.register}\n"
        return out, index

    def mips(self, registers: Registers):
        pass

class ScanfAST(AST):

    def __init__(self, root: Node = None, children: list = None, parent=None, symbolTable: SymbolTable | None = None):
        super().__init__(root, children, parent, symbolTable)
        self.variables = []
        self.format_string = None
        self.format_specifiers = []
        self.width: int = 0

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

    def mips(self, registers: Registers):
        # scanf in mips
        # format the format string
        # ask for input depending on the format string, so different syscall for different types
        # store the input in the variables (registers that are assigned to the variables)
        # check if the completed format string is correct
        pass

class ArrayDeclAST(AST):
    def __init__(self, root: Node = None, children: list = None, parent=None, symbolTable: SymbolTable | None = None,
                 size: int = 0, ptr_size: int = 0, arr_type: str = None, values=None):
        super().__init__(root, children, parent, symbolTable)
        if values is None:
            values = []
        self.size = size
        self.values = values
        self.ptr_size = ptr_size
        self.type = arr_type

    def handle(self):
        return self

    def save(self):
        if len(self.children) > 0:
            if isinstance(self.children[0], ArrayNode):
                return self.children[0].save()
            else:
                return super().save()
        else:
            return super().save()

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

    def mips(self, registers: Registers):
        pass


class IncludeAST(AST):
    def __init__(self, root: Node = None, children: list = None, parent=None, symbolTable: SymbolTable | None = None):
        super().__init__(root, children, parent, symbolTable)

    def getDict(self):
        return {f"#include<{self.root.key}>": self.root.value}, f"#include<{self.root.key}>"

    def handle(self):
        return self

    def llvm(self, scope: bool = False, index: int = 1) -> tuple[str, int]:
        pass

    def llvm_global(self, index: int = 1) -> tuple[str, int]:
        return f"declare i32 @printf(ptr noundef, ...) #2\n\ndeclare i32 @__isoc99_scanf(ptr noundef, ...) #2\n\n", index

    def mips(self, registers: Registers):
        # hardcode the printf and scanf functions
        # printf for int
        out_local = "printf_int:\n"
        out_local += "li $v0, 1\n"
        out_local += "syscall\n"
        out_local += "jr $ra\n\n"
        # printf for string
        out_local += "printf_string:\n"
        out_local += "li $v0, 4\n"
        out_local += "syscall\n"
        out_local += "jr $ra\n\n"
        # printf for char
        out_local += "printf_char:\n"
        out_local += "li $v0, 11\n"
        out_local += "syscall\n"
        out_local += "jr $ra\n\n"
        # printf for float
        out_local += "printf_float:\n"
        out_local += "li $v0, 2\n"
        out_local += "syscall\n"
        out_local += "jr $ra\n\n"
        # scanf for int
        out_local += "scanf_int:\n"
        out_local += "li $v0, 5\n"
        out_local += "syscall\n"
        out_local += "jr $ra\n\n"
        # scanf for string
        out_local += "scanf_string:\n"
        out_local += "li $v0, 8\n"
        out_local += "syscall\n"
        out_local += "jr $ra\n\n"
        # scanf for char
        out_local += "scanf_char:\n"
        out_local += "li $v0, 12\n"
        out_local += "syscall\n"
        out_local += "jr $ra\n\n"
        # scanf for float
        out_local += "scanf_float:\n"
        out_local += "li $v0, 6\n"
        out_local += "syscall\n"
        out_local += "jr $ra\n\n"
        return out_local, ""
