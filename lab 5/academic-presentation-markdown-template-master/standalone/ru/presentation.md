---
## Front matter
lang: ru-RU
title: Презентация лабораторной работы 5
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

# Знакомство с задачей об модели «хищник-жертва»:

## Задание

Постройте график зависимости численности хищников от численности жертв,
а также графики изменения численности хищников и численности жертв при
следующих начальных условиях:

![Задание](image/1.png){ #fig:001 width=70% }



## библиотеки и переменные

```Python
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
```

## Функции и уравнение
```Python
t_5 = np.arange(t0_5, tmax_5,dt_5)
t_5 = np.append(t_5,tmax_5)

def syst(x,t_5):
	dx1_5 = -a_5*x[0]+c_5*x[0]*x[1]
	dx2_5 = b_5*x[1]-d_5*x[0]*x[1]
	return dx1_5, dx2_5
```
## Определение значений размера армии

```Python
v0 = (c_5/d_5, a_5/b_5)

yf = odeint (syst,v0,t_5)

x = []
y = []
  
for i in range(len(yf)):
	x.append(yf[i][0])
	y.append(yf[i][1])
```

## Показать результаты на дисплее
```Python

plt.figure(figsize = (8,8))
plt.plot(x,y,'r', label = 'x')
plt.show()
```
## Первый график 

![График №1](image/2.png){ #fig:002 width=70% }

## Второй график 

![График №2](image/3.png){ #fig:003 width=70% }

