# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 13:55:03 2022

@author: michelle.rosen
"""

import numpy as np
import matplotlib.pyplot as plt
from WKSP02_ProjectileFunctions_Blanks import *

## TEST YOUR RT TO CARTESIAN CONVERSION ##

#POSITIONS
r= 1
transverse= 0
theta= np.pi/2
[x, y]=RTtoCartesian(transverse, r, theta)
print('x = %.3g' %x)
print('y = %.3g \n' %y)

#VELOCITIES
# vr= 
# v_theta= 
# theta=
# [vx, vy]=RTtoCartesian(v_theta, vr, theta)
# print('vx = %.3g' %vx)
# print('vy = %.3g \n' %vy)


# ## TEST YOUR TIME IN THE AIR FUNCTION ##

# x= #m
# y= #m
# vx= #m/s
# vy= #m/s
# t=TimeInTheAir(x,y,vx,vy)
# print('t = %.3g \n' %t)


# ##TEST YOUR TRAJECTORY CALCULATION FUNCTION##

# time=

# x0= #m
# y0= #m
# vx0= #m/s
# vy0= #m/s
# [x, y,vx, vy]=Trajectory(x0,y0,vx0,vy0,time)

# fig1=PlotTraj(x,y,vx,vy,time)
# fig1.suptitle('TITLE')
