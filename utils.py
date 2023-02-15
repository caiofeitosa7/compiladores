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
    nomes_funcoes = [funcao.nome for funcao in memoria_global['funcoes']]
    uso_liberado = memoria_global['constantes'] + memoria_global['variaveis'] + nomes_funcoes

    if funcao_executando:
    	funcao_atual = busca_funcao_por_nome(funcao_executando)
    	uso_liberado += funcao_atual.variaveis

    return uso_liberado


def busca_funcao_por_nome(nome_funcao):
    return [f for f in memoria_global['funcoes'] if f.nome == nome_funcao][0]


def verifica_existencia_id(ID):
	if ID in visivel_no_escopo():		# da forma como está, não aceita variavel local com mesmo nome de uma global
		lanca_excecao(f'O ID {ID} já está sendo usado.')
	elif ID in palavras_reservadas:
		lanca_excecao(f'{ID} é uma palavra reservada, não pode ser utilizada.')

	return False