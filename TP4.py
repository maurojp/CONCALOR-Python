# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:51:47 2017

@author: Pacchiotti Mauro
@author: Paletto Pablo
@author: Bertoluzzi Matias

"""
import numpy as np
from numpy import linalg as la

import matplotlib.ticker as ticker
import matplotlib.cm as cm
import matplotlib as mpl
import matplotlib.pyplot as plt
import time as tiempo
import os

# Caracteristicas del material
cp=460  # Calor especifico
k=52.5 # Conductividad térmica
d=7850 # Densidad
alpha=k/(cp*d) # Difusion termica

###############################################################################
###############################################################################

tolerancia = 0.1 * (10**-8) #Definimos la tolerancia
paso = 2 # Multiplicador de malla, tambien se utiliza para ajustar el paso de tiempo
nx = 20*paso # Puntos de cuadricula en x
ny = 20*paso # Puntos de cuadricula en y
nt = 50 # Numero de pasos de tiempo a calcular
L = 5 # En cmts. dimension del lado de la placa
dx = L/nx # Distancia entre puntos de cuadriculas adyacentes en x
dy = L/ny # Distancia entre puntos de cuadriculas adyacentes en y
dt=500/paso # Cantidad de tiempo que abarca cada momento de tiempo# Cantidad de tiempo que abarca cada momento de tiempo

u = np.zeros((ny,nx)) # Matriz solucion
un = np.zeros((ny,nx)) # Matriz temporal

### Seteo de condiciones iniciales ###
u[0,:]=np.linspace(110,200,nx)
u[-1,:]=np.linspace(20,110,nx)
u[:,0]=np.linspace(110,20,ny)
u[:,-1]=np.linspace(200,110,ny)

### Preparamos la grafica ###
fig = plt.gcf()
fig.show()
fig.canvas.draw()

heatplot=plt.imshow(u,cmap='nipy_spectral')
fig.colorbar(heatplot)
fig.canvas.draw()

norm = 1 #Definimos una norma arbitraria para entrar al bucle
start = tiempo.time()
### Calculo de la solución ###
while(norm > tolerancia):
        os.system('cls')
        un[:] = u[:]

        u[1:-1,1:-1]=un[1:-1,1:-1]+alpha*dt/dx**2*(un[2:,1:-1]-2*un[1:-1,1:-1]+un[0:-2,1:-1])+alpha*dt/dy**2*(un[1:-1,2:]-2*un[1:-1,1:-1]+un[1:-1,0:-2])
        #Calculamos la diferencia de las normas entre la matriz nueva y la matriz anterior
        norm = abs(la.norm(u) - la.norm(un))
        #Imprimimos la norma y la tolerancia
        print("Norma: ",abs(norm)," Tolerancia: ", tolerancia)
        #Mantenemos los bordes con las conndiciones iniciales
        u[0,:]=np.linspace(110,200,nx)
        u[-1,:]=np.linspace(20,110,nx)
        u[:,0]=np.linspace(110,20,ny)
        u[:,-1]=np.linspace(200,110,ny)
        print('\n',u)
        plt.cla()
        plt.imshow(u,cmap='nipy_spectral')
        fig.canvas.draw()
        plt.pause(0.001) #Se pausa la grafica para evitar errores en al momento de graficar

end = tiempo.time()
#Se imprime el tiempo total en el calculo
print("Tiempo total de calculo: ", end-start)

input("Presione una tecla para continuar...")
