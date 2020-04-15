from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox

#Creacion de Tk y Toplevel
root = Tk()
root.withdraw()
window = Toplevel()
window.geometry('304x490')
window.resizable(False,False)
window.title('Tren')
window.configure(bg='black')
window.protocol("WM_DELETE_WINDOW", root.destroy)

#Funcion
def Total_():
    Clase=0
    Ida_Vuelta=1
    if clase.get()!=1 and clase.get()!=2 and clase.get()!=3:
        messagebox.showinfo('Error','Seleccione la clase, por favor.')
    elif clase.get()==1:
        Clase=1
    elif clase.get()==2:
        Clase=1.2
    elif clase.get()==3:
        Clase=2
    if ida_vuelta.get()==1:
        Ida_Vuelta=1.5
    Calculo=round(int(Viajeros.get())*Distancia.get()*Precio.get()*Ida_Vuelta*Clase,2)
    Total.set(Calculo) 
    
#GUI
raw_image=Image.open(r'C:\Users\Agus\Downloads\train.jpg')
resized=raw_image.resize((300,100),Image.ANTIALIAS)
tren=ImageTk.PhotoImage(resized)
label_img = Label(window, image = tren, bd=2)
label_img.pack()
label_img.image = tren
label_viajeros = Label(window, text='Viajeros:', fg='turquoise',bg='black', font=('Open Sans',12), relief= RAISED).pack()
Viajeros = ttk.Spinbox(window, from_=1.0, to=100.0)
Viajeros.set(1)
Viajeros.pack()
ida_vuelta=IntVar()
cb_0 = Checkbutton(window, text='Ida y Vuelta', variable=ida_vuelta, fg='turquoise',bg='black', font=('Open Sans',8), relief= RAISED).pack()
label_Clase = Label(window, text='Clase:', fg='turquoise',bg='black', font=('Open Sans',13), relief= RAISED).pack()
clase=IntVar(0)
cb_1 = Checkbutton(window, text='Turista', onvalue=1, variable=clase, fg='turquoise',bg='black', font=('Open Sans',8), relief= RAISED, width=6).pack()
cb_2 = Checkbutton(window, text='Primera', onvalue=2, variable=clase, fg='turquoise',bg='black', font=('Open Sans',8), relief= RAISED, width=6).pack()
cb_3 = Checkbutton(window, text='Lujo', onvalue=3, variable=clase, fg='turquoise',bg='black', font=('Open Sans',8), relief= RAISED, width=6).pack()
label_Distancia = Label(window, text='Distancia (Kilómetros):', fg='turquoise',bg='black', font=('Open Sans',11), relief= RAISED).pack()
Distancia=IntVar(window,1)
Entry_Distancia = Entry(window, textvariable=Distancia, justify=CENTER)
Entry_Distancia.pack()
label_precio = Label(window, text='Precio:', fg='turquoise',bg='black', font=('Open Sans',11), relief= RAISED).pack()
Precio=DoubleVar(window, 0.1)
Entry_precio = Entry(window, textvariable=Precio, justify=CENTER)
Entry_precio.pack()
label_total = Label(window, text='A pagar (euros):', fg='turquoise',bg='black', font=('Open Sans',11), relief= RAISED).pack()
Total=IntVar(0)
Entry_total = Entry(window, state=DISABLED, textvariable=Total, justify=RIGHT)
Entry_total.pack()
    #Frame_Botones
Botones = Frame(window, width=200, height=100, bg='black',relief=SUNKEN,bd=25)
Botones.pack()
Calcular = Button(Botones, text='Calcular', command=Total_, fg='turquoise',bg='black', font=('Open Sans',11))
Calcular.place(x=0,y=10)
Salir = Button(Botones, text='Salir', command=root.destroy, fg='turquoise',bg='black', font=('Open Sans',11))
Salir.place(x=100,y=10)

root.mainloop()

