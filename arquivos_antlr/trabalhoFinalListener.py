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


    # Enter a parse tree produced by trabalhoFinalParser#AtribValor.
    def enterAtribValor(self, ctx:trabalhoFinalParser.AtribValorContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#AtribValor.
    def exitAtribValor(self, ctx:trabalhoFinalParser.AtribValorContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#AtribID.
    def enterAtribID(self, ctx:trabalhoFinalParser.AtribIDContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#AtribID.
    def exitAtribID(self, ctx:trabalhoFinalParser.AtribIDContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#tipo.
    def enterTipo(self, ctx:trabalhoFinalParser.TipoContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#tipo.
    def exitTipo(self, ctx:trabalhoFinalParser.TipoContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#decFuncaoRetorno.
    def enterDecFuncaoRetorno(self, ctx:trabalhoFinalParser.DecFuncaoRetornoContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#decFuncaoRetorno.
    def exitDecFuncaoRetorno(self, ctx:trabalhoFinalParser.DecFuncaoRetornoContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#decFuncaoVoid.
    def enterDecFuncaoVoid(self, ctx:trabalhoFinalParser.DecFuncaoVoidContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#decFuncaoVoid.
    def exitDecFuncaoVoid(self, ctx:trabalhoFinalParser.DecFuncaoVoidContext):
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


    # Enter a parse tree produced by trabalhoFinalParser#entrada.
    def enterEntrada(self, ctx:trabalhoFinalParser.EntradaContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#entrada.
    def exitEntrada(self, ctx:trabalhoFinalParser.EntradaContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#printe.
    def enterPrinte(self, ctx:trabalhoFinalParser.PrinteContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#printe.
    def exitPrinte(self, ctx:trabalhoFinalParser.PrinteContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#imprime.
    def enterImprime(self, ctx:trabalhoFinalParser.ImprimeContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#imprime.
    def exitImprime(self, ctx:trabalhoFinalParser.ImprimeContext):
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


    # Enter a parse tree produced by trabalhoFinalParser#OperacaoMenosUn.
    def enterOperacaoMenosUn(self, ctx:trabalhoFinalParser.OperacaoMenosUnContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#OperacaoMenosUn.
    def exitOperacaoMenosUn(self, ctx:trabalhoFinalParser.OperacaoMenosUnContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#OperacaoNegacao.
    def enterOperacaoNegacao(self, ctx:trabalhoFinalParser.OperacaoNegacaoContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#OperacaoNegacao.
    def exitOperacaoNegacao(self, ctx:trabalhoFinalParser.OperacaoNegacaoContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#OperacaoMaiorMenor.
    def enterOperacaoMaiorMenor(self, ctx:trabalhoFinalParser.OperacaoMaiorMenorContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#OperacaoMaiorMenor.
    def exitOperacaoMaiorMenor(self, ctx:trabalhoFinalParser.OperacaoMaiorMenorContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#OperacaoAddSub.
    def enterOperacaoAddSub(self, ctx:trabalhoFinalParser.OperacaoAddSubContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#OperacaoAddSub.
    def exitOperacaoAddSub(self, ctx:trabalhoFinalParser.OperacaoAddSubContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#OperacaoMulDiv.
    def enterOperacaoMulDiv(self, ctx:trabalhoFinalParser.OperacaoMulDivContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#OperacaoMulDiv.
    def exitOperacaoMulDiv(self, ctx:trabalhoFinalParser.OperacaoMulDivContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#OperacaoAND.
    def enterOperacaoAND(self, ctx:trabalhoFinalParser.OperacaoANDContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#OperacaoAND.
    def exitOperacaoAND(self, ctx:trabalhoFinalParser.OperacaoANDContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#ExprParenteses.
    def enterExprParenteses(self, ctx:trabalhoFinalParser.ExprParentesesContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#ExprParenteses.
    def exitExprParenteses(self, ctx:trabalhoFinalParser.ExprParentesesContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#Terminal.
    def enterTerminal(self, ctx:trabalhoFinalParser.TerminalContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#Terminal.
    def exitTerminal(self, ctx:trabalhoFinalParser.TerminalContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#OperacaoIgualDif.
    def enterOperacaoIgualDif(self, ctx:trabalhoFinalParser.OperacaoIgualDifContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#OperacaoIgualDif.
    def exitOperacaoIgualDif(self, ctx:trabalhoFinalParser.OperacaoIgualDifContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#OperacaoOR.
    def enterOperacaoOR(self, ctx:trabalhoFinalParser.OperacaoORContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#OperacaoOR.
    def exitOperacaoOR(self, ctx:trabalhoFinalParser.OperacaoORContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#ValorTerminal.
    def enterValorTerminal(self, ctx:trabalhoFinalParser.ValorTerminalContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#ValorTerminal.
    def exitValorTerminal(self, ctx:trabalhoFinalParser.ValorTerminalContext):
        pass


    # Enter a parse tree produced by trabalhoFinalParser#ValorVariavel.
    def enterValorVariavel(self, ctx:trabalhoFinalParser.ValorVariavelContext):
        pass

    # Exit a parse tree produced by trabalhoFinalParser#ValorVariavel.
    def exitValorVariavel(self, ctx:trabalhoFinalParser.ValorVariavelContext):
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