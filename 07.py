x = None
while x is None:
    try:
        x = int(input('Bведите элемент: '))
    except:
        print('заново')

fac = 1
while x > 1:
    fac *= x
    x -= 1
print(fac)
