
---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе 8"
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

![Задание лабораторной работы](image/1.png){ #fig:001 width=70% }
![Задание лабораторной работы](image/2.png){ #fig:001 width=70% }
![Задание лабораторной работы](image/3.png){ #fig:001 width=70% }


# Выполнение лабораторной работы

Для начала мы импортируем библиотеки для построения кода и вводим наши переменные: 

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

Теперь мы создаем список значений t, которое мы будем использовать чтобы вычислять поточечно значения "Численность армии":

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

```
Обратите внимаение, что я также добавил элемент tmax в конец списка. Дело в том, что функция np.arange заполняет от нуля до tmax - dt, поэтому надо добавлять еще один элемент отдельно.


Теперь создаем систему уравнений:
```Python
def f(x,t_8):
  dx1_8 = (c1_8/c1_8)* x[0] - (a1_8/c1_8)*x[0]*x[0] - (b_8/c1_8) * x[0] * x[1]
  dx2_8 = (c2_8/c2_8)* x[1] - (a2_8/c1_8)*x[1]*x[1] - (b_8/c1_8) * x[0] * x[1]
  return dx1_8,dx2_8
```

Запускаем команду odeint, которая найдет значения поточечно.

```Python
x0_8 =[5.5,5]
yf_8 = odeint(f,x0_8,t_8)
```

Теперь создаем график и выводим на экран.
график будет красного цвета с обозначением "x". Размер графика 10 на 10 единиц.

```Python
plt.figure(figsize = (10,10))
plt.plot (t_8,yf_8)
plt.show()
```

И получаем:

![Результат 1](image/4.png){ #fig:002 width=70% }
![Результат 2](image/5.png){ #fig:002 width=70% }


Код:
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
  dx2_8 = (c2_8/c2_8)* x[1] - (a2_8/c1_8)*x[1]*x[1] - (b_8/c1_8) * x[0] * x[1]
  return dx1_8,dx2_8

x0_8 =[5.5,5]
yf_8 = odeint(f,x0_8,t_8)

plt.figure(figsize = (10,10))
plt.plot (t_8,yf_8)
plt.show()
```
# Вывод

Построили код на Python для решения и вывода на экран графиков эффективности рекламы для 3 случаев.