import random
def seleccionar_palabra (palabras):
	#Pido que el jugador elija un tema
	tema = int(input('Elegí un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))
	while (tema>len(palabras)) or (tema < 1):
		print('Ingresá un numero de tema correcto')
		tema = int(input('Elegí un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))
	#Selecciono la palabra a trabajar
	pal = palabras[tema][random.randrange(len(palabras[tema]))]
	return pal




def armar_estructura (pal):
	#armo la estructura de la palabra sobre la cuál se irá armando con las letras
	#que se ingresen. Comienza con tantas rayas como letras tiene la palabra a adivinar
	pal_separada = []
	for y in pal:
		pal_separada.append('_')
	return pal_separada

def actualizar_estructura (pal, pal_separada, cantidad_letras_adivinadas, letra):
			cant = cantidad_letras_adivinadas
			for pos in range(len (pal)):
				if pal[pos] == letra:
					pal_separada[pos] = letra
					cant = cant + 1
			return cant

def imprimir_palabra (pal_separada):
			pal_imprime = ''
			for y in pal_separada:
				pal_imprime = pal_imprime + y + ' '
			print (pal_imprime)

def chequear_victoria (pal, cantidad_letras_adivinadas):
			#averiguo si terminó o debe continuar
			if cantidad_letras_adivinadas == len(pal):
				print ('!Ganaste!')
				return False
			else:
				return True

def chequear_derrota (cantidad_partes_cuerpo, pal):
			if cantidad_partes_cuerpo == 3:
				print ('Perdiste. La palabra era:', pal)
				return False
			else:
				return True

def completar_cuerpo (cantidad_partes_cuerpo, ahorcado):
			for x in range(cantidad_partes_cuerpo):
				print (ahorcado[x])
def main():
	#Preparo el juego
	print('!Bienvenido al Ahorcado (Con funciones ☺)!')
	#Defino conjunto de palabras a trabajar por temas
	palabras = {1:['gato', 'perro','pato','elefante','lobo'], 2:['rojo','azul','verde','amarillo'], 3: ['fideos', 'pizza', 'hamburguesa', 'ensalada']}

	#Defino estructura del ahoracado
	ahorcado = [' O ', '/|\\','/ \\']

	#creo el conjunto de letras ingresadas para evitar la repeticion
	letras = set()

	pal = seleccionar_palabra(palabras)
	pal_separada = armar_estructura(pal)
	#Muestro por pantalla tantas rayas como letras tenga la palabra a adivinar
	print ('- '*len(pal))

	#inicializo variables que permiten saber si se ganó o perdió
	cantidad_letras_adivinadas = 0
	cantidad_partes_cuerpo = 0

	#comienza la interacción con el jugador
	sigue = True
	while sigue:
		#introducción de letras por parte del jugador
		letra = input('Ingresá una letra: ')
		if letra in letras :
			print('Ya ingresaste esa letra')
			sigue = True
		else:
			if letra in pal:
				#coloco la letra en el conjunto de letras ingresadas
				letras.add(letra)
				#Coloco en pal_separada la letra en las posiciones donde se encuentra
				# e incremento la cantidad de letras adivinadas
				cantidad_letras_adivinadas = actualizar_estructura (pal, pal_separada, cantidad_letras_adivinadas, letra)
				#armo la palabra a mostrar al jugador con su letra elegida
				imprimir_palabra (pal_separada)
				#averiguo si terminó o debe continuar
				sigue = chequear_victoria (pal, cantidad_letras_adivinadas)
			else:
				#coloco la letra en el conjunto de letras ingresadas
				letras.add(letra)
				#si se equivocó completo el cuerpo
				cantidad_partes_cuerpo = cantidad_partes_cuerpo + 1
				completar_cuerpo (cantidad_partes_cuerpo, ahorcado)
				#averiguo si terminó o debe continuar
				sigue = chequear_derrota (cantidad_partes_cuerpo, pal)

if __name__ == '__main__':
    main()
