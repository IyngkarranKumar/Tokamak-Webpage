# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 22:09:43 2021

PIC code for two incident beams. PIC method finds DF over all phase space by summing the DF of "superparticles"
of specific regions of phase space.A superparticle is simply a collection of particles
in the same region of phase space. 


@author: iyngk
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import scipy as sc

"""------Setting initial variables------""" 


L=math.pi
DT=0.05             #Length of time steps
NT=200              #Number of time steps
NG=32               #Number of grid points
N=1000;             # number of super-particles
dens=1;             # plasma density
V0=0.2;             # initial mean velocity 
VT=0.0;             # thermal velocity
XP1=1;              # perturbation of positions
alpha_p=dens*L/N;   # (normalized) number of particles per super-particle
rho_back=dens;      # background charge density (of passive, uniform ions)
dx=L/NG;            # size of the grid cells


"""------Loading intial conditions---------"""
xp=np.linspace(0,L-L/N,N) #Even distribution of superparticles along the x axis
xp=np.transpose(xp)
vp=VT*np.random.randn(N)     #Initial v's normally distributed about vth
pm=np.transpose(np.linspace(1,N,N))
pm=1-2*(pm%2)
vp=vp+(pm*V0)

xp=xp+XP1*(L/N)*pm*np.random.rand(N,1)    #Pertubation about evenly spaced points

p=np.arange(1,N+1); 
un=np.ones((NG-1,1))
Poisson=sc.sparse.diags([un,-2*un,un],[-1,0,1],NG-1,NG-1)




""""---------Diagnostics---------"""














