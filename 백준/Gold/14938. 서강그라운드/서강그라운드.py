N, M, R = map(int, input().split())

items = [0] + list(map(int, input().split()))  # 위치 별 아이템 숫자
INF = 10e8
lst = [[INF] * (N + 1) for _ in range(N + 1)]    # 위치 별 연결 상태

for r in range(R):
    a, b, l = map(int, input().split())
    lst[a][b] = l
    lst[b][a] = l
    
result = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])

for n in range(1, N + 1):
    total = items[n]
    for m in range(1, N + 1):
        if m != n and lst[n][m] <= M:
            total += items[m]
    result = max(result, total)

print(result)