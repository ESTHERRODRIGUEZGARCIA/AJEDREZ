#AJEDREZ
#tablero de 8 * 8
def partida():
    tablero1 = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    tablero =[] #es una lista puesto que hay que modificarla
    for i in tablero1.split('\n'): #split para separar los elementos del tablero, vertical y horizontalmente
        tablero.append(i.split('\t'))
    
    file = open(tablero1)
    print(file.tablero1())

    for i in tablero1:
        file.write('\t'.join(i) + '\n')
        #junto los elementos
    file.close()
partida('partida1.txt')    


