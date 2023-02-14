from antlr4 import *
from MyLanguageLexer import MyLanguageLexer
from MyLanguageParser import MyLanguageParser

if __name__ == '__main__':
    lexer = MyLanguageLexer(InputStream('Hi Trekkie'))
    parser = MyLanguageParser(CommonTokenStream(lexer))
    parse_tree = parser.parse()
    print(parse_tree.toStringTree(recog=parser))