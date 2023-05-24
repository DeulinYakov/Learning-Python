print('Здравствуйте, давайте поиграем :)')
answer = input('Задайте ваше слово: ')

dictor = {1: 'АВЕИНОРСТ',
          2: 'ДКЛМПУ',
          3: 'БГЁЬЯ',
          4: 'ЙЫ',
          5: 'ЖЗХЦЧ',
          8: 'ШЭЮ',
          10: 'ФЩЪ'}
noans = answer.upper()
print(noans)
sum = 0

for level in noans:
    for item in dictor.items():
        if level in item[1]:
            sum += item[0]
print(sum)