#holis, franca aca :)

#ttk es boots xq ttk se interpreta como el ttk de tkiinter
import ttkbootstrap as boots
from tkinter import *
from PIL import Image, ImageTk

def tkinter(nom,eje1,eje2,eje3):
    #setup pantalla
    ventana=boots.App(title="HermeSAT",theme="vapor-light")
    ventana.attributes("-fullscreen",True)
    boots.Button(ventana,text="Cambiar tema",command=ventana.toggle_theme,bootstyle="primary").pack()
    boots.set_global_family("Comic Sans")

    #dashboard
    boots.Label(ventana,text="HermeSAT",bootstyle="primary",font=("Franklin Gothic Heavy",50)).pack()

    mapa=Image.open("orbita.png") 
    mapa=mapa.resize((500,400))
    mapa=ImageTk.PhotoImage(mapa)
    Label(ventana,text="Mapa de la distancia del satelite y el lugar de lanzamiento",font=("Arial",14)).pack()
    Label(ventana,image=mapa).pack()
    Label(ventana,text="Circulo verde:La Tierra\nLinea y circulo rojo:Trayecto de tu satelite").pack()

    Label(ventana,text=f"Nombre de tu constelacion:{(nom)}",font=("Arial",14)).pack(pady=10)
    Label(ventana,text=f"Eje X de tu satelite:{(eje1)}",font=("Arial",14)).pack(pady=10)
    Label(ventana,text=f"Eje Y de tu satelite:{(eje2)}",font=("Arial",14)).pack(pady=10)
    Label(ventana,text=f"Eje Z de tu satelite:{(eje3)}",font=("Arial",14)).pack(pady=10)

    ventana.bind("<Escape>",lambda event: ventana.destroy())
    ventana.mainloop()
