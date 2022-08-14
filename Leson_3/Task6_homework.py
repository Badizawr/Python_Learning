# Напишите программу, которая определит позицию
# второго вхождения строки в списке либо сообщит, что её нет
# 
# lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"] # ищем: "qwe", ответ: 3
# lst1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"] # ищем: "йцу", ответ: 5
# lst2 = ["йцу", "фыв", "ячс", "цук", "йцукен"] # ищем: "йцу", ответ: -1
# lst3 = ["123", "234", 123, "567"] # ищем: "123", ответ: -1
# lst4 = [] # ищем: "123", ответ: -1
# 
# 
# n = input('Введите что ищем-> ')
# 
# def find_second_entry(ls, a):
#     num = 0
#     for i in range(len(ls)):
#         if ls[i]== n:
#             num+=1
#             if num==2:
#                 return (i)
#     else:
#         return (-1)
#     
# 
# print(find_second_entry(lst2, n))

counter = 0
for i in range(99, 102):
    temp = i
    while temp > 0:
        counter += 1
        temp //= 10
print(counter)