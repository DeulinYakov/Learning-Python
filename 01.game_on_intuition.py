import random

a = b = h = None
con = True
f = 1
print('Здравствуйте, давайте проверим вашу интуицию')
while con:
    while f == 1:
        while a is None:
            try:
                a = int(input('Введите первое число: '))
            except:
                print('Попробуйте ввести число')
        while b is None:
            try:
                b = int(input('Введите второе число: '))
            except:
                print('Попробуйте ввести число')
        if a > b:
            print('А должно быть меньше В')
            a = b = None
        elif a < b:
            f = 2
    n = random.randint(a, b)
    while f == 2:
        h = input('ваш ответ:')
        if h == 'x':
            f = 0
            con = False
        elif int(n) == int(h):
            print('молодец')
            A = input('чтобы начать заново нажмите "y", для выхода нажмите "x": ')
            if A == 'y':
                f = 1
            if A == 'x':
                f = 0
                con = False
        elif int(n) < int(h):
            print('Меньше')
            continue
        else:
            print('больше')
            continue
