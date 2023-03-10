from AST import AST


class LLVM:
    def __init__(self, input_ast: AST = None) -> None:
        """
        :type input_ast: object AST, default value None
        """
        super().__init__()
        self.ast = input_ast
        self.file_name = None

    def type_checker(self):
        pass

    def convert(self):
        pass

    def execute(self):
        pass
