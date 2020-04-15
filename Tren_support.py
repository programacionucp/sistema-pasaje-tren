import sys
from tkinter import ttk, messagebox

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

def set_Tk_var():
    global chbIdaVuelta
    chbIdaVuelta = tk.IntVar()
    global rbTurista
    rbTurista = tk.IntVar()
    global rbPrimera
    rbPrimera = tk.IntVar()
    global rbLujo
    rbLujo = tk.IntVar()
    global spinbox
    spinbox = tk.StringVar()
    global che46
    che46 = tk.IntVar()
    global selectedButton
    selectedButton = tk.IntVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import Tren
    Tren.vp_start_gui()
