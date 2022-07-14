# сделать функцию, на вход принимающую список, на выходе возращающая словарь, 
# где указаны максимальное число, минимальное, их индексы, и среднее арифметическое

input = [56, 5645, 4, 68, 64, 96, 64, 64, 496, -2415, 6412, -452, 0]

def fun(input_list):
    max = input_list[0]
    min = input_list[0]
    max_index = 0
    min_index = 0
    avg = 0
    for i in range(len(input_list)):
             if input_list[i] > max:
                max = input_list[i]
                max_index = i
    if input_list[i] < min:
            min = input_list[i]
            min_index = i
            avg += input_list[i]
            avg /= len(input_list)

    output = {}
    output["Минимальное значение"] = min
    output["Максимальное значение"] = max
    output["Индек минимального значения"] = min_index
    output["Индек максимального значенияе"] = max_index
    output["Среднее арифметическое"] = avg

    return output


output = fun(input)
print(input)
for k, v in output.items():
    print(f"{k} - {v}")


# N = 5

# def inisp(N):
#     sp = [];
#     for i in range(1,N+1):
#         sp.append(round((1+1/i)**i,2))
#     return sp

# def inib(sp):
#     bib = {}
#     max = sp[0]
#     idmax = 0
#     min = sp[0]
#     idmin = 0
#     sum = 0
#     for i in range(len(sp)):
#         if(max<sp[i]):
#             max = sp[i]
#             idmax = i
#         if(min>sp[i]):
#             min = sp[i]
#             idmin = i
#         sum += sp[i]
#     sred = sum/len(sp)
#     bib['max'] = max
#     bib['idmax'] = idmax
#     bib['min'] = min
#     bib['idmin'] = idmin
#     bib['sred'] = sred
#     return bib

# spisok = inisp(N)
# bibl = {}
# print(spisok)
# bibl = inib(spisok)
# print(bibl)
# file = open('HW1.txt','a')
# for a,b in bibl.items():
#     file.write(f'{a} - {b} ')
# file.write('\n')
# file.close()
