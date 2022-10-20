import numpy as np
import matplotlib.pyplot as plt

tracker_trimmed = np.genfromtxt('tracker_trimmed.csv', delimiter=',', skip_header=2)
tracker_trimmed = np.nan_to_num(tracker_trimmed, nan=0.0)
#Extracting t, x and y
real_time = tracker_trimmed[:,0] - tracker_trimmed[0,0]
y = tracker_trimmed[:,2] - min(tracker_trimmed[:,2])
x = tracker_trimmed[:,1] - min(tracker_trimmed[:,1])
y1 = y[0]
y2 = y[-1]
g = 9.8
vy = []
vx = []

for i in range(len(real_time)-1):
    vy = np.append(vy, (y[i+1] - y[i])/(real_time[i+1] - real_time[i]))
for i in range(len(real_time)-1):
    vx = np.append(vx, (x[i+1] - x[i])/(real_time[i+1] - real_time[i]))
vx_0 = np.mean(vx) + 28.5
#Calculating COR
cor = np.sqrt(2*7.775)/np.sqrt(2*28.61)
print(cor)

#Time Arrays
t_fall = np.sqrt(2*y1)/g
t_rise = np.sqrt(2*y2)/g
t1 = np.linspace(0, t_fall, 1000)
t2 = np.linspace(0, t_rise, 1000)

# x and y arrays
x_fall = vx_0*t1
x_rise = vx_0*(t2-t1)
y_fall = -(1/2)*g*(t1)**2 + y1
y_rise = -(1/2)*g*(t2)**2 + y2
#Plots
plt.plot(x, y, linestyle='dashed')
plt.plot((x_fall+x[0]),y_fall, 'r')
plt.plot(x_rise, y_rise, 'g')
plt.ylabel('y [in]')
plt.xlabel('x [in]')
plt.grid()
plt.show()