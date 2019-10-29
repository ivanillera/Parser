TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"

###################################################################################
#Abajo de todo estan las pruebas. Paraece que las funciones deben escribirse arriba
#Claro, a menos que importemos este Lexer.py a otro archivo y pongamos las pruebas en ese otro archivo
###################################################################################





###########################################################
#Lo de abajo es necesario para este codigo
#Uso esto para encontrar ESTADO RESULTADO_TRAMPA cuando no se encuentran ni digitos ni letras. 
#(Creo que no debemos buscar " " para reconocer palabras porque no seria el objetivo del tp)
###########################################################

Digitos = ["0","1","2","3","4","5","6","7","8","9"]

# TODO Pueden utilizar isalpha https://www.tutorialspoint.com/python/string_isalpha.htm
# para detectar letras
# y pueden utilizar isdigit para detectar numeros
Letras = []
for x in range(97,123):
	Letras.append(chr(x))
	Letras.append("ñ")
for x in range(65,91):
	Letras.append(chr(x))
	Letras.append("Ñ")

def Letra(caracter):
	if not caracter in Letras or len(caracter) == 0:
		return RESULTADO_TRAMPA
	return RESULTADO_ACEPTADO
	
def Digito(caracter):
	if not caracter in Digitos or len(caracter) == 0:  
		return RESULTADO_TRAMPA
	return RESULTADO_ACEPTADO

def ListaSimbolos(cadena):
	for caracter in cadena:
		if Letra(caracter) == RESULTADO_TRAMPA and Digito(caracter) == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
	if len(cadena) == 0:
		return RESULTADO_TRAMPA
	return RESULTADO_ACEPTADO


###########################################################
#las 2 funciones de abajo son para no repetir el codigo en la funcion lexer(cadena)
###########################################################

#Este es necesario para saber si llegue a un estado de TODO RESULTADO_TRAMPA en la cadena introducida
def TodoTrampa(cadena): 
	if(a_eof(cadena) == RESULTADO_TRAMPA and
		a_if(cadena) == RESULTADO_TRAMPA and
		a_else(cadena) == RESULTADO_TRAMPA and
		a_parclose(cadena) == RESULTADO_TRAMPA and
		a_paropen(cadena) == RESULTADO_TRAMPA and
		a_comma(cadena) == RESULTADO_TRAMPA and
		a_var(cadena) == RESULTADO_TRAMPA and
		a_semicolon(cadena) == RESULTADO_TRAMPA and
		a_igual(cadena) == RESULTADO_TRAMPA and
		a_for(cadena) == RESULTADO_TRAMPA and
		a_return(cadena) == RESULTADO_TRAMPA and
		a_while(cadena) == RESULTADO_TRAMPA and
		a_braopen(cadena) == RESULTADO_TRAMPA and
		a_braclose(cadena) == RESULTADO_TRAMPA and
		a_or(cadena) == RESULTADO_TRAMPA and
		a_and(cadena) == RESULTADO_TRAMPA and
		a_equal(cadena) == RESULTADO_TRAMPA and
		a_different(cadena) == RESULTADO_TRAMPA and
		a_bigger(cadena) == RESULTADO_TRAMPA and
		a_smaller(cadena) == RESULTADO_TRAMPA and
		a_smallorequal(cadena) == RESULTADO_TRAMPA and
		a_bigorequal(cadena) == RESULTADO_TRAMPA and
		a_guion(cadena) == RESULTADO_TRAMPA and
		a_plus(cadena) == RESULTADO_TRAMPA and
		a_slash(cadena) == RESULTADO_TRAMPA and
		a_asterisk(cadena) == RESULTADO_TRAMPA and
		a_exclamation(cadena) == RESULTADO_TRAMPA and
		a_true(cadena) == RESULTADO_TRAMPA and
		a_false(cadena) == RESULTADO_TRAMPA and
		a_punto(cadena) == RESULTADO_TRAMPA and
		a_apostrofe(cadena) == RESULTADO_TRAMPA and
		ListaSimbolos(cadena) == RESULTADO_TRAMPA):
			return True

#Este es para retornar el tipo de cadena segun prioridad
def TipoCadena(cadena):
	if a_eof(cadena) == RESULTADO_ACEPTADO:
		return "_EOF"
	elif a_if(cadena) == RESULTADO_ACEPTADO:
		return "_IF"
	elif a_else(cadena) == RESULTADO_ACEPTADO:
		return "_ELSE"
	elif a_parclose(cadena) == RESULTADO_ACEPTADO:
		return "_PARCLOSE"
	elif a_paropen(cadena) == RESULTADO_ACEPTADO:
		return "_PAROPEN"
	elif a_comma(cadena) == RESULTADO_ACEPTADO:
		return "_COMMA"
	elif a_var(cadena) == RESULTADO_ACEPTADO:
		return "_VAR"
	elif a_semicolon(cadena) == RESULTADO_ACEPTADO:
		return "_SEMICOLON"
	elif a_igual(cadena) == RESULTADO_ACEPTADO:
		return "_IGUAL"
	elif a_for(cadena) == RESULTADO_ACEPTADO:
		return "_FOR"
	elif a_return(cadena) == RESULTADO_ACEPTADO:
		return "_RETURN"
	elif a_while(cadena) == RESULTADO_ACEPTADO:
		return "_WHILE"
	elif a_braopen(cadena) == RESULTADO_ACEPTADO:
		return "_BRAOPEN"
	elif a_braclose(cadena) == RESULTADO_ACEPTADO:
		return "_BRACLOSE"
	elif a_or(cadena) == RESULTADO_ACEPTADO:
		return "_OR"
	elif a_and(cadena) == RESULTADO_ACEPTADO:
		return "_AND"
	elif a_equal(cadena) == RESULTADO_ACEPTADO:
		return "_EQUAL"
	elif a_different(cadena) == RESULTADO_ACEPTADO:
		return "_DIFFERENT"
	elif a_bigger(cadena) == RESULTADO_ACEPTADO:
		return "_BIGGER"
	elif a_smaller(cadena) == RESULTADO_ACEPTADO:
		return "_SMALLER"
	elif a_smallorequal(cadena) == RESULTADO_ACEPTADO:
		return "_SMALLOREQUAL"
	elif a_bigorequal(cadena) == RESULTADO_ACEPTADO:
		return "_BIGOREQUAL"
	elif a_guion(cadena) == RESULTADO_ACEPTADO:
		return "_GUION"
	elif a_plus(cadena) == RESULTADO_ACEPTADO:
		return "_PLUS"
	elif a_slash(cadena) == RESULTADO_ACEPTADO:
		return "_SLASH"
	elif a_asterisk(cadena) == RESULTADO_ACEPTADO:
		return "_ASTERISK"
	elif a_exclamation(cadena) == RESULTADO_ACEPTADO:
		return "_EXCLAMATION"
	elif a_true(cadena) == RESULTADO_ACEPTADO:
		return "_TRUE"
	elif a_false(cadena) == RESULTADO_ACEPTADO:
		return "_FALSE"
	elif a_punto(cadena) == RESULTADO_ACEPTADO:
		return "_PUNTO"
	elif a_apostrofe(cadena) == RESULTADO_ACEPTADO:
		return "_APOSTROFE"

	else:
		return "ID" #En caso de que no sea ninguno de los anteriores creo que entonces es ID.



###################################
#Lexer: voy agarrando elementos de la cadena hasta llegar a un estado RESULTADO_TRAMPA.
#Luego del estado RESULTADO_TRAMPA tomo la cadena antes de llegar al estado RESULTADO_TRAMPA, examino lo que tengo y devuelvo una lista con: (tipo, cosa leida).
###################################


def lexer(cadena):
	tokens = []
	tipo = ""
	primerElemento = 0
	ultimoElemento = 0
	
	####print("Lexeando: " + cadena)
	
	# TODO si agregan un espacio o un simbolo especial al final
	# de la cadena entonces no van a tener problema con el ultimo token
	#Repetimos esto hasta leer toda la cadena
	while ultimoElemento != len(cadena):
		ultimoElemento += 1
		subcadena = cadena[primerElemento:ultimoElemento]
		# Para que saltee espacios al incio:
		if cadena[primerElemento] == " ":
			primerElemento = primerElemento + 1
			subcadena = cadena[primerElemento:ultimoElemento]
		
		
		#examino si lo que leo es RESULTADO_TRAMPA en todos los automatas
		if TodoTrampa(subcadena):
			
			#al ser todo RESULTADO_TRAMPA, examino lo que es por prioridad, dsp guardo lo leido y su tipo en una lista
			subcadena = cadena[primerElemento:ultimoElemento-1]
			tipo = TipoCadena(subcadena)
			tokens.append((tipo,subcadena))
			
			primerElemento = ultimoElemento 

		#Esto es lo mismo que arriba porque por alguna razon no pude hacer que la ultma palabra sea examinada por el algoritmo anterior, asi que lo hago aca
		if ultimoElemento == len(cadena):
			tipo = TipoCadena(subcadena)
			tokens.append((tipo,subcadena))

    tokens.append(('_EOF',"EOF"))
	return tokens
	
	
###########################################################
#AUTOMATAS A_ALGO() D_ALGO()
###########################################################

#delta and
def d_and(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "a":
		return 1
	if estado_anterior == 1 and caracter == "n":
		return 2
	if estado_anterior == 2 and caracter == "d":
		return 3	
	return RESULTADO_TRAMPA

#automata and
def a_and(cadena):
	Finales = [3]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_and(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta apostrofe
def d_apostrofe(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "'":
		return 1

	
	return RESULTADO_TRAMPA

#automata apostrofe
def a_apostrofe(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_apostrofe(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO

#delta asterisk
def d_asterisk(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "*":
		return 1
	
	return RESULTADO_TRAMPA

#automata asterisk
def a_asterisk(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_asterisk(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta ">"
def d_bigger(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == ">":
		return 1

	
	return RESULTADO_TRAMPA

#automata ">"
def a_bigger(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_bigger(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta ">="
def d_bigorequal(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == ">":
		return 1
	if estado_anterior == 1 and caracter == "=":
		return 2	
	return RESULTADO_TRAMPA

#automata ">="
def a_bigorequal(cadena):
	Finales = [2]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_bigorequal(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta braclose
def d_braclose(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "}":
		return 1

	
	return RESULTADO_TRAMPA

#automata braclose
def a_braclose(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_braclose(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta braopen
def d_braopen(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "{":
		return 1

	
	return RESULTADO_TRAMPA

#automata braopen
def a_braopen(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_braopen(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO

#delta comma
def d_comma(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == ",":
		return 1

	
	return RESULTADO_TRAMPA

#automata comma
def a_comma(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_comma(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta different
def d_different(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "!":
		return 1
	if estado_anterior == 1 and caracter == "=":
		return 2
	return RESULTADO_TRAMPA

#automata different
def a_different(cadena):
	Finales = [2]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_different(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta else
def d_else(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "e":
		return 1
	if estado_anterior == 1 and caracter == "l":
		return 2
	if estado_anterior == 2 and caracter == "s":
		return 3
	if estado_anterior == 3 and caracter == "e":
		return 4

	
	return RESULTADO_TRAMPA

#automata else
def a_else(cadena):
	Finales = [4]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_else(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta eof
def d_eof(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "e":
		return 1
	if estado_anterior == 1 and caracter == "o":
		return 2
	if estado_anterior == 2 and caracter == "f":
		return 3

	
	return RESULTADO_TRAMPA

#automata eof
def a_eof(cadena):
	Finales = [3]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_eof(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO

def d_equal(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "=":
		return 1
	if estado_anterior == 1 and caracter == "=":
		return 2

	
	return RESULTADO_TRAMPA

#delta egual
def d_equal(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "=":
		return 1
	if estado_anterior == 1 and caracter == "=":
		return 2

	
	return RESULTADO_TRAMPA

#automata egual
def a_equal(cadena):
	Finales = [2]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_equal(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO

#delta exclamation
def d_exclamation(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "!":
		return 1
	
	return RESULTADO_TRAMPA


#automata exclamation
def a_exclamation(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_exclamation(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta false
def d_false(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "f":
		return 1
	if estado_anterior == 1 and caracter == "a":
		return 2
	if estado_anterior == 2 and caracter == "l":
		return 3
	if estado_anterior == 3 and caracter == "s":
		return 4
	if estado_anterior == 4 and caracter == "e":
		return 5

	
	return RESULTADO_TRAMPA

#automata false
def a_false(cadena):
	Finales = [5]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_false(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta for
def d_for(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "f":
		return 1
	if estado_anterior == 1 and caracter == "o":
		return 2
	if estado_anterior == 2 and caracter == "r":
		return 3

	
	return RESULTADO_TRAMPA

#automata for
def a_for(cadena):
	Finales = [3]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_for(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta fun
def d_fun(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "f":
		return 1
	if estado_anterior == 1 and caracter == "u":
		return 2
	if estado_anterior == 2 and caracter == "n":
		return 3

	
	return RESULTADO_TRAMPA

#automata fun
def a_fun(cadena):
	Finales = [3]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_fun(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta "-"
def d_guion(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "-":
		return 1

	
	return RESULTADO_TRAMPA

#automata "-"
def a_guion(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_guion(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta if
def d_if(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "i":
		return 1
	if estado_anterior == 1 and caracter == "f":
		return 2
	return RESULTADO_TRAMPA

#automata if
def a_if(cadena):
	Finales = [2]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_if(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta igual
def d_igual(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "=":
		return 1

	
	return RESULTADO_TRAMPA

#automata igual
def a_igual(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_igual(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO


#delta or
def d_or(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "o":
		return 1
	if estado_anterior == 1 and caracter == "r":
		return 2
	return RESULTADO_TRAMPA

#automata or
def a_or(cadena):
	Finales = [2]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_or(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta parclose
def d_parclose(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == ")":
		return 1

	
	return RESULTADO_TRAMPA

#automata parclose
def a_parclose(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_parclose(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta paropen
def d_paropen(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "(":
		return 1

	
	return RESULTADO_TRAMPA

#automata paropen
def a_paropen(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_paropen(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta "+"
def d_plus(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "+":
		return 1
	return RESULTADO_TRAMPA

#automata "+"
def a_plus(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_plus(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta punto
def d_punto(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == ".":
		return 1
	return RESULTADO_TRAMPA

#automata punto
def a_punto(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_punto(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO


#delta return
def d_return(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "r":
		return 1
	if estado_anterior == 1 and caracter == "e":
		return 2
	if estado_anterior == 2 and caracter == "t":
		return 3
	if estado_anterior == 3 and caracter == "u":
		return 4
	if estado_anterior == 4 and caracter == "r":
		return 5 
	if estado_anterior == 5 and caracter == "n":
		return 6

	
	return RESULTADO_TRAMPA

#automata return
def a_return(cadena):
	Finales = [6]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_return(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta semicolon
def d_semicolon(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == ";":
		return 1

	
	return RESULTADO_TRAMPA

#automata semicolon
def a_semicolon(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_semicolon(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta "/"
def d_slash(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "/":
		return 1
	return RESULTADO_TRAMPA

#automata "/"
def a_slash(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_slash(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO


#delta smaller
def d_smaller(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "<":
		return 1	
	return RESULTADO_TRAMPA

#automata smaller
def a_smaller(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_smaller(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta "<="
def d_smallorequal(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "<":
		return 1
	if estado_anterior == 1 and caracter == "=":
		return 2   
	return RESULTADO_TRAMPA

#automata "<="
def a_smallorequal(cadena):
	Finales = [2]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_smallorequal(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO

#delta true
def d_true(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "t":
		return 1
	if estado_anterior == 1 and caracter == "r":
		return 2
	if estado_anterior == 2 and caracter == "u":
		return 3
	if estado_anterior == 3 and caracter == "e":
		return 4
	
	
	return RESULTADO_TRAMPA

#automata true
def a_true(cadena):
	Finales = [4]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_true(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta var
def d_var(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "v":
		return 1
	if estado_anterior == 1 and caracter == "a":
		return 2
	if estado_anterior == 2 and caracter == "r":
		return 3

	
	return RESULTADO_TRAMPA

#automata var
def a_var(cadena):
	Finales = [3]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_var(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#delta while
def d_while(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "w":
		return 1
	if estado_anterior == 1 and caracter == "h":
		return 2
	if estado_anterior == 2 and caracter == "i":
		return 3
	if estado_anterior == 3 and caracter == "l":
		return 4
	if estado_anterior == 4 and caracter == "e":
		return 5

	
	return RESULTADO_TRAMPA

#automata while
def a_while(cadena):
	Finales = [5]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_while(estado_actual, caracter)
		if estado_proximo == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO
		
#####################################################################################

# TODO mas pruebas, utilicen todos los posibles tokens
# especificados en la gramatica
assert lexer("si senior else eof") == [('ID', 'si'), ('ID', 'senior'), ('_ELSE', 'else'), ('_EOF', 'eof')]
assert lexer("420 >= 200") == [('ID', '420'), ('_BIGOREQUAL', '>='), ('ID', '200')]
assert lexer("if ifno ifyes") == [('_IF', 'if'), ('ID', 'ifno'), ('ID', 'ifyes')]
assert lexer("") == []
assert lexer("chasquibum") == [('ID', 'chasquibum')]
assert lexer(" if ( { } ) else") == [('_IF', 'if'), ('_PAROPEN', '('), ('_BRAOPEN', '{'), ('_BRACLOSE', '}'), ('_PARCLOSE', ')'), ('_ELSE', 'else')]
assert lexer("Hola") == [("ID", "Hola")]
assert lexer("fun funo if for else return whileo while") == [('ID', 'fun'), ('ID', 'funo'), ('_IF', 'if'), ('_FOR', 'for'), ('_ELSE', 'else'), ('_RETURN', 'return'), ('ID', 'whileo'), ('_WHILE', 'while')]

