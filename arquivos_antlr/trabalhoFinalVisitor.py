# Generated from trabalhoFinal.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .trabalhoFinalParser import trabalhoFinalParser
else:
    from trabalhoFinalParser import trabalhoFinalParser

# This class defines a complete generic visitor for a parse tree produced by trabalhoFinalParser.

class trabalhoFinalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by trabalhoFinalParser#vazio.
    def visitVazio(self, ctx:trabalhoFinalParser.VazioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#prog.
    def visitProg(self, ctx:trabalhoFinalParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#decVarConst.
    def visitDecVarConst(self, ctx:trabalhoFinalParser.DecVarConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#decVariaveis.
    def visitDecVariaveis(self, ctx:trabalhoFinalParser.DecVariaveisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#listaIds.
    def visitListaIds(self, ctx:trabalhoFinalParser.ListaIdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#listaAtrib.
    def visitListaAtrib(self, ctx:trabalhoFinalParser.ListaAtribContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#AtribValor.
    def visitAtribValor(self, ctx:trabalhoFinalParser.AtribValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#AtribID.
    def visitAtribID(self, ctx:trabalhoFinalParser.AtribIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#AtribExpressao.
    def visitAtribExpressao(self, ctx:trabalhoFinalParser.AtribExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#tipo.
    def visitTipo(self, ctx:trabalhoFinalParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#decFuncaoRetorno.
    def visitDecFuncaoRetorno(self, ctx:trabalhoFinalParser.DecFuncaoRetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#decFuncaoVoid.
    def visitDecFuncaoVoid(self, ctx:trabalhoFinalParser.DecFuncaoVoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#chamaFunc.
    def visitChamaFunc(self, ctx:trabalhoFinalParser.ChamaFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#passagemParametros.
    def visitPassagemParametros(self, ctx:trabalhoFinalParser.PassagemParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#parametros.
    def visitParametros(self, ctx:trabalhoFinalParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#retornoFuncao.
    def visitRetornoFuncao(self, ctx:trabalhoFinalParser.RetornoFuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#main.
    def visitMain(self, ctx:trabalhoFinalParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#comandos.
    def visitComandos(self, ctx:trabalhoFinalParser.ComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#comandosLoop.
    def visitComandosLoop(self, ctx:trabalhoFinalParser.ComandosLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#entrada.
    def visitEntrada(self, ctx:trabalhoFinalParser.EntradaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#printe.
    def visitPrinte(self, ctx:trabalhoFinalParser.PrinteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#imprime.
    def visitImprime(self, ctx:trabalhoFinalParser.ImprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#impressao.
    def visitImpressao(self, ctx:trabalhoFinalParser.ImpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#forLoop.
    def visitForLoop(self, ctx:trabalhoFinalParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#whileLoop.
    def visitWhileLoop(self, ctx:trabalhoFinalParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#ifElse.
    def visitIfElse(self, ctx:trabalhoFinalParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#verificacao.
    def visitVerificacao(self, ctx:trabalhoFinalParser.VerificacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#comparacao.
    def visitComparacao(self, ctx:trabalhoFinalParser.ComparacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#OperacaoMenosUn.
    def visitOperacaoMenosUn(self, ctx:trabalhoFinalParser.OperacaoMenosUnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#OperacaoNegacao.
    def visitOperacaoNegacao(self, ctx:trabalhoFinalParser.OperacaoNegacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#OperacaoMaiorMenor.
    def visitOperacaoMaiorMenor(self, ctx:trabalhoFinalParser.OperacaoMaiorMenorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#OperacaoAddSub.
    def visitOperacaoAddSub(self, ctx:trabalhoFinalParser.OperacaoAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#OperacaoMulDiv.
    def visitOperacaoMulDiv(self, ctx:trabalhoFinalParser.OperacaoMulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#OperacaoAND.
    def visitOperacaoAND(self, ctx:trabalhoFinalParser.OperacaoANDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#ExprParenteses.
    def visitExprParenteses(self, ctx:trabalhoFinalParser.ExprParentesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#Terminal.
    def visitTerminal(self, ctx:trabalhoFinalParser.TerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#OperacaoIgualDif.
    def visitOperacaoIgualDif(self, ctx:trabalhoFinalParser.OperacaoIgualDifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#OperacaoOR.
    def visitOperacaoOR(self, ctx:trabalhoFinalParser.OperacaoORContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#ValorTerminal.
    def visitValorTerminal(self, ctx:trabalhoFinalParser.ValorTerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#ValorVariavel.
    def visitValorVariavel(self, ctx:trabalhoFinalParser.ValorVariavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#chamaID.
    def visitChamaID(self, ctx:trabalhoFinalParser.ChamaIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by trabalhoFinalParser#salvaID.
    def visitSalvaID(self, ctx:trabalhoFinalParser.SalvaIDContext):
        return self.visitChildren(ctx)



del trabalhoFinalParser