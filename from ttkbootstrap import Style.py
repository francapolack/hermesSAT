#holis, franca aca :)

#ttk es boots xq ttk se interpreta como el ttk de tkiinter
import ttkbootstrap as boots
from tkinter import *
from PIL import Image, ImageTk

def tkinter():
    ventana=Tk()
    ventana.geometry("800x800")
    ventana.iconbitmap("imagenes/avion.ico")
    ventana.title("HermeSAT")

    

    
    titulo=Label(ventana,text="HermeSAT",font=("Lexend",20,"bold"),fg="purple1").pack(pady=10)


    nombre=Label(ventana,text=f"Nombre de tu constelacion:nom",font=("Comfortaa"),fg="black").pack(padx=100)
    ejex=Label(ventana,text=f"Eje X de tu satelite:(ejes)[1]",font=("Comfortaa"),fg="black").pack()
    ejey=Label(ventana,text=f"Eje Y de tu satelite:(ejes[2])",font=("Comfortaa"),fg="black").pack()
    ejez=Label(ventana,text=f"Eje Z de tu satelite:ejes[3]",font=("Comfortaa"),fg="black").pack()

    mapa=Image.open("orbita.png")
    mapa=mapa.resize((250,200))
    mapa=ImageTk.PhotoImage(mapa)
    img_mapa=Label(ventana,text="Mapa de ud. y su satelite",font=("Comfortaa"),fg="black",compound="center",image=mapa).pack()

    ventana.mainloop()
tkinter()