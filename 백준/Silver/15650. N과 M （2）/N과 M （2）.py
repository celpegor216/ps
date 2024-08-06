N, M = map(int, input().split())

def dfs(level, start, now):
    if level == M:
        print(*now)
        return

    for i in range(start, N):    # 중복 없이 M개를 고르고, 고른 수열은 오름차순
        dfs(level + 1, i + 1, now + [i + 1])

dfs(0, 0, [])