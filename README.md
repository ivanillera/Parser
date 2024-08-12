# Parser y Lexer

El código se divide en dos archivos principales: `Lexer.py` y `Parser.py`.

## Lexer.py

El objetivo del `Lexer` es realizar el análisis léxico del código fuente. Define constantes y funciones para identificar tokens en una cadena de entrada. Utiliza autómatas finitos para reconocer patrones como palabras clave, identificadores, operadores, etc. La función `lexer(cadena)` toma una cadena como entrada y devuelve una lista de tokens reconocidos.

- Define constantes como `TRAMPA`, `RESULTADO_ACEPTADO`, `RESULTADO_TRAMPA`, y `RESULTADO_NO_ACEPTADO`.
- Contiene funciones y automatas para el análisis léxico de cadenas.
- La función `lexer(cadena)` analiza una cadena y devuelve una lista de tokens.
- Incluye automatas para reconocer patrones como guiones, la palabra "if", y el signo igual.

## Parser.py

El `Parser` se encarga del análisis sintáctico del código fuente. Importa el módulo `Lexer` para obtener los tokens generados. Define la gramática del lenguaje mediante reglas de producción que describen la estructura del programa. El objetivo es validar la estructura del código según estas reglas y construir una representación interna del mismo para su posterior procesamiento.

- Importa el módulo `Lexer`.
- Define la gramática de un lenguaje en forma de reglas de producción.
- Las reglas definen la estructura de un programa, declaraciones, funciones, parámetros, sentencias, expresiones, asignaciones, etc.

El `Parser.py` se encarga de analizar la estructura del código fuente según las reglas definidas en la gramática, utilizando el análisis léxico proporcionado por `Lexer.py`.

_Este trabajo fue realizado para Sintaxis y Semántica de los Lenguajes, UTN FRD._
