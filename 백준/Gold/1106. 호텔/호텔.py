C, N = map(int, input().split())
dic = dict()

for n in range(N):
    cost, customers = map(int, input().split())

    if cost not in dic.keys() or dic[cost] < customers:
        dic[cost] = customers

lst = sorted(dic.items(), key=lambda x: x[1])
N = 10 ** 5 + 1
length = len(lst)

dp = [[0] * N for _ in range(length)]

for i in range(length):
    for j in range(N):
        if lst[i][0] > j:
            dp[i][j] = dp[i - 1][j]
        elif lst[i][0] == j:
            dp[i][j] = max(lst[i][1], dp[i - 1][j])
        else:
            dp[i][j] = max(dp[i][j - lst[i][0]] + lst[i][1], dp[i - 1][j])

for i in range(N):
    if dp[-1][i] >= C:
        print(i)
        break