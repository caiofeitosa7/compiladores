import sys
from colorama import init, Fore, Style

init()
excessoes = list()


def lanca_excecao(texto, ctx, fecha_programa=True):
    excessoes.append("ERRO na linha " + str(ctx.start.line) + ": ");
    excessoes.append(texto)

def fecha_programa():
    for excessao in excessoes:
        print(Fore.RED + excessao + Style.RESET_ALL)
    sys.exit()
