# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# сохраните список в формате JSON.
import json

a = int(input('введите число ->'))

def numprint(x):
     x = list(range(-x, x+1))
     return x

b = numprint(a)
print(b)
with open('data.json', 'w', encoding='utf-8') as fh:  # открываем файл на чтение
                fh.write(json.dumps(b, ensure_ascii=False))
print('Данные в формате Jsone успешно сохранены')

with open('data.txt', 'w') as fh:  # открываем файл на чтение
                fh.write(str(b))
print('Данные в формате TXT успешно сохранены')