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

decFunc: tipo ID '(' parametros? ')' '{' (decVariaveis* comandos | retornoFuncao) '}'
	| ID '(' parametros? ')' '{' decVariaveis* comandos '}'
    ;

chamaFunc: ID '(' passagemParametros? ')'
    ;

passagemParametros: ID (',' ID)
    | ID
    ;

parametros: tipo ID (',' tipo ID)*
    ;

retornoFuncao: 'return' impressao ';'
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

verificacao: (ID | INT | REAL) comparacao (ID | INT | REAL)
	| ID (IGUAL | DIFERENTE) (ID | BOOL)
	| NEG (ID | BOOL)
	| ID   // precisa verificar se é bool
	| BOOL
	;

comparacao: MAIOR_Q
    | MENOR_Q
    | MAIOR_IGUAL
    | MENOR_IGUAL
    | IGUAL
    | DIFERENTE
    ;

expressao: a=expressao op=('*'|'/') b=expressao
    | a=expressao op=('+'|'-') b=expressao
    | INT    
    | ID
    | '(' expressao ')'
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

ID: [a-zA-Z_]([a-zA-Z_0-9]*) ;
WS: [ \t\n\r]+ -> skip ;
BOOL: 'True' | 'False' ;
REAL: INT+ '.' INT+ ;
STRING: '"' .*? '"' ;
INT: [0-9]+ ;