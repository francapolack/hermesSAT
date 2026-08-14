#holis, franka axa :)

#improtacion de librerias: ttk es boots xq ttk se interpreta como el ttk de tkiinter
import ttkbootstrap as boots
from PIL import Image, ImageTk
import urllib.request
import numpy as np
import cv2
from ultralytics import YOLO
from tkinter import *
#constantes de TKINTER
INFO="Lexend"
TAM_INFO=25
#catalogo de CONSTELACIONES
constelaciones_datos=["sagittarius","Sagitario",4000,90,10,20,"pleiades","Pleiades",5000,1,2,4]
#tema de YOLO
modelo=YOLO(r"C:\Users\frmuu\OneDrive\Documentos\colegio(tareas o ejercicios)\hermesSAT\runs\detect\train-3\weights\best.pt")
resultados=modelo(source=r"C:\Users\frmuu\OneDrive\Imágenes\aguadebebeeeer",show=True,conf=0.5,save=True)

for resultado in resultados:
    for box in resultado.boxes:
        posicion_nombre_cons=int(box.data)

app = boots.App(theme="dracula-dark")
app.geometry("1000x1000")
app.iconbitmap("imagenes/avion.ico")
app.title("HermeSAT")


titulo=boots.Label(app,text="HermeSAT",bootstyle="warning",font=("Georgia",30)).pack()

#vista en vivo de tu satelite


#datos de la constelacion
nombre_constelacion=Label(app,text=f"Nombre de la constelacion:{(constelaciones_datos[posicion+1])}",bootstyle="success",font=(INFO,TAM_INFO,"bold")).pack()
distancia_contelacion=Label(app,text=f"Distancia de la constelacion de la Tierra:{(constelaciones_datos[posicion+2])} km.",bootstyle="success",font=(INFO,TAM_INFO,"bold")).pack()
titulo_ejes=Label(app, text="Ejes del satelite (determinados por la constelacion que lo rodea)",bootstyle="primary",font=(INFO,TAM_INFO,"bold")).pack
x=Label(app,text=f"Eje X:{(constelaciones_datos[posicion+3])}.",bootstyle="success",font=(INFO,TAM_INFO,"bold")).pack()
y=Label(app,text=f"Eje Y:{(constelaciones_datos[posicion+4])}.",bootstyle="success",font=(INFO,TAM_INFO,"bold")).pack()
x=Label(app,text=f"Eje Z:{(constelaciones_datos[posicion+5])}.",bootstyle="success",font=(INFO,TAM_INFO,"bold")).pack()

#loopCamara()
app.mainloop()