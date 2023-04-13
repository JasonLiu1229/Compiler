import sys
from antlr4 import *
from output.MathLexer import MathLexer
from AstCreator import  *
from LLVM import *
import os
def run(directory: str , file_type: str , filenames: list , verbose: bool = False , no_warning: bool = False):
    for filename in filenames:
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
        ast.print(4)
        # ast = visitor.optimise(ast)
        # ast.print()
        # ast.dot_language(filename, visitor.symbol_table)
        # generator = LLVM(ast, visitor.symbol_table, "../Output/" + filename + ".ll")
        # generator.convert()
        # generator.execute()

def main(argv):
    try:
        # argv = -d ../input_files/ -t .c -f Project3 Project2 ...
        # argv = -d ../input_files/ -t .c -i
        directory = ""
        file_type = ""
        filenames = []
        if argv[1] == "-d":
            directory = argv[2]
        if argv[3] == "-t":
            file_type = argv[4]
        if argv[5] == "-f":
            run(directory= directory , file_type= file_type , filenames=argv[6:])
        elif argv[5] == "-i":
            for file in os.listdir(directory):
                if file.endswith(file_type):
                    filenames.append(file[:len(file) - len(file_type)])
            run(directory= directory , file_type= file_type , filenames= filenames)
    except Exception as e:
        print(f'Excepted with error {e}')

if __name__ == '__main__':
    main(sys.argv)