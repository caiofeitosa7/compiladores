grammar trabalhoFinal;

@lexer::header{
from sty import fg, bg, ef, rs
}

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

decVarConst: tipo listaIds ';'
    | 'const' listaAtrib ';'
    ;

tipo: 'int'
    | 'real'
    | 'bool'
    | 'String'
    ;

listaIds: ID (',' ID)*
    ;

listaAtrib: 'int' ID '=' INT (',' ID '=' INT)*
    | 'String' ID '=' STRING (',' ID '=' STRING)*
    | 'bool' ID '=' BOOL (',' ID '=' BOOL)*
    | 'real' ID '=' REAL (',' ID '=' REAL)*
    ;

decFunc: tipo ID '(' listaIds? ')' '{' comandos retornoFuncao ';' '}'
	| 'void' ID '(' listaIds? ')' '{' comandos ';' '}'
    ;

retornoFuncao: expressao
	| ID
	;

main: 'main' '(' ')' '{' comandos '}'
    ;

comandos: decVarConst comandos
    | forLoop comandos
    | ifElse comandos
    | imprime comandos
    | entrada comandos
    | vazio
    ;

imprime: 'print' '(' dado=impressao {print($dado.text.replace('"', ''), end='')} (',' dado2=impressao {print($dado2.text.replace('"', ''), end='')})* ')' ';' {print()}
	;

entrada: 'input' '(' texto=STRING? ')' ';' {input($texto.text.replace('"', ''))}
    ;

impressao: STRING | INT | BOOL | REAL
	| expressao
	| ID
	;

forLoop: 'for' '(' listaAtrib? ';' verificacao ';' expressao ')' '{' comandos ('break')? '}'
    ;

ifElse: 'if' '(' verificacao ')' '{' comandos '}'
    | 'if' '(' verificacao ')' '{' comandos '}' 'else' '{' comandos '}'
    ;

verificacao: (ID | INT | REAL) (MAIOR_Q | MENOR_Q | MAIOR_IGUAL | MENOR_IGUAL | IGUAL | DIFERENTE) (ID | INT | REAL)
	| ID (IGUAL | DIFERENTE) (ID | BOOL)
	| NEG (ID | BOOL)
	| ID   // precisa vrificar se é bool
	| BOOL
	;

expressao returns [int v]: a=expressao op=('*'|'/') b=expressao
    | a=expressao op=('+'|'-') b=expressao
    | INT  {$v=$INT.int}    
    | ID   {$v=$ID.text}											// concluir depois
    | '(' expressao ')'             {$v=$expressao.v}
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