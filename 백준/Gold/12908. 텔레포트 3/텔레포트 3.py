# 출발 / 텔11 / 텔12 / 텔21 / 텔22 / 텔31 / 텔32 / 도착
dots = [list(map(int, input().split()))]
e = list(map(int, input().split()))

for i in range(3):
    tmp = list(map(int, input().split()))

    dots.append([tmp[0], tmp[1]])
    dots.append([tmp[2], tmp[3]])

dots.append(e)

dp = [[0] * 8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if i != j:
            dp[i][j] = abs(dots[i][0] - dots[j][0]) + abs(dots[i][1] - dots[j][1])
            dp[j][i] = dp[i][j]

result = 21e21
used = [0] * 8
def dfs(now, total):
    global result

    if dots[now][0] == e[0] and dots[now][1] == e[1]:
        result = min(result, total)
        return
    
    for i in range(1, 8):
        if not used[i]:
            used[i] = 1

            if i < 7:
                if i % 2:
                    used[i + 1] = 1
                    dfs(i + 1, total + dp[now][i] + 10)
                    used[i + 1] = 0
                else:
                    used[i - 1] = 1
                    dfs(i - 1, total + dp[now][i] + 10)
                    used[i - 1] = 0
            else:
                dfs(i, total + dp[now][i])
            
            used[i] = 0

used[0] = 1
dfs(0, 0)

print(result)