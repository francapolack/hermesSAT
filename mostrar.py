#holis, franca aca :)

#ttk es boots xq ttk se interpreta como el ttk de tkiinter
import ttkbootstrap as boots
from tkinter import *
from PIL import Image, ImageTk

def tkinter(nom,eje1,eje2,eje3):
    #setup pantalla
    ventana=boots.App(title="HermeSAT",theme="pydata-light")
    ventana.attributes("-fullscreen",True)
    boots.Button(ventana,text="Cambiar tema",command=ventana.toggle_theme,bootstyle="primary").grid(row=0,column=1000)
    boots.set_global_family("Comic Sans")

    #dashboard
    boots.Label(ventana,text="HermeSAT",bootstyle="primary",font=("Franklin Gothic Heavy",50)).grid(row=0,column=19)

    mapa=Image.open("orbita.png") 
    mapa=mapa.resize((500,400))
    mapa=ImageTk.PhotoImage(mapa)
    Label(ventana,text="Mapa de la distancia del satelite y el lugar de lanzamiento",font=("Arial",14)).grid(row=1,column=18)
    Label(ventana,image=mapa).grid(row=2,column=18)

    Label(ventana,text=f"Nombre de tu constelacion:{(nom)}").grid(row=7,column=0)
    Label(ventana,text=f"Eje X de tu satelite:{(eje1)}").grid(row=9,column=0)
    Label(ventana,text=f"Eje Y de tu satelite:{(eje2)}").grid(row=11,column=0)
    Label(ventana,text=f"Eje Z de tu satelite:{(eje3)}").grid(row=13,column=0)

    ventana.bind("<Escape>",lambda event: ventana.destroy())
    ventana.mainloop()
