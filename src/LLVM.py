from AST import *

class LLVM:

    # TODO: var_node
    # TODO: AST
    def __init__(self, input_ast: AST = None, file_name: str = "Output.ll") -> None:
        """
        :type input_ast: object AST, default value None
        """
        super().__init__()
        self.ast = input_ast
        self.file_name = file_name

    def var_node_convert(self, node: VarNode, scope_toggle: bool):
        with open(self.file_name, 'a') as f:
            ll_string = ""
            if scope_toggle:  # true global @
                ll_string = "@" + node.key + " = "
            else:  # false local %
                ll_string = "%" + node.key + " = alloca "
            if node.const:
                ll_string += "constant "
            if node.type == "int":
                ll_string += "i32"
            elif node.type == "char":
                ll_string += "i8"
            elif node.type == "float":
                ll_string += "float"
            if node.ptr:
                ll_string += "*" * node.total_deref
            else:
                ll_string += " "
            ll_string += node.value
            f.write(ll_string)

    def ast_convert(self, ast: AST):
        pass

    def type_checker(self):
        pass

    def convert(self):
        pass

    def execute(self):
        pass
