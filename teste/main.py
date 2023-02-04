from antlr4 import *

from gen.Expr2022Parser import Expr2022Parser
from gen.Expr2022Lexer import Expr2022Lexer
from Expr2022MyListener import Expr2022MyListener

if __name__== '__main__':
    data = FileStream('input2.txt')
    lexer = Expr2022Lexer(data)
    stream = CommonTokenStream(lexer)

    parser = Expr2022Parser(stream)
    tree = parser.lines()

    l = Expr2022MyListener()
    walker = ParseTreeWalker()
    walker.walk(l, tree)