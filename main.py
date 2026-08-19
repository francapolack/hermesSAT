#holi bienvenidos al codigo d hermesat en caso de q me lo esten revisando
#aca escribe franca su fiel servidora :))

#ta re jede el loop TODO:hacer un loop que no intente asesinar a mi computadora
#tmb TODO:comentar bien :B

#xq carajo tengo 40 librerias 
from ultralytics import YOLO
import math
from matplotlib import pyplot as plt
import cv2
import urllib.request
import numpy as np


#CONSTANTES
url="http://cam.jgp"#TODO:configure l8r to my wifi

#1)Nombre en ingles de la clase 2)Nombre en español 3)Ascension recta (en horas)
constelaciones_datos=["scorpius","Escorpio",18,"canis_major","Canis Mayor",7,"pleiades",4,"sagittarius","Sagitario",20]

tierra_mas_orbita=6871 

yolov=YOLO(r"C:\Users\frmuu\OneDrive\Documentos\colegio(tareas o ejercicios)\hermesSAT\runs\detect\train-3\weights\best.pt")

#ARMAR MAPA CON LOS DATOS DE LA CONSTELACION
def mapita(x,y):
    equis=[0,x]
    i=[0,y]

    plt.style.use('dark_background')
    fig,ax=plt.subplots(figsize=(12,8))

    Tierra=plt.Circle((0,0),800,color='green')
    ax.add_patch(Tierra)

    ax.plot(equis,i,'o-',markersize=8,color='red')

    ax.set_aspect('equal')
    ax.grid(True,linestyle='dashed',alpha=0.5)

    ax.set_xlim(40000,-40000)
    ax.set_ylim(40000,-40000)

    ax.set_xlabel("EjeX desde la tierra")
    ax.set_ylabel("EjeY desde la tierra")

    plt.tight_layout()

    plt.savefig('orbita.png',dpi=1000)
    plt.show()

#CALCULAR EJES X,Y,Z
def calculo_ejes(ascension,nombre):
    #convertimos las horas de ascension en grados
    tasa_conversion=15
    grado_constelacion=ascension*tasa_conversion

    #coseno y seno de las horas en grados 
    cos=math.cos(math.radians(grado_constelacion))#dice raidans porq la funcion math requiere que el angulo sea radianes no grados (si lo ponemos sin convertir nos arruina los datos)
    sin=math.sin(math.radians(grado_constelacion))

    #calculo de ejeX
    ejex=tierra_mas_orbita*cos*cos
    #calculo de ejeY
    ejey=tierra_mas_orbita*cos*sin
    #calculo de ejeZ
    ejez=tierra_mas_orbita*sin
    print("------------------")
    print(nombre)
    print("------------------")
    print(ejex)
    print("------------------")
    print(ejey)
    print("------------------")
    print(ejez)
    mapita(ejex,ejey)

#SACAR IMAGEN DE LA ESP32
def imagenp32():
    pidoimagen=urllib.request.urlopen(url)#pido info a la url local (le pido la img)
    pidoimagennp=np.array(bytearray(pidoimagen.read()),dtype=np.uint8)#decodifico lo que me manda la url local (imagen esp en un array)
    frame=cv2.imdecode(pidoimagennp,-1)
    alto,ancho,_=frame.shape
    blob=cv2.dnn.blobFromImage(frame,1/255.0,(640,640),swapRB=True,crop=False)
    return blob

#DETECCION CON YOLOV8
def busqueda_datos(modelo):
    resultados=modelo((imagenp32),show=False,conf=0.5,save=True)
    for resultado in resultados:
        for box in resultado.boxes:
            posicion_nombre_cons=int(box.data[0][-1])
            nombre=modelo.names[posicion_nombre_cons]
            if nombre in constelaciones_datos:
                posicion=constelaciones_datos.index(nombre)
                if posicion:
                    num=constelaciones_datos[posicion-1]
                    num=int(num)
                    nom=constelaciones_datos[posicion]
                    calculo_ejes(num,nom)
                    if cv2.waitKey(1) & 0xFF==ord('q'):
                        break




#----------------------------------------------------------------------------------------------
#MAIN MAIIIIIN ACA ESTA EL MAAAAAAAAIN
while True:
    try:
        busqueda_datos(yolov)
    except Exception as e:
        print(f"ERROR:{e}")




#lo estoy conteniendo en una funcion para ver si lo llamo cuando la ESP32 se refresque
# def deteccion(modelo):
#     estrella="NO"
#     while estrella=="NO":
#         cap=cv2.VideoCapture(url)
#         while cap.isOpened():
#             yay,frame=cap.read()#yay es que si se leyo
#             if yay:     
                
#             cap.release()
                            
"""
                        print("--------------------------------------------------------")
                        print(f"Nombre de la constelacion:{(constelaciones_datos[posicion+1])}")
                        print(f"Distancia de la constelacion de la Tierra:{(constelaciones_datos[posicion+2])}")
                        print("Ejes del satelite (determinados por la constelacion que lo rodea):")
                        print(f"Eje X:{(constelaciones_datos[posicion+3])}.")
                        print(f"Eje Y:{(constelaciones_datos[posicion+4])}.")
                        print(f"Eje Z:{(constelaciones_datos[posicion+5])}.")
                        print("--------------------------------------------------------")
                        estrella="SI"
                    else:
                        print("No se detecto constelacion.. seguimos buscando!!")
                    """

busqueda_datos(yolov,r"C:\Users\frmuu\OneDrive\Imágenes\aguadebebeeeer")

            