
def menu():
    x = (input('Выберите варианты \n (1)добавить сотрудника (2)удалить сотрудника; (3)Изменить данные (4) Импорт БД \
        (5) Экспорт БД (6)Выход из программы\nВвод: '))
    while True:
        try:
            x = int(x)
            if x < 1 or x > 6:
                x = (input('Введите корректное число')) 
            else:
                break
        except ValueError: 
            x = print("Вы ввели не число. Повторите ввод")
    return x
