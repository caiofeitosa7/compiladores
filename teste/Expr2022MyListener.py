from antlr4 import *

from gen.Expr2022Listener import Expr2022Listener

if __name__ is not None and "." in __name__:
    from gen.Expr2022Parser import Expr2022Parser
else:
    from gen.Expr2022Parser import Expr2022Parser

# Definicao da classe MyListener para evitar sobreposicao durante a geracao do ANTLR
class Expr2022MyListener(Expr2022Listener):

    # Exit a parse tree produced by Expr2022Parser#line.
    def exitLine(self, ctx:Expr2022Parser.LineContext):
        print("Expressao: ", ctx.expr().getText())
        print("Valor: ", ctx.expr().val)

    # Exit a parse tree produced by Expr2022Parser#SomaSub.
    def exitSomaSub(self, ctx: Expr2022Parser.SomaSubContext):
        if ctx.op.text == '+':
            ctx.val = ctx.e1.val + ctx.term().val
        else:
            ctx.val = ctx.e1.val - ctx.term().val

    # Exit a parse tree produced by Expr2022Parser#Termo.
    def exitTermo(self, ctx:Expr2022Parser.TermoContext):
        ctx.val = ctx.term().val

    # Exit a parse tree produced by Expr2022Parser#DIVMult.
    def exitDIVMult(self, ctx: Expr2022Parser.DIVMultContext):
        if ctx.op.text == '*':
            ctx.val = ctx.t1.val * ctx.factor().val
        else:
            ctx.val = ctx.t1.val / ctx.factor().val

    # Exit a parse tree produced by Expr2022Parser#Fator.
    def exitFator(self, ctx:Expr2022Parser.FatorContext):
        ctx.val = ctx.factor().val

    # Exit a parse tree produced by Expr2022Parser#ExpParenteses.
    def exitExpParenteses(self, ctx:Expr2022Parser.ExpParentesesContext):
        ctx.val = ctx.expr().val

    # Exit a parse tree produced by Expr2022Parser#Numero.
    def exitNumero(self, ctx:Expr2022Parser.NumeroContext):
        ctx.val = float(ctx.NUM().getText())

    # Exit a parse tree produced by Expr2022Parser#Identificador.
    def exitIdentificador(self, ctx:Expr2022Parser.IdentificadorContext):
        if (ctx.ID().getText() in ['i','j','k']):
            ctx.val = 1.0
        else:
            ctx.val = 0.0

    def enterLines(self, ctx:Expr2022Parser.LinesContext):
        print("Avaliador de Expressões")
