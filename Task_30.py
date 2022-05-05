# 30. Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  = 3.141. 10-1d≤10-10

import os
from math import pi
from random import*
os.system("cls")

d = randint(1, 10)
print('Вывод = ', d)

print('Пи = ', round(pi, d), '\n')