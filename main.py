#holi bienvenidos al codigo d hermesat en caso de q me lo esten revisando
#aca escribe franca su fiel servidora :))
from ultralytics import YOLO
import math
import cv2
import urllib.request

url="http://cam.jgp"#TODO:configure l8r to my wifi

#lista completa de los datos de las constelaciones,orden es: 
#1)Nombre en ingles de la clase,2)Nombre en español,3)Ascencion recta
constelaciones_datos=["scorpius","Escorpio",18,"canis_major","Canis Mayor",7,"pleiades",4,"sagittarius","Sagitario",20]
tierra_mas_orbita=6871 #6371km de distancia desde el radio de la tierra + 500km de lanzamiento del satelite
    
def calculo_ejes(ascension,nombre):
    #convertimos las horas de ascension en grados
    tasa_conversion=math.degrees(15)
    grado_constelacion=ascension*tasa_conversion
    #calculo de ejeX
    cos=math.cos(grado_constelacion)
    cos_grado=math.degrees(cos)
    sin=math.sin(grado_constelacion)
    sin_grado=math.degrees(sin)
    ejex=tierra_mas_orbita*cos_grado*cos_grado
    #calculo de ejeY
    ejey=tierra_mas_orbita*cos_grado*sin_grado
    #calculo de ejeZ
    ejez=tierra_mas_orbita*sin_grado
    print("------------------")
    print(nombre)
    print("------------------")
    print( ejex)
    print("------------------")
    print(ejey)
    print("------------------")
    print(ejez)


#lo estoy conteniendo en una funcion para ver si lo llamo cuando la ESP32 se refresque
def deteccion(modelo):
    estrella="NO"
    while estrella=="NO":
        #cap=cv2.VideoCapture(url)
        #while cap.isOpened():
            #yay,frame=cap.read()#yay es que si se leyo
            #if yay:     
            resultados=modelo(source=r"C:\Users\frmuu\OneDrive\Imágenes\aguadebebeeeer",show=False,conf=0.5,save=True)
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
                            break

                            
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
yolov=YOLO(r"C:\Users\frmuu\OneDrive\Documentos\colegio(tareas o ejercicios)\hermesSAT\runs\detect\train-3\weights\best.pt")
deteccion(yolov)

            