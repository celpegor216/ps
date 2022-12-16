N, M = map(int, input().split())

lst = sorted(map(int, input().split()))

used = [0] * N

def dfs(level, path):
    if level == M:
        print(*path)
        return

    for n in range(N):
        if not used[n]:
            used[n] = 1
            dfs(level + 1, path + [lst[n]])
            used[n] = 0

dfs(0, [])