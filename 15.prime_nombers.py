def prime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


for i in range(1, 50):
    print(f'{i}: {prime(i)}')