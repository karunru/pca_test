import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.loadtxt("test_data",delimiter=",")
print(data)
rx = data[:,0]
ry = data[:,1]

averx = np.average(rx)
avery = np.average(ry)

xx = rx - averx
xy = ry - avery

V = np.zeros((2,2))

V[0][0] = np.dot(rx-averx,rx-averx.T) / 30
V[0][1] = np.dot(rx-averx,ry-avery.T) / 30
V[1][0] = np.dot(ry-avery,rx-averx.T) / 30
V[1][1] = np.dot(ry-avery,ry-avery.T) / 30

la, u = np.linalg.eig(V)

print(averx)
print(avery)
print(V)
print(la)
print(u)
print(u[:,0])

#new_x = u.T*V*u*rx - averx
#new_y = u.T*V*u*ry - avery

# plt.plot(rx,ry,"bo")
#plt.plot([0,0],u[:,0], "-k")
plt.plot(xx,xy,"ro")
#plt.plot(new_x,new_y,"ro")
plt.show()
