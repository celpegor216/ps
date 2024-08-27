N = int(input())

def dfs(level, now):
    if now == 1:
        return

    half = int(now ** 0.5) + 1
    for i in range(2, half):
        if not now % i:
            return

    if level == N:
        print(now)
        return

    for i in range(1, 10):
        dfs(level + 1, now * 10 + i)

dfs(0, 0)