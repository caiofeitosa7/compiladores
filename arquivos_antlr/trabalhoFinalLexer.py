# Generated from trabalhoFinal.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from sty import fg, bg, ef, rs



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2&")
        buf.write("\u00e5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \7")
        buf.write(" \u00b6\n \f \16 \u00b9\13 \3!\6!\u00bc\n!\r!\16!\u00bd")
        buf.write("\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u00cb\n")
        buf.write("\"\3#\6#\u00ce\n#\r#\16#\u00cf\3#\3#\6#\u00d4\n#\r#\16")
        buf.write("#\u00d5\3$\3$\7$\u00da\n$\f$\16$\u00dd\13$\3$\3$\3%\6")
        buf.write("%\u00e2\n%\r%\16%\u00e3\3\u00db\2&\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&\3\2\6\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\5\2\13\f\17\17\"\"\3\2\62;\2\u00eb\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\3K\3\2\2")
        buf.write("\2\5M\3\2\2\2\7S\3\2\2\2\tW\3\2\2\2\13\\\3\2\2\2\ra\3")
        buf.write("\2\2\2\17h\3\2\2\2\21j\3\2\2\2\23l\3\2\2\2\25n\3\2\2\2")
        buf.write("\27p\3\2\2\2\31r\3\2\2\2\33w\3\2\2\2\35|\3\2\2\2\37\u0082")
        buf.write("\3\2\2\2!\u0088\3\2\2\2#\u008c\3\2\2\2%\u0092\3\2\2\2")
        buf.write("\'\u0095\3\2\2\2)\u009a\3\2\2\2+\u009c\3\2\2\2-\u009e")
        buf.write("\3\2\2\2/\u00a0\3\2\2\2\61\u00a2\3\2\2\2\63\u00a4\3\2")
        buf.write("\2\2\65\u00a6\3\2\2\2\67\u00a9\3\2\2\29\u00ab\3\2\2\2")
        buf.write(";\u00ad\3\2\2\2=\u00b0\3\2\2\2?\u00b3\3\2\2\2A\u00bb\3")
        buf.write("\2\2\2C\u00ca\3\2\2\2E\u00cd\3\2\2\2G\u00d7\3\2\2\2I\u00e1")
        buf.write("\3\2\2\2KL\7=\2\2L\4\3\2\2\2MN\7e\2\2NO\7q\2\2OP\7p\2")
        buf.write("\2PQ\7u\2\2QR\7v\2\2R\6\3\2\2\2ST\7k\2\2TU\7p\2\2UV\7")
        buf.write("v\2\2V\b\3\2\2\2WX\7t\2\2XY\7g\2\2YZ\7c\2\2Z[\7n\2\2[")
        buf.write("\n\3\2\2\2\\]\7d\2\2]^\7q\2\2^_\7q\2\2_`\7n\2\2`\f\3\2")
        buf.write("\2\2ab\7U\2\2bc\7v\2\2cd\7t\2\2de\7k\2\2ef\7p\2\2fg\7")
        buf.write("i\2\2g\16\3\2\2\2hi\7.\2\2i\20\3\2\2\2jk\7*\2\2k\22\3")
        buf.write("\2\2\2lm\7+\2\2m\24\3\2\2\2no\7}\2\2o\26\3\2\2\2pq\7\177")
        buf.write("\2\2q\30\3\2\2\2rs\7x\2\2st\7q\2\2tu\7k\2\2uv\7f\2\2v")
        buf.write("\32\3\2\2\2wx\7o\2\2xy\7c\2\2yz\7k\2\2z{\7p\2\2{\34\3")
        buf.write("\2\2\2|}\7r\2\2}~\7t\2\2~\177\7k\2\2\177\u0080\7p\2\2")
        buf.write("\u0080\u0081\7v\2\2\u0081\36\3\2\2\2\u0082\u0083\7k\2")
        buf.write("\2\u0083\u0084\7p\2\2\u0084\u0085\7r\2\2\u0085\u0086\7")
        buf.write("w\2\2\u0086\u0087\7v\2\2\u0087 \3\2\2\2\u0088\u0089\7")
        buf.write("h\2\2\u0089\u008a\7q\2\2\u008a\u008b\7t\2\2\u008b\"\3")
        buf.write("\2\2\2\u008c\u008d\7d\2\2\u008d\u008e\7t\2\2\u008e\u008f")
        buf.write("\7g\2\2\u008f\u0090\7c\2\2\u0090\u0091\7m\2\2\u0091$\3")
        buf.write("\2\2\2\u0092\u0093\7k\2\2\u0093\u0094\7h\2\2\u0094&\3")
        buf.write("\2\2\2\u0095\u0096\7g\2\2\u0096\u0097\7n\2\2\u0097\u0098")
        buf.write("\7u\2\2\u0098\u0099\7g\2\2\u0099(\3\2\2\2\u009a\u009b")
        buf.write("\7,\2\2\u009b*\3\2\2\2\u009c\u009d\7\61\2\2\u009d,\3\2")
        buf.write("\2\2\u009e\u009f\7-\2\2\u009f.\3\2\2\2\u00a0\u00a1\7/")
        buf.write("\2\2\u00a1\60\3\2\2\2\u00a2\u00a3\7#\2\2\u00a3\62\3\2")
        buf.write("\2\2\u00a4\u00a5\7?\2\2\u00a5\64\3\2\2\2\u00a6\u00a7\7")
        buf.write("#\2\2\u00a7\u00a8\7?\2\2\u00a8\66\3\2\2\2\u00a9\u00aa")
        buf.write("\7@\2\2\u00aa8\3\2\2\2\u00ab\u00ac\7>\2\2\u00ac:\3\2\2")
        buf.write("\2\u00ad\u00ae\7@\2\2\u00ae\u00af\7?\2\2\u00af<\3\2\2")
        buf.write("\2\u00b0\u00b1\7>\2\2\u00b1\u00b2\7?\2\2\u00b2>\3\2\2")
        buf.write("\2\u00b3\u00b7\t\2\2\2\u00b4\u00b6\t\3\2\2\u00b5\u00b4")
        buf.write("\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b8\3\2\2\2\u00b8@\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba")
        buf.write("\u00bc\t\4\2\2\u00bb\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2")
        buf.write("\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\3")
        buf.write("\2\2\2\u00bf\u00c0\b!\2\2\u00c0B\3\2\2\2\u00c1\u00c2\7")
        buf.write("V\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4\7w\2\2\u00c4\u00cb")
        buf.write("\7g\2\2\u00c5\u00c6\7H\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8")
        buf.write("\7n\2\2\u00c8\u00c9\7u\2\2\u00c9\u00cb\7g\2\2\u00ca\u00c1")
        buf.write("\3\2\2\2\u00ca\u00c5\3\2\2\2\u00cbD\3\2\2\2\u00cc\u00ce")
        buf.write("\5I%\2\u00cd\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00cd")
        buf.write("\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1")
        buf.write("\u00d3\7\60\2\2\u00d2\u00d4\5I%\2\u00d3\u00d2\3\2\2\2")
        buf.write("\u00d4\u00d5\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3")
        buf.write("\2\2\2\u00d6F\3\2\2\2\u00d7\u00db\7$\2\2\u00d8\u00da\13")
        buf.write("\2\2\2\u00d9\u00d8\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00dc")
        buf.write("\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00de\3\2\2\2\u00dd")
        buf.write("\u00db\3\2\2\2\u00de\u00df\7$\2\2\u00dfH\3\2\2\2\u00e0")
        buf.write("\u00e2\t\5\2\2\u00e1\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2")
        buf.write("\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4J\3\2\2")
        buf.write("\2\n\2\u00b7\u00bd\u00ca\u00cf\u00d5\u00db\u00e3\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class trabalhoFinalLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    MUL = 20
    DIV = 21
    ADD = 22
    SUB = 23
    NEG = 24
    IGUAL = 25
    DIFERENTE = 26
    MAIOR_Q = 27
    MENOR_Q = 28
    MAIOR_IGUAL = 29
    MENOR_IGUAL = 30
    ID = 31
    WS = 32
    BOOL = 33
    REAL = 34
    STRING = 35
    INT = 36

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'const'", "'int'", "'real'", "'bool'", "'String'", "','", 
            "'('", "')'", "'{'", "'}'", "'void'", "'main'", "'print'", "'input'", 
            "'for'", "'break'", "'if'", "'else'", "'*'", "'/'", "'+'", "'-'", 
            "'!'", "'='", "'!='", "'>'", "'<'", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>",
            "MUL", "DIV", "ADD", "SUB", "NEG", "IGUAL", "DIFERENTE", "MAIOR_Q", 
            "MENOR_Q", "MAIOR_IGUAL", "MENOR_IGUAL", "ID", "WS", "BOOL", 
            "REAL", "STRING", "INT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "MUL", "DIV", 
                  "ADD", "SUB", "NEG", "IGUAL", "DIFERENTE", "MAIOR_Q", 
                  "MENOR_Q", "MAIOR_IGUAL", "MENOR_IGUAL", "ID", "WS", "BOOL", 
                  "REAL", "STRING", "INT" ]

    grammarFileName = "trabalhoFinal.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


