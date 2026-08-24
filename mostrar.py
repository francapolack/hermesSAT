#holis, franca aca :)

#ttk es boots xq ttk se interpreta como el ttk de tkiinter
import ttkbootstrap as boots
from tkinter import *
from PIL import Image, ImageTk

def tkinter(nom,eje1,eje2,eje3):
    fuente_normal="Lexend",30,"bold"
    ventana=Tk()
    ventana.attributes("-fullscreen",True)
    ventana.geometry("800x800")
    ventana.iconbitmap("imagenes/avion.ico")
    ventana.title("HermeSAT")
    
    titulo=Label(ventana,text="HermeSAT",font=("Impact",100,"bold"),fg="purple1").pack(pady=10)


    nombre=Label(ventana,text=f"Nombre de tu constelacion:{(nom)}",font=(fuente_normal),fg="black").pack(padx=100,pady=100)
    ejex=Label(ventana,text=f"Eje X de tu satelite:{(eje1)}",font=(fuente_normal),fg="black").pack()
    ejey=Label(ventana,text=f"Eje Y de tu satelite:{(eje2)}",font=(fuente_normal),fg="black").pack()
    ejez=Label(ventana,text=f"Eje Z de tu satelite:{(eje3)}",font=(fuente_normal),fg="black").pack()

    mapa=Image.open("orbita.png")
    mapa=mapa.resize((800,800))
    mapa=ImageTk.PhotoImage(mapa)
    img_mapa=Label(ventana,text="Mapa de ud. y su satelite",font=("Comfortaa"),fg="black",compound="left",image=mapa).pack()

    ventana.bind("<Escape>",lambda event: ventana.destroy())
    ventana.mainloop()