---
## Front matter
lang: ru-RU
title: Презентация для лабораторной работы №3
author: |
	Оразклычев Давут\inst{1}
institute: |
	\inst{1}RUDN University, Moscow, Russian Federation
date: 2020-2021 г., Москва

## Formatting
mainfont: Times New Roman
romanfont: Times New Roman
sansfont: Times New Roman
monofont: Times New Roman
toc: false
slide_level: 2
theme: metropolis
header-includes:
- \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
- '\makeatletter'
- '\beamer@ignorenonframefalse'
- '\makeatother'
aspectratio: 43
section-titles: true
---

# Знакомство с боевой задачей

## Задание

Постройте графики изменения численности войск армии Х и армии У для следующих случаев: (рис. -@fig:001)

![Задание](image/1.png){ #fig:001 width=70% }



##  библиотеки и переменные

```Python
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas
import scipy as sp
from scipy.integrate import odeint 
X_p = 32500
Y_p = 13800
T_p = 0
///Задание 1
a = 0.12
b = 0.54
c = 0.4
h = 0.27
///
///Задание 2
a = 0.26
b = 0.8
c = 0.62
h = 0.13
///
Limit_time = 3
Step_p = 0.05
```

## Функции и уравнение
```Python
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
///Задание 1
    dydt = -c*x - h*y + q(Time_p)
///
///Задание 2
        dydt = -c*x*y - h*y + q(Time_p)
///
    return (dxdt,dydt)
```
## Определение значений размера армии

```Python
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
```

## Показать результаты на дисплее
```Python
plt.figure(figsize =(20,15))
plt.plot(Time_p,zero, 'b')
plt.plot(Time_p,x,'r',label = 'x')
plt.plot(Time_p,y,'y',label = 'y')
plt.ylabel('Численность состава восйк')
plt.xlabel('Время')
///Задание 1
plt.title('Модель боевых действий между регулярными войсками')
///
///Задание 2
plt.title('Модель ведение боевых действий с участием регулярных войск и партизанских отрядов')
///
plt.legend(loc ='upper right')
plt.show()
```
## Первый график 

![Модель боевых действий между регулярными войсками](image/2.png){ #fig:002 width=70% }

## Второй график 

![Модель ведение боевых действий с участием регулярных войск и партизанских отрядов](image/3.png){ #fig:003 width=70% }


## {.standout}

Спасибо за внимание.
