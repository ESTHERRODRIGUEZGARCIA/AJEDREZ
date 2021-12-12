# AJEDREZ

Mi dirección de github para este repositorio es la siguiente:

https://github.com/ESTHERRODRIGUEZGARCIA/AJEDREZ.git

Vamos a realizar el juego del ajedrez. La primera tarea consiste en escribir un programa que guarde en un fichero la secuencia de tableros de una partida de ajedrez. Partiremos del tablero inicial donde las filas del tablero están separadas por cambios de línea y las columnas por tabuladores.

♜	 ♞	 ♝	 ♛  	♚	   ♝	   ♞	   ♜

♟	♟	♟	♟	♟	♟	♟	♟
							
							



							
♙	♙	♙	♙	♙	 ♙	♙	 ♙

♖	♘	♗	♕	♔	♗	♘	♖

El programa debe guardar el tablero inicial en un fichero con el nombre que elija el usuario. Después debe preguntar al usuario si quiere hacer un movimiento o terminar la partida. Cada vez que el usuario quiera hacer un nuevo movimiento debe preguntar la fila y la columna de la pieza que quiere mover y la fila y la columna a la que la quiere mover. Tras ello añadirá el tablero resultante al final del fichero anterior.

Además, una vez generado el fichero con los tableros sucesivos de una partida de ajedrez, el programa preguntará por un movimiento y mostrará por pantalla el tablero correspondiente ese movimiento. Por ejemplo, utilizando el fichero partida-ajedrez.txt, si el usuario introduce el movimiento 2, debería mostrar por pantalla el siguiente tablero:

![image](https://user-images.githubusercontent.com/91721860/145718160-454dccbc-6904-4623-96d2-a644590a28f8.png)



Hemos resuelto el juego del ajedrez. El diagrama de flujo que tenemos en nuestro código es el siguiente:

![image](https://user-images.githubusercontent.com/91721860/145719244-a2e923d1-4dab-4383-ae08-2a98e6841347.png)


El código utilizado:

'''

import chess 
board=('♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖') 
#tupla pues este tablero es siempre el mismo
print(board)
def partida(tablero):
    board = []

    tablero = board #es una lista puesto que hay que modificarla 
    board_list = board.split(" ") #solucionar excepcion 'list' object has no attribute 'split'
    for i in board_list.split('\n'): #split para separar los elementos del tablero, vertical y horizontalmente
        tablero.append(i.split('\t'))
        print(board_list)
    file = open(tablero, "w") #Modo de Escritura (Write)

    for i in board:
        file.write('\t'.join(i) + '\n') #si convertimos una cadena en lista podremos modificarla. Y luego volver a convertirla en cadena.
        #junto los elementos
    file.close()
    #comienza la partida
    turno = 0 #no se ha jugado todavía
    while True:
        continuar = str(input("¿Quiere seguir jugando? \n Posibles respuestas: Si/No"))
        if continuar != "Si":
            break
        elif continuar == "Si": 
            #la pieza está en una posición, el usuario debe moverla
            fila1 = int(input("Introduce la fila en la que está la ficha que quieres mover: "))
            columna1 = int(input("Introduce la columna en la que está la ficha que quieres mover: "))
            fila2 = int(input("Introduce la fila hacia donde quieres mover la ficha: "))
            columna2 = int(input("Introduce la columna donde quieres mover la ficha: "))
            tablero = tablero[fila1 + columna1 + fila2 + columna2]
            turno += 1
            file = open(tablero, "a") #Modo de Solo escritura al final (“a”)
            file.write("Has realizado ", str(turno), "movimientos \n")
            for i in board:
                file.write('\t'.join(i) + '\n')
                #junto los elementos
            file.close()
    return 

partida("1 ")

'''
