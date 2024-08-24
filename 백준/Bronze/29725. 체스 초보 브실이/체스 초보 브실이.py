N = 8
lst = [input() for _ in range(N)]

dic = {'k': 0, 'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9}

white = 0
black = 0

for i in range(N):
    for j in range(N):
        if lst[i][j] == '.':
            continue
        elif lst[i][j].isupper():
            white += dic[lst[i][j].lower()]
        else:
            black += dic[lst[i][j]]

print(white - black)