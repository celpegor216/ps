# 해답: https://velog.io/@woosangchul/%EB%B0%B1%EC%A4%80-2662-%EA%B8%B0%EC%97%85%ED%88%AC%EC%9E%90-%ED%8C%8C%EC%9D%B4%EC%8D%AC

N, M = map(int, input().split())

lst = [[0] * (M + 1)]

for n in range(N):
    lst.append(list(map(int, input().strip().split())))

dp = [[0] * (M + 1) for _ in range(N + 1)]
used = [[[0] * (M + 1) for _ in range(M + 1)] for _ in range(N + 1)]

for n in range(1, N + 1):    # 투자액
    for m in range(1, M + 1):    # 기업
        maxv = 0
        maxu = [0] * (M + 1)

        for k in range(1, n + 1):    # 현재 기업에 투자할 금액
            if maxv < dp[n - k][m - 1] + lst[k][m]:
                maxv = dp[n - k][m - 1] + lst[k][m]
                maxu = used[n - k][m - 1][:]
                maxu[m] = k
        
        if dp[n][m - 1] < maxv:
            dp[n][m] = maxv
            used[n][m] = maxu[:]
        else:
            dp[n][m] = dp[n][m - 1]
            used[n][m] = used[n][m - 1][:]

print(dp[-1][-1])
print(*used[-1][-1][1:])