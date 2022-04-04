# Manual técnico y de usuario
Saludos, nuestro código es sencillo. Se ejectua el código Main en Java y se sigue cada instrucción.

ESTE ES UN EJEMPLO CORRECTO:

	Entre el número de estados: 4
	Entre los símbolos de entrada sin separar con espacios: ab
	Entre las transiciones, o -1 si ya no existen más tranciciones para crear:
	0 a $ 1 A$
	1 a A 1 aA
	1 a a 1 aa
	1 b a 2 .
	1 b A 3 .
	2 b a 2 .
	2 b A 3 .
	-1
	Ingrese el número de estados finales separados por espacios y entre -1 para continuar: 1 3 -1
	Estado actual: 0: $, ingrese un solo simbolo: a
	Estado actual: 1: A$, ingrese un solo simbolo: a
	Estado actual: 1: aA$, ingrese un solo simbolo: a
	Estado actual: 1: aaA$, ingrese un solo simbolo: a
	Estado actual: 2: aaaA$, ingrese un solo simbolo: b
	Estado actual: 2: aaA$, ingrese un solo simbolo: b
	Estado actual: 2: aA$, ingrese un solo simbolo: b
	Estado actual: 2: A$, ingrese un solo simbolo: b
	Estado actual: 3: $, ingrese un solo simbolo: -1
	La hilera es aceptada
	¿Coninuar probando hileras S/N?
	S
	Estado actual: 0: $ Ingrese un solo símbolo: a
	Estado actual: 1: A$ Ingrese un solo símbolo: b
	Estado actual: 3: $ Ingrese un solo símbolo: a
	La hilera no se acepta
	¿Continuar probando hileras S/N?
	S
	Estados actuales: 0: $, Ingrese un solo símbolo: b
	La hilera no se acepta
	¿Continuar probando hileras S/N?
	Estados actuales: 0: $, Ingrese un solo símbolo: c
	La hilera no se acepta
	¿Continuar probando hileras S/N?
	N
	Programa finalizado.
