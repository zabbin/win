#-*- coding: utf-8 -*-

import pylab
import math

# Картинка в левом верхнем углу

x1 = range (1, 100)
data1 = [math.exp (-n * n / 1000.0) for n in x1]

# Разбиваем окно на две  строки и два столбца. Вывод будет осуществляться в первую область
pylab.subplot (2, 2, 1)

# Вывод данных
pylab.plot (x1, data1, "r")


# Картинка в правом верхнем углу
fracs = [10, 20, 30, 40]

# Разбиваем окно на две  строки и два столбца. Вывод будет осуществляться во вторую область
pylab.subplot (2, 2, 2)
pylab.pie (fracs)

# Картинка снизу
x2 = range (0, 720)

data2 = [math.sin (n * math.pi / 180.0) for n in x2]
data3 = [math.sin (n * math.pi / 180.0 + math.pi / 3) for n in x2]

# Разбиваем окно на две строки и один столбец. Вывод будет осуществляться во вторую область
pylab.subplot (2, 1, 2)

# Вывод данных
pylab.plot (x2, data2)
pylab.plot (x2, data3, "--")

# Добавим легенду
pylab.legend (["label 1", "label 2"])

# Включим сетку
pylab.grid(True)

# Нарисовать все
pylab.show()