# В ящике имеется 15 деталей, из которых 9 окрашены. 
# Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все извлеченные детали окрашены?

# Рассчитываем вероятность по формуле: P = n/m, где n - кол-во благоприятных исходов, m - кол-во общих исходов
# Кол-во общих исходов m расчитываем как кол-во возможных сочетаний 3-х деталей из 15-ти возможных
# Для рассчета кол-ва сочетаний используется функция "c"
from math import factorial as fc

def c (n, k):
    return fc(n) / (fc(k)*fc(n-k))

m = c(15, 3)

# Расчитываем кол-во сочетаний 3-х деталей из 9-ти окрашенных
n = c(9, 3) 

print (f'Вероятность того, что все извлеченные детали окрашены составляет {n/m*100}%')