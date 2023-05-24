def detting_numbers():
    dci = []
    elems = None
    while elems != 'end':
        try:
            elems = input('Bведите элемент списка: ')
            dci.append(int(elems))
        except:
            return dci


def operations(sim, dic):
    """
    Функция берёт два списка,
    в одном списке операции
    в другом списке цифры
    """
    for i in sim:
        if i == 'add':
            total = 0
            for num in dic:
                total += num
            print(f'Сумма элементов списка = {total}')
        elif i == 'sub':
            total1 = 0
            for num in dic:
                total1 -= num
            print(f'Разность элементов списка = {total1}')
        elif i == 'mul':
            total2 = 1
            for num in dic:
                total2 *= num
            print(f'Произведение элементов списка = {total2}')
        else:
            total3 = 1
            for num in dic:
                total3 /= num
            print(f'Частное элементов списка = {total3}')


user = input('Выберите операцию(и): [add, sub, mul, div] ')
#add sub mul div
print(operations(user.split(), detting_numbers()))
