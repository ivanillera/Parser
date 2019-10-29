from Lexer import *

## FALTA REEMPLAZAR ( POR PAROPEN
prods = {
    'Programa':[
    ['ListaDecl','_EOF']
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
    ['fun', 'Funcion']
    ],

    'Funcion': [
    ['Identificador', '_PAROPEN', 'ListaParametros', '_PARCLOSE', 'Bloque']
    ],

    'ListaParametros': [
    ['λ'],
    ['Parametros']
    ],

    'Parametros':[
    ['Identificador'],
    ['Parametros','_COMMA','Identificador']
    ],

    'VarDecl':[
    ['var','Identificador',';'],
    ['var','Identificador','=','Expresion',';']
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
    ['Expresion',';']
    ],

    'Expresion':[
    ['Asignacion']
    ],

    'Asignacion':[
    ['Identificador','=','Primitivo'],
    ['OLogico']
    ],

    'ForSent':[
    ['for', '_PAROPEN', 'PriArg AdicArg', ';', 'AdicArg', '_PARCLOSE', 'Sentencia']
    ],

    'PriArg':[
    ['VarDecl'], 
    ['ExprSent'], 
    [';']
    ],

    'AdicArg':[
    ['λ'],
    ['Expresion']
    ],

    'IfSent': [
    ['_IF','_PAROPEN','Expresion','_PARCLOSE','Sentencia', '_ELSE','Sentencia'],
    ['_IF','_PAROPEN','Expresion','_PARCLOSE','Sentencia']
    ],

    'ReturnSent':[
    ['return','Expresion',';'],
    ['return',';']
    ],

    'WhileSent': [
    ['while','_PAROPEN','Expresion','_PARCLOSE','Sentencia']
    ],

    'Bloque': [
    ['{','ListaSent','}']
    ],

    'ListaSent': [
    ['Sentencia','ListaSent'],
    ['λ']
    ],

    'OLogico': [
    ['YLogico'],
    ['YLogico','or','OLogico']
    ],

    'YLogico': [
    ['Igua'],
    ['Igua','and','YLogico']
    ],

    'Igua': [
    ['Comparacion'],
    ['Comparacion','==','Igua'],
    ['Comparacion','!=','Igua']
    ],

    'Comparacion': [
    ['Suma'],
    ['Suma','>','Comparacion'],
    ['Suma','>=','Comparacion'],
    ['Suma','<','Comparacion'],
    ['Suma','<=','Comparacion']
    ],

    'Suma': [
    ['Mult'],
    ['-','Suma'],
    ['+','Suma']
    ],

    'Mult': [
    ['Unario'],
    ['/','Mult'],
    ['*','Mult']
    ],

    'Unario': [
    ['!','Unario'],
    ['-','Unario'],
    ['Primitivo']
    ],

    'Primitivo': [
    ['true'],
    ['false'],
    ['Numero'],
    ['String'],
    ['Identificador'],
    ['_PAROPEN','Expresion','_PARCLOSE']
    ]

}

### FIN DE PRODUCCIONES ###

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
        tipo_token_apuntado = token_apuntdo[0] # Primer elemento de tupla.
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

            if noEsTerminal(simbolo):
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


assert parser('a + b') == True
assert parser('fun (a + b)') == True




