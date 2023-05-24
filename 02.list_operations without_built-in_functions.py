dci = []
elems = None
while elems != 'end':
    try:
        elems = input('Bведите элемент списка: ')
        dci.append(int(elems))
    except:
        break


print(dci)
minn = dci[0]
for i in range(1, len(dci)):
    if dci[i] < minn:
        minn = dci[i]

maxx = dci[0]
for i in range(1, len(dci)):
    if dci[i] > maxx:
        maxx = dci[i]

summa = 0
colvo = 0
for i in range(len(dci)):
    summa += dci[i]
    colvo += 1

avr = summa / colvo
nowdic = []
while len(dci) != 0:
    smalle = dci[0]
    for i in range(1, len(dci)):
        if dci[i] < smalle:
            smalle = dci[i]
    nowdic.append(smalle)
    dci.remove(smalle)

print('Минимум ', minn)
print('Большее ', maxx)
print('Среднее ', avr)
print('Красивый ', nowdic)