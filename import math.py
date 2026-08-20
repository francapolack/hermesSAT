import math
from matplotlib import pyplot as plt
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

mapita(x,y)