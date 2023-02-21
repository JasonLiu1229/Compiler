class treeNode:
    def __init__(self, token, value):
        self.token = token
        self.value = value

class AST:
    def __init__(self, rootNode, inputString) -> None:
        super().__init__()
        self.input = inputString
        self.root = rootNode
        self.nodes = []

    def insert(self, treeNode, substring):
        self.nodes.insert(AST(treeNode, substring))