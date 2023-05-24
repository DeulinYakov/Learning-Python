dci = []

summ = sum(dci[0])
for i in range(len(dci)):
    temp = 0
    for j in range(len(dci)):
        temp += dci[j][i]
    if temp != summ or sum(dci[i]) !=summ:
        print('f')
    print('t')
