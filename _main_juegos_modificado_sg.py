import json
import time
import PySimpleGUI as sg
import hangmanEs
import reversegamEs
import tictactoeModificadoEs


def mostrar_mensaje():
	sg.Popup("*"*7 + " No ingresaste un nombre " + "*"*7, title="Ups!!")
	
def guardar_datos(nombre, event, lista):
	#Registro la hora
    dia_y_hora = time.strftime("%d/%m/%Y, %H:%M:%S")
    #Cargo la información en una lista
    lista.append([nombre, [event, dia_y_hora]])
    
def copiar(lista):
	with open("registro_juegos.json", "a") as archivo_datos:
		for info in lista:
			dic = { info[0]:info[1] }
			json.dump(dic, archivo_datos, indent=4)
		archivo_datos.close()

def main(args):
	sg.theme("LightBrown5")
#	sg.theme("DarkBlue4")	

	sigo_jugando = True 
	lista = []
	
	while sigo_jugando:	
	
		layout = [  
			[sg.Text(" ")],
			[sg.Text(" ", size=(6,1)), sg.Text("Nombre del jugador: ", size=(15,1)), sg.Text(" ", size=(6,1))], 
			[sg.Text(" ", size=(1,1)), sg.Input(key="nombre", size=(27,1)), sg.Text(" ", size=(1,1))],
			[sg.Text(" ", size=(4,1)), sg.Text("A qué juego querés jugar? "), sg.Text(" ", size=(1,1))], 
			[sg.Text(" ", size=(8,1)), sg.Button("Ahorcado", size=(10,1)), sg.Text(" ", size=(8,1))],
			[sg.Text(" ", size=(8,1)), sg.Button("Ta-Te-Ti", size=(10,1)), sg.Text(" ", size=(8,1))], 
			[sg.Text(" ", size=(8,1)), sg.Button("Otello", size=(10,1)), sg.Text(" ", size=(8,1))],
			[sg.Text(" ")],
			[sg.Text(" ", size=(9,1)), sg.Button("Salir", size=(8,1), button_color = ("white", "brown"))],
			[sg.Text(" ")]
		]

		window = sg.Window("::::::::: JUEGOS :::::::::", layout)
		window.Finalize()
		
		event, values = window.Read()	
		
		if event in ("Salir", None):
			sigo_jugando = False
			copiar(lista)
		elif values["nombre"].replace(" ", "") is "":
			window.Close()
			mostrar_mensaje()
		elif event is "Ahorcado":
			guardar_datos(values["nombre"], event, lista)
			window.Close()
			hangmanEs.main()
		elif event is "Ta-Te-Ti":
			guardar_datos(values["nombre"], event, lista)
			window.Close()
			tictactoeModificadoEs.main()
		elif event is "Otello":
			guardar_datos(values["nombre"], event, lista)
			window.Close()
			reversegamEs.main()

		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
