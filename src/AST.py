class Node:
    def __init__(self, token, value):
        self.token = token
        self.value = value

    class exprNode:
        def __init__(self) -> None:
            super().__init__()

    class bin_opNode:
        def __init__(self) -> None:
            super().__init__()

    class un_opNode:
        def __init__(self) -> None:
            super().__init__()

    class comp_opNode:
        def __init__(self) -> None:
            super().__init__()

    class comp_eqNode:
        def __init__(self) -> None:
            super().__init__()

    class log_opNode:
        def __init__(self) -> None:
            super().__init__()

class AST:
    def __init__(self, rootNode, inputString) -> None:
        self.input = inputString
        self.root = rootNode
        self.nodes = []

    def insert(self, Node, substring):
        self.nodes.insert(AST(Node, substring))