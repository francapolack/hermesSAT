#holis, franca aca :)

#ttk es boots xq ttk se interpreta como el ttk de tkiinter
import ttkbootstrap as boots
from tkinter import *

def tkinter(nom,ejes):
    ventana=Tk()
    ventana.geometry("800x800")
    ventana.iconbitmap("imagenes/avion.ico")
    ventana.title("HermeSAT")


    titulo=Label(ventana,text="HermeSAT",font=("Lexend",20,"bold"),fg="purple1").pack(pady=10)


    nombre=Label(ventana,text=f"Nombre de tu constelacion:{(nom)}").pack()
    ejex=Label(ventana,text=f"Eje X de tu satelite:{(ejes)[1]}").pack()

    ventana.mainloop()