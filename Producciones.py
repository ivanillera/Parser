prods = {
    'Programa':[
    ['ListaDecl','"eof"']
    ],

    'ListaDecl':[
    ['ListaDecl','Declaracion'],
    ['λ']
    ],

    'Declaracion':[
    ['FunDecl'],
    ['VarDecl'],
    ['Sentencia']
    ],

    'FunDecl': [
    [' "fun" ', 'Funcion']
    ],

    'Funcion': [
    ['Identificador', ' "(" ', 'ListaParametros', ' ")" ', 'Bloque']
    ],

    'ListaParametros': [
    ['λ'],
    ['Parametros']
    ],

    'Parametros':[
    ['Identificador'],
    ['Parametros','","','Identificador']
    ],

    'VarDecl':[
    ['"var"','Identificador','";"'],
    ['"var"','Identificador','"="','Expresion','";"']
    ],

    'Sentencia':[
    ['ExprSent'],
    ['ForSent'],
    ['IfSent'],
    ['ReturnSent'],
    ['WhileSent'],
    ['Bloque']
    ],

    'ExprSent':[
    ['Expresion','";"']
    ],

    'Expresion':[
    ['Asignacion']
    ],

    'Asignacion':[
    ['Identificador','"="','Primitivo'],
    ['OLogico']
    ],

    'ForSent':[
    ['"for"', '"("', 'PriArg AdicArg', '";"', 'AdicArg', '")"', 'Sentencia']
    ],

    'PriArg':[
    ['VarDecl'], 
    ['ExprSent'], 
    ['";"']
    ],

    'AdicArg':[
    ['λ'],
    ['Expresion']
    ],

    'IfSent': [
    ['"if"','"("','Expresion','")"','Sentencia', '"else"','Sentencia'],
    ['"if"','"("','Expresion','")"','Sentencia']
    ],

    'ReturnSent':[
    ['"return"','Expresion','";"'],
    ['"return"','";"']
    ],

    'WhileSent': [
    ['"while"','"("','Expresion','")"','Sentencia']
    ],

    'Bloque': [
    ['"{"','ListaSent','"}"']
    ],

    'ListaSent': [
    ['Sentencia','ListaSent'],
    ['λ']
    ],

    'OLogico': [
    ['YLogico'],
    ['YLogico','"or"','OLogico']
    ],

    'YLogico': [
    ['Igua'],
    ['Igua','"and"','YLogico']
    ],

    'Igua': [
    ['Comparacion'],
    ['Comparacion','"=="','Igua'],
    ['Comparacion','"!="','Igua']
    ],

    'Comparacion': [
    ['Suma'],
    ['Suma','">"','Comparacion'],
    ['Suma','">="','Comparacion'],
    ['Suma','"<"','Comparacion'],
    ['Suma','"<="','Comparacion']
    ],

    'Suma': [
    ['Mult'],
    ['"-"','Suma'],
    ['"+"','Suma']
    ],

    'Mult': [
    ['Unario'],
    ['"/"','Mult'],
    ['"*"','Mult']
    ],

    'Unario': [
    ['"!"','Unario'],
    ['"-"','Unario'],
    ['Primitivo']
    ],

    'Primitivo': [
    ['"true"'],
    ['"false"'],
    ['Numero'],
    ['String'],
    ['Identificador'],
    ['"("','Expresion','")"']
    ]

}