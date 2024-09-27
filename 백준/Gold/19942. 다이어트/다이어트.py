N = int(input())
minimums = list(map(int, input().split()))
lst = [list(map(int, input().split())) for _ in range(N)]


result_total = 21e8
result_combination = []
def dfs(level, start, now, total, path):
    global result_total, result_combination

    if total >= result_total:
        return

    for i in range(4):
        if now[i] < minimums[i]:
            break
    else:
        result_total = total
        result_combination = path
        return

    for i in range(start, N):
        nxt = now[:]
        for j in range(4):
            nxt[j] += lst[i][j]
        dfs(level + 1, i + 1, nxt, total + lst[i][-1], path + [i + 1])

dfs(0, 0, [0] * 4, 0, [])

if not result_combination:
    print(-1)
else:
    print(result_total)
    print(*result_combination)