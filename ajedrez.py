#AJEDREZ
#tablero de 8 * 8
from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.title('AJEDREZ')
tkcomienzo = ''
tkfin = ''
boton1 = ''
boton2 = ''
color2 = ''
color1 = ''
error = ''

def btnClick(botones):
    global boton1, boton2, color2, color1, boton1text, boton2text
    if tkcomienzo != '':
        boton2 = botones
        color2 = botones['bg']
        boton2text = botones['text']
    if tkfin == '' and tkcomienzo == '':
        boton1 = botones
        boton1 = botones['bg']
        boton1texto = botones['text']

def undo_coloring():
	for i in fields_dic:
		if fields_dic[i]['fg'] == 'luz verde':
			fields_dic[i]['fg'] = 'black'
		if fields_dic[i]['text'] == '\u0E4F':
			fields_dic[i]['text'] = ''	

def btnID(id):
	global tkcomienzo, tkfin, boton1, boton2, error, jug_blancos, jug_negros, fields_dic, turno, error
	cuadrado_color = []
	fields_dic = {'a1':a1,'a2': a2,'a3': a3,'a4': a4,'a5':a5,'a6':a6,'a7':a7,'a8':a8,'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6,'b7':b7,'b8':b8,'c2':c1,'c2':c2,'c3':c3,'c4':c4,'c5':c5,'c6':c6,'c7':c7,'c8':c8,'d1':d1,'d2':d2,'d3':d3,'d4':d4,'d5':d5,'d6':d6,'d7':d7,'d8':d8,'e1':e1,'e2':e2,'e3':e3,'e4':e4,'e5':e5,'e6':e6,'e7':e7,'e8':e8,'f1':f1,'f2':f2,'f3':f3,'f4':f4,'f5':f5,'f6':f6,'f7':f7,'f8':f8,'g1':g1,'g2':g2,'g3':g3,'g4':g4,'g5':g5,'g6':g6,'g7':g7,'g8':g8,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6,'h7':h7,'h8':h8}
	if error != 4:
		if tkcomienzo != '':
			tkfin = id
		if turno == 'W' and (boton1['text'] in [WR, WN, WP, WQ, WK, WB] or boton1['text'] ==  WK + '\nBien!'):
			if tkfin == '' and tkcomienzo == '' and boton1['text'] != '':
				tkcomienzo = id
				boton1['bg'] = 'luz verde'
		elif turno == 'B' and (boton1['text'] in [BR, BN, BP, BQ, BK, BB] or boton1['text'] ==  BK + '\nBien!'):
			if tkfin == '' and tkcomienzo == '' and boton1['text'] != '':
				tkcomienzo = id
				boton1['bg'] = 'luz verde'	

		if tkcomienzo != '' and tkfin == '': 
			posiciones()
			trad_a = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7}
			trad_b = {'8' : 0, '7' : 1, '6' : 2, '5' : 3, '4' : 4, '3' : 5, '2' : 6, '1' : 7}
			pos1 = (trad_b[tkcomienzo[1]], trad_a[tkcomienzo[0]])
			trad_a_1 = {0 : 'a', 1 : 'b' , 2 : 'c', 3 : 'd', 4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h'}
			trad_b_2 = {0 : '8', 1 : '7', 2 : '6', 3 : '5', 4 : '4', 5 : '3', 6 : '2', 7 : '1'}
			if turno == 'W':
				for i in jug_blancos:
					if i.posicion == pos1:
						for i in i.posibles_mov:
							fn = trad_a_1[i[1]]
							sn = trad_b_2[i[0]]
							fld = fn+sn
							for item in fields_dic:
								if item == fld:
									cuadrado_color.append(item)
									fields_dic[item]['fg'] = 'luz verde'
									if fields_dic[item]['text'] == '':
										fields_dic[item]['text'] = '\u0E4F'
			else:
				for i in jug_blancos:
					if i.position == pos1:
						for i in i.posibles_mov:
							fn = trad_a_1[i[1]]
							sn = trad_b_2[i[0]]
							fld = fn+sn
							for item in fields_dic:
								if item == fld:
									cuadrado_color.append(item)
									fields_dic[item]['fg'] = 'luz verde'
									if fields_dic[item]['text'] == '':
										fields_dic[item]['text'] = '\u0E4F'
				
		
		
		if tkcomienzo != '' and tkfin != '':
			main()
			if error == '':
				tkcomienzo = ''
				tkfin = ''
				boton1['bg'] = color2
				if color2 == 'luz verde':
					boton2['bg'] = color1
				else:
					boton2['bg'] = color2				
				boton1['text'] = ''
				boton2['text'] = boton1text
				fields = [a1,a2,a3,a4,a5,a6,a7,a8,b1,b2,b3,b4,b5,b6,b7,b8,c1,c2,c3,c4,c5,c5,c6,c7,c8,d1,d2,d3,d4,d5,d6,d7,d8,e1,e2,e3,e4,e5,e6,e7,e8,f1,f2,f3,f4,f5,f6,f7,f8,g1,g2,g3,g4,g5,g6,g7,g8,h1,h2,h3,h4,h5,h6,h7,h8]
				for i in fields:
					if i['text'] == BK + '\nBien!':
						i['text'] = BK
					if i['text'] == WK + '\nBien!':
						i['text'] = WK
				error = ''
				undo_coloring()
			elif error == 3:
				tkcomienzo = ''
				tkfin = ''
				boton1['bg'] = color1
				if color2 == 'luz verde':
					boton2['bg'] = color1
				else:
					boton2['bg'] = color2				
				boton1['text'] = ''
				boton2['text'] = boton1_text
				cuadrados = [a1,a2,a3,a4,a5,a6,a7,a8,b1,b2,b3,b4,b5,b6,b7,b8,c1,c2,c3,c4,c5,c5,c6,c7,c8,d1,d2,d3,d4,d5,d6,d7,d8,e1,e2,e3,e4,e5,e6,e7,e8,f1,f2,f3,f4,f5,f6,f7,f8,g1,g2,g3,g4,g5,g6,g7,g8,h1,h2,h3,h4,h5,h6,h7,h8]
				if turno == 'B':
					for i in cuadrados:
						if i['text'] == BK:
							i['text'] = BK + '\nBien!'
				elif turno == 'W':
					for i in cuadrados:
						if i['text'] == WK:
							i['text'] = WK + '\nBien!'	
				tkcomienzo = ''
				tkfin = ''
				boton1['bg'] = color1
				if color2 == 'luz verde':
					boton2['bg'] = color1
				else:
					boton2['bg'] = color2	
				error = ''
				undo_coloring()
			elif error == 2:
				tkcomienzo = ''
				tkfin = ''
				boton1['bg'] = color1
				if color2 == 'luz verde':
					boton2['bg'] = color1
				else:
					boton2['bg'] = color2				
				boton1['text'] = ''
				boton2['text'] = boton1text
				cuadrados = [a1,a2,a3,a4,a5,a6,a7,a8,b1,b2,b3,b4,b5,b6,b7,b8,c1,c2,c3,c4,c5,c5,c6,c7,c8,d1,d2,d3,d4,d5,d6,d7,d8,e1,e2,e3,e4,e5,e6,e7,e8,f1,f2,f3,f4,f5,f6,f7,f8,g1,g2,g3,g4,g5,g6,g7,g8,h1,h2,h3,h4,h5,h6,h7,h8]
				if turno == 'W':
					for i in cuadrados:
						if i['text'] == BK:
							i['text'] = BK + '\nbien \nmate!'
				elif turno == 'B':
					for i in cuadrados:
						if i['text'] == WK:
							i['text'] = WK + '\nbien \nmate!'	
				tkcomienzo = ''
				tkfin = ''
				boton1['bg'] = color1
				if color1 == 'luz verde':
					boton2['bg'] = color1
				else:
					boton2['bg'] = color2	
				error = 4	
				undo_coloring()		
			else:
				tkcomienzo = ''
				tkfin = ''
				boton1['bg'] = color1
				if color2 == 'luz verde':
					boton2['bg'] = color1
				else:
					boton2['bg'] = color2	
				error = ''
				undo_coloring()