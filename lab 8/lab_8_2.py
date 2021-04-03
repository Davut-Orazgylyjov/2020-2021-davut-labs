import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint

p_cr_8 = 35
N__8 = 41
q_8 = 1

tau1_8 = 14
tau2_8 = 7

p1_8 = 6.5
p2_8 = 15


a1_8 = p_cr_8 / (tau1_8 * tau1_8 * p1_8 * p1_8 * N__8 *q_8)
a2_8 = p_cr_8 / (tau2_8 * tau1_8 * p2_8 * p1_8 * N__8 *q_8)
b_8 = p_cr_8 / (tau1_8 * tau1_8 * tau2_8 * tau2_8 * p1_8 * p1_8*p2_8*p2_8*N__8*q_8)
c1_8 = (p_cr_8 - p1_8)/ (tau1_8*tau1_8)
c2_8 = (p_cr_8 - p1_8)/ (tau2_8*tau2_8)

t0_8 = 0
tmax_8 = 30
dt_8 = 0.01


t_8 = np.arange(t0_8,tmax_8,dt_8)
t_8 = np.append(t_8,tmax_8)

def f(x,t_8):
	dx1_8 = (c1_8/c1_8)* x[0] - (a1_8/c1_8)*x[0]*x[0] - (b_8/c1_8) * x[0] * x[1]
	dx2_8 = (c2_8/c2_8)* x[1] - ((a2_8/c1_8)+0.00021)*x[1]*x[1] - (b_8/c1_8) * x[0] * x[1]
	return dx1_8,dx2_8

x0_8 =[5.5,5]
yf_8 = odeint(f,x0_8,t_8)

plt.figure(figsize = (10,10))
plt.plot (t_8,yf_8)
plt.show()