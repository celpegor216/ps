N, M = map(int, input().split())
lst = sorted(set(map(int, input().split())))
N = len(lst)

def dfs(level, before, path):
    if level == M:
        print(path)
        return

    for n in range(before, N):
        dfs(level + 1, n, path + f'{lst[n]} ')

dfs(0, 0, '')
