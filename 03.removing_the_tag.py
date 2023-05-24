srt = input('Введите строку с тегами: ')
newsrt = ""
flag = 0
while flag < len(srt):

    if srt[flag] == '<':
        while srt[flag] != '>':
            flag += 1

    if srt[flag] == '>':    
        flag += 1
        continue
    else:
        newsrt += srt[flag]
    flag += 1

print(newsrt)
