class Node:
    def __init__(self, token, value):
        self.token = token
        self.value = value

    class ExprNode:
        def __init__(self) -> None:
            super().__init__()

    class BinOpNode:
        def __init__(self) -> None:
            super().__init__()

    class UnOpNode:
        def __init__(self) -> None:
            super().__init__()

    class CompOpNode:
        def __init__(self) -> None:
            super().__init__()

    class CompEqNode:
        def __init__(self) -> None:
            super().__init__()

    class LogOpNode:
        def __init__(self) -> None:
            super().__init__()

class AST:
    def __init__(self, root_node, input_string) -> None:
        self.input = input_string
        self.root = root_node
        self.nodes = []

    def insert(self, node, substring):
        self.nodes.insert(AST(node, substring))