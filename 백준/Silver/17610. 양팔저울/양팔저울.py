K = int(input())
lst = list(map(int, input().split()))

used = [0] * (sum(lst) + 1)

def dfs(level, total):
    if level == K:
        if total >= 0:
            used[total] = 1
        return

    for nxt in (total, total + lst[level], total - lst[level]):
        dfs(level + 1, nxt)

dfs(0, 0)

print(used.count(0))