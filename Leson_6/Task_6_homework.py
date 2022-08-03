# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('RLE1_decode.txt', 'r') as data:
    text = data.read().replace(' ', '')


def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

secret = coding(text)  


with open('RLE2_encoded.txt', 'w') as data1:
    text2 = data1.write(secret)


def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

with open('RLE2_encoded.txt', 'r') as data2:
    text3 = data2.read()

magic = decoding(text3)


with open('RLE3_magic.txt', 'w') as data3:
    text2 = data3.write(magic)

