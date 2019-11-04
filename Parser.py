from Lexer import *

prods = {
    'Programa':[
        ['ListaDecl', '_EOF'],
        ['_EOF']
    ],

    'ListaDecl':[
        ['Declaracion'],
        ['ListaDeclPrima', 'Declaracion']
    ],

    'ListaDeclPrima':[
        ['Declaracion', 'ListaDeclPrima'],
        ['Declaracion']
    ],

    'Declaracion':[
        ['FunDecl'],
        ['VarDecl'],
        ['Sentencia']
    ],

    'FunDecl':[
        ['_FUN', 'Funcion']
    ],

    'Funcion':[
        ['ID', '_PAROPEN', 'ListaParametros', '_PARCLOSE', 'Bloque'],
        ['ID', '_PAROPEN', '_PARCLOSE', 'Bloque']
    ],

    'ListaParametros':[
        ['Parametros']
    ],

    'Parametros':[
        ['ID', 'ParametrosPrima'],
        ['ID']
    ],

    'ParametrosPrima':[
        ['_COMMA', 'ID', 'ParametrosPrima']
    ],

    'VarDecl':[
        ['_VAR', 'ID', '_SEMICOLON'],
        ['_VAR', 'ID', '_IGUAL', 'Expresion', '_SEMICOLON']
    ],

    'Sentencia':[
        ['ExprSent'],
        ['ForSent'],
        ['IfSent'],
        ['ReturnSent'],
        ['WhileSent'],
        ['Bloque', '_SEMICOLON'],
    ],

    'ExprSent':[
        ['Expresion', '_SEMICOLON']
    ],

    'Expresion':[
        ['Asignacion']
    ],

    'Asignacion':[
        ['ID', '_IGUAL', 'Primitivo'],
        ['OLogico', '_SEMICOLON']
    ],

    'ForSent':[
        ['FOR', '_PAROPEN', 'PriArg', 'AdicArg', '_SEMICOLON', 'AdicArg', '_PARCLOSE', 'Sentencia'],
        ['FOR', '_PAROPEN', 'PriArg', '_SEMICOLON', '_PARCLOSE', 'Sentencia']
    ],

    'PriArg':[
        ['VarDecl'],
        ['ExprSent'],
        ['_SEMICOLON']
    ],

    'AdicArg':[
        ['Expresion']
    ],

    'IfSent':[
        ['_IF', '_PAROPEN', 'Expresion', '_PARCLOSE', 'Sentencia', '_ELSE', 'Sentencia'],
        ['_IF', '_PAROPEN', 'Expresion', '_PARCLOSE', 'Sentencia']
    ],

    'ReturnSent':[
        ['_RETURN', 'Expresion', '_SEMICOLON'],
        ['_RETURN', '_SEMICOLON']
    ],

    'WhileSent':[
        ['_WHILE', '_PAROPEN', 'Expresion', '_PARCLOSE', 'Sentencia']
    ],

    'Bloque':[
        ['_BRAOPEN', 'ListaDecl', '_BRACLOSE', '_SEMICOLON'],
        ['_BRAOPEN', '_BRACLOSE', '_SEMICOLON']
    ],

    'OLogico':[
        ['YLogico'],
        ['YLogico', '_OR', 'OLogico']
    ],

    'YLogico':[
        ['Igua'],
        ['Igua', '_AND', 'YLogico']
    ],

    'Igua':[
        ['Comparacion'],
        ['Comparacion', '_EQUAL', 'Igua'],
        ['Comparacion', '_DIFFERENT', 'Igua']
    ],

    'Comparacion':[
        ['Suma'],
        ['Suma', '_BIGGER', 'Comparacion'],
        ['Suma', '_BIGOREQUAL', 'Comparacion'],
        ['Suma', '_SMALLER', 'Comparacion'],
        ['Suma', '_SMALLOREQUAL', 'Comparacion']
    ],

    'Suma':[
        ['Mult'],
        ['_GUION', 'Suma'],
        ['_PLUS', 'Suma']
    ],

    'Mult':[
        ['Unario'],
        ['_SLASH', 'Mult'],
        ['_ASTERISK', 'Mult']
    ],

    'Unario':[
        ['_EXCLAMATION', 'Unario'],
        ['_GUION', 'Unario'],
        ['Primitivo']
    ],

    'Primitivo':[
        ['_TRUE'],
        ['_FALSE'],
        ['Numero'],
        ['String'],
        ['ID'],
        ['_PAROPEN', 'Expresion', '_PARCLOSE']
    ]

}

no_Terminales = ['Programa',
                'ListaDecl',
                'ListaDeclPrima', # Agregado por eliminacion de recursividad izq
                'Declaracion',
                'FunDecl',
                'Funcion',
                'ListaParametros',
                'Parametros',
                'ParametrosPrima', # Agregado por eliminacion de recursividad izq
                'VarDecl',
                'Sentencia',
                'ExprSent',
                'Expresion',
                'Asignacion',
                'ForSent',
                'PriArg',
                'AdicArg',
                'IfSent',
                'ReturnSent',
                'WhileSent',
                'Bloque',
                'ListaSent',
                'OLogico',
                'YLogico',
                'Igua',
                'Comparacion',
                'Suma',
                'Mult',
                'Unario',
                'Primitivo'
]


def esTerminal(simbolo):
    return not esNoTerminal(simbolo)

def esNoTerminal(simbolo):    
    return simbolo in no_Terminales

def parser(cadena):
    self = {
        'tokens' : lexer(cadena),
        'index' : 0,
        'error' : False,
    }




    def parse():
        pni('Programa')
        if self['index'] == len(self['tokens']): #Para solucionar list index out of range
            self['index'] -= 1
        token_apuntado = self['tokens'][self['index']]
        if self['error'] == False and token_apuntado[0] == '_EOF':
            return True
        else:
            return False

    def procesar(parteDerecha):
        for simbolo in parteDerecha:
            token_apuntado = self['tokens'][self['index']]
            tipo_token_apuntado = token_apuntado[0]
            self['error'] = False
            if esTerminal(simbolo):
                if simbolo == tipo_token_apuntado :
                    self['index'] += 1
                else:
                    self['error'] = True
                    break

            elif esNoTerminal(simbolo):
                pni(simbolo)
                if self['error'] == True:
                    break 

    def pni(noTerminal):
        for parteDerecha in prods[noTerminal]:
            self['error'] = False
            indexAux = self['index'] 
            procesar(parteDerecha)
            if self['error'] == False:
                break
            if self['error'] == True:
                self['index'] = indexAux


    return parse()

casos = [
    ('var id ;', True), 
    ('', True), 
    ('fun id ( ) { } ', False), 
    ('fun id ( ) { var id ;}', False),
    ('fun id ( ) { var id ; } ;', True),
    ('fun s;', False) ,
    ('a+b = c', False),
    ('fun id ( id ) { var id ; } ;',True),
    ('program begin end;', False)

]
for c,r  in casos:
    assert parser(c) == r



