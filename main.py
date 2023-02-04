import sys
from antlr4 import *
from sty import fg, bg, ef, rs

from arquivos_antlr.trabalhoFinalLexer import trabalhoFinalLexer
from arquivos_antlr.trabalhoFinalParser import trabalhoFinalParser

if __name__ == '__main__':
    if not sys.argv[1].endswith('.py'):
        print(fg.red + 'ERRO: A extensão do arquivo deve ser .py' + fg.rs)
        sys.exit()

    print('\n', '-'*15, 'Trabalho Final', '-'*15, '\n')

    with open(sys.argv[1]) as file:
        exp = ''.join(file.readlines())
        
    print(exp, '\n')
    
    data = InputStream(exp)
    
    # Lexer
    
    lexer = trabalhoFinalLexer(data)
    tokens = CommonTokenStream(lexer)
    
    # print(tokens)
    
    # for i in lexer.getAllTokens():
    #     print(i, i.text)
    # lexer.reset()

    # Parser
    parser = trabalhoFinalParser(tokens)
    tree = parser.prog()
    
    
    