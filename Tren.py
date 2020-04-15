from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import Tren_support

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Tren_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    root.withdraw
    Tren_support.set_Tk_var()
    top = Toplevel1 (root)
    Tren_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    w.withraw
    Tren_support.set_Tk_var()
    top = Toplevel1(w)
    Tren_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        ventana = Frame(top)
        ventana.place(x=98,y=4)
        ventana.config(bd=1, relief='ridge')

        img = Image.open(r'C:\Users\brian\Programación ll\train.png')
        image2 = img.resize((150, 100), Image.ANTIALIAS)
        tren = ImageTk.PhotoImage(image2, master=ventana)
        lbl_img = Label(ventana, image = tren, relief = GROOVE)
        lbl_img.grid()
        lbl_img.image = tren

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1366x705+-3+0")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Tren")
        top.configure(background="skyblue")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        tipoClase = IntVar(top, 0)
        def calc_Pasajeros_():
            Clase = 0
            ida_Vuelta = 1
            if tipoClase.get() != 1 and tipoClase.get() != 2 and tipoClase.get() != 3:
                messagebox.showinfo ('Ocurrió un error', 'Seleccione una clase válida', icon = 'error')
            elif tipoClase.get() == 1:
                Clase = 1
            elif tipoClase.get() == 2:
                Clase = 1.2
            elif tipoClase.get() == 3:
                Clase = 2
            if Ida_Vuelta.get() == 1:
                ida_Vuelta = 1.5
            calculo = round(int(self.cantPersonas.get())*Distancia.get()*Precio.get()*ida_Vuelta*Clase,2)
            totalMonto.set(calculo)
        self.txtViajeros = tk.Label(top)
        self.txtViajeros.place(relx=0.037, rely=0.156, height=18, width=76)
        self.txtViajeros.configure(activebackground="#f9f9f9")
        self.txtViajeros.configure(activeforeground="black")
        self.txtViajeros.configure(background="skyblue")
        self.txtViajeros.configure(disabledforeground="#a3a3a3")
        self.txtViajeros.configure(foreground="#000000")
        self.txtViajeros.configure(highlightbackground="#d9d9d9")
        self.txtViajeros.configure(highlightcolor="black")
        self.txtViajeros.configure(text='''Viajeros:''')

        self.cantPersonas = tk.Spinbox(top, from_=1.0, to=100.0)
        self.cantPersonas.place(relx=0.051, rely=0.184, relheight=0.041
                , relwidth=0.143)
        self.cantPersonas.configure(activebackground="#f9f9f9")
        self.cantPersonas.configure(background="#c0c0c0")
        self.cantPersonas.configure(buttonbackground="#d9d9d9")
        self.cantPersonas.configure(disabledforeground="#a3a3a3")
        self.cantPersonas.configure(font="TkDefaultFont")
        self.cantPersonas.configure(foreground="black")
        self.cantPersonas.configure(highlightbackground="black")
        self.cantPersonas.configure(highlightcolor="black")
        self.cantPersonas.configure(insertbackground="black")
        self.cantPersonas.configure(selectbackground="#c4c4c4")
        self.cantPersonas.configure(selectforeground="black")

        Ida_Vuelta = IntVar(top)
        self.txtIdaVuelta = tk.Checkbutton(top)
        self.txtIdaVuelta.place(relx=0.007, rely=0.227, relheight=0.054
                , relwidth=0.152)
        self.txtIdaVuelta.configure(activebackground="#ececec")
        self.txtIdaVuelta.configure(activeforeground="#000000")
        self.txtIdaVuelta.configure(background="skyblue")
        self.txtIdaVuelta.configure(disabledforeground="#a3a3a3")
        self.txtIdaVuelta.configure(foreground="#000000")
        self.txtIdaVuelta.configure(highlightbackground="#d9d9d9")
        self.txtIdaVuelta.configure(highlightcolor="black")
        self.txtIdaVuelta.configure(justify='left')
        self.txtIdaVuelta.configure(text='''Ida y vuelta''')
        self.txtIdaVuelta.configure(variable=Ida_Vuelta)

        self.txtTipoClase = tk.Label(top)
        self.txtTipoClase.place(relx=0.029, rely=0.27, height=32, width=76)
        self.txtTipoClase.configure(activebackground="#f9f9f9")
        self.txtTipoClase.configure(activeforeground="black")
        self.txtTipoClase.configure(background="skyblue")
        self.txtTipoClase.configure(disabledforeground="#a3a3a3")
        self.txtTipoClase.configure(foreground="#000000")
        self.txtTipoClase.configure(highlightbackground="#d9d9d9")
        self.txtTipoClase.configure(highlightcolor="black")
        self.txtTipoClase.configure(text='''Clase:''')

        self.txtTurista = tk.Radiobutton(top)
        self.txtTurista.place(relx=0.051, rely=0.312, relheight=0.041
                , relwidth=0.053)
        self.txtTurista.configure(activebackground="#ececec")
        self.txtTurista.configure(activeforeground="#000000")
        self.txtTurista.configure(background="skyblue")
        self.txtTurista.configure(disabledforeground="#a3a3a3")
        self.txtTurista.configure(foreground="#000000")
        self.txtTurista.configure(highlightbackground="#d9d9d9")
        self.txtTurista.configure(highlightcolor="black")
        self.txtTurista.configure(justify='left')
        self.txtTurista.configure(text='''Turista''')
        self.txtTurista.configure(variable=tipoClase)
        self.txtTurista.configure(value=1)

        self.txtPrimera = tk.Radiobutton(top)
        self.txtPrimera.place(relx=0.051, rely=0.355, relheight=0.027
                , relwidth=0.053)
        self.txtPrimera.configure(activebackground="#ececec")
        self.txtPrimera.configure(activeforeground="#000000")
        self.txtPrimera.configure(background="skyblue")
        self.txtPrimera.configure(disabledforeground="#a3a3a3")
        self.txtPrimera.configure(foreground="#000000")
        self.txtPrimera.configure(highlightbackground="#d9d9d9")
        self.txtPrimera.configure(highlightcolor="black")
        self.txtPrimera.configure(justify='left')
        self.txtPrimera.configure(text='''Primera''')
        self.txtPrimera.configure(variable=tipoClase)
        self.txtPrimera.configure(value=2)

        self.txtLujo = tk.Radiobutton(top)
        self.txtLujo.place(relx=0.044, rely=0.383, relheight=0.041
                , relwidth=0.053)
        self.txtLujo.configure(activebackground="#ececec")
        self.txtLujo.configure(activeforeground="#000000")
        self.txtLujo.configure(background="skyblue")
        self.txtLujo.configure(disabledforeground="#a3a3a3")
        self.txtLujo.configure(foreground="#000000")
        self.txtLujo.configure(highlightbackground="#d9d9d9")
        self.txtLujo.configure(highlightcolor="black")
        self.txtLujo.configure(justify='left')
        self.txtLujo.configure(text='''Lujo''')
        self.txtLujo.configure(variable=tipoClase)
        self.txtLujo.configure(value=3)

        self.txtDistancia = tk.Label(top)
        self.txtDistancia.place(relx=0.007, rely=0.44, height=21, width=214)
        self.txtDistancia.configure(activebackground="#f9f9f9")
        self.txtDistancia.configure(activeforeground="black")
        self.txtDistancia.configure(background="skyblue")
        self.txtDistancia.configure(disabledforeground="#a3a3a3")
        self.txtDistancia.configure(foreground="#000000")
        self.txtDistancia.configure(highlightbackground="#d9d9d9")
        self.txtDistancia.configure(highlightcolor="black")
        self.txtDistancia.configure(text='''Distancia (Kilómetros):''')

        Distancia = IntVar(top, 1)
        self.distanciaKm = tk.Entry(top)
        self.distanciaKm.place(relx=0.059, rely=0.482,height=20, relwidth=0.12)
        self.distanciaKm.configure(background="white")
        self.distanciaKm.configure(disabledforeground="#a3a3a3")
        self.distanciaKm.configure(font="TkFixedFont")
        self.distanciaKm.configure(foreground="#000000")
        self.distanciaKm.configure(highlightbackground="#d9d9d9")
        self.distanciaKm.configure(highlightcolor="black")
        self.distanciaKm.configure(insertbackground="black")
        self.distanciaKm.configure(selectbackground="#c4c4c4")
        self.distanciaKm.configure(selectforeground="black")
        self.distanciaKm.configure(textvariable=Distancia)

        self.txtPrecio = tk.Label(top)
        self.txtPrecio.place(relx=0.029, rely=0.525, height=21, width=76)
        self.txtPrecio.configure(activebackground="#f9f9f9")
        self.txtPrecio.configure(activeforeground="black")
        self.txtPrecio.configure(background="skyblue")
        self.txtPrecio.configure(disabledforeground="#a3a3a3")
        self.txtPrecio.configure(foreground="#000000")
        self.txtPrecio.configure(highlightbackground="#d9d9d9")
        self.txtPrecio.configure(highlightcolor="black")
        self.txtPrecio.configure(text='''Precio:''')

        Precio = DoubleVar(top, 0.1)
        self.entryPrecio = tk.Entry(top)
        self.entryPrecio.configure(textvariable=Precio)
        self.entryPrecio.place(relx=0.059, rely=0.567,height=20, relwidth=0.12)
        self.entryPrecio.configure(background="white")
        self.entryPrecio.configure(disabledforeground="#a3a3a3")
        self.entryPrecio.configure(font="TkFixedFont")
        self.entryPrecio.configure(foreground="#000000")
        self.entryPrecio.configure(highlightbackground="#d9d9d9")
        self.entryPrecio.configure(highlightcolor="black")
        self.entryPrecio.configure(insertbackground="black")
        self.entryPrecio.configure(selectbackground="#c4c4c4")
        self.entryPrecio.configure(selectforeground="black")

        self.txtPagarEuros = tk.Label(top)
        self.txtPagarEuros.place(relx=0.037, rely=0.61, height=21, width=82)
        self.txtPagarEuros.configure(activebackground="#f9f9f9")
        self.txtPagarEuros.configure(activeforeground="black")
        self.txtPagarEuros.configure(background="skyblue")
        self.txtPagarEuros.configure(disabledforeground="#a3a3a3")
        self.txtPagarEuros.configure(foreground="#000000")
        self.txtPagarEuros.configure(highlightbackground="#d9d9d9")
        self.txtPagarEuros.configure(highlightcolor="black")
        self.txtPagarEuros.configure(text='''A pagar euros:''')

        totalMonto = IntVar()
        self.montoEuros = tk.Entry(top)
        self.montoEuros.configure(textvariable=totalMonto)
        self.montoEuros.place(relx=0.059, rely=0.652,height=20, relwidth=0.12)
        self.montoEuros.configure(background="#000000")
        self.montoEuros.configure(disabledforeground="#a3a3a3")
        self.montoEuros.configure(font="-family {Times New Roman} -size 11")
        self.montoEuros.configure(foreground="#ffff00")
        self.montoEuros.configure(highlightbackground="#d9d9d9")
        self.montoEuros.configure(highlightcolor="black")
        self.montoEuros.configure(insertbackground="black")
        self.montoEuros.configure(selectbackground="#c4c4c4")
        self.montoEuros.configure(selectforeground="black")

        self.frameCalSalir = tk.Frame(top)
        self.frameCalSalir.place(relx=0.044, rely=0.723, relheight=0.105
                , relwidth=0.135)
        self.frameCalSalir.configure(relief='groove')
        self.frameCalSalir.configure(borderwidth="2")
        self.frameCalSalir.configure(relief="groove")
        self.frameCalSalir.configure(background="skyblue")
        self.frameCalSalir.configure(highlightbackground="#d9d9d9")
        self.frameCalSalir.configure(highlightcolor="black")

        self.btnCal = tk.Button(self.frameCalSalir)
        self.btnCal.place(relx=0.108, rely=0.27, height=34, width=57)
        self.btnCal.configure(activebackground="#ececec")
        self.btnCal.configure(activeforeground="#000000")
        self.btnCal.configure(background="skyblue")
        self.btnCal.configure(disabledforeground="#a3a3a3")
        self.btnCal.configure(foreground="#000000")
        self.btnCal.configure(highlightbackground="#d9d9d9")
        self.btnCal.configure(highlightcolor="black")
        self.btnCal.configure(pady="0")
        self.btnCal.configure(text='''Calcular''')
        self.btnCal.configure(command=calc_Pasajeros_)


        self.btnSalir = tk.Button(self.frameCalSalir)
        self.btnSalir.place(relx=0.541, rely=0.27, height=34, width=57)
        self.btnSalir.configure(activebackground="#ececec")
        self.btnSalir.configure(activeforeground="#000000")
        self.btnSalir.configure(background="skyblue")
        self.btnSalir.configure(disabledforeground="#a3a3a3")
        self.btnSalir.configure(foreground="#000000")
        self.btnSalir.configure(highlightbackground="#d9d9d9")
        self.btnSalir.configure(highlightcolor="black")
        self.btnSalir.configure(pady="0")
        self.btnSalir.configure(text='''Salir''')
        self.btnSalir.configure(command=root.destroy)

if __name__ == '__main__':
    vp_start_gui()
