import sys
from antlr4 import *
from output.MathLexer import MathLexer
from output.MathParser import MathParser
from output.MathVisitor import MathVisitor
from output.MathListener import MathListener
from AST import  AstCreator

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MathLexer(input_stream)
    parser = MathParser(CommonTokenStream(lexer))
    parse_tree = parser.math()
    visitor = AstCreator()
    ast = visitor.visit(parse_tree)
    ast = visitor.optimise(ast)
    ast.print()
    print(parse_tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)