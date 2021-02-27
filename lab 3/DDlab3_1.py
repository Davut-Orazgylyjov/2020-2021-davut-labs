import matplotlib.pyplot as plt
import math
import numpy as np
import pandas
import scipy as sp
from scipy.integrate import odeint 

X_p = 32500

Y_p = 13800
T_p = 0

a = 0.12
b = 0.54
c = 0.4
h = 0.27

Limit_time = 3
Step_p = 0.05

Time_p = np.arange(T_p, Limit_time, Step_p)

Time_p = np.append(Time_p, Limit_time)

def p(Time_p):
    return abs((math.sin(Time_p+1)))

def q(Time_p):
    return abs((math.cos(Time_p+2)))

def Equation_p(Function_p,Time_p):
    x = Function_p[0]
    y = Function_p[1]
    dxdt = -a*x-b*y+p(Time_p)
    dydt = -c*x -  h*y+q(Time_p)
    return (dxdt,dydt)

Vector_p = (X_p,Y_p)

Answer_p = odeint(Equation_p,Vector_p,Time_p)

x = []
y = []

for i in range(len(Answer_p)):
    x.append(Answer_p[i][0])
    y.append(Answer_p[i][1])

zero = []
for i in range (len(Time_p)):
    zero = np.append(zero,0)


plt.figure(figsize =(20,15))
plt.plot(Time_p,zero, 'b')
plt.plot(Time_p,x,'r',label = 'x')
plt.plot(Time_p,y,'y',label = 'y')
plt.ylabel('Численность состава восйк')
plt.xlabel('Время')
plt.title('Модель боевых действий между регулярными войсками')
plt.legend(loc ='upper right')


plt.show()
