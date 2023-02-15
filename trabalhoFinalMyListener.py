from utils import *
from antlr4 import *
from arquivos_antlr.trabalhoFinalParser import trabalhoFinalParser


palavras_reservadas = ('if', 'else', 'return', 'print', 'input', 'for', 'while', 'break',
                            'True', 'False', 'int', 'real', 'bool', 'String', 'main')
memoria_global = {
    'contantes': [],
    'variaveis': {},
    'funcoes': []
}

funcao_executando = ''


def salva_variavel(tipo, variavel, valor):
    if tipo == 'real':
    	try:
    		valor = float(valor)
    	except Exception as e:
    		lanca_excecao(f'O valor {valor} não corresponde ao tipo real.')
    elif tipo == 'String':
    	valor = str(valor)
    elif tipo == 'int':
    	try:
    		valor = int(valor)
    	except Exception as e:
    		lanca_excecao(f'O valor {valor} não corresponde ao tipo int.')
    else:
    	try:
    		valor = bool(valor)
    	except Exception as e:
    		lanca_excecao(f'O valor {valor} não corresponde ao tipo bool.')

    if funcao_executando:
        funcao = busca_funcao_por_nome(funcao_executando)
        funcao.variaveis[variavel] = valor
    else:
    	memoria_global['variaveis'][variavel] = valor


class Funcao():
    tipos = ('int', 'real', 'bool', 'String')

    def __init__(self, nome, tipo_retorno, parametros:dict):
        self.nome = nome
        self.variaveis = parametros
        self.tipo_retorno = tipo_retorno

    def verifica_tipo_retorno(t):
        tipo = type(t)

        if tipo_retorno == 'real' and tipo is float:
            return True
        elif tipo_retorno == 'int' and tipo is int:
            return True
        elif tipo_retorno == 'bool' and tipo is bool:
            return True
        elif tipo_retorno == 'String' and tipo is str:
            return True

        return False


class MyListener(ParseTreeListener):
	def enterAtribuicao(self, ctx:trabalhoFinalParser.AtribuicaoContext):
		tipo = ctx.tipo().getText()
		variavel = ctx.ID().getText()

		if ctx.BOOL():
			valor = ctx.BOOL().getText()
		elif ctx.INT():
			valor = ctx.INT().getText()
		elif ctx.REAL():
			valor = ctx.REAL().getText()
		elif ctx.STRING():
			valor = ctx.STRING().getText()

		salva_variavel(tipo, variavel, valor)
        
