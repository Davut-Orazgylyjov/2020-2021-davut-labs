---
# Front matter
lang: ru-RU
title: "Отчет для лабораторной работе  №5"
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

Постройте график зависимости численности хищников от численности жертв,
а также графики изменения численности хищников и численности жертв 

# Задание

![Задание](image/1.png){ #fig:001 width=70% }


# Выполнение лабораторной работы

Импортируем библиотеки и переменные

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

Создаем список t

```Python
t_5 = np.arange(t0_5, tmax_5,dt_5)
t_5 = np.append(t_5,tmax_5)
```

Создаем функции и уравнение:
```Python
def syst(x,t_5):
  dx1_5 = -a_5*x[0]+c_5*x[0]*x[1]
  dx2_5 = b_5*x[1]-d_5*x[0]*x[1]
  return dx1_5, dx2_5
```

Создаем вектор значений
```Python
v0 = (c_5/d_5, a_5/b_5)

yf = odeint (syst,v0,t_5)

x = []
y = []
  
for i in range(len(yf)):
  x.append(yf[i][0])
  y.append(yf[i][1])
```

Показать результаты на дисплее

```Python
plt.figure(figsize = (8,8))
plt.plot(x,y,'r', label = 'x')
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

a = 0.58
b = 0.048
c = 0.38
d = 0.028

t0 = 0
tmax = 400
dt = 0.1


t = np.arange(t0, tmax, dt)
t = np.append(t, tmax)

def syst(x,t):
  dx1 = -a*x[0]+c*x[0]*x[1]
  dx2 = b*x[1]-d*x[0]*x[1]
  return dx1, dx2


v0 = (7,15)

yf = odeint (syst, v0, t)

x = []
y = []
  
for i in range(len(yf)):
  x.append(yf[i][0])
  y.append(yf[i][1])

plt.figure(figsize = (8,8))
plt.plot(x,y, 'r', label = 'x')
plt.show()
```

Код на Python для графика 2:
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


t_5 = np.arange(t0_5, tmax_5,dt_5)
t_5 = np.append(t_5,tmax_5)

def syst(x,t_5):
  dx1_5 = -a_5*x[0]+c_5*x[0]*x[1]
  dx2_5 = b_5*x[1]-d_5*x[0]*x[1]
  return dx1_5, dx2_5

v0 = (c_5/d_5, a_5/b_5)

yf = odeint (syst,v0,t_5)

x = []
y = []
  
for i in range(len(yf)):
  x.append(yf[i][0])
  y.append(yf[i][1])

plt.figure(figsize = (8,8))
plt.plot(x,y,'r', label = 'x')
plt.show()

```

# Вывод

Построили код на Python для решения и вывода на экран графика зависимости численности хищников от численности жертв, а также стационарного состояния системы.


Построили код на Python для решения модели «хищник-жертва».