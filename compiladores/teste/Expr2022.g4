grammar Expr2022;

lines: line+
    ;

line: expr NEWLINE
    ;

expr returns [float val]
    : e1=expr op=('+'|'-') term  #SomaSub
    | term          #Termo
    ;

term returns [float val]
    : t1=term op=('/'|'*') factor #DIVMult
    | factor             #Fator
    ;
    
factor returns [float val]
    : '(' expr ')'  #ExpParenteses
    | NUM           #Numero
    | ID            #Identificador
    ;

ID: [a-zA-Z][a-zA-Z0-9]* ;
NUM: [0-9]+('.'[0-9]+)? ;
NEWLINE: '\r'?'\n' ;
WS: [ \t]+ -> skip;
