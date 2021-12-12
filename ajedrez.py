#AJEDREZ
#tablero de 8 * 8
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


partida("partida1.txt ")

#tarea2
def board(tablero, n):
    
    file = open(tablero, 'r')#método readline, lo abre  solo para ser leído; no puede ser editado.
    tableros = file.read().split('\n')
    for i in tableros[n*9:n*9+8]:
            print(i)
    return

board('partida1.txt', 2)



