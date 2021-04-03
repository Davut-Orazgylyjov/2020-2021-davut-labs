---
## Front matter
lang: ru-RU
title: Презентация лабораторной работы 8
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

# Знакомство с задачей

## Задание 1_1

![Задание](image/1.png){ #fig:001 width=70% }

## Задание 1_2

![Задание](image/2.png){ #fig:002 width=70% }

## Задание 1_3

![Задание](image/3.png){ #fig:003 width=70% }



## библиотеки и переменные

```Python
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
```

## Функции
```Python
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
```

## Значения графика

```Python
x0_8 =[5.5,5]
yf_8 = odeint(f,x0_8,t_8)
```

## Вывод на матрицу

```Python
plt.figure(figsize = (10,10))
plt.plot (t_8,yf_8)
plt.show()
```
## График 1

![График 1](image/4.png){ #fig:004 width=70% }

## График 2

![График 2](image/5.png){ #fig:005 width=70% }
