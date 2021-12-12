# AJEDREZ

Vamos a realizar el juego de la ajedrez. La primera tarea consiste en escribir un programa que guarde en un fichero la secuencia de tableros de una partida de ajedrez. Partiremos del tablero inicial donde las filas del tablero están separadas por cambios de línea y las columnas por tabuladores.

♜	 ♞	 ♝	 ♛  	♚	   ♝	   ♞	   ♜

♟	♟	♟	♟	♟	♟	♟	♟
							
							



							
♙	♙	♙	♙	♙	 ♙	♙	 ♙

♖	♘	♗	♕	♔	♗	♘	♖

El programa debe guardar el tablero inicial en un fichero con el nombre que elija el usuario. Después debe preguntar al usuario si quiere hacer un movimiento o terminar la partida. Cada vez que el usuario quiera hacer un nuevo movimiento debe preguntar la fila y la columna de la pieza que quiere mover y la fila y la columna a la que la quiere mover. Tras ello añadirá el tablero resultante al final del fichero anterior.

Además, una vez generado el fichero con los tableros sucesivos de una partida de ajedrez, el programa preguntará por un movimiento y mostrará por pantalla el tablero correspondiente ese movimiento. Por ejemplo, utilizando el fichero partida-ajedrez.txt, si el usuario introduce el movimiento 2, debería mostrar por pantalla el siguiente tablero:

♜	♞	♝	♛	♚	♝	♞	♜

♟	♟	♟		♟	♟	♟	♟
							
			  ♟				
						     ♙	
							
♙	♙	♙	♙	♙	♙		♙

♖	♘	♗	♕	♔	♗	♘	♖
