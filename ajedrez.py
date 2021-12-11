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
        boton2text = botones['texto']
    if tkfin == '' and tkcomienzo == '':
        boton1 = botones
        boton1 = botones['bg']
        boton1texto = botones['texto']
