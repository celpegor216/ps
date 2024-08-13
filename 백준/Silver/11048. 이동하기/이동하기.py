N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i == j == 0:
            continue
        elif i == 0:
            lst[i][j] += lst[i][j - 1]
        elif j == 0:
            lst[i][j] += lst[i - 1][j]
        else:
            lst[i][j] += max(lst[i - 1][j], lst[i][j - 1], lst[i - 1][j - 1])

print(lst[-1][-1])