from Lexer import *


## TODO: RECURSIVIDAD IZQUIERDA.
prods = {
    'Programa':[
        ['ListaDecl','_EOF']
    ],

    'ListaDecl':[
        ['Declaracion','ListaDeclPrima'],
        []
    ],

    'ListaDeclPrima':[
        ['ListaDecl'],
        []
    ],

   ## 'ListaDecl':[ Original con recursividad izquierda.
   ##     ['ListaDecl','Declaracion'],
   ##     []
   ## ],

    'Declaracion':[
        ['FunDecl'],
        ['VarDecl'],
        ['Sentencia']
    ],

    'FunDecl': [
        ['fun', 'Funcion']
    ],

    'Funcion': [
        ['ID', '_PAROPEN', 'ListaParametros', '_PARCLOSE', 'Bloque']
    ],

    'ListaParametros': [
        [],
        ['Parametros']
    ],

    'Parametros' : [
        ['ID'],
        ['_COMMA','ID','ParametrosPrima']
    ],

    'ParametrosPrima' : [
        ['Parametros']
    ],

    ##'Parametros':[ Original con recursividad.
    ##    ['ID'],
    ##    ['Parametros','_COMMA','ID']
    ##,

    'VarDecl':[
        ['_VAR','ID','_SEMICOLON'],
        ['_VAR','ID','_IGUAL','Expresion','_SEMICOLON']
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
        ['Expresion','_SEMICOLON']
    ],

    'Expresion':[
        ['Asignacion']
    ],

    'Asignacion':[
        ['ID','_IGUAL','Primitivo'],
        ['OLogico']
    ],

    'ForSent':[
        ['for', '_PAROPEN', 'PriArg AdicArg', '_SEMICOLON', 'AdicArg', '_PARCLOSE', 'Sentencia']
    ],

    'PriArg':[
        ['VarDecl'], 
        ['ExprSent'], 
        ['_SEMICOLON']
    ],

    'AdicArg':[
        [],
        ['Expresion']
    ],

    'IfSent': [
        ['_IF','_PAROPEN','Expresion','_PARCLOSE','Sentencia', '_ELSE','Sentencia'],
        ['_IF','_PAROPEN','Expresion','_PARCLOSE','Sentencia']
    ],

    'ReturnSent':[
        ['return','Expresion','_SEMICOLON'],
        ['return','_SEMICOLON']
    ],

    'WhileSent': [
        ['_WHILE','_PAROPEN','Expresion','_PARCLOSE','Sentencia']
    ],

    'Bloque': [
        ['_BRAOPEN','ListaSent','_BRACLOSE','_SEMICOLON']
    ],

    'ListaSent': [
        ['Sentencia','ListaSent'],
        []
    ],

    'OLogico': [
        ['YLogico'],
        ['YLogico','_OR','OLogico']
    ],

    'YLogico': [
        ['Igua'],
        ['Igua','_AND','YLogico']
    ],

    'Igua': [
        ['Comparacion'],
        ['Comparacion','_EQUAL','Igua'],
        ['Comparacion','_DIFERENT','Igua']
    ],

    'Comparacion': [
        ['Suma'],
        ['Suma','_BIGGER','Comparacion'],
        ['Suma','_BIGOREQUAL','Comparacion'],
        ['Suma','_SMALLER','Comparacion'],
        ['Suma','_SMALLOREQUAL','Comparacion']
    ],

    'Suma': [
        ['Mult'],
        ['_GUION','Suma'],
        ['_PLUS','Suma']
    ],

    'Mult': [
        ['Unario'],
        ['_SLASH','Mult'],
        ['_ASTERISK','Mult']
    ],

    'Unario': [
        ['_EXCLAMATION','Unario'],
        ['_GUION','Unario'],
        ['Primitivo']
    ],

    'Primitivo': [
        ['_TRUE'],
        ['_FALSE'],
        ['Numero'],
        ['String'],
        ['ID'],
        ['_PAROPEN','Expresion','_PARCLOSE']
    ]

}
 ############################
terminales = [
    '_EOF', 'fun', '_PAROPEN', '_PARCLOSE', '_COMMA', '_VAR', '_SEMICOLON',
    '_IGUAL', 'for', '_IF', '_ELSE', 'return', '_WHILE', '_BRAOPEN', '_BRACLOSE',
    '_OR', '_AND', '_EQUAL', '_DIFERENT', '_BIGGER', '_SMALLER', '_SMALLOREQUAL',
    '_BIGOREQUAL', '_GUION', '_PLUS', '_SLASH', '_ASTERISK', '_EXCLAMATION', 
    '_TRUE', '_FALSE'

]

def esTerminal(simbolo):
    simbolo in terminales

def esNoTerminal(simbolo):    
    simbolo in prods

def parser(cadena):
    self = {
        'tokens' : lexer(cadena),
        'index' : 0,
        'error' : False,
    }

    def esFinDeCadena():
        index = self['index']
        tokens = self['tokens']
        token_apuntado = tokens[index]
        tipo_token_apuntado = token_apuntado[0] # Primer elemento de tupla.
        return tipo_token_apuntado == '_EOF'



    def Parse():
        pni('Programa')
        if self['error'] == False and esFinDeCadena():
            return True
        else:
            return False

    def procesar(parteDerecha):

        print(('procesar: ', parteDerecha, self ))
        index = self['index']
        tokens = self['tokens']
        token_apuntado = tokens[index]

        for simbolo in parteDerecha:

            if esTerminal(simbolo):
                if simbolo == token_apuntado:
                    index += 1
                else:
                    self['error'] = True
                    break   

            if esNoTerminal(simbolo):
                pni(simbolo)
                if self['error'] == True:
                    break
    
    def pni(noTerminal):

        print(('pni: ', noTerminal, self ))

        for parteDerecha in prods[noTerminal]:
            indexAux = self['index'] 

            procesar(parteDerecha) #Intenta usar esa producción.
            if self['error'] == False:
                break
            if self['error'] == True: 
                print('No funcionó, backtracking.')
                self['index'] = indexAux #Índice Auxiliar representa al pivote de retroceso.
            
    
    return Parse()


print(parser('a'))
#assert parser('a + b') == True
#ssert parser('fun (a + b)') == True

