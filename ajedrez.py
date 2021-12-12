#AJEDREZ
#tablero de 8 * 8
import chess 
  
board=('♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖') 
  
print(board)
def partida(tablero):
    board = []

    tablero = board #es una lista puesto que hay que modificarla
    for i in board.split('\n'): #split para separar los elementos del tablero, vertical y horizontalmente
        tablero.append(i.split('\t'))
    
    file = open(tablero)

    for i in board:
        file.write('\t'.join(i) + '\n')
        #junto los elementos
    file.close()
    #comienza la partida
    turno = 0 #no se ha jugado todavía
    while True:
        continuar = str(input("¿Quiere seguir jugando? \n Posibles respuestas: Si/No"))
        if continuar == "No":
            break
        elif continuar == "Si": 
            #la pieza está en una posición, el usuario debe moverla
            fila1 = int(input("Introduce la fila en la que está la ficha que quieres mover: "))
            columna1 = int(input("Introduce la columna en la que está la ficha que quieres mover: "))
            fila2 = int(input("Introduce la fila hacia donde quieres mover la ficha: "))
            columna2 = int(input("Introduce la columna donde quieres mover la ficha: "))
            tablero = tablero[fila1 + columna1 + fila2 + columna2]
            turno += 1
            file = open(tablero)
            file.write("Has realizado ", turno, "movimientos")
            for i in board:
                file.write('\t'.join(i) + '\n')
                #junto los elementos
            file.close()
    return 


partida(" ")


