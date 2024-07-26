N = 9
M = 3

lst = [input().split() for _ in range(N)]

dic = dict()

for i in range(M):
    for j in range(M):
        if i == j == 1:
            continue

        dic[lst[M + i][M + j]] = []

for i in range(0, N, M):
    for j in range(0, N, M):
        if i == j == M:
            continue

        key = lst[i + 1][j + 1]

        for k in range(M):
            for l in range(M):
                if k == l == 1:
                    continue
                dic[key].append(lst[i + k][j + l])

        dic[key].sort()

keys = sorted(dic.keys())

for i in range(N - 1):
    print(f'#{i + 1}. {keys[i]}')

    for j in range(N - 1):
        print(f'#{i + 1}-{j + 1}. {dic[keys[i]][j]}')