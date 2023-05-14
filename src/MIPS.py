import os

from register_management import *
from SymbolTable import *
from AST import *


class MIPS:
    """
    Converts AST of C language to MIPS
    """
    def __init__(self, in_ast, in_file: str = "out.asm"):
        self.ast = in_ast
        self.nodes = []
        self.mips = in_file
        self.registers = Registers()

    def mips_dfs(self):
        # returns a list with all the AST in the tree in DFS order to convert to MIPS
        visited = []
        not_visited = [self.ast]
        while len(not_visited) > 0:
            temp = not_visited.pop()
            if temp not in visited:
                # if a scope, skip
                # if include instruction, skip
                if isinstance(temp, FuncDeclAST) or isinstance(temp, FuncDefnAST) or isinstance(temp, ScanfAST) or isinstance(temp, ArrayDeclAST) or \
                        isinstance(temp, IncludeAST):
                    visited.append(temp)
                if isinstance(temp, AST):
                    for child in temp.children:
                        not_visited.append(child)
        visited.reverse()
        self.nodes = visited
        return visited

    def convert(self):
        """
        Converts AST to MIPS
        """
        self.mips_dfs()
        global_str = local_str = variables = ""
        # global_str += self.allocate_stack()
        # global_str += self.deallocate_stack()
        with open(self.mips, "w") as f:
            for node in self.nodes:
                new_loc, new_glob, new_list = node.mips(self.registers)
                global_str += new_glob
                local_str += new_loc
            variables += "\t.data\n"
            for key, value in self.registers.globalObjects.data[0].items():
                variables += f"\t{value}: .asciiz \"{key}\"\n"
            for key, value in self.registers.globalObjects.data[1].items():
                variables += f"\t{value}: .float \"{key}\"\n"
            variables += ".text\n"
            f.write(variables)
            f.write(global_str)
            f.write(local_str)
        print("MIPS code generated in " + self.mips)

    def execute(self, execute_with: str = "Mars"):
        """
        Executes the MIPS code with Mars as default, but can be changed to SPIM
        :param execute_with: "Mars" or "SPIM"
        """
        if execute_with == "Mars":
            os.system("java -jar ../Help/Mars4_5_Mod.jar " + self.mips)
        elif execute_with == "SPIM":
            os.system("spim -file " + self.mips)
        else:
            print("Invalid execution method")

    @staticmethod
    def add(rReg: str, op1: str, op2: str):
        return f"add {rReg}, {op1}, {op2}"

    @staticmethod
    def addi(rReg: str, op1: str, op2: str):
        return f"addi {rReg}, {op1}, {op2}"

    @staticmethod
    def sub(rReg: str, op1: str, op2: str):
        return f"sub {rReg}, {op1}, {op2}"

    @staticmethod
    def mul(rReg: str, op1: str, op2: str):
        return f"mul {rReg}, {op1}, {op2}"

    @staticmethod
    def div(rReg: str, op1: str, op2: str):
        return f"div {rReg}, {op1}, {op2}"

    @staticmethod
    def and_(rReg: str, op1: str, op2: str):
        return f"and {rReg}, {op1}, {op2}"

    @staticmethod
    def or_(rReg: str, op1: str, op2: str):
        return f"or {rReg}, {op1}, {op2}"

    @staticmethod
    def xor(rReg: str, op1: str, op2: str):
        return f"xor {rReg}, {op1}, {op2}"

    @staticmethod
    def nor(rReg: str, op1: str, op2: str):
        return f"nor {rReg}, {op1}, {op2}"

    @staticmethod
    def slt(rReg: str, op1: str, op2: str):
        return f"slt {rReg}, {op1}, {op2}"

    @staticmethod
    def sll(rReg: str, op1: str, op2: str):
        return f"sll {rReg}, {op1}, {op2}"

    @staticmethod
    def srl(rReg: str, op1: str, op2: str):
        return f"srl {rReg}, {op1}, {op2}"

    @staticmethod
    def sra(rReg: str, op1: str, op2: str):
        return f"sra {rReg}, {op1}, {op2}"

    @staticmethod
    def lw(rReg: str, op1: str, op2: str):
        return f"lw {rReg}, {op1}({op2})"

    @staticmethod
    def sw(rReg: str, op1: str, op2: str):
        return f"sw {rReg}, {op1}({op2})"

    @staticmethod
    def beq(rReg: str, op1: str, op2: str):
        return f"beq {rReg}, {op1}, {op2}"

    @staticmethod
    def bne(rReg: str, op1: str, op2: str):
        return f"bne {rReg}, {op1}, {op2}"

    @staticmethod
    def j(op1: str):
        return f"j {op1}"

    @staticmethod
    def jr(rReg: str):
        return f"jr {rReg}"

    @staticmethod
    def jal(op1: str):
        return f"jal {op1}"

    @staticmethod
    def syscall():
        return "syscall"

    @staticmethod
    def label(label: str):
        return f"{label}:"

    @staticmethod
    def li(rReg: str, op1: str):
        return f"li {rReg}, {op1}"

    @staticmethod
    def la(rReg: str, op1: str):
        return f"la {rReg}, {op1}"

    @staticmethod
    def move(rReg: str, op1: str):
        return f"move {rReg}, {op1}"

    @staticmethod
    def mfhi(rReg: str):
        return f"mfhi {rReg}"

    @staticmethod
    def mflo(rReg: str):
        return f"mflo {rReg}"

    @staticmethod
    def nop():
        return "nop"

    @staticmethod
    def allocate_stack():
        # Allocate every register to stack
        out = "allocate_stack:\n"
        out += f"\taddi $sp, $sp, -100\n"
        count = 0
        for i in range(2,32):
            if i in [26, 27, 28, 29, 30]:
                count += 1
                continue
            out += f"\tsw ${i}, {(i - count)*4}($sp)\n"
        # jump back to function
        out += f"\tjr $ra\n\n"
        return out

    @staticmethod
    def deallocate_stack():
        # Deallocate every register from stack
        out = "deallocate_stack:\n"
        count = 0
        for i in range(2,32):
            if i in [26, 27, 28, 29, 30]:
                count += 1
                continue
            out += f"\tlw ${i}, {(i - count)*4}($sp)\n"
        out += f"\taddi $sp, $sp, 100\n"
        # jump back to function
        out += f"\tjr $ra\n\n"
        return out