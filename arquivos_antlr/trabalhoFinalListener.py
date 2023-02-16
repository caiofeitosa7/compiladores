# Generated from trabalhoFinal.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .trabalhoFinalParser import trabalhoFinalParser
else:
    from trabalhoFinalParser import trabalhoFinalParser

# This class defines a complete listener for a parse tree produced by trabalhoFinalParser.
class trabalhoFinalListener(ParseTreeListener):

    # Enter a parse tree produced by trabalhoFinalParser#vazio.
    def enterVazio(self, ctx:trabalhoFinalParser.VazioContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#vazio.
    def exitVazio(self, ctx:trabalhoFinalParser.VazioContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#prog.
    def enterProg(self, ctx:trabalhoFinalParser.ProgContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#prog.
    def exitProg(self, ctx:trabalhoFinalParser.ProgContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#decVarConst.
    def enterDecVarConst(self, ctx:trabalhoFinalParser.DecVarConstContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#decVarConst.
    def exitDecVarConst(self, ctx:trabalhoFinalParser.DecVarConstContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#decVariaveis.
    def enterDecVariaveis(self, ctx:trabalhoFinalParser.DecVariaveisContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#decVariaveis.
    def exitDecVariaveis(self, ctx:trabalhoFinalParser.DecVariaveisContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#listaIds.
    def enterListaIds(self, ctx:trabalhoFinalParser.ListaIdsContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#listaIds.
    def exitListaIds(self, ctx:trabalhoFinalParser.ListaIdsContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#listaAtrib.
    def enterListaAtrib(self, ctx:trabalhoFinalParser.ListaAtribContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#listaAtrib.
    def exitListaAtrib(self, ctx:trabalhoFinalParser.ListaAtribContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#atribuicao.
    def enterAtribuicao(self, ctx:trabalhoFinalParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#atribuicao.
    def exitAtribuicao(self, ctx:trabalhoFinalParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#tipo.
    def enterTipo(self, ctx:trabalhoFinalParser.TipoContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#tipo.
    def exitTipo(self, ctx:trabalhoFinalParser.TipoContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#decFunc.
    def enterDecFunc(self, ctx:trabalhoFinalParser.DecFuncContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#decFunc.
    def exitDecFunc(self, ctx:trabalhoFinalParser.DecFuncContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#chamaFunc.
    def enterChamaFunc(self, ctx:trabalhoFinalParser.ChamaFuncContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#chamaFunc.
    def exitChamaFunc(self, ctx:trabalhoFinalParser.ChamaFuncContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#passagemParametros.
    def enterPassagemParametros(self, ctx:trabalhoFinalParser.PassagemParametrosContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#passagemParametros.
    def exitPassagemParametros(self, ctx:trabalhoFinalParser.PassagemParametrosContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#parametros.
    def enterParametros(self, ctx:trabalhoFinalParser.ParametrosContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#parametros.
    def exitParametros(self, ctx:trabalhoFinalParser.ParametrosContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#retornoFuncao.
    def enterRetornoFuncao(self, ctx:trabalhoFinalParser.RetornoFuncaoContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#retornoFuncao.
    def exitRetornoFuncao(self, ctx:trabalhoFinalParser.RetornoFuncaoContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#main.
    def enterMain(self, ctx:trabalhoFinalParser.MainContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#main.
    def exitMain(self, ctx:trabalhoFinalParser.MainContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#comandos.
    def enterComandos(self, ctx:trabalhoFinalParser.ComandosContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#comandos.
    def exitComandos(self, ctx:trabalhoFinalParser.ComandosContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#comandosLoop.
    def enterComandosLoop(self, ctx:trabalhoFinalParser.ComandosLoopContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#comandosLoop.
    def exitComandosLoop(self, ctx:trabalhoFinalParser.ComandosLoopContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#printe.
    def enterPrinte(self, ctx:trabalhoFinalParser.PrinteContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#printe.
    def exitPrinte(self, ctx:trabalhoFinalParser.PrinteContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#entrada.
    def enterEntrada(self, ctx:trabalhoFinalParser.EntradaContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#entrada.
    def exitEntrada(self, ctx:trabalhoFinalParser.EntradaContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#impressao.
    def enterImpressao(self, ctx:trabalhoFinalParser.ImpressaoContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#impressao.
    def exitImpressao(self, ctx:trabalhoFinalParser.ImpressaoContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#forLoop.
    def enterForLoop(self, ctx:trabalhoFinalParser.ForLoopContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#forLoop.
    def exitForLoop(self, ctx:trabalhoFinalParser.ForLoopContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#whileLoop.
    def enterWhileLoop(self, ctx:trabalhoFinalParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#whileLoop.
    def exitWhileLoop(self, ctx:trabalhoFinalParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#ifElse.
    def enterIfElse(self, ctx:trabalhoFinalParser.IfElseContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#ifElse.
    def exitIfElse(self, ctx:trabalhoFinalParser.IfElseContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#verificacao.
    def enterVerificacao(self, ctx:trabalhoFinalParser.VerificacaoContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#verificacao.
    def exitVerificacao(self, ctx:trabalhoFinalParser.VerificacaoContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#comparacao.
    def enterComparacao(self, ctx:trabalhoFinalParser.ComparacaoContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#comparacao.
    def exitComparacao(self, ctx:trabalhoFinalParser.ComparacaoContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#expressao.
    def enterExpressao(self, ctx:trabalhoFinalParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#expressao.
    def exitExpressao(self, ctx:trabalhoFinalParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#chamaID.
    def enterChamaID(self, ctx:trabalhoFinalParser.ChamaIDContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#chamaID.
    def exitChamaID(self, ctx:trabalhoFinalParser.ChamaIDContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#salvaID.
    def enterSalvaID(self, ctx:trabalhoFinalParser.SalvaIDContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#salvaID.
    def exitSalvaID(self, ctx:trabalhoFinalParser.SalvaIDContext):
        pass



del trabalhoFinalParser