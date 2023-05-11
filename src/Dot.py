from AST import *


class dot:
    def __init__(self, in_ast: AST, in_filename: str = "../Output/ast.dor") -> None:
        self.dot = {}
        self.ast: AST = in_ast
        self.filename = in_filename

    def connect(self):
        visited = []
        not_visited = [self.ast]
        while len(not_visited) > 0:
            current = not_visited.pop()
            visited.append(current)
            if isinstance(current, AST):
                for child in current.children:
                    if child not in visited and child not in not_visited and not isinstance(child, Node):
                        not_visited.append(child)
                    temp_ast = None
                    if not isinstance(child, Node) and child not in self.dot and not isinstance(child, ReturnInstr):
                        self.dot[child] = []
                        temp_ast = child
                    elif isinstance(child, ReturnInstr):
                        temp_ast = copy.deepcopy(child)
                        if temp_ast.root.value is None:
                            temp_ast.root.value = temp_ast.children[0].value
                        self.dot[temp_ast] = []
                    else:
                        temp_ast = AST()
                        temp_ast.root = child
                        self.dot[temp_ast] = []
                    try:
                        self.dot[temp_ast].append(current)
                    except Exception as e:
                        print(e)
                        # print(temp_ast)
                        # print(current)
                        # print(self.dot)
                        exit(1)

        # write as dot file
        with open(self.filename, "w") as f:
            f.write("digraph {\n")
            for key in self.dot:
                for value in self.dot[key]:
                    f.write(f" \"{value.root.key}\" ->  \"{key.root.key if key.root.key not in ['int', 'char', 'float'] else str(key.root.key) + ':' + str(key.root.value)}\"\n")
            f.write("}")
