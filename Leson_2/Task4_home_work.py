#  - Напишите программу, которая принимает на вход
#  вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

# print(sum(map(float, list(input('Введите число -> ')))))

num = input ('Введите вещественное число : ')

def Cal_num(num):
    result = 0
    for i in range (len(num)):
         if num[i].isdigit():
            result += int (num[i])
    print(result)

Cal_num(num)