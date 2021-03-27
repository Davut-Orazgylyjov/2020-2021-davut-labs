---
# Front matter
lang: ru-RU
title: "Отчет для лабораторной работе №7"
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

Решение заданий

# Задание

![Задание](image/1.png){ #fig:001 width=70% }


# Выполнение лабораторной работы

Импортируем библиотеки и переменные

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
Создаем список t

```Python
t_7 = np.arange(t0_7, tmax_7, dt_7)
t_7 = np.append(t_7, tmax_7)

```
Создаем функции и уравнение:
```Python
def k(t_7):
  return 0.205

def p(t_7):
  return 0.000023

def f(x, t_7):
  return (k(t_7) + p(t_7)*x)*(N1_7-x)
```

Создаем вектор значений

```Python
yf = odeint(f, x01_7, t_7)
```

Показать результаты на дисплее

```Python
plt.figure(figsize=(10,10))
plt.plot(t_7,yf,'r',label='S(t_7)')
plt.show()
```

получаем:

![Результат 1](image/2.png){ #fig:002 width=70% }


![Результат 2](image/3.png){ #fig:003 width=70% }


![Результат 3](image/4.png){ #fig:004 width=70% }




Код на Python для графика 1:
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

t_7 = np.arange(t0_7, tmax_7, dt_7)
t_7 = np.append(t_7, tmax_7)

def k(t_7):
  return 0.205

def p(t_7):
  return 0.000023

def f(x, t_7):
  return (k(t_7) + p(t_7)*x)*(N1_7-x)

yf = odeint(f, x01_7, t_7)

plt.figure(figsize=(10,10))
plt.plot(t_7,yf,'r',label='S(t_7)')
plt.show()
```

Код на Python для графика 2:
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
```

Код на Python для графика 3:
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

t_7 = np.arange(t0_7, tmax_7, dt_7)
t_7 = np.append(t_7, tmax_7)

def k(t_7):
  return 0.05*math.sin(t_7)

def p(t_7):
  return 0.03*math.cos(4*t_7)

def f(x, t_7):
  return (k(t_7) + p(t_7)*x)*(N1_7-x)


yf = odeint(f, x01_7, t_7)

plt.figure(figsize=(10,10))
plt.plot(t_7,yf,'r',label='S(t_7)')
plt.show()
```

# Вывод

Построили код на Python для решения и вывода на экран график распространения рекламы, математическая модель.

