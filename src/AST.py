# External libraries
from Node import *
import antlr4.error.ErrorListener
import json

# Standard Variables
keywords = ["var", "int", "binary_op", "unary_op", "comp_op", "comp_eq", "bin_log_op" , "un_log_op", "assign_op" , "const_var"]
keywords_datatype = ["int" , "float" , "char"]
keywords_binary = ["binary_op", "comp_op", "comp_eq", "bin_log_op" , "un_log_op"]
keywords_unary = ["unary_op"]
keywords_indecr = ["incr" , "decr"]
keywords_assign = ["assign_op"]
keywords_functions = ["printf"]
conversions = [("float" , "int") , ("int" , "char") , ("float" , "char")]
conv_promotions = [("int" , "float") , ("char" , "int") , ("char" , "float")]

class ErrorListener (antlr4.error.ErrorListener.ErrorListener):
    def __init__(self):
        super(ErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Gives an error when there is a syntax error
        :return: a syntax error class
        """
        out = "Syntax error at line " + str(line) + ":" + str(column) + ": '"
        if offendingSymbol is not None:
            out += offendingSymbol.text
        out += "'" + "\n" + msg
        raise SyntaxError(out)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        """
        Gives an error when there is an ambiguity
        :return: None
        """
        # raise Exception("Ambiguity")
        super().reportAmbiguity(recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs)

class AST:
    def __init__(self, root : Node = None, children : list[Node] = None) -> None:
        """
        Initializer function
        :param root: assign root node
        :param children: assign children if given
        """
        super().__init__()
        if children is None:
            children = []
        self.root : Node | None = root
        self.children : list[Node] | [] = children
        self.dic_count = {"instr" : 0, "expr" : 0}

    def add_child(self, child):
        """
        Adds a child to the ast
        :param child: node
        :return: none
        """
        if child is None:
            return
        if not isinstance(child, AST) and not isinstance(child , Node):
            if not isinstance(child , AST):
                raise TypeError("child must be set to an AST")
            if not isinstance(child , Node):
                raise TypeError("child must be set to a Node")
        self.children.insert(len(self.children), child)

    def save(self):
        """
        saves the ast in a dictionary
        :return: dictionary
        """
        out = {self.root.key: self.root.value}
        if out[self.root.key] is None:
            out[self.root.key] = []
        else:
            out["children"] = []
        for i in range(len(self.children)):
            if self.children[i] is not None and self.root.value is None:
                out[self.root.key].insert(len(out[self.root.key]) , self.children[i].save())
            elif self.children[i] is not None:
                out["children"].insert(len(out["children"]) , self.children[i].save())
        return out

    def save_dot(self):
        """
        saves the ast in a dot format in a dictionary
        :return: dot format dictionary
        """
        name = ""
        if self.root.key in self.dic_count:
            name = '\"' + self.root.key + self.dic_count[self.root.key] +'\"'
            self.dic_count[self.root.key] += 1
        else:
            name = '\"' + self.root.key + '\"'

        out = {name: self.root.value}
        if out[name] is None:
            out[name] = []
        else:
            out["children"] = []

        for i in range(len(self.children)):
            if self.children[i] is not None and self.root.value is None:
                out[name].append(self.children[i].save_dot())
            elif self.children[i] is not None:
                out["children"].insert(len(out["children"]), self.children[i].save_dot())
        return out

    def print(self , indent : int = 4):
        """
        prints json format of ast
        :param indent:
        :return:
        """
        print(json.dumps(self.save() , indent=indent))

    def dot_language(self, file_name):
        """
        Create dot language format file

        :param file_name: string that determines the file name
        :return: None
        """
        # Create file
        file = open("../Output/" + file_name + ".dot", "w+")
        file.close()

        # Start of dot language
        # self.recursive_dot(new_dictionary, count)
        self.connect("../Output/" + file_name + ".dot", self.save_dot())


        # print dot language

        file = open("../Output/" + file_name + ".dot", "r")

        file_contents = file.read()

        # print(file_contents)

        file.close()

    def connect(self, file_name : str, dictionary):
        """
        connects the dictionary items together, to form a completed dot format file
        :return: None
        """
        with open(str(file_name), "w") as f:
            # A = AGraph(dictionary , directed=True)
            # A.graph_attr["shape"] = "tree"
            # A.write(file_name)
            f.write("digraph { \n\tnode [shape=tree];\n\tgraph[smothing=avg_dist]\n")
            for key, value in dictionary.items():
                string = str(key) + "\t->\t{\n"
                for v in value:
                    string += "\t" + str(v) + "\n"
                string += "}\n"
                f.write(string)
            f.write("}")

    def get_str(self):
        """
        string version of the root
        :return: str
        """
        return self.root.key + '\t' + ':' + '\t' + str(self.root.value)

    def get_dot(self):
        """
        dot format version of the root
        :return: str
        """
        return '\"' + self.root.key + '\"' + '\t' + '->' + '\t' + str(self.root.value)
