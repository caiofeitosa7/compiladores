import string
from utils import *
from antlr4 import *
from funcao import Funcao
from antlr4.error.ErrorListener import ErrorListener
from arquivos_antlr.trabalhoFinalParser import trabalhoFinalParser
from arquivos_antlr.trabalhoFinalListener import trabalhoFinalListener


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
salvando_variavel = False


class MyListener(ParseTreeListener):
    def enterDecVarConst(self, ctx):
        global tipo_declaracao, salvando_variavel
        tipo_declaracao = ctx.t.getText()
        salvando_variavel = True
        
    def exitDecVarConst(self, ctx):
        global tipo_declaracao, salvando_variavel
        salvando_variavel = False

    def enterDecVariaveis(self, ctx):
        global tipo_declaracao, salvando_variavel
        tipo_declaracao = ctx.t.getText()
        salvando_variavel = True
        
    def exitDecVariaveis(self, ctx):
        global tipo_declaracao, salvando_variavel
        salvando_variavel = False

    def exitSalvaID(self, ctx):
        salva_variavel(ctx.ID().getText())

    def exitAtribValor(self, ctx):
        valor = ctx.valor.text
        variavel = ctx.ID().getText()
        salva_variavel(variavel, valor)
        
    def exitAtribID(self, ctx):
        variavel = ctx.ID().getText()
        valor = ctx.chamaID().valor
        salva_variavel(variavel, valor)
        
    def exitChamaID(self, ctx):
        nome_variavel = ctx.ID().getText()

        if not nome_variavel in visivel_no_escopo():
            lanca_excecao(f'{nome_variavel} não foi definido(a).')
        else:
            variavel = busca_variavel_por_nome(nome_variavel)
            ctx.type = converte_tipo_variavel(type(variavel[1]))
            ctx.valor = variavel[1]
    
    def exitValorTerminal(self, ctx):
        if ctx.BOOL():
             ctx.valor = True if ctx.BOOL().getText() == 'True' else False
        elif ctx.INT():
            ctx.valor = int(ctx.INT().getText())
        elif ctx.REAL():
            ctx.valor = float(ctx.REAL().getText())
        elif ctx.STRING():
            ctx.valor = str(ctx.STRING().getText())
        ctx.type = type(ctx.valor)
            
    def exitValorVariavel(self, ctx):
        ctx.type = ctx.chamaID().type
        ctx.valor = ctx.chamaID().valor
        
    def exitTerminal(self, ctx):
        ctx.type = ctx.chamaTerminal().type
        ctx.valor = ctx.chamaTerminal().valor

    def enterDecFuncaoRetorno(self, ctx):
        nome_funcao = ctx.ID().getText()
        tipo_retorno = ctx.tipo().getText()
        salva_funcao(nome_funcao, tipo_retorno)

    def exitDecFuncaoRetorno(self, ctx):
        global funcao_executando
        funcao_executando = ''

    def enterDecFuncaoVoid(self, ctx):
        nome_funcao = ctx.ID().getText()
        salva_funcao(nome_funcao)

    def exitDecFuncaoVoid(self, ctx):
        global funcao_executando
        funcao_executando = ''

    def exitRetornoFuncao(self, ctx):
        funcao = busca_funcao_por_nome(funcao_executando)
        tipo_retorno_passado = converte_tipo_variavel(ctx.expressao().type)
        
#         print(memoria_global['funcoes'][0].nome, memoria_global['funcoes'][0].variaveis)
        
        if funcao.tipo_retorno == 'void':
            lanca_excecao(f'A funcao {funcao_executando} não aceita return. É necessário definir um tipo de retorno no cabeçalho da função.')
        elif funcao.tipo_retorno != tipo_retorno_passado:
            lanca_excecao(f'A funcao {funcao_executando} deveria retornar um valor do tipo `{funcao.tipo_retorno}` e não `{tipo_retorno_passado}`')
        
        def exitOperacaoAddSub(self, ctx):
            pass
        
        ### continuar aqui ###
            
        
    
    
def salva_funcao(nome_funcao, tipo_retorno='void', parametros=dict()):
    global funcao_executando
    funcao_executando = nome_funcao
    memoria_global['funcoes'].append(Funcao(nome_funcao, tipo_retorno, parametros))

#     print(memoria_global['funcoes'][0].nome, memoria_global['funcoes'][0].parametros, memoria_global['funcoes'][0].tipo_retorno)


def converte_tipo_variavel(tipo):
    '''
        Converte um tipo python em um tipo da nova linguagem criada
    '''
    
    for tipo_real, tipo_python in mapa_tipos.items():
        if tipo == tipo_python:
            return tipo_real


def verifica_tipo_atribuicao(nome_variavel, tipo_variavel, valor):
    '''
        Compara o tipo da variável com o tipo do valor que será atribuido a ela.
        Se o valor for compatível com o tipo da variável, ele é retornado.
    '''
    
    if tipo_variavel == 'real':
        try:
            valor = float(valor)
        except Exception as e:
            if not valor:
                valor = float()
            else:
                lanca_excecao(f'O valor "{valor}"não pode ser atribuído à {nome_variavel}, pois não corresponde ao tipo real.')

    elif tipo_variavel == 'String':
        valor = str(valor).replace('"', '')
        if not valor:
            valor = str()

    elif tipo_variavel == 'int':
        try:
            valor = int(valor)
        except Exception as e:
            if not valor:
                valor = int()
            else:
                lanca_excecao(f'O valor "{valor}" não pode ser atribuído à {nome_variavel}, pois não corresponde ao tipo int.')
    else:
        try:
            valor = bool(valor)
        except Exception as e:
            lanca_excecao(f'O valor "{valor}" não pode ser atribuído à {nome_variavel}, pois não corresponde ao tipo bool.')
            
    return valor
    
    
def salva_variavel(nome_variavel, valor=None):
    '''
        Salva uma variável de acordo com o escopo em que foi instanciada.
    '''
    
    if nome_variavel[0] in string.digits:
        lanca_excecao('Nomes de variáveis não podem iniciar com números.')
    
    tipo_variavel = tipo_declaracao
    
    if not funcao_executando:
        variavel = busca_variavel_por_nome(nome_variavel)    # retorna (nome_variavel, valor_variavel)
    else:
        variavel = busca_variavel_por_nome(nome_variavel, somente_escopo_local=True)

    if not salvando_variavel and variavel:
        tipo_variavel = converte_tipo_variavel(type(variavel[1]))
    
    if not verifica_existencia_id(nome_variavel) and not salvando_variavel:
        lanca_excecao(f'A variavel "{nome_variavel}" não foi instanciada.')
    else:
        valor = verifica_tipo_atribuicao(nome_variavel, tipo_variavel, valor)
        
        if funcao_executando:
            funcao = busca_funcao_por_nome(funcao_executando)
            funcao.variaveis[nome_variavel] = valor
        else:
            memoria_global['variaveis'][nome_variavel] = valor

#     print(memoria_global['variaveis'])

    
def visivel_no_escopo(somente_escopo_local=False):
    '''
        Lista todos os IDs que podem ser referenciados no escopo atual
    '''
    
    uso_liberado = set()

    if funcao_executando:
        funcao_atual = busca_funcao_por_nome(funcao_executando)
        uso_liberado = set(list(funcao_atual.variaveis.keys()))
        
        if somente_escopo_local:
            return uso_liberado

    nomes_funcoes = [funcao.nome for funcao in memoria_global['funcoes']]
    escopo_global = list(memoria_global['constantes'].keys()) + list(memoria_global['variaveis'].keys()) + nomes_funcoes

    for identificador in escopo_global:
        uso_liberado.add(identificador)

    return uso_liberado


def busca_variavel_por_nome(nome_variavel, somente_escopo_local=False):
    '''
       Procura a variável pelo nome passado por parâmetro.
       Retorna uma tupla onde a primeira posição é o nome da variável e a segunda é o valor.
       
       Returns: (nome_variavel, valor_variavel)
    '''
    
    if nome_variavel not in visivel_no_escopo(somente_escopo_local):
        return False
    
    if funcao_executando:
        funcao = busca_funcao_por_nome(funcao_executando)
        return [v for v in funcao.variaveis.items() if v[0] == nome_variavel][0]
    return [v for v in memoria_global['variaveis'].items() if v[0] == nome_variavel][0]


def busca_funcao_por_nome(nome_funcao: str):
    '''
        Verifica se a função passada por parâmetro já foi instanciada.
    '''
    
    if nome_funcao not in [f.nome for f in memoria_global['funcoes']]:
        lanca_excecao(f'A função {nome_funcao} não foi definida.')
        
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
                if not salvando_variavel:
                    return True
                lanca_excecao(f'A variável "{ID}" já existe em {funcao_executando}.')
                return False

    elif ID in visivel_no_escopo():
        if not salvando_variavel:
            return True
        
        lanca_excecao(f'O ID "{ID}" já está sendo usado.')
        return False

    elif ID in palavras_reservadas:
        lanca_excecao(f'{ID} é uma palavra reservada, não pode ser utilizada.')
        return False

    return False