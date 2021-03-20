---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе 6"
subtitle: "НФИбд-02-18"
author: "Оразклычев Давут"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Постройте графики изменения числа особей в каждой из трех групп.

# Задание

![Задание](image/1.png){ #fig:001 width=70% }


# Выполнение лабораторной работы

Импортируем библиотеки и переменные

```Python
import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint

a = 0.17
b = 0.046

R0 = 1
I0 = 30
N = 5000
S0 = N - I0 - R0

t0 = 0
tmax = 200
dt = 0.01
```
Создаем список t

```Python
t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)
```
Создаем функции и уравнение:

```Python

def syst(x, t):
    dx1 = 0
    dx2 = -b * x[1]
    dx3 = b * x[1]
    return dx1, dx2, dx3

```
Создаем вектор значений

```Python
v0 = (S0, I0, R0)
yf = odeint(syst, v0, t)

y1 = []
y2 = []
y3 = []

for i in range(len(yf)):
    y1.append(yf[i][0])
    y2.append(yf[i][1])
    y3.append(yf[i][2])

```
Показать результаты на дисплее

```Python
plt.figure(figsize=(10, 10))
plt.plot(t, y1, 'r', label='S(t)')
plt.plot(t, y2, 'b', label='I(t)')
plt.plot(t, y3, 'g', label='R(t)')
plt.legend( loc = "upper right")

plt.show()
```

И получаем:

![Результат 1](image/2.png){ #fig:002 width=70% }


![Результат 2](image/3.png){ #fig:003 width=70% }



Код на Python для графика 1:
```Python
import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint

a = 0.17
b = 0.046

R0 = 1
I0 = 30
N = 5000
S0 = N - I0 - R0

t0 = 0
tmax = 200
dt = 0.01

t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)

def syst(x, t):
    dx1 = 0
    dx2 = -b * x[1]
    dx3 = b * x[1]
    return dx1, dx2, dx3


v0 = (S0, I0, R0)
yf = odeint(syst, v0, t)

y1 = []
y2 = []
y3 = []

for i in range(len(yf)):
    y1.append(yf[i][0])
    y2.append(yf[i][1])
    y3.append(yf[i][2])

plt.figure(figsize=(10, 10))
plt.plot(t, y1, 'r', label='S(t)')
plt.plot(t, y2, 'b', label='I(t)')
plt.plot(t, y3, 'g', label='R(t)')
plt.legend( loc = "upper right")

plt.show()

```

Код на Python для графика 2:
```Python
import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint

a = 0.17
b = 0.046

R0 = 1
I0 = 30
N = 5000
S0 = N - I0 - R0

t0 = 0
tmax = 200
dt = 0.01

t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)

def syst(x, t):
    dx1 = -a *x[0]
    dx2 = a*x[0] - b*x[1]
    dx3 = b * x[1]
    return dx1, dx2, dx3


v0 = (S0, I0, R0)
yf = odeint(syst, v0, t)

y1 = []
y2 = []
y3 = []

for i in range(len(yf)):
    y1.append(yf[i][0])
    y2.append(yf[i][1])
    y3.append(yf[i][2])

plt.figure(figsize=(10, 10))
plt.plot(t, y1, 'r', label='S(t)')
plt.plot(t, y2, 'b', label='I(t)')
plt.plot(t, y3, 'g', label='R(t)')
plt.legend( loc = "upper right")

plt.show()

```

# Вывод

Построили код на Python для решения изменения числа особей в каждой из трех групп.

