a = b = None
answer = None
print('Здравствуйте, давайте проверим мою интуицию')
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

a -= 1
b += 1
i = 1
while answer != '=':

    c = (a + b) // 2
    print(c)
    answer = input('Укажите "<" ">" или "=": ')
    if b - 1 == a:
        print('Попался жулик')
        answer = '='
    elif answer == '>':
        a = c
        i += 1
    elif answer == '=':
        print('Круасавчик')
    elif answer == '<':
        b = c
        i += 1
