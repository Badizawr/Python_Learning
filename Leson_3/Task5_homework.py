# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

from random import randint
lst = [randint(-10, 10) for i in range(20)]

n =int (input('Введите число для поиска-> '))
print(lst)

try:
    if lst.count(n) > 0:
        print('Такое число встречается', lst.count(n), 'раз')
    
except:
    print('такого числа нет')