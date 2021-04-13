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
from scipy import sparse

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
un=np.ones(NG-1)
Poisson=sc.sparse.diags([un,-2*un,un],[-1,0,1],[NG-1,NG-1])




""""---------Diagnostics---------"""
time=np.arange(1,NT*DT,DT)
Phi=0; mat=0;
Eg=np.zeros(NG)
mom=np.zeros(NT)
E_kin=np.zeros(NT)
E_pot=np.zeros(NT)
vp_history=np.zeros([len(vp),NT]) #Holds velocities
Eg_history=np.zeros([NG,NT])


"""--------Main Loop------------"""
for t in range(1,NT+1):
    mom[t-1]=sum(vp*alpha_p) # Momentum vector for superparticles at time t
    E_kin[t-1]=sum(0.5*np.square(vp)*alpha_p)
    E_pot[t-1]=sum(0.5*np.square(Eg)*dx)
    
    xp=np.remainder(xp+vp*DT,L)
    vp_history[:,t-1]=vp
    Eg_history[:,t-1]=Eg
    
    #To project to grid
    g1=np.floor_divide(xp,dx)
    g=np.array([g1,g1+1])
    
    fraz1=1-np.abs(xp/dx-g1)
    fraz=np.array([fraz1,1-fraz1])
    
    #out
    

    
    









