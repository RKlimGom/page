# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:00:53 2020

@author: rerkl
"""
#this isprogram to estimate lateral displacement of an object hanged by a cable
#and subject to a lateral load, basedo on item 5.2.2.2 of DNV-RP-H103 Ap.2011


import numpy as np
import random
import math
import decimal
import datetime

sm  = 1025  #specific mass of the fluid (kg/m3)
g   = 9.81    #acceleration of gravity (m/s2)
M   = 1000000 #weight of the object (t)
m   = 80  #weight of the cabel per unit length (kg/m)
V   = 150 #volume of the obect (m3)
L   = 1700 #cable length
Cdx = 0.4 #Drag coefficient of the object - lateral direction
Cdm = 1.0 #Drag coefficient of the cable - lateral direction
Ax  = 20  #x-Projected area of the lifted object 
Dc  = 0.125 #cable diameter (m)
Uc  = 0.3   #Current velocity (m/s) 
Ac  = 3.14*(pow(Dc,2))*0.25

W   = M*g - sm*g*V #submerged weight of the object (N)
w   = m*g - sm*g*Ac #submerged weight of the cable (N/m)


#weight relation
k = W/(wc*L)
print("k =", k)

#drag force x
Fdx = 0.5*sm*Cdx*Ax*pow(Uc,2)
print("Fd =",Fdx, "N")

#ratio between drag force and the weight of the cable
lamratio = Fdx / (wc*L)
print("\u03BB =", round(lamratio,2))

#hydrodynamica drag force per unit length of the cable
q = 0.5*sm*Cdm*Dc*pow(Uc,2)
print("q =", round(q,2), "N/m")

#horizontal offset of the object (item 5.2.2.2 of DNV-RP-H103 Ap.2011)
ksi = L*(q*k/w - lamratio)*math.log(k/(k+1),math.e)-(q*L/w)
print("\u03BE =", round(ksi,2),"m")
print()
print()
print("Lateral displacement of ",round(ksi,2),"m for a water depth of",L,"m")










