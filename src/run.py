import sys
from antlr4 import *
from output.MathLexer import MathLexer
from AstCreator import *
from LLVM import *
import os
import argparse


def run(directory: str, file_type: str, filenames: list, verbose: bool = False, no_warning: bool = False):
    for filename in filenames:
        try:
            print(f">>> Parsing {directory}{filename}{file_type}\n")
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
            ast.print(4, True, filename)
            visitor.symbol_table.print()
            # ast.dot_language(filename, visitor.symbol_table)
            generator = LLVM(ast, visitor.symbol_table, "../Output/" + filename + ".ll")
            generator.convert()
            generator.execute()
            print(">>> Finished execution with exit code 0\n")
        except Exception as e:
            print(f'Excepted with error \"{e}\"\n')
            continue

def main():
    parser = argparse.ArgumentParser(prog="Compiler", description="Compiles the C files")
    parser.add_argument('-d', '--directory', help='directory of the file that needs to be parsed', required=True)
    parser.add_argument('-t', '--fType', help='file type that needs to be checked', required=True)
    parser.add_argument('-a', '--all', action='store_true', help='this flag defines that all files will be checked')
    parser.add_argument('-f', '--files', nargs='+', help='this flag will define which specific files we want to test')

    try:
        args = parser.parse_args()
        filenames = []
        if args.files is not None:
            run(directory=args.directory, file_type=args.fType, filenames=args.files)
        else:
            for file in os.listdir(args.directory):
                if file.endswith(args.fType):
                    filenames.append(file[:len(file) - len(args.fType)])
            run(directory=args.directory, file_type=args.fType, filenames=filenames)
    except Exception as e:
        print(f'Excepted with error \"{e}\"')



if __name__ == '__main__':
    main()
