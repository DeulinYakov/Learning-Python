import random

print("Привет! Давайте поиграем в угадайку чисел!")


def inputab():
    a, b = None, None
    while a is None:
        try:
            a = int(input('Из какого диапазона вы хотите угадать число?: '))
        except:
            print(a)
            print('Вы написали неправильно. пробовать снова')

    while b is None:
        try:
            b = int(input('До какого числа вы хотите угадывать? : '))
        except:
            print('Вы написали неправильно. пробовать снова')

    while b is not None:
        if a >= b:
            print('Вы написали неправильно. пробовать снова')
            inputab()

        n = random.randint(a, b)

        f = True

        while f == True:

            answer = input('введите ответ: ')

            if answer == 'x':
                print('До свидания')
                break
            else:
                while answer.isdigit() != True:
                    print('Вы написали неправильно. пробовать сноваn')
                    answer = int(input('Введите число: '))

                answer = int(answer)

                if n > answer:
                    print('Число больше ')
                elif n < answer:
                    print('Число меньше ')
                elif n == answer:
                    print('Поздравляем! Вы победили!\n')
                    f = False

                    again = input("Хотите сыграть снова? Введите 'да' или 'нет': \n").lower()
                    while again != "да" and again != "нет":
                        print('Вы написали неправильно. Попробуйте снова. ')
                        again = input("Хотите сыграть снова? Введите 'да' или 'нет': \n").lower()

                    if again == 'нет':
                        print('До свидания')
                        break
                    elif again == 'да':
                        inputab()


inputab()
