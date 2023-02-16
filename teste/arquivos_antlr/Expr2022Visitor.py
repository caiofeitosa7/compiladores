# Generated from Expr2022.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Expr2022Parser import Expr2022Parser
else:
    from Expr2022Parser import Expr2022Parser

# This class defines a complete generic visitor for a parse tree produced by Expr2022Parser.

class Expr2022Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Expr2022Parser#lines.
    def visitLines(self, ctx:Expr2022Parser.LinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2022Parser#line.
    def visitLine(self, ctx:Expr2022Parser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2022Parser#Termo.
    def visitTermo(self, ctx:Expr2022Parser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2022Parser#SomaSub.
    def visitSomaSub(self, ctx:Expr2022Parser.SomaSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2022Parser#Fator.
    def visitFator(self, ctx:Expr2022Parser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2022Parser#DIVMult.
    def visitDIVMult(self, ctx:Expr2022Parser.DIVMultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2022Parser#ExpParenteses.
    def visitExpParenteses(self, ctx:Expr2022Parser.ExpParentesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2022Parser#Numero.
    def visitNumero(self, ctx:Expr2022Parser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr2022Parser#Identificador.
    def visitIdentificador(self, ctx:Expr2022Parser.IdentificadorContext):
        return self.visitChildren(ctx)



del Expr2022Parser