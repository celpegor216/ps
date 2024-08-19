N, M = map(int, input().split())
lst_A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
lst_B = [list(map(int, input().split())) for _ in range(M)]

result = [[0] * K for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            result[n][k] += lst_A[n][m] * lst_B[m][k]

for line in result:
    print(*line)