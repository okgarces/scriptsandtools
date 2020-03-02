# -*- coding: utf-8 -*-
frase = 'Tu tiempo es limitado, de modo que no lo malgastes viviendo la vida de alguien distinto. No quedes atrapado en el dogma, que es vivir como otros piensan que deberías vivir. No dejes que los ruidos de las opiniones de los demás acallen tu propia voz interior. Y, lo que es más importante, ten el coraje para hacer lo que te dicen tu corazón y tu intuición.'.decode('UTF-8')

count = 0
mas_repetida = ''
actual = 0
for i in frase:

	for j in frase:
		if i == j and i != ',' and i!='.' and i !=' ':
			actual=actual+1


	print i, actual
	if actual >= count:
		mas_repetida = i
		count = actual

	actual = 0

print mas_repetida
