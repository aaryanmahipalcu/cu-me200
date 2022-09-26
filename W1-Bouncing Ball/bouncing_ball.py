#This code was written by Aaryan Mahipal, Amelia Roopnarine and Arin Rothschild

import numpy as np
import matplotlib.pyplot as plt

tracker_framerate = 30 #fps

tracker_data = np.genfromtxt('dynamicsTracker.txt', delimiter=',', skip_header=2)
tracker_data = np.nan_to_num(tracker_data, nan=0.0)

real_time = tracker_data[:,0] - tracker_data[0,0]
y = tracker_data[:,2] - min(tracker_data[:,2])

#First Order Forward Difference for Velocity and Acceleration
vy = []
ay = []

for i in range(len(real_time)-1):
    vy = np.append(vy, (y[i+1] - y[i])/(real_time[i+1] - real_time[i]))
for i in range(len(real_time)-2):
    ay = np.append(ay, (vy[i+1] - vy[i])/(real_time[i+1] - real_time[i]))

#Plots
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(real_time, y)
ax1.set_ylabel('y[m]')
ax2 = fig1.add_subplot(312)
ax2.plot(real_time[:-1], vy)
ax2.set_ylabel('v[m/s]')
ax2.grid()
ax3 = fig1.add_subplot(313)
ax3.plot(real_time[:-2], ay)
ax3.set_ylabel('a[m/s^2]')
ax3.set_xlabel('time[s]')
fig1.tight_layout
fig1.show()

