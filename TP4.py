# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:51:47 2017

@author: Usuario
"""
import numpy as np
import matplotlib.pylab as plt

# Caracteristicas del material
cp=0.11 # Calor especifico
k=0.13 # Conductividad térmica
d=7.8 # Densidad
alpha=k/(cp*d) # Difusion termica

# Seteo del Entorno
t=0 # Tiempo inicial
L=100 # En cmts. dimension del lado de la placa
N=200 # Cantidad de puntos (discretizacion)
dx=dy=L/N
time=50
dt=0.5
E=alpha*dt/dx**2 # Factor de Estabilidad

# Formo la Matriz inicial con las condiciones iniciales
P=np.zeros((N,N))
P[1,198] = 200
P[198,1] = 20
 
# Matriz de resultados
sol=[]
sol.append(P) #guardo situacion inicial

# Nucleo
while t<time:
    for i in range(1,199):
        for j in range(1,199):
            P[1,198] = 200
            P[198,1] = 20
            if (i==198 and j==1) or (i==1 and j==198):
                P[1,198] = 200
                P[198,1] = 20
                print(P[i,j])
            else:
                P[i,j]=((1-E)*P[i,j])+E*((P[i-1,j]+P[i+1,j]+P[i,j-1]+P[i,j+1])/1.5)
            sol.append(P)
    t+=dt

plt.imshow(P,'hot')
plt.show()