N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

total = N * M * 2

for n in range(N):
    for m in range(1, M):
        total += abs(lst[n][m - 1] - lst[n][m])
    total += lst[n][0] + lst[n][-1]

for m in range(M):
    for n in range(1, N):
        total += abs(lst[n - 1][m] - lst[n][m])
    total += lst[0][m] + lst[-1][m]

print(total)