# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from itertools import accumulate # функция для проверки последовательности
import operator # нужен mul для умножения

n = int(input('Введите число-> '))


def get_prods(a):
    return list(accumulate([x for x in range(1, a + 1)], operator.mul))

print(get_prods(n))