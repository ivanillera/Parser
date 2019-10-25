prods = {
    'Programa':[
    ['ListaDecl','eof']
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
    ['Identificador', '(', 'ListaParametros', ' )', 'Bloque']
    ],

    'ListaParametros': [
    ['λ'],
    ['Parametros']
    ],

    'Parametros':[
    ['Identificador'],
    ['Parametros',',','Identificador']
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
    ['for', '(', 'PriArg AdicArg', ';', 'AdicArg', ')', 'Sentencia']
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
    ['if','(','Expresion',')','Sentencia', 'else','Sentencia'],
    ['if','(','Expresion',')','Sentencia']
    ],

    'ReturnSent':[
    ['return','Expresion',';'],
    ['return',';']
    ],

    'WhileSent': [
    ['while','(','Expresion',')','Sentencia']
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
    ['(','Expresion',')']
    ]

}

### FIN DE PRODUCCIONES ###
terminales = ['eof', 'fun', '(', ')', ',', 'var', ';', '=', 'for', 'if', 'else', 'return', 'while', '{', '}', 'or', 'and', '==','>', '<', '>=', '<=', '-', '+', '/', '*', '!', 'true', 'false', 'a'..'z', 'A'..'Z', '0'..'9' ]
def esTerminal(simbolo):
   simbolo in terminales


def noEsTerminal(simbolo):    
    simbolo not in terminales

def finDeCadena(i):
    tokens(i) == '#'


def parser(tokens):

    self = {
        'tokens' : tokens,
        'index' : 0,
        'error' : false,
    }

    def Parse():
        pni('Programa')
        if error == False and finDeCadena(cadena[index]):

    def procesar(parteDerecha):
        for simbolo in parteDerecha:
            if esTerminal(simbolo):
                if simbolo == tokens[index]:
                    index += 1
                else:
                    error = True
                    break   
            if noEsTerminal(simbolo):
                pni(simbolo)
                if error == True:
                    break
    
    def pni(noTerminal):
        for parteDerecha in prods[noTerminal]:
            indexAux = index 
            procesar(parteDerecha) #Intenta usar esa producción.
            if error == False:
                break
            if error == True: 
                index = indexAux #Índice Auxiliar representa al pivote de retroceso.
            Parse()
    
                
        
