# Generated from Expr2022.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("C\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\7\b&\n\b\f\b\16\b")
        buf.write(")\13\b\3\t\6\t,\n\t\r\t\16\t-\3\t\3\t\6\t\62\n\t\r\t\16")
        buf.write("\t\63\5\t\66\n\t\3\n\5\n9\n\n\3\n\3\n\3\13\6\13>\n\13")
        buf.write("\r\13\16\13?\3\13\3\13\2\2\f\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\3\2\6\4\2C\\c|\5\2\62;C\\c|\3\2")
        buf.write("\62;\4\2\13\13\"\"\2H\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5")
        buf.write("\31\3\2\2\2\7\33\3\2\2\2\t\35\3\2\2\2\13\37\3\2\2\2\r")
        buf.write("!\3\2\2\2\17#\3\2\2\2\21+\3\2\2\2\238\3\2\2\2\25=\3\2")
        buf.write("\2\2\27\30\7-\2\2\30\4\3\2\2\2\31\32\7/\2\2\32\6\3\2\2")
        buf.write("\2\33\34\7\61\2\2\34\b\3\2\2\2\35\36\7,\2\2\36\n\3\2\2")
        buf.write("\2\37 \7*\2\2 \f\3\2\2\2!\"\7+\2\2\"\16\3\2\2\2#\'\t\2")
        buf.write("\2\2$&\t\3\2\2%$\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2")
        buf.write("\2(\20\3\2\2\2)\'\3\2\2\2*,\t\4\2\2+*\3\2\2\2,-\3\2\2")
        buf.write("\2-+\3\2\2\2-.\3\2\2\2.\65\3\2\2\2/\61\7\60\2\2\60\62")
        buf.write("\t\4\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2\2\2\63")
        buf.write("\64\3\2\2\2\64\66\3\2\2\2\65/\3\2\2\2\65\66\3\2\2\2\66")
        buf.write("\22\3\2\2\2\679\7\17\2\28\67\3\2\2\289\3\2\2\29:\3\2\2")
        buf.write("\2:;\7\f\2\2;\24\3\2\2\2<>\t\5\2\2=<\3\2\2\2>?\3\2\2\2")
        buf.write("?=\3\2\2\2?@\3\2\2\2@A\3\2\2\2AB\b\13\2\2B\26\3\2\2\2")
        buf.write("\t\2\'-\63\658?\3\b\2\2")
        return buf.getvalue()


class Expr2022Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    ID = 7
    NUM = 8
    NEWLINE = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'/'", "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUM", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "ID", 
                  "NUM", "NEWLINE", "WS" ]

    grammarFileName = "Expr2022.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


