import queue
import subprocess
from array import array
from AST import *
from struct import *
from decimal import *


class LLVM:

    def __init__(self, input_ast: AST = None, symbol_table=None, file_name: str = "../Output/Output.ll") -> None:
        """
        :type input_ast: object AST, default value None
        """
        super().__init__()
        self.ast = input_ast
        self.nodes = list()
        self.symbol_table = symbol_table
        self.file_name = file_name
        self.index_queue = []

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
                var_type = "float"
            ll_string += var_type
            if node.ptr:
                ll_string += "*" * node.total_deref
            else:
                ll_string += " "
            # allocate the value
            if not scope_toggle:
                ll_string += "\n"
            while isinstance(node.value, Node):
                node = node.value
            else:
                # match type
                if node.value is None:
                    if node.type == "int":
                        node.value = 0
                    elif node.type == "float":
                        node.value = 0.0
                    elif node.type == "char":
                        node.value = ord('\0')
                if not scope_toggle and not node.const:
                    ll_string += "\tstore " + var_type + " "
                    if isinstance(node.value, float):
                        val = array('f', [node.value])
                        node.value = val[0]
                        ll_string += str(val[0])
                    elif isinstance(node.value , str):
                        ll_string += str(ord(node.value))
                    else:
                        ll_string += str(node.value)
                    ll_string += "," + var_type + "* %" + str(node.key) + "\n"
                else:
                    if isinstance(node.value , float):
                        val = array('f', [node.value])
                        node.value = val[0]
                        ll_string += str(val[0]) + "\n"
                    elif isinstance(node.value , str):
                        ll_string += str(ord(node.value))
                    else:
                        ll_string += str(node.value) + "\n"
            ll_string += "\n"
            if node.const or scope_toggle:
                open(self.file_name , 'a').write(ll_string)
            return ll_string

    def printf_int(self, value : int, index : int = 0):
        #   %1 = alloca i32, align 4
        #   store i32 value, ptr %1, align 4
        #   %2 = load i32, ptr %1, align 4
        #   %3 = call i32 (ptr, ...) @printf(ptr noundef @.str, i32 noundef %2)
        out = ""
        out += '\t%' + str(index) + "= alloca i32, align 4 \n"
        out += "\tstore i32 " + str(value) + ", ptr %" + str(index) + ", align 4 \n"
        out += '\t%' + str(index + 1) + "= load i32, ptr %" + str(index) + ", align 4 \n"
        index += 1
        out += '\t%' + str(index + 1) + "= call i32 (ptr, ...) @printf(ptr noundef @.str" + str(self.index_queue[0]) + \
               ", i32 noundef %" + str(index) + ')\n'
        index += 1
        self.index_queue.remove(self.index_queue[0])
        return out, index

    def printf_float(self, val: float , index : int = 1):
        """
        define dso_local i32 @main() #0 {
          %1 = alloca float, align 4
          store float 1.600000e+01, ptr %1, align 4
          %2 = load float, ptr %1, align 4
          %3 = fpext float %2 to double
          %4 = call i32 (ptr, ...) @printf(ptr noundef @.str, double noundef %3)
          ret i32 0
        }
        :param val:
        :param index:
        :return:
        """
        ll_out = ""
        # allocate the float parameter variable
        ll_out += "\t%" + str(index) + " = alloca float, align 4\n"
        # store the float value
        ll_out += "\tstore float " + str(val) + ", ptr %" + str(index) + ", align 4\n"
        index += 1
        ll_out += "\t%" + str(index) + " = load float, ptr %" + str(index-1) + ", align 4\n"
        index += 1
        ll_out += "\t%" + str(index) + " = fpext float %" + str(index-1) + " to double\n"
        index += 1
        ll_out += "\t%" + str(index) + " = call i32 (ptr, ...) @printf(ptr noundef @.str" + str(self.index_queue[0]) + ", double noundef %" \
                  + str(index-1) + ")\n"
        index += 1
        self.index_queue.remove(self.index_queue[0])
        return ll_out , index

    def printf_char(self, val: str , index : int = 1):
        """
            define dso_local i32 @main() #0 {
                %1 = alloca i8, align 1
                store i8 16, ptr %1, align 1
                %2 = load i8, ptr %1, align 1
                %3 = sext i8 %2 to i32
                %4 = call i32 (ptr, ...) @printf(ptr noundef @.str, i32 noundef %3)
                ret i32 0
            }
                :param val:
                :param index:
                :return:
                """
        ll_out = ""
        # allocate the float parameter variable
        ll_out += "\t%" + str(index) + " = alloca float, align 1\n"
        # store the float value
        ll_out += "\tstore i8 " + str(ord(val)) + ", ptr %" + str(index) + ", align 1\n"
        index += 1
        ll_out += "\t%" + str(index) + " = load i8, ptr %" + str(index - 1) + ", align 1\n"
        index += 1
        ll_out += "\t%" + str(index) + " = sext i8 %" + str(index - 1) + " to i32\n"
        index += 1
        ll_out += "\t%" + str(index) + " = call i32 (ptr, ...) @printf(ptr noundef @.str" + str(
            self.index_queue[0]) + ", i32 noundef %" \
                  + str(index - 1) + ")\n"
        index += 1
        self.index_queue.remove(self.index_queue[0])
        return ll_out, index

    @staticmethod
    def sub(type: str, op1: str, op2: str):
        return f"sub nsw {type} {op1}, {op2}"

    @staticmethod
    def mul(type, op1, op2):
        return f"mul nsw {type} {op1}, {op2}"

    @staticmethod
    def add(type: str, op1: str, op2: str):
        return f"add nsw {type} {op1}, {op2}"

    @staticmethod
    def sdiv(type: str, op1: str, op2: str):
        return f"sdiv {type} {op1}, {op2}"

    @staticmethod
    def udiv(type: str, op1: str, op2: str):
        return f"udiv {type} {op1}, {op2}"

    @staticmethod
    def mod(type: str, op1: str, op2: str):
        return f"urem {type} {op1}, {op2}"

    @staticmethod
    def incr(type: str, op: str):
        return LLVM.add(type, op, "1")

    @staticmethod
    def decr(type: str, op: str):
        return LLVM.sub(type, op, "1")

    @staticmethod
    def comp_gt(type: str, op1: str, op2: str):
        return f'icmp sgt {type} {op1}, {op2}'

    @staticmethod
    def comp_lt(type: str, op1: str, op2: str):
        return f'icmp slt {type} {op1}, {op2}'

    @staticmethod
    def comp_eq(type: str, op1: str, op2: str):
        return f'icmp eq {type} {op1}, {op2}'

    @staticmethod
    def comp_leq(type: str, op1: str, op2: str):
        return f'icmp sle {type} {op1}, {op2}'

    @staticmethod
    def comp_geq(type: str, op1: str, op2: str):
        return f'icmp sge {type} {op1}, {op2}'

    @staticmethod
    def comp_neq(type: str, op1: str, op2: str):
        return f'icmp ne {type} {op1}, {op2}'

    @staticmethod
    def and_op(type: str, op1: str, op2: str):
        return f"and {type} {op1}, {op2}"

    @staticmethod
    def or_op(type: str, op1: str, op2: str):
        return f"or {type} {op1}, {op2}"

    @staticmethod
    def not_op(type: str, op: str):
        return f"not {type} {op}"

    @staticmethod
    def assign(type: str, value, ptr):
        return f"store {type} {value}, {type}* {ptr}"

    def functionNodeConvert(self, func: FunctionNode , declr : bool = False , defn: bool = False ,
                            glob_decl : bool = False , index_local: int = 1, index_global: int = 1):
        # Output string , declared as empty
        ll_out = ""
        # Write the llvm code
        if declr:
            with open(self.file_name, 'a') as f:
                if func.key == "printf":
                    f.write("declare i32 @printf(ptr noundef, ...)\n\n")
        if glob_decl:
            with open(self.file_name, 'a') as f:
                print_val = ""
                # Check the function name
                if func.key == "printf":
                    # Get the function parameters
                    print_val = func.value["par0"]
                    # Define our string
                    std_decl = "@.str" + str(index_global) + " = private unnamed_addr constant ["
                    std_decl += '4'
                    std_decl += " x i8] c" + "\""
                    if isinstance(print_val , VarNode):
                        if print_val.type == "int":
                            std_decl += "%d\\0A\\00\""
                        elif print_val.type == "float":
                            std_decl += "%f\\0A\\00\""
                        elif print_val.type == "char":
                            std_decl += "%c\\0A\\00\""
                    else:
                        if print_val.key == "int":
                            std_decl += "%d\\0A\\00\""
                        elif print_val.key == "float":
                            std_decl += "%f\\0A\\00\""
                        elif print_val.type == "char":
                            std_decl += "%c\\0A\\00\""

                    ll_out += std_decl + " align 1\n\n"
                f.write(ll_out)
                return index_global
        if defn:
            if func.body is not None:
                pass
        else:
            # Get function parameters
            print_val = func.value["par0"]
            """
            # ll_out += "\t; load the value of @" + print_val.key + "\n\n"
            # Comment about what it does
            ll_out += "\t;print par" + str(index) + "\n"
            # Assign pointers of the correct type for local variables
            ptr1 = "\t%ptr" + str(index) + " = getelementptr inbounds  ["
            if isinstance(print_val.value, str):
                ptr1 += str(len(print_val.value))
            else:
                ptr1 += '4'
            ptr1 += " x i8], ["
            if isinstance(print_val.value, str):
                ptr1 += str(len(print_val.value))
            else:
                ptr1 += '4'
            ptr1 += " x i8]* " + "@.str" + str(index) + ' , '
            # check type of printed variable
            if isinstance(print_val , VarNode) and print_val.type == "int" or print_val.type == "float" :
                ptr1 += "i64 0 , i64 0"
            elif print_val.key == "int" or print_val.key == "float":
                ptr1 += "i64 0 , i64 0"
            # Call printf
            ll_out += ptr1 + "\n"
            ll_out += "\tcall i32 (i8*, ...) @printf(i8* %ptr" + str(index) + " , i8* %ptr" + str(index) + ")\n"
            """
            if isinstance(print_val.value , float):
                ret = self.printf_float(print_val.value, index_local)
                ll_out += ret[0]
                index_local = ret[1]
            elif isinstance(print_val.value , int):
                ret = self.printf_int(print_val.value, index_local)
                ll_out += ret[0]
                index_local = ret[1]
            elif isinstance(print_val.value , str):
                ret = self.printf_char(print_val.value, index_local)
                ll_out += ret[0]
                index_local = ret[1]
            return ll_out , index_local

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

    def convertNode(self, input_node : Node , global_scope : bool = False , index: int = 1) -> int:
        with open(self.file_name , 'a') as f:
            # if isinstance(input_node , VarNode):
            #     f.write(self.var_node_convert(input_node , global_scope))
            if isinstance(input_node , FunctionNode):
                if len(self.index_queue) == 0:
                    self.index_queue.append(index)
                ret = self.functionNodeConvert(input_node, index_local=index)
                f.write(ret[0])
                # self.index_queue.insert(0, ret[1])
                index = ret[1]
        return index

    def convert(self):
        # clear file
        f = open(self.file_name, 'w')
        glob_index = []
        for val in self.symbol_table.values():
            if isinstance(val , VarNode):
                self.var_node_convert(val, True)
            elif isinstance(val , list):
                i = 1
                defn = True
                declr = True
                for entry in val:
                    if isinstance(entry , FunctionNode):
                        self.index_queue.append(i)
                        i = self.functionNodeConvert(entry, declr=declr, defn=defn, glob_decl=True, index_global=i) + 1
                        defn = False
                        declr = False
        # begin of main function
        with open(self.file_name, 'a') as f:
            f.write("define dso_local i32 @main () {\n")

        self.ast_convert(self.ast)
        i = 1
        for node in self.nodes:
            i = self.convertNode(node , False , index=i)

        # end of main
        with open(self.file_name, 'a') as f:
            f.write("\tret i32 0\n}")

    def execute(self):
        subprocess.run(["lli" , "-opaque-pointers", self.file_name])