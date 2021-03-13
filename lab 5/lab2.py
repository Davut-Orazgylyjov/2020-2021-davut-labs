import matplotlib.pyplot as plt
import numpy as np

from scipy.integrate import odeint

a_5 = 0.58
b_5 = 0.048
c_5 = 0.38
d_5 = 0.028

t0_5 = 0
tmax_5 = 400
dt_5 = 0.1


t_5 = np.arange(t0_5, tmax_5,dt_5)
t_5 = np.append(t_5,tmax_5)

def syst(x,t_5):
	dx1_5 = -a_5*x[0]+c_5*x[0]*x[1]
	dx2_5 = b_5*x[1]-d_5*x[0]*x[1]
	return dx1_5, dx2_5

v0 = (c_5/d_5, a_5/b_5)

yf = odeint (syst,v0,t_5)

x = []
y = []
  
for i in range(len(yf)):
	x.append(yf[i][0])
	y.append(yf[i][1])

plt.figure(figsize = (8,8))
plt.plot(x,y,'r', label = 'x')
plt.show()