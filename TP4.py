# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:51:47 2017

@author: Usuario
"""
import numpy as np
from numpy import linalg as la
import matplotlib.pylab as plt
import time as tiempo
import os

# Caracteristicas del material
# cp=0.11 # Calor especifico
# k=0.13 # Conductividad térmica
# d=7.8 # Densidad
cp=460
k=52.5
d=7850
alpha=k/(cp*d) # Difusion termica

###############################################################################
###############################################################################

tolerancia = 0.1 * (10**-4)
paso = 2
nx = 20*paso # Puntos de cuadricula en x
ny = 20*paso # Puntos de cuadricula en y
nt = 50 # Numero de pasos de tiempo a calcular
L = 5 # En cmts. dimension del lado de la placa
dx = L/nx # Distancia entre puntos de cuadriculas adyacentes en x
dy = L/ny # Distancia entre puntos de cuadriculas adyacentes en y
C = .25 # Número de Courant
#dt =(C*dx*dy/alpha)/paso # Cantidad de tiempo que abarca cada momento de tiempo
dt=500/paso
u = np.zeros((ny+1,nx+1)) # Matriz solucion
un = np.zeros((ny+1,nx+1)) # Matriz temporal

### Seteo de condiciones iniciales ###
u[1,nx-1] = 200
u[ny-1, 1] = 20

u[1,2:-2] = u[2,2:-2]
u[-2,2:-2] = u[-3,2:-2]
u[2:-2,1] = u[2:-2,2]
u[2:-2,-2] = u[2:-2,-3]

# u[1,2:-2] = u[2,2:-2]
# u[-2,2:-2] = u[-3,2:-2]
# u[2:-2,1] = u[2:-2,2]
# u[2:-2,-2] = u[2:-2,-3]

print(u)
# u[0,:]=np.linspace(0,200,nx)
# u[-1,:]=np.linspace(20,0,nx)
# u[:,0]=np.linspace(0,20,ny)
# u[:,-1]=np.linspace(200,0,ny)

fig = plt.gcf()
fig.show()
fig.canvas.draw()

plt.imshow(u,'hot')
fig.canvas.draw()
norm = 1
### Calculo de la solución ###
while(norm > tolerancia):
        os.system('cls')
        un[:] = u[:]
        u[1:-1,1:-1]=un[1:-1,1:-1]+alpha*dt/dx**2*(un[2:,1:-1]-2*un[1:-1,1:-1]+un[0:-2,1:-1])+alpha*dt/dy**2*(un[1:-1,2:]-2*un[1:-1,1:-1]+un[1:-1,0:-2])
        # for i in range(nx-1):
        #     for j in range(ny-1):
        #         u[i,j] = un[i,j] + (alpha * dt)*(((un[i-1,j] - 2*un[i,j] + un[i+1,j])/dx)+((un[i,j-1] - 2*un[i,j] + un[i,j+1])/dy))
        norm = abs(la.norm(u) - la.norm(un))
        print("Norma: ",abs(norm)," Tolerancia: ", tolerancia)

        # u[1,2:-2] = u[2,2:-2]
        # u[-2,2:-2] = u[-3,2:-2]
        # u[2:-2,1] = u[2:-2,2]
        # u[2:-2,-2] = u[2:-2,-3]
        # u[1,nx-1] = 200
        # u[ny-1, 1] = 20
        # u[0,1:-1] = u[1,1:-1]
        # u[-1,1:-1] = u[-2,1:-1]
        # u[1:-1,0] = u[1:-1,1]
        # u[1:-1,-1] = u[1:-1,-2]

        print('\n',u)
        #print(((n*100)/nt), '%')
        #plt.pause(0.05)
        plt.cla()
        plt.imshow(u, 'hot')
        fig.canvas.draw()
        plt.pause(0.01)

###############################################################################
###############################################################################
# tolerance = 0.5
# tolerance_ss = 0.001
#
# k = 1
# err_SS_max = []
# err_SS_max.append(1)
# err_SS_min = []
# err_SS_min.append(1)
#
# paso=2
# nx = 20 # Puntos de cuadricula en x
# ny = 20# Puntos de cuadricula en y
# nt = 50 # Numero de pasos de tiempo a calcular
# lx = 1 # Longitud en metros
# ly = 1 # Longitud en metros
# dx = lx/nx # Distancia entre puntos de cuadriculas adyacentes en x
# dy = ly/ny # Distancia entre puntos de cuadriculas adyacentes en y
# C = .25 # Número de Courant
# #dt =C*dx*dy/alpha # Cantidad de tiempo que abarca cada momento de tiempo
# dt = 25
#
# if(dt <= 1/(2*alpha*((1/dx**2)+(1/dy**2)))):
#     print("Error de estabilidad")
#
# T = np.zeros((nx+2,ny+2,75000))
# T[2,nx-1,:]=200
# T[ny-1, 2,:] = 20
# #print(T[:,:,5])
#
# Tss = np.zeros((nx+2,ny+2))
# Tss2 = np.zeros((nx+2,ny+2))
# Tss[2,nx-1] = 200
# Tss[ny-1, 2] = 20
# Tss2[2,nx-1] = 200
# Tss2[ny-1, 2] = 20
# #print(Tss)
#
# while (err_SS_max[k-1] >= tolerance_ss or err_SS_min[k-1] >= tolerance_ss):
#     for i in range(2,nx):
#         for j in range(2,ny):
#             Tss2[i,j] = 0.25*(Tss[i+1,j]+Tss[i,j+1]+Tss[i-1,j]+Tss[i,j-1])
#     k = k+1
#     #flag = Tss2 - Tss
#     #print(flag)
#     err_SS_max.append(abs(np.amax(np.amax(Tss2-Tss))))
#     #print("Max: ", err_SS_max)
#     err_SS_min.append(abs(np.amin(np.amin(Tss2-Tss))))
#     #print("Min: ", err_SS_min)
#     #print(Tss)
#     Tss = Tss2
#     #input()
#
# k=1
# err_R_k_max = []
# err_R_k_max.append(100)
# err_R_k_min = []
# err_R_k_min.append(100)
#
# fig = plt.gcf()
# fig.show()
# fig.canvas.draw()
#
# plt.imshow(T[:,:,k],'hot')
# fig.canvas.draw()
#
# while (err_R_k_max[k-1]>=tolerance or err_R_k_min[k-1]>=tolerance):
#     for i in range(2,nx):
#         for j in range(2,ny):
#             k1 = alpha*(((T[i-1,j,k]-2*T[i,j,k]+T[i+1,j,k])/dx**2)+((T[i,j-1,k]-2*T[i,j,k]+T[i,j+1,k])/dy**2))
#             Tk = T[:,:,k]+k1*dt;
#             k2 = alpha*(((Tk[i-1,j]-2*Tk[i,j]+Tk[i+1,j])/dx**2)+((Tk[i,j-1]-2*Tk[i,j]+Tk[i,j+1])/dy**2))
#             T[i,j,k+1] =T[i,j,k]+(dt/2)*(k1+k2);
#     print(T[:,:,k])
#     plt.pause(0.05)
#     plt.cla()
#     plt.imshow(T[:,:,k], 'hot')
#     fig.canvas.draw()
#     k = k+1
#     err_R_k_max.append(abs(np.amax(np.amax(T[:,:,k]-Tss))))
#     err_R_k_min.append(abs(np.amin(np.amin(T[:,:,k]-Tss))))




##################################################################################


##################################################################################
# # Seteo del Entorno
# t=0 # Tiempo inicial
# L=5 # En cmts. dimension del lado de la placa
# N=20 # Cantidad de puntos (discretizacion)
# dx=dy=L/N
# time=20
# dt=.25*dx*dy/alpha
# E=alpha*dt/dx**2 # Factor de Estabilidad
#
# # Formo la Matriz inicial con las condiciones iniciales
# P=np.zeros((N,N))
# P=np.pad(P, pad_width=1, mode='constant', constant_values=0)
# P[1,N] = 200
# P[N,1] = 20
# Temp=np.zeros((N+2,N+2))
#
# print(P.shape)
#
# # Matriz de resultados
# sol=[]
# sol.append(P) #guardo matriz inicial
#
# fig = plt.gcf()
# fig.show()
# fig.canvas.draw()
#
# plt.imshow(P,'hot')
# fig.canvas.draw()

# # Nucleo
# for n in range(time + 1):
#     Temp[:] = P[:]
#     P[1:-1,1:-1] = Temp[1:-1,1:-1] + alpha*dt*dx**2*(Temp[2:,1:-1]-2*Temp[1:-1,1:-1]+Temp[0:-2,1:-1]) + alpha*dt/dy**2*(Temp[1:-1,2:]-2*Temp[1:-1,1:-1]+Temp[1:-1,0:-2])
#     P[1,N] = 200
#     P[N,1] = 20
#     sol.append(P)
#     #print(P)
    # plt.imshow(P, 'hot')
    # fig.canvas.draw()
#

# while t<time:
#
#     for i in range(1,N+1):
#         for j in range(1,N+1):
#             #Temp[i,j] = P[i, j] - (E*dt/dx*(P[i,j] - P[i-1,j]))-(E*dt/dy*(P[i,j]-P[i,j-1]))
#             Temp[i,j]=E*(P[i-1,j]+P[i+1,j]-4*P[i,j]+P[i,j-1]+P[i,j+1])
#             Temp[1,N] = 200
#             Temp[N,1] = 20
#     P=Temp
#     sol.append(P)
#     Temp=np.zeros((N+2,N+2))
#     t+=dt
#     #tiempo.sleep(0.5)
#
#     plt.imshow(P,'hot')
#     fig.canvas.draw()

input("Press Enter to continue...")
