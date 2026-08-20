#holis, franca aca :)

#ttk es boots xq ttk se interpreta como el ttk de tkiinter
import ttkbootstrap as boots
from tkinter import *
from funciones import *


ventana=Tk()
ventana.geometry("800x800")
ventana.iconbitmap("imagenes/avion.ico")
ventana.title("HermeSAT")


titulo=Label(ventana,text="HermeSAT",font=("Lexend",20,"bold"),fg="purple1")
titulo.pack(pady=10)



ventana.mainloop()