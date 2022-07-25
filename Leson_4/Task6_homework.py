# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N



def primfacs(n):
   fac = list()
   i = 2
   while (i <= n):
    if (n % i) == 0:
         fac.append(i)
         n = n / i
    else:
        i += 1
  
   return fac

try:
    a = int(input('Введите число для факторизации -> '))
    print(primfacs(a))

except:
    print('Что-то пошло не так')