N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
used = [[0] * N for _ in range(N)]
used[0][0] = 1

for i in range(N):
    for j in range(N):
        for k in range(i):
            if lst[k][j] == i - k:
                used[i][j] += used[k][j]

        for k in range(j):
            if lst[i][k] == j - k:
                used[i][j] += used[i][k]

print(used[-1][-1])