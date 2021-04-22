# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 13:08:32 2021

@author: iyngk
"""
import math
import numpy as np
import matplotlib as plt

u=1.67e-27
m_de = 2*u; q_de=1;
m_be = 9*u; q_be=4;
K=1

x = np.linspace(10,10000,100)
def sputtering_ratio(x,m_ion):
    
    
    