"""
1.Развернуть одномерный массив (сделать так, чтобы его элементы шли в обратном порядке).
2.Найти максимальный нечетный элемент в массиве.
3.Замените все нечетные элементы массива на ваше любимое число.
4.Создайте массив первых n нечетных чисел, записанных в порядке убывания.
  Например, если n=5, то ответом будет array([9, 7, 5, 3, 1]).
  Функции, которые могут пригодиться при решении: .arange()
5.вычислите самое близкое и самое дальнее числа к данному в рассматриваемом массиве чисел.
  Например, если на вход поступают массив array([0, 1, 2, 3, 4])
  и число 1.33, то ответом будет (1, 4). Функции, которые могут
  пригодиться при решении: .abs(), .argmax(), .argmin()
6.Вычисляющую первообразную заданного полинома
  (в качестве константы возьмите ваше любимое число).
  Например, если на вход поступает массив коэффициентов
  array([4, 6, 0, 1]), что соответствует полиному  4x^3+6x^2+1 ,
  на выходе получается массив коэффициентов array([1, 2, 0, 1, -2]),
  соответствующий полиному  x^4+2x^3+x−2 .
  Функции, которые могут пригодиться при решении: .append()
7.Пользуясь пунктом 6, посчитайте первую производную
  для заданного полинома в заданной точке.
"""

import numpy as np
# 1
data = np.array([1, 2, 3, 4])
reversed_data = np.flip(data)
print(f"1: {reversed_data}")
# 2
data = np.array([1, 2, 3, 4])
need_items = data[data % 2 != 0]
max_item = np.max(need_items)
print(f"2: {max_item}")
# 3
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
data[data % 2 != 0] = 55
print(f"3: {data}")
# 4
n = int(input())
need_items = np.arange(1, 2*n, 2)
reverse_items = np.flip(need_items)
print(f"4: {reverse_items}")
# 5
to_input = input()
array = np.array([float(x) for x in to_input.split()])
num = float(input())
dif = np.abs(array - num)
closest_indx = np.argmin(dif)
furthest_indx = np.argmax(dif)
closest = array[closest_indx]
furthest = array[furthest_indx]
print(f"5: {closest, furthest}")
# 6


def integral(coef, constant=-2):
    n = len(coef)
    integral_coef = [0] * n

    for i in range(n):
        integral_coef[i] = coef[i] / (n - i)

    integral_coef.append(constant)
    return np.array(integral_coef)


to_input = input()
array = np.array([float(x) for x in to_input.split()])
result = integral(array)
print(f"6: {result}")
# 7


def derivative(coef, x):
    n = len(coef)
    value = 0

    for i in range(n):
        value += coef[i] * x ** (n - i - 1)

    return value


x = int(input())
value = derivative(array, x)
print(f"7: {value}")
