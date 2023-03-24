import sys
from colorama import init, Fore, Style

init()
excessoes = list()


def lanca_excecao(texto, fecha_programa=True):
    excessoes.append('ERRO: ' + texto)


def fecha_programa():
    for excessao in excessoes:
        print(Fore.RED + excessao + Style.RESET_ALL)
    sys.exit()
