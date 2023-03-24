grammar trabalhoFinal;

@parser::members {

# "memoria" para guardar os pares variavel/valor
memoria = dict()

def salva_variavel(variavel, valor):
	memoria[variavel] = valor


def expr_dual (left, op, right):
    if op == MUL:
        return left * right
    elif op == DIV:
        return left / right
    elif op == ADD:
        return left + right
    elif op == SUB:
        return left - right
    elif op == MAIOR_Q:
        return left > right
    elif op == MENOR_Q:
        return left < right
    elif op == MAIOR_IGUAL:
        return left >= right
    else:
        return left <= right


def expr_unico (op, right):
    if (op == NEG):
        tipo_valor = type(memoria.get(right, right))

        if (tipo_valor is bool):
            return not right
        else:
            print(fg.red + f'ERRO: a operação {NEG} só aceita valor do tipo bool.' + fg.rs)
    else:
        valor = memoria.get(right, right)

        if type(valor) in (int, float):
            return valor * (-1)
        else:
            print(fg.red + 'ERRO: valor deve ser do tipo int ou real.' + fg.rs)
}


vazio:
	;

prog: decVarConst* decFunc* main
    ;

decVarConst: t=tipo listaIds
    | 'const' t=tipo listaAtrib
    ;

decVariaveis: t=tipo listaIds
    | t=tipo listaAtrib
    ;

listaIds
    : salvaID ',' listaIds
    | salvaID ';'
    ;

listaAtrib
    : atribuicao ',' listaAtrib
    | atribuicao ';'
    ;

atribuicao: ID '=' valor=(STRING | INT | BOOL | REAL)      #AtribValor
    | ID '=' chamaID                                       #AtribID
    ;

tipo: 'int'
    | 'real'
    | 'bool'
    | 'String'
    ;

decFunc: tipo ID '(' parametros? ')' '{' (decVariaveis* comandos | retornoFuncao) '}'       #decFuncaoRetorno
    | ID '(' parametros? ')' '{' decVariaveis* comandos '}'                                 #decFuncaoVoid
    ;

chamaFunc: ID '(' passagemParametros? ')'
    ;

passagemParametros: ID (',' ID)
    | ID
    ;

parametros: tipo ID (',' tipo ID)*
    ;

retornoFuncao returns [type, valor]
    : 'return' expressao ';'
    ;

main: 'main' '(' ')' '{' decVariaveis* comandos '}'
    ;

comandos: forLoop comandos
    | ifElse comandos
    | printe comandos
    | entrada comandos
    | retornoFuncao comandos
    | listaAtrib comandos
    | vazio
    ;

comandosLoop: forLoop comandosLoop
    | ifElse comandosLoop
    | printe comandosLoop
    | entrada comandosLoop
    | retornoFuncao comandosLoop
    | listaAtrib comandos
    | 'break' ';'
    | vazio
    ;

entrada: 'input' '(' texto=STRING? ')' ';' {input($texto.text.replace('"', ''))}
    | 'input' '(' passagemParametros ')' ';'
    ;

printe: 'print' '(' impressao ')' ';' {print()}
	;

imprime returns [valor]
    : impressao imprime
    | impressao
    ;

impressao returns [valor]
    : (STRING | INT | BOOL | REAL)
    | chamaFunc
	| expressao
	| ID
	;

forLoop: 'for' '(' tipo listaAtrib? ';' verificacao ';' expressao ')' '{' comandosLoop '}'
    ;

whileLoop: 'while' '(' verificacao ')' '{' comandosLoop '}'
    ;

ifElse: 'if' '(' verificacao ')' '{' comandos '}'
    | 'if' '(' verificacao ')' '{' comandos '}' 'else' '{' comandos '}'
    ;

verificacao: (chamaID | INT | REAL) op=comparacao (chamaID | INT | REAL)
	| chamaID (IGUAL | DIFERENTE) (chamaID | BOOL)
	| NEG (chamaID | BOOL)
	| chamaID   // precisa verificar se é bool
	| BOOL
	;

comparacao: MAIOR_Q
    | MENOR_Q
    | MAIOR_IGUAL
    | MENOR_IGUAL
    | IGUAL
    | DIFERENTE
    ;

expressao returns [type, valor]
    : op_esq=expressao  op=OR                    op_dir=expressao                                   #OperacaoOR
    | op_esq=expressao  op=AND                   op_dir=expressao                                   #OperacaoAND
    | op_esq=expressao  op=( MAIOR_IGUAL | MENOR_IGUAL | MAIOR_Q | MENOR_Q ) op_dir=expressao       #OperacaoMaiorMenor
    | op_esq=expressao  op=( IGUAL | DIFERENTE ) op_dir=expressao                                   #OperacaoIgualDif
    | op_esq=expressao  op=( ADD | SUB )         op_dir=expressao                                   #OperacaoAddSub
    | op_esq=expressao  op=( MUL | DIV )         op_dir=expressao                                   #OperacaoMulDiv
    |                   op=SUB                   op_dir=expressao                                   #OperacaoMenosUn
    |                   op=NEG                   op_dir=expressao                                   #OperacaoNegacao
    | '(' expressao ')'                                                                             #ExprParenteses
    | chamaTerminal                                                                                 #Terminal
    ;

chamaTerminal returns [type, valor]
    : (STRING | INT | BOOL | REAL)             #ValorTerminal
    | chamaID                                  #ValorVariavel
    ;

chamaID returns [type, valor]
    : ID
    ;

salvaID: ID
    ;



// Regras lexicas

MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
NEG : '!' ;
IGUAL: '=';
DIFERENTE: '!=';
MAIOR_Q: '>' ;
MENOR_Q: '<' ;
MAIOR_IGUAL: '>=' ;
MENOR_IGUAL: '<=' ;
OR: '||';
AND: '&&';

ID: [a-zA-Z_]([a-zA-Z_0-9]*) ;
WS: [ \t\n\r]+ -> skip ;
BOOL: 'True' | 'False' ;
REAL: INT+ '.' INT+ ;
STRING: '"' .*? '"' ;
INT: [0-9]+ ;