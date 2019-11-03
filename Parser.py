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
        ['FUN', 'Funcion']
    ],

    'Funcion':[
        ['ID', '_PAROPEN', 'ListaParametros', '_PARCLOSE', 'Bloque'],
        ['ID', '_PAROPEN', '_PARCLOSE', 'Bloque']
    ],

    'ListaParametros':[
        ['Parametros']
    ],

    'Parametros':[
        ['ID', 'Parametros2'],
        ['ID']
    ],

    'Parametros2':[
        ['_COMMA', 'ID', 'Parametros2']
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
        ['IF', '_PAROPEN', 'Expresion', '_PARCLOSE', 'Sentencia', '_ELSE', 'Sentencia'],
        ['IF', '_PAROPEN', 'Expresion', '_PARCLOSE', 'Sentencia']
    ],

    'ReturnSent':[
        ['RETURN', 'Expresion', '_SEMICOLON'],
        ['RETURN', '_SEMICOLON']
    ],

    'WhileSent':[
        ['WHILE', '_PAROPEN', 'Expresion', '_PARCLOSE', 'Sentencia']
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
        ['Suma', '_SMALLORQUAL', 'Comparacion']
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
 ############################
# terminales = [
    #'_EOF', 'fun', '_PAROPEN', '_PARCLOSE', '_COMMA', '_VAR', '_SEMICOLON',
    #'_IGUAL', 'for', '_IF', '_ELSE', 'return', '_WHILE', '_BRAOPEN', '_BRACLOSE',
    #'_OR', '_AND', '_EQUAL', '_DIFERENT', '_BIGGER', '_SMALLER', '_SMALLOREQUAL',
    #'_BIGOREQUAL', '_GUION', '_PLUS', '_SLASH', '_ASTERISK', '_EXCLAMATION', 
    #'_TRUE', '_FALSE'

#]

no_Terminales = ['Programa',
                'ListaDecl',
                'ListaDeclPrima', 
                'Declaracion',
                'FunDecl',
                'Funcion',
                'ListaParametros',
                'Parametros',
                'ParametrosPrima', 
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
        'error' : False
    }




    def parse():
        pni('Programa')
        if self['index'] == len(self['tokens']):
            self['index'] -= 1
        
        token_apuntado = self['tokens'][self['index']]
        tipo_token_apuntado = token_apuntado[0]
        print('Comparando:', tipo_token_apuntado)
        if self['error'] or tipo_token_apuntado !='_EOF':
            print('Cadena no aceptada')
            return False
        else:
            print('Cadena aceptada')
            return True

    def procesar(parteDerecha):

        print(('Procesar: ', parteDerecha, self ))

        

        for simbolo in parteDerecha:

            index = self['index']
            tokens = self['tokens']
            token_apuntado = tokens[index]
            tipo_token_apuntado = token_apuntado[0]
            print('Token apuntado: ', token_apuntado)
            print('Tipo token: ', tipo_token_apuntado)

            self['error'] = False

            if esTerminal(simbolo):
                if simbolo == tipo_token_apuntado:
                    index += 1
                else:
                    self['error'] = True
                    break   

            elif esNoTerminal(simbolo):
                pni(simbolo)
                if self['error'] == True:
                    break
    
    def pni(noTerminal):

        print(('pni: ', noTerminal, self ))

        for parteDerecha in prods[noTerminal]:
            indexAux = self['index'] 

            procesar(parteDerecha) #Intenta usar esa producción.
            if self['error'] == True:
                print('No funcionó, BACKTRACKING.')
                self['index'] = indexAux #Índice Auxiliar representa al pivote de retroceso.
            else:
                break

           
            
    
    return parse()


#print(parser(''))
# print(parser(''))
print(parser('fun id () {var id;};'))
#assert parser('a + b') == True
#ssert parser('fun (a + b)') == True

