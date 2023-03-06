from utils import *
from antlr4 import *
from arquivos_antlr.trabalhoFinalParser import trabalhoFinalParser


palavras_reservadas = ('if', 'else', 'return', 'print', 'input', 'for', 'while', 'break',
                            'True', 'False', 'int', 'real', 'bool', 'String', 'main')
memoria_global = {
    'constantes': {},
    'variaveis': {},
    'funcoes': []
}

mapa_tipos = {
    'real': float,
    'String': str,
    'bool': bool,
    'int': int
}


'''
    A variável funcao_executando define qual escopo está ativo no momento.
    Quando ela não está vazia (guardando o nome da função em execução), significa que uma função está executando, ao passo que o escopo é local.
    Quando funcao_executando está vazia, nenhuma função está em execução, o escopo ativo é o global.
'''
funcao_executando = ''
tipo_declaracao = ''


class Funcao():
    ####### Tá faltando verificar a quantidade e o tipo dos parâmetros quando a função for chamada ########

    def __init__(self, nome, tipo_retorno, parametros:dict):
        self.nome = nome
        self.parametros = parametros
        self.variaveis = self.parametros
        self.tipo_retorno = tipo_retorno

    def verifica_tipo_retorno(t):
        '''
            Verifica se o retorno utilizado é o tipo especificado quando a função foi instanciada.
        '''

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
    def enterDecVarConst(self, ctx):
        global tipo_declaracao
        tipo_declaracao = ctx.t.getText()

    def enterDecVariaveis(self, ctx):
        global tipo_declaracao
        tipo_declaracao = ctx.t.getText()

    def exitSalvaID(self, ctx):
        salva_variavel(ctx.ID().getText())

    def exitAtribuicao(self, ctx):
        variavel = ctx.ID().getText()
        valor = ctx.valor.text
        salva_variavel(variavel, valor)
        

    # def enterTipo(self, ctx):
    # # if (not ctx.real) and (not ctx.inteiro) and (not ctx.boolean) and (not ctx.string):
    #   if ctx.t.getText() not in mapa_tipos.keys():
    #       lanca_excecao('Tipo inválido.')
    #   type = ctx.t.getText()

    #   print(ctx.t.getText())


#     def exitPrinte(self, ctx):
#         print(ctx.dado, end='')


    # def exitID(self, ctx):
    #     ctx.tipo = type()
    #     ctx.ID().getText()

    # def exitImprime(self, ctx):
    #     print(ctx.valor, end='')

    # def exitImpressao(self, ctx):
    #     print(ctx.valor, end='')

    # def exitChamaID(self, ctx):
    #     elem = ctx.ID().getText()
        
    #     print(elem)

    #     if not elem in visivel_no_escopo():
    #         lanca_excecao(f'{elem} não foi definido.')
    #     else:
    #         if funcao_executando:
    #             funcao = busca_funcao_por_nome(funcao_executando)
    #             ctx.valor = funcao.variaveis[str(elem)]




def salva_variavel(variavel, valor=None):
    '''
        Salva uma variável de acordo com seu tipo e escopo em que foi instanciada.
    '''
    if tipo_declaracao == 'real':
        try:
            valor = float(valor)
        except Exception as e:
            if not valor:
                valor = float()
            else:
                lanca_excecao(f'O valor {valor} não corresponde ao tipo real.')

    elif tipo_declaracao == 'String':
        valor = str(valor).replace('"', '')
        if not valor:
            valor = str()

    elif tipo_declaracao == 'int':
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

    for key, val in memoria_global['variaveis'].items():
        print(key, type(val))

    
def visivel_no_escopo():
    '''
        Lista todos os IDs que podem ser referenciados no escopo atual
    '''
    uso_liberado = set()

    if funcao_executando:
        funcao_atual = busca_funcao_por_nome(funcao_executando)
        uso_liberado = set(list(funcao_atual.variaveis.keys()))

    nomes_funcoes = [funcao.nome for funcao in memoria_global['funcoes']]
    escopo_global = list(memoria_global['constantes'].keys()) + list(memoria_global['variaveis'].keys()) + nomes_funcoes

    for identificador in escopo_global:
        uso_liberado.add(identificador)

    return uso_liberado


def busca_funcao_por_nome(nome_funcao):
    '''
        Verifica se a função passada por parâmetro já foi instanciada.
    '''
    return [f for f in memoria_global['funcoes'] if f.nome == nome_funcao][0]


def verifica_existencia_id(ID):
    '''
        Verifica se já existe o nome de uma variável ou funcão já instanciada com o ID do parâmetro.
        Essa verificação é feita de acordo com o escopo: primeiro verifica dentro da função,
        se houver alguma executando; Depois verifica no escopo global e palavras reservadas.
    '''
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
