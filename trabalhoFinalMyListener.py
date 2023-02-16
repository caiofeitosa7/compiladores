from utils import *
from antlr4 import *
from arquivos_antlr.trabalhoFinalParser import trabalhoFinalParser


palavras_reservadas = ('if', 'else', 'return', 'print', 'input', 'for', 'while', 'break',
                            'True', 'False', 'int', 'real', 'bool', 'String', 'main')
memoria_global = {
    'constantes': [],
    'variaveis': {},
    'funcoes': []
}

mapa_tipos = {
    'real': float
}

funcao_executando = ''


class Funcao():
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
    def exitAtribuicao(self, ctx):
    #def exitAtribuicao(self, ctx:trabalhoFinalParser.AtribuicaoContext):
        variavel = ctx.ID().getText()
        tipo = ctx.type

        if ctx.BOOL():
            valor = ctx.BOOL().getText()
        elif ctx.INT():
            valor = ctx.INT().getText()
        elif ctx.REAL():
            valor = ctx.REAL().getText()
        elif ctx.STRING():
            valor = ctx.STRING().getText()

        salva_variavel(tipo, variavel, valor)

    def exitTipo(self, ctx):
        if (not ctx.real) and (not ctx.inteiro) and (not ctx.boolean) and (not ctx.string):
            lanca_excecao('Tipo inválido.')

    def exitPrinte(self, ctx):
        print(ctx.dado, end='')

#     def exitImprime(self, ctx):
#         print(ctx.valor, end='')

#     def exitImpressao(self, ctx):
#         print(ctx.valor, end='')


    def exitSalvaID(self, ctx):
        salva_variavel(ctx.type, ctx.ID().getText())

    def exitChamaID(self, ctx):
        elem = ctx.ID().getText()
        
        print(elem)

        if not elem in visivel_no_escopo():
            lanca_excecao(f'{elem} não foi definido.')
        else:
            if funcao_executando:
                funcao = busca_funcao_por_nome(funcao_executando)
                ctx.valor = funcao.variaveis[str(elem)]




def salva_variavel(tipo, variavel, valor=None):
    if tipo == 'real':
        try:
            valor = float(valor)
        except Exception as e:
            if not valor:
                valor = float()
            else:
                lanca_excecao(f'O valor {valor} não corresponde ao tipo real.')

    elif tipo == 'String':
        valor = str(valor)
        if not valor:
            valor = str()

    elif tipo == 'int':
        try:
            valor = int(valor)
        except Exception as e:
            if not valor:
                valor = int()
            else:
                lanca_excecao(f'O valor {valor} não corresponde ao tipo int.')
    else:
        try:
            valor = bool(valor)
        except Exception as e:
            lanca_excecao(f'O valor {valor} não corresponde ao tipo bool.')

    if not verifica_existencia_id(variavel):
        if funcao_executando:
            funcao = busca_funcao_por_nome(funcao_executando)
            funcao.variaveis[variavel] = valor
        else:
            memoria_global['variaveis'][variavel] = valor

    print(memoria_global['variaveis'])

    
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
