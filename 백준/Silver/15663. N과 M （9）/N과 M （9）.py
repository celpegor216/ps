N, M = map(int, input().split())
lst = sorted(map(int, input().split()))

used = [0] * N
results = []

def dfs(level, path):
    if level == M:
        if path not in results:
            results.append(path)
        return

    for n in range(N):
        if not used[n]:
            used[n] = 1
            dfs(level + 1, path + f'{lst[n]} ')
            used[n] = 0

dfs(0, '')

for item in results:
    print(item)