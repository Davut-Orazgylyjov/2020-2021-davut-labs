import numpy as np
import matplotlib.pyplot as plt
import math

from scipy.integrate import odeint

N1_7 = 2300
x01_7 = 20

t0_7 = 0
tmax_7 = 30
dt_7 = 0.1

t_7 = np.arange(t0_7, tmax_7, dt_7)
t_7 = np.append(t_7, tmax_7)

def k(t_7):
	return 0.0000305

def p(t_7):
	return 0.24

def f(x, t_7):
	return (k(t_7) + p(t_7)*x)*(N1_7-x)


yf = odeint(f, x01_7, t_7)

plt.figure(figsize=(10,10))
plt.plot(t_7,yf,'r',label='S(t_7)')
plt.show()