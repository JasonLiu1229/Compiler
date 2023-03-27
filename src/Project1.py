import sys
from antlr4 import *
from output.MathLexer import MathLexer
from AstCreator import  *
from LLVM import *

def main(argv):
    try:
        # argv = directory , file_type , files
        directory = argv[1]
        file_type = argv[2]
        for filename in argv[3:]:
            input_stream = FileStream(directory + filename + file_type)
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
            # ast.print()
            ast = visitor.optimise(ast)
            ast.print()
            ast.dot_language(filename)
            generator = LLVM(ast , visitor.symbol_table , "../Output/" + filename + ".ll")
            generator.convert()
    except Exception as e:
        print(str(e))
    # print(parse_tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)