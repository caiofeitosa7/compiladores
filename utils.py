import sys
from sty import fg, bg, ef, rs

# excessoes = list()


# def fecha_programa():
# 	for e in excessoes:
# 		print(fg.red + '\nERRO: ' + texto + fg.rs)
# 	sys.exit()


def lanca_excecao(texto):
	print(fg.red + '\nERRO: ' + texto + fg.rs)
	sys.exit()


def visivel_no_escopo():
	uso_liberado = set()
	
	if funcao_executando:
		funcao_atual = busca_funcao_por_nome(funcao_executando)
		uso_liberado = set(list(funcao_atual.variaveis.keys()))
	
	nomes_funcoes = [funcao.nome for funcao in memoria_global['funcoes']]
	escopo_global = memoria_global['constantes'] + list(memoria_global['variaveis'].keys()) + nomes_funcoes
	
	for identificador in escopo_global:
		uso_liberado.add(identificador)
	
	return uso_liberado


def busca_funcao_por_nome(nome_funcao):
	return [f for f in memoria_global['funcoes'] if f.nome == nome_funcao][0]


def verifica_existencia_id(ID):
	if funcao_executando:
		funcao_atual = busca_funcao_por_nome(funcao_executando)
		variaveis_escopo = list(funcao_atual.variaveis.keys())
		
		for v in variaveis_escopo:
			if v == ID:
				lanca_excecao(f'A variável "{ID}" já existe em {funcao_executando}.')
	
	elif ID in visivel_no_escopo():
		lanca_excecao(f'O ID "{ID}" já está sendo usado.')

	elif ID in palavras_reservadas:
		lanca_excecao(f'{ID} é uma palavra reservada, não pode ser utilizada.')

	return False
