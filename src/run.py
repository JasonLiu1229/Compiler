import sys
from antlr4 import *
from output.MathLexer import MathLexer
from AstCreator import *
from LLVM import *
from MIPS import *
import os
import argparse
import Dot


def run(directory: str, file_type: str, filenames: list, verbose: bool = True, no_warning: bool = False):
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
            visitor = AstCreator(filename=directory + filename + file_type)
            ast = visitor.visit(parse_tree)
            # handle tree
            ast = visitor.resolve(ast)
            # check if the main function exists
            if not ast.symbolTable.exists("main"):
                raise Exception("No main function found")
            if verbose:
                ast.print(4, True, filename)
                ast.symbolTable.print(True)
            if not no_warning:
                visitor.warn()
            # dot = Dot.dot(ast, "../Output/" + filename + ".dot")
            # dot.connect()
            # ast.dot_language(filename, visitor.symbol_table)
            # generator = LLVM(ast,  "../Output/" + filename + ".ll")
            # generator.convert()
            # generator.execute()
            generator = MIPS(ast, "../Output/" + filename + ".asm")
            generator.convert()
            print(">>> Finished execution with exit code 0\n")
        except Exception as e:
            print(f'Excepted with error \"{str(e)}\"\n')
            continue


def main():
    parser = argparse.ArgumentParser(prog="Compiler", description="Compiles the C files")
    parser.add_argument('-d', '--directory', help='directory of the file that needs to be parsed', required=True)
    parser.add_argument('-t', '--type', help='file type that needs to be checked', required=True)
    parser.add_argument('-a', '--all', action='store_true', help='this flag defines that all files will be checked')
    parser.add_argument('-f', '--files', nargs='+', help='this flag will define which specific files we want to test')
    parser.add_argument('-i', '--index', help='index of which file it is in the directory')
    parser.add_argument('-v', '--verbose', action='store_true', help='this flag will print the AST')
    parser.add_argument('-nw', '--no_warning', action='store_true', help='this flag will not print the warnings')

    try:
        args = parser.parse_args()
        filenames = []
        if args.files is not None:
            run(directory=args.directory, file_type=args.type, filenames=args.files, verbose=args.verbose, no_warning=args.no_warning)
        elif args.index is not None:
            files = os.listdir(args.directory)
            files_one = [files[int(args.index) - 1][:len(files[int(args.index) - 1]) - len(args.type)]]
            run(directory=args.directory, file_type=args.type, filenames=files_one, verbose=args.verbose, no_warning=args.no_warning)
        else:
            for file in os.listdir(args.directory):
                if file.endswith(args.type):
                    filenames.append(file[:len(file) - len(args.type)])
            run(directory=args.directory, file_type=args.type, filenames=filenames, verbose=args.verbose, no_warning=args.no_warning)
    except Exception as e:
        print(f'Excepted with error \"{e}\"')


if __name__ == '__main__':
    main()
