lst = []

for i in range(5):
    word = list(input())

    if len(word) < 15:
        word = word + [''] * (15 - len(word))

    lst.append(word)

for j in range(15):
    for i in range(5):
        if lst[i][j]:
            print(lst[i][j], end = '')