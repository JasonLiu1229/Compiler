from array import array

import numpy

from AST import *
from struct import *
from decimal import *
import numpy as np
class LLVM:

    # TODO: var_node
    # TODO: AST

    def __init__(self, input_ast: AST = None, symbol_table = None , file_name: str = "../Output/Output.ll") -> None:
        """
        :type input_ast: object AST, default value None
        """
        super().__init__()
        self.ast = input_ast
        self.symbol_table = symbol_table
        self.file_name = file_name

    def var_node_convert(self, node: VarNode, scope_toggle: bool):
        with open(self.file_name, 'a') as f:
            var_type = ""
            ll_string = "\t"
            if scope_toggle:  # true global @
                ll_string += "@" + str(node.key) + " = "
            else:  # false local %
                ll_string += "%" + str(node.key) + " = "
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
                var_type = "float"     # We had problems getting the exact decimal representation of our floats, so we're using doubles now
            ll_string += var_type
            if node.ptr:
                ll_string += "*" * node.total_deref
            else:
                ll_string += " "
            # allocate the value
            if not scope_toggle:
                ll_string += "\n\t"
            while isinstance(node.value , Node):
                ll_string += node.get_str() + "\n"
            else:
                # match type
                if not scope_toggle and not node.const:
                    ll_string += "store " + var_type + " "
                    if isinstance(node.value , float):
                        val = array('f' , [node.value])
                        ll_string += str(val[0])
                    else:
                        ll_string += str(node.value)
                    ll_string += "," + var_type + "* %" + str(node.key) + "\n"
                else:
                    ll_string += str(node.value) + "\n"

            f.write(ll_string)

    def ast_convert(self, ast: AST):
        pass

    def type_checker(self):
        pass

    def convert(self):
        # clear file
        open(self.file_name, 'w')
        # begin of main function
        with open(self.file_name, 'a') as f:
            f.write("define i32 @main () {\n")
        for node in self.symbol_table.values():
            self.var_node_convert(node, False)

        # end of main
        with open(self.file_name, 'a') as f:
            f.write("\tret i32 0\n}")

    def execute(self):
        pass
