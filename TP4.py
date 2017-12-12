# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:51:47 2017

@author: Usuario
"""
import numpy as np
import matplotlib.pylab as plt
import time as tiempo

# Caracteristicas del material
cp=0.11 # Calor especifico
k=0.13 # Conductividad térmica
d=7.8 # Densidad
alpha=k/(cp*d) # Difusion termica

# Seteo del Entorno
t=0 # Tiempo inicial
L=5 # En cmts. dimension del lado de la placa
N=20 # Cantidad de puntos (discretizacion)
dx=dy=L/N
time=20
dt=0.2
E=alpha*dt/dx**2 # Factor de Estabilidad

# Formo la Matriz inicial con las condiciones iniciales
P=np.zeros((N,N))
P=np.pad(P, pad_width=1, mode='constant', constant_values=0)
P[1,N] = 200
P[N,1] = 20
Temp=np.zeros((N+2,N+2))

# Matriz de resultados
sol=[]
sol.append(P) #guardo matriz inicial

fig = plt.gcf()
fig.show()
fig.canvas.draw()

plt.imshow(P,'hot')
fig.canvas.draw()

# Nucleo
while t<time:

    for i in range(1,N+1):
        for j in range(1,N+1):
            #Temp[i,j] = P[i, j] - (E*dt/dx*(P[i,j] - P[i-1,j]))-(E*dt/dy*(P[i,j]-P[i,j-1]))
            Temp[i,j]=E*(P[i-1,j]+P[i+1,j]-4*P[i,j]+P[i,j-1]+P[i,j+1])
            Temp[1,N] = 200
            Temp[N,1] = 20
    P=Temp
    sol.append(P)
    Temp=np.zeros((N+2,N+2))
    t+=dt
    #tiempo.sleep(0.5)

    plt.imshow(P,'hot')
    fig.canvas.draw()

tiempo.sleep(2)
