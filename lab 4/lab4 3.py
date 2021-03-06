import numpy as nmp
import math
import matplotlib.pyplot as plt

from scipy.integrate import odeint

a_1 = 5
b_1 = 2.00

Time_null = 0
Time_Max = 37
Step = 0.05

t = nmp.arange(Time_null, Time_Max, Step)
t = nmp.append(t, Time_Max)

def p(t):
	return (2 * math.sin(t*6))
	return 0

def syst(x,t):
	return x[1], -a_1 * a_1 * x[0] - b_1 * x[1] - p(t)

v0 = (1, 1.2)

yf = odeint(syst, v0, t)

x = []
y = []

for i in range(len(yf)):
	x.append(yf[i][0])
	y.append(yf[i][1])

plt.figure(figsize = (10,10))
plt.plot(x,y,'r', label = 'x')
plt.show()
