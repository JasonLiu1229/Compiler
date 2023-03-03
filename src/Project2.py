import sys
from antlr4 import *
from output.MathLexer import MathLexer
from output.MathParser import MathParser
from output.MathVisitor import MathVisitor
from output.MathListener import MathListener
from AST import  AstCreator
from AST import  ErrorListener

def main(argv):
    pass



if __name__ == '__main__':
    main(sys.argv)