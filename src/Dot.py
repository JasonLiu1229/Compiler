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
                    if child not in visited and child not in not_visited:
                        not_visited.append(child)
                    if child not in self.dot:
                        self.dot[child] = []
                    self.dot[child].append(current)

        # write as dot file
        with open(self.filename, "w") as f:
            f.write("digraph {\n")
            for key in self.dot:
                for value in self.dot[key]:
                    f.write(f"\"{key.root.key}\" -> \"{value.root.key}\"\n")
            f.write("}")
