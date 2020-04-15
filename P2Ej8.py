cadena = input('Ingrese una palabra: ')

cadena = cadena.replace(' ', '')
# PASAR LAS LETRAS A UNa TUPLA(?) Y DESPUES HACER EL FOR CON LAS LETRAS QUE ESTAN EN EL CONJUNTO (NO REPETIDAS)
#EN LA TUPLA SE PUEDE GUARDAR LA LETRA Y LA CANTIDAD DE VECES Q APARECE
registro = ()
tam = 0
cant = 0

for letra in cadena:
    registro.add(letra)

tam = len(registro)
       
for i in range(tam):
    for letra in cadena:
        if (letra == registro[i]):
            cant = cant + 1
    print('La letra ', letra, ' se repite ', cant, ' veces. ')
    cant = 0
