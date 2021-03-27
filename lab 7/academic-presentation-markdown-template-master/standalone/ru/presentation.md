---
## Front matter
lang: ru-RU
title: Презентация лабораторной работы 7
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

# Знакомство с заданием

## Задание
Постройте график распространения рекламы, математическая модель которой описывается
следующим уравнением
![Задание](image/1.png){ #fig:001 width=70% }



## библиотек и переменных

```Python
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint
N1_7 = 2300
x01_7 = 20
t0_7 = 0
tmax_7 = 30
dt_7 = 0.1
```

## Функции и уравнение
```Python
t_7 = np.arange(t0_7, tmax_7, dt_7)
t_7 = np.append(t_7, tmax_7)
def k(t_7):
	return 0.205
def p(t_7):
	return 0.000023
def f(x, t_7):
	return (k(t_7) + p(t_7)*x)*(N1_7-x)
```
## Определение значений для графика

```Python
yf = odeint(f, x01_7, t_7)
```

## Показать результаты на дисплее
```Python
plt.figure(figsize=(10,10))
plt.plot(t_7,yf,'r',label='S(t_7)')
plt.show()
```
## График №1

![График 1](image/2.png){ #fig:002 width=70% }

## График №2

![График 2](image/3.png){ #fig:003 width=70% }

## График №3

![График 3](image/4.png){ #fig:004 width=70% }
