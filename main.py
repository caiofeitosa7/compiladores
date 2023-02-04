import sys
from antlr4 import *

from arquivos_antlr.trabalhoFinalLexer import trabalhoFinalLexer
from arquivos_antlr.trabalhoFinalParser import trabalhoFinalParser

if __name__ == '__main__':
    print('AntLR com Python:\n')
    
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
    
    
    