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
