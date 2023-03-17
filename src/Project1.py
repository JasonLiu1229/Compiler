import sys

import colorama.initialise

from AST import *
from antlr4 import *
from output.MathLexer import MathLexer


def main(argv):
    colorama.init(autoreset=True)
    input_stream = FileStream(argv[1])
    # Create error listener
    error_listener = ErrorListener()
    lexer = MathLexer(input_stream)
    # Remove previous error listener and add new error listener to lexer
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    parser = MathParser(CommonTokenStream(lexer))
    # Remove previous error listener and add new error listener to parser
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    parse_tree = parser.math()
    visitor = AstCreator()
    ast = visitor.visit(parse_tree)
    ast = visitor.optimise(ast)
    ast.print()
    visitor.warn()
    # ast.dot_language("../../Output/test1")
    # print(parse_tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)