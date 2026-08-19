from matplotlib import pyplot as plt 
import numpy as np
#holiii franca d vuelta

#codigo de dibujo del mapa 
x,y=[0,1717.750000000001],[0,-2975.2302747014396]
#lo hacemos oscuroo
plt.style.use('dark_background')

fig,ax=plt.subplots(figsize=(12,8))

Tierra=plt.Circle((0,0),800,color='green')
ax.add_patch(Tierra)

ax.plot(x,y,'o-',markersize=8,color='red')

ax.set_aspect('equal')
ax.grid(True,linestyle='dashed',alpha=0.5)

# #eje x y eje y del grafico (relacionados con los ejes del satelite (?cambiar o no?))

ax.set_xlim(40000,-40000)
ax.set_ylim(40000,-40000)


# #nombre y todo
ax.set_xlabel("X desde la tierra")
ax.set_ylabel("Y desde la tierra")

plt.tight_layout()

plt.savefig('orbita.png',dpi=1000)
plt.show()