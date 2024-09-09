N = int(input())
lst = sorted(map(int, input().split()))

used = set()
def dfs(level, start, total):
    used.add(total)

    if start == N:
        return

    for i in range(start, N):
        dfs(level + 1, i + 1, total + lst[i])

dfs(0, 0, 0)

used = sorted(used)
for i in range(1, len(used)):
    if used[i] > i:
        print(i)
        break
else:
    print(i + 1)
