# union-find로 풀려고 했는데 아니었음
# bfs도 안 되는군...

N, M = map(int, input().split())
lst = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

result = 0
used = [0] * N
def dfs(level, now):
    global result

    if result:
        return

    if level == 5:
        result = 1
        return

    for nxt in lst[now]:
        if not used[nxt]:
            used[nxt] = 1
            dfs(level + 1, nxt)
            used[nxt] = 0


for n in range(N):
    dfs(0, n)

    if result:
        break

print(result)