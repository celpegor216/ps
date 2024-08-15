N, M = map(int, input().split())
lst_a = [list(map(int, input().split())) for _ in range(N)]
lst_b = [list(map(int, input().split())) for _ in range(N)]

result = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        result[i][j] = lst_a[i][j] + lst_b[i][j]

for line in result:
    print(*line)