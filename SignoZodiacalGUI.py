from tkinter import *
from SignoZodiacalFuncion import *

root = Tk()
root.title("Zodiac Room")
root.resizable(1,1)
root.geometry("500x282")
root.iconbitmap("Planetarium.ico")

bg = PhotoImage(file="imagenes\Planetarium_Room.png")
canvas1 = Canvas(root, width=500, height=282)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
canvas1.pack(fill = "both", expand = True)

mesesCon30Dias =[4,6,9,11]
primera_activacion=True
drop_menu_dia = ""
dia_var=StringVar()

def mes_seleccionado(x):
    global primera_activacion, drop_menu_dia, dia_var
    if not primera_activacion:
        drop_menu_dia.destroy()
    y = 32
    if x in mesesCon30Dias:
        y = 31
    if x == 2:
        y = 30
    dia_list = (range(1, y))
    dia_var.set(dia_list[0])
    drop_menu_dia = OptionMenu(root, dia_var, *dia_list)
    canvas1.create_window(290, 125, anchor=CENTER, window= drop_menu_dia)
    primera_activacion =False
    return dia_var

def boton_aceptar_funcion():
    mes = mes_var.get()
    dia = dia_var.get()
    signo_Zodiacal = Signo_zodiacal(mes, dia)
    canvas1.itemconfig(canvas_resultado, text= signo_Zodiacal)
    """
    #Esta es otra manera para hacerlo pero con label, queda mas feo
    #Si la vas a usar comenta la forma de abajo y descomenta la creacion de los labels
    imagen_aspecto = PhotoImage(file=(diccionario_aspecto[signo_Zodiacal]))
    label_aspecto.config(image=imagen_aspecto)
    label_aspecto.image = imagen_aspecto
    imagen_signo = PhotoImage(file=(diccionario_signo[signo_Zodiacal]))
    label_signo.config(image=imagen_signo)
    label_signo.image = imagen_signo
    """
    imagen_aspecto_funcion = PhotoImage(file=(diccionario_aspecto[signo_Zodiacal]))
    canvas1.itemconfig(canvas_imagen_aspecto, image=imagen_aspecto_funcion)
    label_aspecto.image = imagen_aspecto_funcion
    #canvas_imagen_aspecto.image = imagen_aspecto
    imagen_signo_funcion = PhotoImage(file=(diccionario_signo[signo_Zodiacal]))
    canvas1.itemconfig(canvas_imagen_signo, image=imagen_signo_funcion)
    label_signo.image = imagen_signo_funcion
    #No entiendo porque cuando lo asigno a este labe(que no esta siendo usado) funciona
    #canvas1.canvas_imagen_signo.image = imagen_signo
    #No tengo idea de porque funciona cuando falla en esta linea, si la comento no anda nada
    

mes_list = (range(1, 13))
mes_var = StringVar()
mes_var.set(mes_list[0])
drop_menu_mes = OptionMenu(root, mes_var, *mes_list, command=mes_seleccionado)

boton_aceptar = Button(root, text="ACEPTAR", bd=0, command=boton_aceptar_funcion, font=("Upheaval TT (BRK)","12"))
imagen_aspecto = PhotoImage(file="imagenes\Character_Isaac_appearance.png")
imagen_signo = PhotoImage(file="imagenes\signo.png")
imagen_pedestal = PhotoImage(file="imagenes\pedestal.png")

label_aspecto = Label(root, textvariable="inicial" ,image=imagen_aspecto)
label_signo = Label(root, textvariable="inicial" ,image=imagen_signo)

canvas1_titulo = canvas1.create_text(250, 55, anchor=CENTER, text="INGRESA TU FECHA DE NACIMIENTO:", fill="white", font=("Upheaval TT (BRK)","12"))
canvas_imagen_aspecto = canvas1.create_image(250, 85, image=imagen_aspecto, anchor=CENTER)
#canvas_imagen_aspecto = canvas1.create_window(250, 85, anchor=CENTER,window=label_aspecto)
canvas_drop_menu_mes = canvas1.create_window(210, 125, anchor=CENTER, window= drop_menu_mes)
canvas_boton_aceptar = canvas1.create_window(250, 160, anchor=CENTER, window=boton_aceptar)
canvas_imagen_signo = canvas1.create_image(250, 190, image=imagen_signo, anchor=CENTER)
#canvas_imagen_signo = canvas1.create_window(250, 190, anchor=CENTER,window=label_signo)
canvas_imagen_pedestal = canvas1.create_image(250, 215, image=imagen_pedestal, anchor=CENTER)
canvas_resultado = canvas1.create_text(250, 242, anchor=CENTER, text="", fill="white", font=("Upheaval TT (BRK)","12"))

root.mainloop()