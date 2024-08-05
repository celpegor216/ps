N, L, R, X = map(int, input().split())
lst = list(map(int, input().split()))

result = 0
def dfs(level, now):
    global result

    if level == N:
        if len(now) > 1:
            total = sum(now)
            diff = max(now) - min(now)

            if L <= total <= R and diff >= X:
                result += 1
        return

    dfs(level + 1, now)
    dfs(level + 1, now + [lst[level]])

dfs(0, [])
print(result)