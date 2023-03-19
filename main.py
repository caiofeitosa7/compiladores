import sys
import utils
from antlr4 import *
from sty import fg, bg, ef, rs

from trabalhoFinalMyListener import MyListener
from arquivos_antlr.trabalhoFinalLexer import trabalhoFinalLexer
from arquivos_antlr.trabalhoFinalParser import trabalhoFinalParser

if __name__ == '__main__':
    if not sys.argv[1].endswith('.py'):
        utils.lanca_excecao('A extensão do arquivo deve ser .py')
        sys.exit()

    print('\n', '-'*15, 'Trabalho Final', '-'*15, '\n')

    with open(sys.argv[1]) as file:
        exp = ''.join(file.readlines())
    
    data = InputStream(exp)
    
    # Lexer
    lexer = trabalhoFinalLexer(data)
    tokens = CommonTokenStream(lexer)
    
    # Parser
    parser = trabalhoFinalParser(tokens)
    tree = parser.prog()

    # Listener
    l = MyListener()
    walker = ParseTreeWalker()
    walker.walk(l, tree)
    