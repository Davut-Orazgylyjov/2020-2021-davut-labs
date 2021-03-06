---
## Front matter
lang: ru-RU
title: Презентация лабораторной работы 4
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


# Знакомство с задачей об осциляторах

## Задание

Постройте фазовый портрет гармонического осциллятора и решение уравнения гармонического осциллятора: (рис. -@fig:001)

![Задание](image/1.png){ #fig:001 width=70% }



##  библиотеки и переменные

```Python
import numpy as nmp
import math
import matplotlib.pyplot as plt

from scipy.integrate import odeint

a_1 = 3.5
b_1 = 0.00

Time_null = 0
Time_Max = 37
Step = 0.05

```

## Функции и уравнение
```Python

t = nmp.arange(Time_null, Time_Max, Step)
t = nmp.append(t, Time_Max)

def p(t):
	return 0

def syst(x,t):
	return x[1], -a_1 * a_1 * x[0] - b_1 * x[1] - p(t)
```
## Определение значений размера армии

```Python
v0 = (1, 1.2)

yf = odeint(syst, v0, t)

x = []
y = []

for i in range(len(yf)):
	x.append(yf[i][0])
	y.append(yf[i][1])
```

## Показать результаты на дисплее
```Python
plt.figure(figsize = (10,10))
plt.plot(x,y,'r', label = 'x')
plt.show()

```
## Первый график 

![Колебания гармонического осциллятора без затуханий и без действий внешней силы](image/2.png){ #fig:002 width=70% }


## Второй график 

![Колебания гармонического осциллятора c затуханием и без действий внешней силы](image/3.png){ #fig:003 width=70% }


## Третий график 

![Колебания гармонического осциллятора c затуханием и под действием внешней силы](image/4.png){ #fig:004 width=70% }

