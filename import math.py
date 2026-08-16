import math

r=6871
ascension=20
tasa=15

conversion=math.radians(300)
#coseno 
cos=math.cos(conversion)
#seno
sin=math.sin(conversion)
print(f"{"SEPARADOR":-^30}")
x=r*cos*cos
print(f"EjeX:{x}")
print(f"{"SEPARADOR":-^30}")
y=r*cos*sin
print(f"EjeY:{y}")
print(f"{"SEPARADOR":-^30}")
z=r*sin
print(f"EjeZ{z}")
print(f"{"SEPARADOR":-^30}")