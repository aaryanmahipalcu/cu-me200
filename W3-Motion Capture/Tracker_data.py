# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 06:55:18 2021
ME200:  Motion Capture Workshop
Prof. Rosen, Giglia, Sidebotham
The Cooper Union

PART 1:  TRACKER DATA
@author: george.sidebotham2
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

##### IMPORT TRACKER DATA ######
tracker_data = np.genfromtxt('dynamics_3_data.txt', delimiter=',', skip_header=2)
print(tracker_data[:10][:])  
#This line prints the first 10 rows (and shows the syntax needed to isolate
#a subset of a large file), just to confirm importing went well
print("Value at 8th row, third column = %.5g" %tracker_data[7,2])
#This line isolates and individual point, and reminds you that
#indexing starts at 0, so third column is index 2    
n = 99
t = (tracker_data[:,0] - tracker_data[0,0])
y = (tracker_data[:,2] - tracker_data[0,2])*1000
x = (tracker_data[:,1] - tracker_data[0,1])*1000
#### CREATE nx1 ARRAYS for time and position ####
 #pulls out y data from tracker_data, corrects for any unit mismatch, and subtracts the initial value   
# These create nx1 arrays of x and y, with the initial point as a zero reference
# and multiplied by -1000 to flip orientation and convert m to mm.

####  BONUS:  NUMERICAL DERIVATIVES ####
vx = []
ax = []
for i in range(len(t)-1):
    vx = np.append(vx, (x[i+1]-x[i])/(t[i+1]-t[i]))
for i in range(len(t)-2):
    ax = np.append(ax, (vx[i+1]-vx[i])/(t[i+1]-t[i]))


#### PLOT TRACKER DATA  ####
##YOUR PLOTTING CODE HERE##
plt.plot(t, y, 'r', label='y position')
plt.plot(t, x, 'b', label='x position')
plt.xlabel('time (t)')
plt.ylabel('x position (mm)')
plt.legend()
plt.grid()
plt.show()
####  BONUS PLOT: VELOCITY & ACCELERATION ####
fig1 = plt.figure()
ax1 = fig1.add_subplot(211)
ax1.title.set_text("Velocity (mm/s) vs t (s)")
ax1.plot(t[:-1], vx)
ax1.set_xlabel('time (s)')
ax1.set_ylabel('velocity (mm/s)')
ax2 = fig1.add_subplot(212)
ax2.title.set_text("acceleration (mm/s^2) vs time (s)")
ax2.plot(t[:-2], ax)
ax2.set_xlabel("time (s)")
ax2.set_ylabel("acceleration (mm/s^2)")
fig1.subplots_adjust(hspace=0.5)
fig1.show()

df = pd.read_csv('cam_obj_data.csv')
df

n = 99
#Creating nx1 arrays for the position
x_pos = df.cam_x - df.cam_x[0]
y_pos = df.cam_y - df.cam_y[0]
z_pos = df.cam_z - df.cam_z[0]

#Creating nx1 arrays for the object
x_obj = df.obj_x - df.obj_x[0]
y_obj = df.obj_y - df.obj_y[0]
z_obj = df.obj_z - df.obj_z[0]

x_rel = x_obj - x_pos
y_rel = y_obj - y_pos
z_rel = z_obj - z_pos

fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.title.set_text("X Position (mm) vs time (s)")
ax1.plot(t, x_pos, 'r', label='x_pos camera')
ax1.plot(t, x_obj, 'b', label='x_pos object')
ax1.plot(t, x_rel, 'g', label='x_pos camera relative to object')
ax1.set_ylabel('x position (mm)')
ax1.legend(loc='best')
ax2 = fig1.add_subplot(312)
ax2.title.set_text("Y Position (mm) vs time (s)")
ax2.plot(t, y_pos, 'r', label='y_pos camera')
ax2.plot(t, y_obj, 'b', label='y_pos object')
ax2.plot(t, y_rel, 'g', label='y_pos camera relative to object')
ax2.set_ylabel('y position (mm)')
ax2.legend(loc='best')
ax3 = fig1.add_subplot(313)
ax3.title.set_text("Z Position (mm) vs time (s)")
ax3.plot(t, z_pos, 'r', label='z_pos camera')
ax3.plot(t, z_obj, 'b', label='z_pos object')
ax3.plot(t, z_rel, 'g', label='z_pos camera relative to object')
ax3.set_xlabel('time (s)')
ax3.set_ylabel('z position (mm)')
ax3.legend(loc='best')
fig1.subplots_adjust(hspace=1)
fig1.show()
fig1.tight_layout()

#NUMERICAL DERIVATIVES, using first order forward difference approximation
vx = []
ax =[]
vx_cam = []
vx_obj = []
vx_rel = []
ax_cam = []
ax_obj = []
ax_rel = []
for i in range(98):
    vx = np.append(vx, (x[i+1]-x[i])/(t[i+1]-t[i]))
for i in range(97):
    ax = np.append(ax, (vx[i+1]-vx[i])/(t[i+1]-t[i]))
for i in range(98):
    vx_cam = np.append(vx_cam, (x_pos[i+1]-x_pos[i])/(t[i+1]-t[i]))
for i in range(97):
    ax_cam = np.append(ax_cam, (vx_cam[i+1]-vx_cam[i])/(t[i+1]-t[i]))
for i in range(98):
    vx_obj = np.append(vx_obj, (x_obj[i+1]-x_obj[i])/(t[i+1]-t[i]))
for i in range(97):
    ax_obj = np.append(ax_obj, (vx_obj[i+1]-vx_obj[i])/(t[i+1]-t[i]))
for i in range(98):
    vx_rel = np.append(vx_rel, (x_rel[i+1]-x_rel[i])/(t[i+1]-t[i]))
for i in range(97):
    ax_rel = np.append(ax_rel, (vx_rel[i+1]-vx_rel[i])/(t[i+1]-t[i]))

#Vicon Plots for Velocity and Acceleration

fig2 = plt.figure()
ax1 = fig2.add_subplot(311)
ax1.title.set_text("X Position (mm) vs time (s)")
ax1.plot(t, x_pos, 'r', label='x_pos camera')
ax1.plot(t, x_obj, 'b', label='x_pos object')
ax1.plot(t, x_rel, 'g', label='x_pos camera relative to object')
ax1.set_ylabel('x position (mm)')
ax1.legend(loc='best')
ax2 = fig2.add_subplot(312)
ax2.title.set_text("X Velocity (m/s) vs time (s)")
ax2.plot(t[0:-1], vx_cam, 'r', label='x_vel camera')
ax2.plot(t[0:-1], vx_obj, 'b', label='x_vel object')
ax2.plot(t[0:-1], vx_rel, 'g', label='x_vel camera relative to object')
ax2.set_ylabel('x velocity (m/s)')
ax2.legend(loc='best')
ax3 = fig2.add_subplot(313)
ax3.title.set_text("X Acceleration (m/s^2) vs time (s)")
ax3.plot(t[0:-2], ax_cam, 'r', label='x_acc camera')
ax3.plot(t[0:-2], ax_obj, 'b', label='x_acc object')
ax3.plot(t[0:-2], ax_rel, 'g', label='x_acc camera relative to object')
ax3.set_xlabel('time (s)')
ax3.set_ylabel('x acceleration (m/s^2)')
ax3.legend(loc='best')
fig2.subplots_adjust(hspace=0.5)
fig2.show()
fig2.tight_layout()

x_tracker_new = x- x_obj[0]     #pulls out x data from tracker_data, corrects for any unit mismatch, and subtracts the initial value 
y_tracker_new = y- y_obj[0]

fig3 = plt.figure()

ax1 = fig3.add_subplot(211)
ax2 = fig3.add_subplot(212)

ax1.plot(t, x_pos, label='Camera', color='m')
ax1.plot(t, x_tracker_new, label='Object', color='c')
ax1.set_title('X Postions')
ax1.set_ylabel('position (mm)')
ax1.legend()

ax2.plot(t, z_pos, label='Camera', color='m')
ax2.plot(t, y_tracker_new, label='Object', color='c')
ax2.set_title('Vertical Postions')
ax2.set_xlabel('time (s)')
ax2.set_ylabel('postion (mm)')
ax2.legend()

fig3.tight_layout()