TARGET = input()
T = len(TARGET)
lst = [input() for _ in range(2)]
N = len(lst[0])

dp = [[[0] * T for _ in range(N)] for _ in range(2)]

for n in range(N):
    for i in range(2):
        for t in range(T):
            if lst[i][n] == TARGET[t]:
                if t == 0:
                    dp[i][n][t] = 1
                else:
                    opp = 1 if not i else 0
                    for j in range(n):
                        if lst[opp][j] == TARGET[t - 1]:
                            dp[i][n][t] += dp[opp][j][t - 1]

result = 0
for n in range(N):
    for i in range(2):
        result += dp[i][n][-1]

print(result)