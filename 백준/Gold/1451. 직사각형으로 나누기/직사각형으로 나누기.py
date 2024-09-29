N, M = map(int, input().split())
lst = [[0] * (M + 1)] + [[0] + list(map(int, input())) for _ in range(N)]

memo = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        memo[i][j] = lst[i][j] + memo[i - 1][j] + memo[i][j - 1] - memo[i - 1][j - 1]

result = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        a = memo[i][j]

        # 열을 전부 차지하는 경우
        if j == M:
            # 열로 나누는 경우
            for k in range(1, M + 1):
                b = memo[-1][k] - memo[i][k]
                c = memo[-1][-1] - (a + b)
                result = max(result, a * b * c)
            
            # 행으로 나누는 경우
            for k in range(i + 1, N + 1):
                b = memo[k][-1] - a
                c = memo[-1][-1] - (a + b)
                result = max(result, a * b * c)

        # 행을 전부 차지하는 경우
        elif i == N:
            # 열로 나누는 경우
            for k in range(j + 1, M + 1):
                b = memo[-1][k] - a
                c = memo[-1][-1] - (a + b)
                result = max(result, a * b * c)
            
            # 행으로 나누는 경우
            for k in range(1, N + 1):
                b = memo[k][-1] - memo[k][j]
                c = memo[-1][-1] - (a + b)
                result = max(result, a * b * c)

        # 그 외의 경우
        else:
            # 열로 이어지는 경우
            b = memo[i][-1] - a
            c = memo[-1][-1] - (a + b)
            result = max(result, a * b * c)

            # 행으로 이어지는 경우
            b = memo[-1][j] - a
            c = memo[-1][-1] - (a + b)
            result = max(result, a * b * c)


print(result)