import sys
from antlr4 import *
from Grammars.output.MathLexer import MathLexer
from Grammars.output.MathParser import MathParser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MathLexer(input_stream)
    parser = MathParser(CommonTokenStream(lexer))
    parse_tree = parser.math()
    print(parse_tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)