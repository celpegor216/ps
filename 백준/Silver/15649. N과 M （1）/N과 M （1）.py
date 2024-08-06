N, M = map(int, input().split())

used = [0] * N
def dfs(level, now):
    if level == M:
        print(*now)
        return

    for i in range(N):
        if not used[i]:
            used[i] = 1
            dfs(level + 1, now + [i + 1])
            used[i] = 0

dfs(0, [])