N = int(input())
M = int(input())

lst = [[0] * (N + 1) for _ in range(N + 1)]

for m in range(M):
    a, b = map(int, input().split())

    lst[a][b] = 1
    lst[b][a] = 1

used = [0] * (N + 1)

for n in range(2, N + 1):
    if lst[1][n]:
        used[n] = 1
        for i in range(2, N + 1):
            if lst[n][i]:
                used[i] = 1

print(sum(used))