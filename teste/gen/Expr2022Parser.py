# Generated from Expr2022.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16")
        buf.write("\n\2\r\2\16\2\17\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\7")
        buf.write("\4\33\n\4\f\4\16\4\36\13\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5")
        buf.write("&\n\5\f\5\16\5)\13\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\61\n")
        buf.write("\6\3\6\2\4\6\b\7\2\4\6\b\n\2\4\3\2\3\4\3\2\5\6\2\62\2")
        buf.write("\r\3\2\2\2\4\21\3\2\2\2\6\24\3\2\2\2\b\37\3\2\2\2\n\60")
        buf.write("\3\2\2\2\f\16\5\4\3\2\r\f\3\2\2\2\16\17\3\2\2\2\17\r\3")
        buf.write("\2\2\2\17\20\3\2\2\2\20\3\3\2\2\2\21\22\5\6\4\2\22\23")
        buf.write("\7\13\2\2\23\5\3\2\2\2\24\25\b\4\1\2\25\26\5\b\5\2\26")
        buf.write("\34\3\2\2\2\27\30\f\4\2\2\30\31\t\2\2\2\31\33\5\b\5\2")
        buf.write("\32\27\3\2\2\2\33\36\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2")
        buf.write("\2\35\7\3\2\2\2\36\34\3\2\2\2\37 \b\5\1\2 !\5\n\6\2!\'")
        buf.write("\3\2\2\2\"#\f\4\2\2#$\t\3\2\2$&\5\n\6\2%\"\3\2\2\2&)\3")
        buf.write("\2\2\2\'%\3\2\2\2\'(\3\2\2\2(\t\3\2\2\2)\'\3\2\2\2*+\7")
        buf.write("\7\2\2+,\5\6\4\2,-\7\b\2\2-\61\3\2\2\2.\61\7\n\2\2/\61")
        buf.write("\7\t\2\2\60*\3\2\2\2\60.\3\2\2\2\60/\3\2\2\2\61\13\3\2")
        buf.write("\2\2\6\17\34\'\60")
        return buf.getvalue()


class Expr2022Parser ( Parser ):

    grammarFileName = "Expr2022.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'/'", "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUM", 
                      "NEWLINE", "WS" ]

    RULE_lines = 0
    RULE_line = 1
    RULE_expr = 2
    RULE_term = 3
    RULE_factor = 4

    ruleNames =  [ "lines", "line", "expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    ID=7
    NUM=8
    NEWLINE=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LinesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Expr2022Parser.LineContext)
            else:
                return self.getTypedRuleContext(Expr2022Parser.LineContext,i)


        def getRuleIndex(self):
            return Expr2022Parser.RULE_lines

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLines" ):
                listener.enterLines(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLines" ):
                listener.exitLines(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLines" ):
                return visitor.visitLines(self)
            else:
                return visitor.visitChildren(self)




    def lines(self):

        localctx = Expr2022Parser.LinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_lines)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.line()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Expr2022Parser.T__4) | (1 << Expr2022Parser.ID) | (1 << Expr2022Parser.NUM))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(Expr2022Parser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(Expr2022Parser.NEWLINE, 0)

        def getRuleIndex(self):
            return Expr2022Parser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = Expr2022Parser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.expr(0)
            self.state = 16
            self.match(Expr2022Parser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.val = None


        def getRuleIndex(self):
            return Expr2022Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.val = ctx.val


    class TermoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Expr2022Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(Expr2022Parser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermo" ):
                return visitor.visitTermo(self)
            else:
                return visitor.visitChildren(self)


    class SomaSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Expr2022Parser.ExprContext
            super().__init__(parser)
            self.e1 = None # ExprContext
            self.op = None # Token
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(Expr2022Parser.TermContext,0)

        def expr(self):
            return self.getTypedRuleContext(Expr2022Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSomaSub" ):
                listener.enterSomaSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSomaSub" ):
                listener.exitSomaSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSomaSub" ):
                return visitor.visitSomaSub(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Expr2022Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = Expr2022Parser.TermoContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 19
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Expr2022Parser.SomaSubContext(self, Expr2022Parser.ExprContext(self, _parentctx, _parentState))
                    localctx.e1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 21
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 22
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==Expr2022Parser.T__0 or _la==Expr2022Parser.T__1):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 23
                    self.term(0) 
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.val = None


        def getRuleIndex(self):
            return Expr2022Parser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.val = ctx.val


    class FatorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Expr2022Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(Expr2022Parser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFator" ):
                return visitor.visitFator(self)
            else:
                return visitor.visitChildren(self)


    class DIVMultContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Expr2022Parser.TermContext
            super().__init__(parser)
            self.t1 = None # TermContext
            self.op = None # Token
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(Expr2022Parser.FactorContext,0)

        def term(self):
            return self.getTypedRuleContext(Expr2022Parser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDIVMult" ):
                listener.enterDIVMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDIVMult" ):
                listener.exitDIVMult(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDIVMult" ):
                return visitor.visitDIVMult(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Expr2022Parser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = Expr2022Parser.FatorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 30
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Expr2022Parser.DIVMultContext(self, Expr2022Parser.TermContext(self, _parentctx, _parentState))
                    localctx.t1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 32
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 33
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==Expr2022Parser.T__2 or _la==Expr2022Parser.T__3):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 34
                    self.factor() 
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.val = None


        def getRuleIndex(self):
            return Expr2022Parser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.val = ctx.val



    class NumeroContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Expr2022Parser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(Expr2022Parser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class ExpParentesesContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Expr2022Parser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(Expr2022Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpParenteses" ):
                listener.enterExpParenteses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpParenteses" ):
                listener.exitExpParenteses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpParenteses" ):
                return visitor.visitExpParenteses(self)
            else:
                return visitor.visitChildren(self)


    class IdentificadorContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Expr2022Parser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(Expr2022Parser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentificador" ):
                listener.enterIdentificador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentificador" ):
                listener.exitIdentificador(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentificador" ):
                return visitor.visitIdentificador(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = Expr2022Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_factor)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Expr2022Parser.T__4]:
                localctx = Expr2022Parser.ExpParentesesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(Expr2022Parser.T__4)
                self.state = 41
                self.expr(0)
                self.state = 42
                self.match(Expr2022Parser.T__5)
                pass
            elif token in [Expr2022Parser.NUM]:
                localctx = Expr2022Parser.NumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(Expr2022Parser.NUM)
                pass
            elif token in [Expr2022Parser.ID]:
                localctx = Expr2022Parser.IdentificadorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.match(Expr2022Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        self._predicates[3] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




