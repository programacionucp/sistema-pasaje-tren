#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Apr 14, 2020 03:43:12 PM -03  platform: Windows NT
########################## Proyecto Sistema Pasajes de Tren#########################################################
########################## Ramirez Damian Andres ###################################################################

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

import Viajero01_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    Viajero01_support.set_Tk_var()
    top = Toplevel1 (root)
    Viajero01_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    Viajero01_support.set_Tk_var()
    top = Toplevel1 (w)
    Viajero01_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Arial} -size 14"
        font9 = "-family {Arial} -size 12"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("298x648+626+43")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Agencia de tour")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#646464646464")

        self.Viajeros = ttk.Label(top)
        self.Viajeros.place(relx=0.07, rely=0.164, height=41, width=1192)
        self.Viajeros.configure(background="#d9d9d9")
        self.Viajeros.configure(foreground="#000000")
        self.Viajeros.configure(font="-family {Arial} -size 12")
        self.Viajeros.configure(relief="flat")
        self.Viajeros.configure(anchor='w')
        self.Viajeros.configure(justify='left')
        self.Viajeros.configure(text='''Viajeros''')
        self.Viajeros.configure(compound='bottom')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.034, rely=0.897, relwidth=0.93)

        self.btnCalcular = ttk.Button(top)
        self.btnCalcular.place(relx=0.104, rely=0.931, height=25, width=96)
        self.btnCalcular.configure(command=Viajero01_support.calculo)
        self.btnCalcular.configure(takefocus="")
        self.btnCalcular.configure(text='''Calcular''')
        self.btnCalcular.configure(compound='center')

        self.btnSalir = ttk.Button(top)
        self.btnSalir.place(relx=0.584, rely=0.931, height=25, width=96)
        self.btnSalir.configure(command=Viajero01_support.destroy_window)
        self.btnSalir.configure(takefocus="")
        self.btnSalir.configure(text='''Salir''')

        self.LblClase = tk.Label(top)
        self.LblClase.place(relx=0.104, rely=0.36, height=22, width=65)
        self.LblClase.configure(activebackground="#f9f9f9")
        self.LblClase.configure(activeforeground="black")
        self.LblClase.configure(background="#d9d9d9")
        self.LblClase.configure(disabledforeground="#a3a3a3")
        self.LblClase.configure(font="-family {Arial} -size 12")
        self.LblClase.configure(foreground="#000000")
        self.LblClase.configure(highlightbackground="#d9d9d9")
        self.LblClase.configure(highlightcolor="black")
        self.LblClase.configure(text='''Clase''')

        self.Spinbox1 = tk.Spinbox(top, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.138, rely=0.228, relheight=0.031
                , relwidth=0.738)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="#c9c9c9")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(font="TkDefaultFont")
        self.Spinbox1.configure(foreground="#000000")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(selectforeground="black")
        self.Spinbox1.configure(textvariable=Viajero01_support.spinbox)

        self.lblDistancia = ttk.Label(top)
        self.lblDistancia.place(relx=0.138, rely=0.603, height=20, width=77)
        self.lblDistancia.configure(background="#d9d9d9")
        self.lblDistancia.configure(foreground="#000000")
        self.lblDistancia.configure(font="-family {Arial} -size 12")
        self.lblDistancia.configure(relief="flat")
        self.lblDistancia.configure(anchor='w')
        self.lblDistancia.configure(justify='left')
        self.lblDistancia.configure(text='''Distancia''')

        self.EntryDistancia = ttk.Entry(top)
        self.EntryDistancia.place(relx=0.138, rely=0.636, relheight=0.034
                , relwidth=0.742)
        self.EntryDistancia.configure(textvariable=Viajero01_support.EntryDis)
        self.EntryDistancia.configure(takefocus="")

        self.blbPrecio = ttk.Label(top)
        self.blbPrecio.place(relx=0.138, rely=0.701, height=20, width=58)
        self.blbPrecio.configure(background="#d9d9d9")
        self.blbPrecio.configure(foreground="#000000")
        self.blbPrecio.configure(font="-family {Arial} -size 12")
        self.blbPrecio.configure(relief="flat")
        self.blbPrecio.configure(anchor='w')
        self.blbPrecio.configure(justify='left')
        self.blbPrecio.configure(text='''Precio''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.EntryPrecio = ttk.Entry(top)
        self.EntryPrecio.place(relx=0.138, rely=0.735, relheight=0.034
                , relwidth=0.742)
        self.EntryPrecio.configure(textvariable=Viajero01_support.EntryPre)
        self.EntryPrecio.configure(takefocus="")
        self.EntryPrecio.configure(cursor="ibeam")

        self.lblPagar = ttk.Label(top)
        self.lblPagar.place(relx=0.168, rely=0.787, height=41, width=138)
        self.lblPagar.configure(background="#d9d9d9")
        self.lblPagar.configure(foreground="#000000")
        self.lblPagar.configure(font="-family {Arial} -size 13")
        self.lblPagar.configure(relief="flat")
        self.lblPagar.configure(anchor='w')
        self.lblPagar.configure(justify='left')
        self.lblPagar.configure(text='''A Pagar (EUR):''')

        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.R2_Turista = ttk.Checkbutton(top)
        self.R2_Turista.place(relx=0.309, rely=0.407, relwidth=0.198
                , relheight=0.0, height=22)
        self.R2_Turista.configure(variable=Viajero01_support.R2_tur)
        self.R2_Turista.configure(takefocus="")

        self.lbl02_tur = tk.Label(top)
        self.lbl02_tur.place(relx=0.413, rely=0.407, height=22, width=54)
        self.lbl02_tur.configure(background="#d9d9d9")
        self.lbl02_tur.configure(disabledforeground="#a3a3a3")
        self.lbl02_tur.configure(font=font9)
        self.lbl02_tur.configure(foreground="#000000")
        self.lbl02_tur.configure(text='''Turista''')

        self.R3_Primera = ttk.Checkbutton(top)
        self.R3_Primera.place(relx=0.309, rely=0.474, relwidth=0.104
                , relheight=0.0, height=22)
        self.R3_Primera.configure(variable=Viajero01_support.R3_prim)
        self.R3_Primera.configure(takefocus="")

        self.lbl03_prim = ttk.Label(top)
        self.lbl03_prim.place(relx=0.413, rely=0.474, height=20, width=61)
        self.lbl03_prim.configure(background="#d9d9d9")
        self.lbl03_prim.configure(foreground="#000000")
        self.lbl03_prim.configure(font=font9)
        self.lbl03_prim.configure(relief="flat")
        self.lbl03_prim.configure(anchor='w')
        self.lbl03_prim.configure(justify='left')
        self.lbl03_prim.configure(text='''Primera''')

        self.R4_VIP = ttk.Checkbutton(top)
        self.R4_VIP.place(relx=0.309, rely=0.539, relwidth=0.07, relheight=0.0
                , height=22)
        self.R4_VIP.configure(variable=Viajero01_support.R3_vip)
        self.R4_VIP.configure(takefocus="")

        self.R1_ida = ttk.Checkbutton(top)
        self.R1_ida.place(relx=0.309, rely=0.295, relwidth=0.07, relheight=0.0
                , height=22)
        self.R1_ida.configure(variable=Viajero01_support.R1_ida)
        self.R1_ida.configure(takefocus="")

        self.lbl01_ida = ttk.Label(top)
        self.lbl01_ida.place(relx=0.413, rely=0.295, height=20, width=86)
        self.lbl01_ida.configure(background="#d9d9d9")
        self.lbl01_ida.configure(foreground="#000000")
        self.lbl01_ida.configure(font=font9)
        self.lbl01_ida.configure(relief="flat")
        self.lbl01_ida.configure(anchor='w')
        self.lbl01_ida.configure(justify='left')
        self.lbl01_ida.configure(text='''Ida y Vuelta''')

        self.lbl04_vip = ttk.Label(top)
        self.lbl04_vip.place(relx=0.413, rely=0.539, height=20, width=36)
        self.lbl04_vip.configure(background="#d9d9d9")
        self.lbl04_vip.configure(foreground="#000000")
        self.lbl04_vip.configure(font=font9)
        self.lbl04_vip.configure(relief="flat")
        self.lbl04_vip.configure(anchor='w')
        self.lbl04_vip.configure(justify='left')
        self.lbl04_vip.configure(takefocus="0")
        self.lbl04_vip.configure(text='''VIP''')

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.034, rely=0.343, relwidth=0.93)
        self.TSeparator2.configure(takefocus="0")

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=0.034, rely=0.586, relwidth=0.93)
        self.TSeparator3.configure(takefocus="0")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.134, rely=0.833, relheight=0.051
                , relwidth=0.748)
        self.Canvas1.configure(background="#000000")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(takefocus="0")

        self.lbl_total = tk.Label(top)
        self.lbl_total.place(relx=0.47, rely=0.849, height=20, width=117)
        self.lbl_total.configure(activebackground="#000000")
        self.lbl_total.configure(activeforeground="white")
        self.lbl_total.configure(background="#000000")
        self.lbl_total.configure(disabledforeground="#000000")
        self.lbl_total.configure(font=font11)
        self.lbl_total.configure(foreground="#ffff00")
        self.lbl_total.configure(highlightbackground="#000000")
        self.lbl_total.configure(highlightcolor="#000000")
        self.lbl_total.configure(text='''''')

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="-family {Segoe UI} -size 9")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)

    @staticmethod
    def popup2(event, *args, **kwargs):
        Popupmenu2 = tk.Menu(root, tearoff=0)
        Popupmenu2.configure(activebackground="#f9f9f9")
        Popupmenu2.configure(activeborderwidth="1")
        Popupmenu2.configure(activeforeground="black")
        Popupmenu2.configure(background="#d9d9d9")
        Popupmenu2.configure(borderwidth="1")
        Popupmenu2.configure(disabledforeground="#a3a3a3")
        Popupmenu2.configure(font="-family {Segoe UI} -size 9")
        Popupmenu2.configure(foreground="black")
        Popupmenu2.post(event.x_root, event.y_root)

if __name__ == '__main__':
    vp_start_gui()





