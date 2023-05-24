def perfect(a):
    num = []
    for i in range(1, a):
        if a % i == 0:
            num.append(i)
        return sum(num) == a


for j in range(1, 50):
    print(f"{j}: {perfect(j)}")
