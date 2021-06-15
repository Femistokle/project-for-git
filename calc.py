a = input('Введите данные ')
b = input('Введите данные ')
if a.isdigit() and b.isdigit():
    print("Сумма = " + str(int(a) + int(b)))
else:
    print('Вы ввели не число')
