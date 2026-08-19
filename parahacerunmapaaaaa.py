from matplotlib import pyplot as plt 

#holiii franca d vuelta
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface
ax.plot_surface(x, y, z)

# Set an equal aspect ratio
ax.set_aspect('equal')

plt.show()

#codigo de dibujo del mapa 
# x=1717.750000000001
# y=-2975.2302747014396
# #lo hacemos oscuroo
# plt.style.use('dark_background')

# fig,ax=plt.subplots(figsize=(12,8))

# Tierra=plt.Circle((0,0),800,color='green')
# ax.add_patch(Tierra)

# ax.plot(x,ls='solid',color='royalblue',marker='o')
# ax.plot(y,ls='solid',color='yellow',marker='o')

# ax.set_aspect('equal')
# ax.grid(True,linestyle='dashed',alpha=0.5)

# #eje x y eje y del grafico (relacionados con los ejes del satelite (?cambiar o no?))

# ax.set_xlim(40000,-40000)
# ax.set_ylim(40000,-40000)


# #nombre y todo
# ax.set_xlabel("X desde la tierra")
# ax.set_ylabel("Y desde la tierra")

# plt.tight_layout()

# plt.savefig('orbita.png',dpi=300)
# plt.show()