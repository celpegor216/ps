from collections import deque

N, M, S = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

for line in lst:
    line.sort()

result_dfs = [S]
used_dfs = [0] * (N + 1)
used_dfs[S] = 1

def dfs(now):
    for nxt in lst[now]:
        if not used_dfs[nxt]:
            result_dfs.append(nxt)
            used_dfs[nxt] = 1
            dfs(nxt)

dfs(S)

result_bfs = [S]
used_bfs = [0] * (N + 1)
used_bfs[S] = 1

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()

        for nxt in lst[now]:
            if not used_bfs[nxt]:
                result_bfs.append(nxt)
                used_bfs[nxt] = 1
                q.append(nxt)

bfs(S)

print(*result_dfs)
print(*result_bfs)