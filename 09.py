word = 'агаггагагагаыв'
d = dict()

for i in word:
    d[i] = word.count(i)
print(d)