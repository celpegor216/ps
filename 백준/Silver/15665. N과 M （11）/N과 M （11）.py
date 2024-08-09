N, M = map(int, input().split())
lst = sorted(map(int, input().split()))

used = set()

def dfs(level, now):
    if level == M:
        tup = tuple(now)

        if tup not in used:
            used.add(tup)
            print(*tup)
        return

    for n in range(N):
        dfs(level + 1, now + [lst[n]])

dfs(0, [])