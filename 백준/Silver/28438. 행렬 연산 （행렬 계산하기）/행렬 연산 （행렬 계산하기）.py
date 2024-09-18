import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
rows = [0] * N
cols = [0] * M

for _ in range(Q):
    cmd, a, b = map(int, input().split())

    if cmd == 1:
        rows[a - 1] += b
    else:
        cols[a - 1] += b

result = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        result[i][j] += rows[i] + cols[j]

for line in result:
    print(*line)