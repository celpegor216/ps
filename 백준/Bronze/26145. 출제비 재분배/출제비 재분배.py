N, M = map(int, input().split())
lst = list(map(int, input().split()))
i_to_j = [list(map(int, input().split())) for _ in range(N)]

result = lst + [0] * M

for i in range(N):
    for j in range(N + M):
        result[i] -= i_to_j[i][j]
        result[j] += i_to_j[i][j]

print(*result)