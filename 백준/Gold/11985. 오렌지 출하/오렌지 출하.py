N, M, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]

dp = [0, K]

for n in range(1, N):
    tmp = dp[-1] + 21e10
    for m in range(M):
        if n < m:
            break

        tmp = min(tmp, dp[-m - 1] + K + (m + 1) * (max(lst[n - m:n + 1]) - min(lst[n - m:n + 1])))

    dp.append(tmp)

print(dp[-1])