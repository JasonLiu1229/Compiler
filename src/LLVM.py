from array import array

import numpy

from AST import *
from struct import *
from decimal import *
import numpy as np


class LLVM:

    # TODO: var_node
    # TODO: AST

    def __init__(self, input_ast: AST = None, symbol_table=None, file_name: str = "../Output/Output.ll") -> None:
        """
        :type input_ast: object AST, default value None
        """
        super().__init__()
        self.ast = input_ast
        self.nodes = list()
        self.symbol_table = symbol_table
        self.file_name = file_name

    def var_node_convert(self, node: VarNode, scope_toggle: bool):
        with open(self.file_name, 'a') as f:
            var_type = ""
            ll_string = ""
            if not scope_toggle and node.const:
                return ""
            if scope_toggle or node.const:  # true global @
                ll_string += "@" + str(node.key) + " = "
            else:  # false local %
                ll_string += "\t%" + str(node.key) + " = "
            # const or global
            if node.const:
                ll_string += "constant "
            elif scope_toggle:
                ll_string += "global "
            elif not scope_toggle:
                ll_string += "alloca "
            # get type
            if node.type == "int":
                var_type = "i32"
            elif node.type == "char":
                var_type = "i8"
            elif node.type == "float":
                var_type = "float"  # We had problems getting the exact decimal representation of our floats, so we're using doubles now
            ll_string += var_type
            if node.ptr:
                ll_string += "*" * node.total_deref
            else:
                ll_string += " "
            # allocate the value
            if not scope_toggle:
                ll_string += "\n\t"
            while isinstance(node.value, Node):
                node = node.value
            else:
                # match type
                if not scope_toggle and not node.const:
                    ll_string += "store " + var_type + " "
                    if isinstance(node.value, float):
                        val = array('f', [node.value])
                        ll_string += str(val[0])
                    elif isinstance(node.value , str):
                        ll_string += str(ord(node.value))
                    else:
                        ll_string += str(node.value)
                    ll_string += "," + var_type + "* %" + str(node.key) + "\n"
                else:
                    if isinstance(node.value , float):
                        val = array('f', [node.value])
                        ll_string += str(val[0]) + "\n"
                    else:
                        ll_string += str(node.value) + "\n"
            ll_string += "\n"
            return ll_string

    def functionNodeConvert(self, func: FunctionNode , declr : bool = False , defn: bool = False ,
                            glob_decl : bool = False , index: int = 0):
        # Output string , declared as empty
        ll_out = ""
        # Write the llvm code
        if declr:
            with open(self.file_name, 'a') as f:
                if func.key == "printf":
                    f.write("declare i32 @printf(i8*, ...)\n\n")
        if glob_decl:
            with open(self.file_name, 'a') as f:
                print_val = ""
                # Check the function name
                if func.key == "printf":
                    # Get the function parameters
                    print_val = func.value["par0"]
                    # Define our string
                    std_decl = "@.str" + str(index) + " = private unnamed_addr constant [" + str(len(str(print_val.value))) + " x i8] c" \
                               + "\""
                    if isinstance(print_val , VarNode):
                        if print_val.type == "int":
                            std_decl += "%d\\00\""
                        elif print_val.type == "float":
                            std_decl += "%f\\00\""
                    else:
                        if print_val.key == "int":
                            std_decl += "%d\\00\""
                        elif print_val.key == "float":
                            std_decl += "%f\\00\""

                    ll_out += std_decl + "\n\n"
                f.write(ll_out)
        if defn:
            if func.body is not None:
                pass
        else:
            """
                ; print message 1
                %str_ptr = getelementptr inbounds ([13 x i8], [13 x i8]* @.str, i64 0, i64 0)
                call i32 @printf(i8* %str_ptr)
            """
            # Get the function parameters
            print_val = func.value["par0"]
            # Comment about what it does
            ll_out += "\t;print " + str(index) + "\n"
            # Assign pointers of the correct type for local variables
            ptr1 = "\t%ptr" + str(index) + " = getelementptr inbounds  ([" + str(len(str(print_val.value))) + " x i8], " \
                   + "[" + str(len(str(print_val.value))) + " x i8]*" + "@.str" + str(index)
            # check type of printed variable
            if print_val.key == "int" or print_val.key == "float":
                ptr1 += ", i64 0 , i64 0)"
            ll_out += ptr1 + "\n"
            return ll_out

    def ast_convert(self, ast: AST):
        list1 = [self.ast]
        check = True
        while check:
            for child in list1:
                if isinstance(child, AST):
                    index = list1.index(child)
                    list1.remove(child)
                    for _child in child.children:
                        list1.insert(index, _child)
            check = False
            for child in list1:
                if isinstance(child, AST):
                    check = True
        list1.reverse()
        # for child in list1:
        #     if isinstance(child, FunctionNode):
        #         self.functionNodeConvert(child)
        #     elif isinstance(child, VarNode):
        #         self.var_node_convert(child, False)  # True : Global False : Local
        self.nodes = list1

    def type_checker(self):
        pass

    def convertNode(self, input_node : Node , global_scope : bool = False , index: int = 0):
        with open(self.file_name , 'a') as f:
            if isinstance(input_node , VarNode):
                f.write(self.var_node_convert(input_node , global_scope))
            elif isinstance(input_node , FunctionNode):
                f.write(self.functionNodeConvert(input_node , index=index))
                index += 1
        return index

    def convert(self):
        # clear file
        open(self.file_name, 'w')
        for val in self.symbol_table.values():
            if isinstance(val , VarNode):
                self.var_node_convert(val, True)
            elif isinstance(val , list):
                i = 0
                defn = True
                declr = True
                for entry in val:
                    if isinstance(entry , FunctionNode):
                        self.functionNodeConvert(entry , declr=declr , defn=defn , glob_decl=True , index=i)
                        i += 1
                        defn = False
                        declr = False
        # begin of main function
        with open(self.file_name, 'a') as f:
            f.write("define i32 @main () {\n")

        self.ast_convert(self.ast)
        i = 0
        for node in self.nodes:
            i = self.convertNode(node , False , index=i)

        # end of main
        with open(self.file_name, 'a') as f:
            f.write("\tret i32 0\n}")

    def execute(self):
        pass
