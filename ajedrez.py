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

BR = '\u265C'
BN = '\u265E'
BB = '\u265D'
BQ = '\u265B'
BK = '\u265A'
BP = '\u265F'

WR = '\u2656'
WN = '\u2658'
WP = '\u2659'
WQ = '\u2655'
WK = '\u2654'
WB = '\u2657'

a8 = Button(tk, text=BR, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(a8), btnID('a8')])
a8.grid(row=1, column=1)
b8 = Button(tk, text=BN, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(b8), btnID('b8')])
b8.grid(row=1, column=2)
c8 = Button(tk, text=BB, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(c8), btnID('c8')])
c8.grid(row=1, column=3)
d8 = Button(tk, text=BQ, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(d8), btnID('d8')])
d8.grid(row=1, column=4)
e8 = Button(tk, text=BK, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(e8), btnID('e8')])
e8.grid(row=1, column=5)
f8 = Button(tk, text=BB, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(f8), btnID('f8')])
f8.grid(row=1, column=6)
g8 = Button(tk, text=BN, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(g8), btnID('g8')])
g8.grid(row=1, column=7)
h8 = Button(tk, text=BR, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(h8), btnID('h8')])
h8.grid(row=1, column=8)
a7 = Button(tk, text=BP, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(a7), btnID('a7')])
a7.grid(row=2, column=1)
b7 = Button(tk, text=BP, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(b7), btnID('b7')])
b7.grid(row=2, column=2)
c7 = Button(tk, text=BP, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(c7), btnID('c7')])
c7.grid(row=2, column=3)
d7 = Button(tk, text=BP, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(d7), btnID('d7')])
d7.grid(row=2, column=4)
e7 = Button(tk, text=BP, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(e7), btnID('e7')])
e7.grid(row=2, column=5)
f7 = Button(tk, text=BP, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(f7), btnID('f7')])
f7.grid(row=2, column=6)
g7 = Button(tk, text=BP, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(g7), btnID('g7')])
g7.grid(row=2, column=7)
h7 = Button(tk, text=BP, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(h7), btnID('h7')])
h7.grid(row=2, column=8)
a6 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(a6), btnID('a6')])
a6.grid(row=3, column=1)
b6 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(b6), btnID('b6')])
b6.grid(row=3, column=2)
c6 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(c6), btnID('c6')])
c6.grid(row=3, column=3)
d6 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(d6), btnID('d6')])
d6.grid(row=3, column=4)
e6 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(e6), btnID('e6')])
e6.grid(row=3, column=5)
f6 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(f6), btnID('f6')])
f6.grid(row=3, column=6)
g6 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(g6), btnID('g6')])
g6.grid(row=3, column=7)
h6 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(h6), btnID('h6')])
h6.grid(row=3, column=8)
a5 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(a5), btnID('a5')])
a5.grid(row=4, column=1)
b5 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(b5), btnID('b5')])
b5.grid(row=4, column=2)
c5 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(c5), btnID('c5')])
c5.grid(row=4, column=3)
d5 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(d5), btnID('d5')])
d5.grid(row=4, column=4)
e5 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(e5), btnID('e5')])
e5.grid(row=4, column=5)
f5 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(f5), btnID('f5')])
f5.grid(row=4, column=6)
g5 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(g5), btnID('g5')])
g5.grid(row=4, column=7)
h5 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(h5), btnID('h5')])
h5.grid(row=4, column=8)
a4 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(a4), btnID('a4')])
a4.grid(row=5, column=1)
b4 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(b4), btnID('b4')])
b4.grid(row=5, column=2)
c4 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(c4), btnID('c4')])
c4.grid(row=5, column=3)
d4 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(d4), btnID('d4')])
d4.grid(row=5, column=4)
e4 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(e4), btnID('e4')])
e4.grid(row=5, column=5)
f4 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(f4), btnID('f4')])
f4.grid(row=5, column=6)
g4 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(g4), btnID('g4')])
g4.grid(row=5, column=7)
h4 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(h4), btnID('h4')])
h4.grid(row=5, column=8)
a3 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(a3), btnID('a3')])
a3.grid(row=6, column=1)
b3 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(b3), btnID('b3')])
b3.grid(row=6, column=2)
c3 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(c3), btnID('c3')])
c3.grid(row=6, column=3)
d3 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(d3), btnID('d3')])
d3.grid(row=6, column=4)
e3 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(e3), btnID('e3')])
e3.grid(row=6, column=5)
f3 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(f3), btnID('f3')])
f3.grid(row=6, column=6)
g3 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(g3), btnID('g3')])
g3.grid(row=6, column=7)
h3 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(h3), btnID('h3')])
h3.grid(row=6, column=8)
a2 = Button(tk, text=WP, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(a2), btnID('a2')])
a2.grid(row=7, column=1)
b2 = Button(tk, text=WP, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(b2), btnID('b2')])
b2.grid(row=7, column=2)
c2 = Button(tk, text=WP, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(c2), btnID('c2')])
c2.grid(row=7, column=3)
d2 = Button(tk, text=WP, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(d2), btnID('d2')])
d2.grid(row=7, column=4)
e2 = Button(tk, text=WP, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(e2), btnID('e2')])
e2.grid(row=7, column=5)
f2 = Button(tk, text=WP, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(f2), btnID('f2')])
f2.grid(row=7, column=6)
g2 = Button(tk, text=WP, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(g2), btnID('g2')])
g2.grid(row=7, column=7)
h2 = Button(tk, text=WP, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(h2), btnID('h2')])
h2.grid(row=7, column=8)
a1 = Button(tk, text=WR, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(a1), btnID('a1')])
a1.grid(row=8, column=1)
b1 = Button(tk, text=WN, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(b1), btnID('b1')])
b1.grid(row=8, column=2)
c1 = Button(tk, text=WB, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(c1), btnID('c1')])
c1.grid(row=8, column=3)
d1 = Button(tk, text=WQ, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(d1), btnID('d1')])
d1.grid(row=8, column=4)
e1 = Button(tk, text=WK, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(e1), btnID('e1')])
e1.grid(row=8, column=5)
f1 = Button(tk, text=WB, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(f1), btnID('f1')])
f1.grid(row=8, column=6)
g1 = Button(tk, text=WN, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick(g1), btnID('g1')])
g1.grid(row=8, column=7)
h1 = Button(tk, text=WR, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick(h1), btnID('h1')])
h1.grid(row=8, column=8)

class Figure(object):
	def __init__(self, name, object_name, color, pos1, posibles_mov):
		self.object_name = object_name
		self.name = name
		self.color = color
		self.posicion = pos1
		self.posibles_mov = posibles_mov

	def update_position():
		self.posicion = pe   