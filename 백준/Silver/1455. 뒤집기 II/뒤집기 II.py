N, M = map(int, input().split())
lst = [[False] * M for _ in range(N)]

for n in range(N):
    tmp = input()
    for m in range(M):
        if tmp[m] == '1':
            lst[n][m] = True

result = 0
n = N - 1
m = M - 1
while n >= 0 and m >= 0:
    for i in range(n, -1, -1):
        if lst[i][m]:
            result += 1

            for k in range(i + 1):
                for l in range(m + 1):
                    lst[k][l] = not lst[k][l]

    for j in range(m, -1,- 1):
        if lst[n][j]:
            result += 1

            for k in range(n + 1):
                for l in range(j + 1):
                    lst[k][l] = not lst[k][l]

    n -= 1
    m -= 1

print(result)