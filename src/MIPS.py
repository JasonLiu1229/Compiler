from register_management import *

class MIPS:
    """
    Converts AST of C language to MIPS
    """
    def __init__(self, in_ast, in_file: str = "out.asm"):
        self.ast = in_ast
        self.mips = in_file
        self.registers = Registers()

    def convert(self):
        """
        Converts AST to MIPS
        """
        with open(self.mips, "w") as f:
            pass
        pass

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
    def lw(rReg: str, op1: str, op2: str):
        return f"lw {rReg}, {op1}({op2})"

    @staticmethod
    def sw(rReg: str, op1: str, op2: str):
        return f"sw {rReg}, {op1}({op2})"
