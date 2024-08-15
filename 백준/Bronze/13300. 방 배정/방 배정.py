N, K = map(int, input().split())
lst = [[0] * 2 for _ in range(6)]

for _ in range(N):
    S, Y = map(int, input().split())
    lst[Y - 1][S] += 1

result = 0
for i in range(6):
    for j in range(2):
        result += lst[i][j] // K
        if lst[i][j] % K:
            result += 1

print(result)