---
# Front matter
lang: ru-RU
title: "Отчет по лабораторной работе 2"
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

Решить задачу о погоне

# Задание

Вариант 41

На море в тумане катер береговой охраны преследует лодку браконьеров.
Через определенный промежуток времени туман рассеивается, и лодка
обнаруживается на расстоянии 17,4 км от катера. Затем лодка снова скрывается в
тумане и уходит прямолинейно в неизвестном направлении. Известно, что скорость
катера в 4,8 раза больше скорости браконьерской лодки.

1. Запишите уравнение, описывающее движение катера, с начальными
условиями для двух случаев (в зависимости от расположения катера
относительно лодки в начальный момент времени).
2. Постройте траекторию движения катера и лодки для двух случаев.
3. Найдите точку пересечения траектории катера и лодки 


# Выполнение лабораторной работы

Чтобы лодка нашла лодку, она должна сначала двигаться по прямой к полюсу (месту, где лодку видели в последний раз) в течение *t* времени. За это время лодка преодолеет расстояние *x*, а лодка либо *k-x*, либо *k + x*, в зависимости от положения лодки. Время для этого расстояния будет *x / v* и *k-x / 4.8v* или *k + x / 4.8v*

Приравниваем равенства, так как время там одинаковое:

$\frac{x}{v}$ = $\frac{k-x}{4.8v}$ (случай 1)

$\frac{x}{v}$ = $\frac{k+x}{4.8v}$ (случай 2)

Сокращаем и получаем два значения:

x~1~ = $\frac{k}{5.8}$

x~2~ = $\frac{k}{3.8}$


Теперь, когда наша лодка находится на том же расстоянии от шеста, что и лодка, нам нужно, чтобы лодка отошла от шеста с той же скоростью, что и лодка, при этом также вращаясь вокруг шеста, чтобы встретить лодку.

Для этого мы выделим две скорости V~t~ и V~r~. (рис. -@fig:001)

![Разложение скоростей катера на радиальную и тангенциальную состовляющие](image/3.png){ #fig:001 width=70% }


Vr это скорость отдаления от полюса, она должна быть равна скорости лодки будет равна (V~r~ = V)
Теперь нужно найти V~t~. Для этого мы используем теорему Пифагора, чтобы получить: V~t~ = $\sqrt{22.04}$v 


Теперь у нас следующие уравнения:

*$\frac{dr}{dt}$ = v*

*r$\frac{d\Theta}{dt}$ = $\sqrt{22.04}v$*

и их начальные условия:

$\Theta$~0~=0

r~0~=x~1~

или


$\Theta$~0~=$-\pi$

r~0~=x~2~


Скоращаем производную по *t*, приравниваем  и получаем это уравнения:

*$\frac{dr}{d\Theta}$ = $\frac{r}{\sqrt{22.04}}$*


Теперь у нас есть функция для полярных координат, которая покажет траекторию катера для двух случаев (рис. -@fig:002) (рис. -@fig:003)


![Траектории катера и лодки для случая 1. Катер обозначен зеленым, а лодка красным](image/1.png){ #fig:002 width=15% }


![Траектории катера и лодки для случая 2](image/2.png){ #fig:003 width=15% }

Для первого случая вы можете видеть, что они встретились на расстоянии 58 единиц от полюса, а для второго случая - на 110 единиц.


Код на Scilab для случая 1:
```Scilab
s=17.4;
fi=3*%pi/4;
function dr=f(tetha, r)
dr=r/sqrt(22.04);
endfunction;
r0=s;
tetha0=0*(-%pi);
tetha=0:0.01:2*%pi;
r=ode(r0,tetha0,tetha,f);
function xt=f2(t)
 xt=tan(fi)*t;
endfunction
t=0:1:200;
polarplot(tetha,r,style = color('green')); 
plot2d(t,f2(t),style = color('red'));
```

Код на Scilab для случая 2:
```Scilab

s=17.4;
fi=3*%pi/4;
function dr=f(tetha, r)
dr=r/sqrt(22.04);
endfunction;
r0=s;
tetha0=1*(-%pi);
tetha=0:0.01:2*%pi;
r=ode(r0,tetha0,tetha,f);
function xt=f2(t)
 xt=tan(fi)*t;
endfunction
t=0:1:200;
polarplot(tetha,r,style = color('green')); 
plot2d(t,f2(t),style = color('red'));
```
# Выводы

Решили проблему погони и познакомились с новым языком программирования Scilab.
