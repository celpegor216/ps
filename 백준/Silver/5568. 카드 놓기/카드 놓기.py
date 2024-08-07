N = int(input())
K = int(input())
lst = [input() for _ in range(N)]

result = set()
used = [0] * N    # 순열

def dfs(level, now):
    if level == K:
        result.add(now)
        return

    for n in range(N):
        if not used[n]:
            used[n] = 1
            dfs(level + 1, now + lst[n])
            used[n] = 0

dfs(0, '')

print(len(result))