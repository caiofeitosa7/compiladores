class Funcao():
    def __init__(self, nome, tipo_retorno, parametros):
        self.nome = nome
        self.parametros = parametros
        self.variaveis = self.parametros
        self.tipo_retorno = tipo_retorno

    def verifica_tipo_retorno(self, t: str):
        '''
            Verifica se o retorno utilizado é o tipo especificado quando a função foi instanciada.
        '''

        tipo = type(t)

        if self.tipo_retorno == 'real' and tipo is float:
            return True
        elif self.tipo_retorno == 'int' and tipo is int:
            return True
        elif self.tipo_retorno == 'bool' and tipo is bool:
            return True
        elif self.tipo_retorno == 'String' and tipo is str:
            return True

        return False

    def verifica_numero_e_tipo_parametros(self, parametros: dict):
        """
            Verifica se a função recebeu o número e o tipo correto de parâmetros
        """

        """ Verificando a quantidade dos parâmetros """
        return True if len(self.parametros) == len(parametros) else False

        """
            Tipo dos parâmetros
            Necessário transformar o dicionário em uma lista temporariamente para que os itens possam ser indexados
        """
        lista_parametros_passados = list(parametros.values())
        lista_parametros = list(self.parametros.values())

        for i in range(len(lista_parametros)):
            if type(lista_parametros[i]) is not type(lista_parametros_passados[i]):
                return False

        return True