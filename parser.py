from lexer1.py import tokens


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


NT_config = [
    ('Programa',NT_Programa),
    ('ListaDecl',NT_ListaDecl),
    ('Declaracion',NT_Declaracion),
    ('FunDecl',NT_FunDecl),
    ('Funcion',NT_Funcion),
    ('ListaParametros',NT_ListaParametros),
    ('Parametros',NT_Parametros),
    ('VarDecl',NT_VarDecl),
    ('Sentencia',NT_Sentencia),
    ('ExprSent',NT_ExprSent),
    ('Expresion',NT_Expresion),
    ('Asignacion',NT_Asignacion),
    ('ForSent',NT_ForSent),
    ('PriArg',NT_PriArg),
    ('AdicArg',NT_AdicArg),
    ('IfSent',NT_IfSent),
    ('ReturnSent',NT_ReturnSent),
    ('WhileSent',NT_WhileSent),
    ('Bloque',NT_Bloque),
    ('OLogico',NT_OLogico),
    ('YLogico',NT_YLogico),
    ('Igua',NT_Igua),
    ('Comparacion',NT_Comparacion),
    ('Suma',NT_Suma),
    ('Mult',NT_Mult),
    ('Unario',NT_Unario),
    ('Primitivo',NT_Primitivo)
]


producciones = [] #lista que contiene a las distintas producciones asociadas a un mismo no terminal
produccionj = [] #produccion nro j de las producciones asociadas a un mismo no terminal(cada produccion es una lista)


def procesar(produccionj):
    n = len(produccionj) #cantidad de elementos de la lista que es la parte derecha de la produccionj de un mismo no terminal
    for i in range(n)
        Xi = produccionj [i]
        if Xi in tokens and cadena[puntero] == Xi :
            puntero += 1
        else
            error = True

        if Xi in prods: #si Xi es un no terminal
            for NT,procedure in NT_config:
                if Xi == NT:
                    procedure() #utiliza el procedimiento correspondiente al no terminal Xi


def NT_Programa (puntero):
    j = 0
    error = True
    producciones = prods['Programa']
    while error and (j < 1):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_ListaDecl ():
    j = 0
    error = True
    producciones = prods['ListaDecl']
    while error and (j<2):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1
    
def NT_Declaracion ():
    j = 0
    error = True
    producciones = prods['Declaracion']
    while error and (j<3):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_FunDecl ():
    j = 0
    error = True
    producciones = prods['FunDecl']
    while error and (j<1):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_Funcion ():
    j = 0
    error = True
    producciones = prods['Funcion']
    while error and (j<1):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_ListaParametros ():
    j = 0
    error = True
    producciones = prods['ListaParametros']
    while error and (j<2):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_Parametros ():
    j = 0
    error = True
    producciones = prods['Parametros']
    while error and (j<2):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_VarDecl ():
    j = 0
    error = True
    producciones = prods['VarDecl']
    while error and (j<2):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_Sentencia ():
    j = 0
    error = True
    producciones = prods['Sentencia']
    while error and (j<6):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_ExprSent ():
    j = 0
    error = True
    producciones = prods['ExprSent']
    while error and (j<1):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_Expresion ():
    j = 0
    error = True
    producciones = prods['Expresion']
    while error and (j<1):
        error = False
        produccionj = producciones [j]
        procesar(produccionj):
        j += 1

def NT_Asignacion ():
    j = 0
    error = True
    producciones = prods['Asignacion']
    while error and (j<2):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1 

def NT_ForSent ():
    j = 0
    error = True
    producciones = prods['ForSent']
    while error and (j<1):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1 

def NT_PriArg ():
    j = 0
    error = True
    producciones = prods['PriArg']
    while error and (j<3):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1 

def NT_AdicArg ():
    j = 0
    error = True
    producciones = prods['AdicArg']
    while error and (j<2):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_IfSent ():
    j = 0
    error = True
    producciones = prods['IfSent']
    while error and (j<2):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def ReturnSent ():
    j = 0
    error = True
    producciones = prods['ReturnSent']
    while error and (j<2):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_WhileSent ():
    j = 0
    error = True
    producciones = prods['WhileSent']
    while error and (j<1):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_Bloque ():
    j = 0
    error = True
    producciones = prods['Bloque']
    while error and (j<1):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_OLogico ():
    j = 0
    error = True
    producciones = prods['OLogico']
    while error and (j<2):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_YLogico ():
    j = 0
    error = True
    producciones = prods['YLogico']
    while error and (j<2):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_Igua ():
    j = 0
    error = True
    producciones = prods['Igua']
    while error and (j<3):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_Comparacion ():
    j = 0
    error = True
    producciones = prods['Comparacion']
    while error and (j<3):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_Suma ():
    j = 0
    error = True
    producciones = prods['Suma']
    while error and (j<3):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_Mult ():
    j = 0
    error = True
    producciones = prods['Mult']
    while error and (j<3):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1 

def NT_Unario ():
    j = 0
    error = True
    producciones = prods['Unario']
    while error and (j<3):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1

def NT_Primitivo ():
    j = 0
    error = True
    producciones = prods['Primitivo']
    while error and (j<6):
        error = False
        produccionj = producciones [j]
        procesar(produccionj)
        j += 1
