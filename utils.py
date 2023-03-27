import sys
from colorama import init, Fore, Style

init()
excessoes = list()


def lanca_excecao(texto, ctx, fecha_programa=False):
    excessoes.append("ERRO Linha " + str(ctx.start.line) + ": ");
    excessoes.append(texto)
    
    if fecha_programa:
        fecha_programa()

def fecha_programa():
    for excessao in excessoes:
        print(Fore.RED + excessao + Style.RESET_ALL)
    sys.exit()
