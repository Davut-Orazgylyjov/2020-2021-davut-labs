import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint

a = 0.58
b = 0.048
c = 0.38
d = 0.028

t0 = 0
tmax = 400
dt = 0.1


t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)

def syst(x,t):
	dx1 = -a*x[0]+c*x[0]*x[1]
	dx2 = b*x[1]-d*x[0]*x[1]
	return dx1, dx2


v0 = (7,15)

yf = odeint (syst, v0, t)

x = []
y = []
  
for i in range(len(yf)):
	x.append(yf[i][0])
	y.append(yf[i][1])

plt.figure(figsize = (8,8))
plt.plot(x,y, 'r', label = 'x')
plt.show()