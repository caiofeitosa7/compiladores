grammar trabalhoFinal;

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

atribuicao: ID '=' valor=(BOOL | INT | STRING | REAL)      #AtribValor
    | ID '=' chamaID                                       #AtribID
    | ID '=' expressao                                     #AtribExpressao
    ;

tipo: 'int'
    | 'real'
    | 'bool'
    | 'String'
    ;

decFunc: tipo ID '(' parametros? ')' '{' (decVariaveis* comandos | retornoFuncao) '}'       #decFuncaoRetorno
    | ID '(' parametros? ')' '{' decVariaveis* comandos '}'                                 #decFuncaoVoid
    ;

chamaFuncao: ID '(' passagemParametros? ')'
    ;

passagemParametros: ID ',' passagemParametros
    | ID
    ;

parametros: tipo ID (',' tipo ID)
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
    | whileLoop comandos
    | retornoFuncao comandos
    | listaAtrib comandos
    | 
    ;

comandosLoop: forLoop comandosLoop
    | ifElseLoop comandosLoop                  
    | printe comandosLoop
    | entrada comandosLoop
    | whileLoop comandosLoop
    | retornoFuncao comandosLoop
    | listaAtrib comandosLoop
    | 'break' ';' comandosLoop
    |
    ;

entrada: 'input' '(' passagemParametros? ')' ';'
    ;

printe: 'print' '(' imprime ')' ';'
	;

imprime returns [valor]
    : impressao ',' imprime
    | impressao
    ;

impressao returns [valor]
    : chamaTerminal
    | chamaFuncao
	| expressao
	;

listaAtribFor
    : atribuicao ',' listaAtribFor
    | atribuicao
    ;

forLoop: 'for' '(' listaAtribFor? ';' verif=expressao ';' listaAtribFor ')' '{' comandosLoop '}'
    ;

whileLoop: 'while' '(' expressao ')' '{' comandosLoop '}'
    ;

ifElse: 'if' '(' expressao ')' '{' comandos '}'                                 #IF
    | 'if' '(' expressao ')' '{' comandos '}' 'else' '{' comandos '}'           #IFElse
    ;

ifElseLoop: 'if' '(' expressao ')' '{' comandosLoop '}'                           #IFLoop
    | 'if' '(' expressao ')' '{' comandosLoop '}' 'else' '{' comandosLoop '}'     #IFElseLoop
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
IGUAL: '==';
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