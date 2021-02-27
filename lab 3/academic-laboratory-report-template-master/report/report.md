---
# Front matter
lang: ru-RU
title: "Отчет для лабораторной работы №3"
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

Между страной Х и страной У идет война. Численность состава войск
исчисляется от начала войны, и являются временными функциями
x(t) и y(t). В начальный момент времени страна Х имеет армию численностью 32500 человек, а в распоряжении страны У армия численностью в 13800 человек. Для упрощения
модели считаем, что коэффициенты a, b, c, h постоянны. Также считаем P(t) и Q(t) непрерывные функции.

Постройте графики изменения численности войск армии Х и армии У для следующих случаев: (рис. -@fig:001)

![Задание](image/1.png){ #fig:001 width=70% }



# Выполнение лабораторной работы

Импортируем библиотеки и переменные

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

Создаем список значений Time_p, для вычислять поточечно значения 'Численность состава войск':

```Python
Time_p = np.arange(T_p, Limit_time, Step_p)
Time_p = np.append(Time_p, Limit_time)
```

Создаем функции и уравнение:
```Python
--функция п
def p(Time_p):
    return abs((math.sin(Time_p+1)))
--функция q
def q(Time_p):
    return abs((math.cos(Time_p+2)))

--уравнение
def Equation_p(Function_p,Time_p):
    x = Function_p[0]
    y = Function_p[1]
    dxdt = -a*x - b*y + p(Time_p)
///Задание 1
    dydt = -c*x - h*y + q(Time_p)
///
///Задание 2
        dydt = -c*x*y - h*y + q(Time_p)
///
    return (dxdt,dydt)
```

Создаем вектор значений

```Python
Vector_p = (X_p, Y_p)

//даем ему наши функции odeint
Answer_p = odeint(Equation_p, Vector_p, Time_p)

//создаем заранее списки
x = []
y = []

//через цикл добавляем ответы в массив X и массив Y
for i in range(len(Answer_p)):
    x.append(Answer_p[i][0])
    y.append(Answer_p[i][1])


//создаем нулевую полосу где по графику мы поймем что война идет в чьюто сторону 
zero = []
for i in range (len(Time_p)):
    zero = np.append(zero,0)

```


Теперь создаем график и показываем результаты на дисплее
```Python
//создаем график
plt.figure(figsize = (20, 15))
//полоска нулевая будет синей
plt.plot(Time_p, zero, 'b')
//пишем кривую которачя посторется по точкам которые находятся по координатам списка Time_p и списка X
plt.plot(Time_p, x, 'r', label = 'x')
//тоже самое только по списку Y
plt.plot(Time_p, y, 'g', label = 'y')
plt.ylabel('Численность состава войск')
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

И получаем: (рис. -@fig:002)

![Модель боевых действий между регулярными войсками](image/2.png){ #fig:002 width=70% }



(рис. -@fig:002)

![Модель ведение боевых действий с участием регулярных войск и партизанских отрядов](image/3.png){ #fig:003 width=70% }


Код на Python для случая 1:
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

```

Код на Python для случая 2:
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

a = 0.26
b = 0.8
c = 0.62
h = 0.13

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
    dydt = -c*x*y -  h*y+q(Time_p)
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
plt.title('Модель ведение боевых действий с участием регулярных войск и партизанских отрядов')
plt.legend(loc ='upper right')


plt.show()

```
# Выводы

Написали скрипт для вывода моделей боевых действий на дисплей.