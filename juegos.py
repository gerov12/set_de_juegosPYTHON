'''Para guardar los datos de las partidas decidí utilizar una lista de diccionarios;
una lista ya que esta se ira expandiendo a medida que le agregue nuevas partidas y ademas es una estructura compatible con el formato de archivo que elegí.
La lista contiene diccionarios ya que estos me permitieron guardar para cada partida los datos necesarios (tiempo, nick del jugador, juego elegido, etc.) y luego accederlos facilmente gracias a las keys.
Elegí el formato JSON porque era el formato mas simple para guardar los tipos de datos que el programa manipula (cadenas y numeros),
no vi necesidad de usar un archivo binario, y un CSV no me daba la comodidad de acceder a los datos de las partidas por medio de las keys como si lo hizo JSON.
'''


import reversegam
import tictactoeModificado
import ahorcadoConFunciones
import PySimpleGUI as sg
import time
import json

sg.ChangeLookAndFeel('DarkAmber')

layout = [[sg.Text(time.strftime("%d/%m/%y")+" - "+time.strftime("%H:%M"))],
			[sg.Text("Ingrese su nick"),sg.Button("Historial de partidas")],
			[sg.Input(key="nickname")],
			[sg.Text("Seleccione un juego")],
			[sg.Listbox(values = ["Ahorcado", "TA-TE-TI","Otello"],select_mode="LISTBOX_SELECT_MODE_SINGLE",size=(50,5), key="LB")],
			[sg.Button("Jugar"),sg.Button("Salir")]
]

def main(args):

	excepcion = False

	try:
		archivo = open("Historial.txt", "x")
		partidas = []
	except FileExistsError:
		archivo = open("Historial.txt", "r")
		partidas = json.load(archivo)
		archivo.close()
		excepcion = True

	while True:

		window = sg.Window('GAMES').Layout(layout)

		event, values = window.Read()
		window.Close()                              #la ventana se cierra al jugar y se abre nuevamente al finalizar
		if event in (None, "Salir"):
			break
		elif event == "Jugar" and len(values["LB"]):
			horaJ = time.strftime("%H:%M")
			inicio = time.time()
			selected = values["LB"]
			if "Ahorcado" in selected:
				ahorcadoConFunciones.main()
			elif "TA-TE-TI" in selected:
				tictactoeModificado.main()
			elif "Otello" in selected:
				reversegam.main()

			datos = {
				"Fecha": time.strftime("%d/%m/%y"),
				"Hora": horaJ,
	            "Tiempo": int(time.time() - inicio),
	            "Nick": values["nickname"],
				"Juego": selected[0]
	        }
			partidas.append(datos)

			print("Por favor, vuelva a la ventana para seleccionar otro juego")
		elif event == "Historial de partidas":
			salida =[]
			for p in partidas:
				aux = "{} - {}hs\
				\n{} jugó al {}\
				\ndurante {} segundos".format(p["Fecha"],p["Hora"],p["Nick"],p["Juego"],str(p["Tiempo"]))
				salida.append(aux)
			layoutH = [[sg.Listbox(salida, size=(60,10))],
			[sg.Exit()]]
			window2 = sg.Window('Historial').Layout(layoutH)
			eventos, valores = window2.Read()
			window2.Close()

	if excepcion: #si el archivo ya existia lo sobreescribo con el nuevo historial
		archivo = open("Historial.txt", "w")
	json.dump(partidas, archivo) #si no guardo el historial en el nuevo archivo
	archivo.close()

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
