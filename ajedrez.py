#AJEDREZ
#tablero de 8 * 8
def partida(tablero):
    tablero1 = { 
    U+2656: ♜, 
    U+2658: ♞, 
    chr(U+2657): ♝, 
    chr(U+2655): ♛, 
    chr(U+2654): ♚, 
    chr(U+2657): ♝,
    chr(U+2658): ♞,
    chr(U+2656): ♜,
    chr(U+2659): ♟,
    chr(U+2659): ♟,
    chr(U+2659): ♟,
    chr(U+2659): ♟,
    chr(U+2659): ♟,
    chr(U+2659): ♟,
    chr(U+2659): ♟,
    chr(U+2659): ♟, 
    }
print("Ficha: {}".format(" ".join(tablero1.keys())))
print("Valor: {}".format(list(tablero1.values())))
    '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    tablero =[] #es una lista puesto que hay que modificarla
    for i in tablero1.split('\n'): #split para separar los elementos del tablero, vertical y horizontalmente
        tablero.append(i.split('\t'))
    
    file = open(tablero)

    for i in tablero1:
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
            for i in tablero1:
                file.write('\t'.join(i) + '\n')
                #junto los elementos
            file.close()
    return 


partida(tablero)    


