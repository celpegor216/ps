import sys
sys.setrecursionlimit(10 ** 5)

N, M, S = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

for line in lst:
    line.sort()

used = [0] * (N + 1)
cnt = 1
def dfs(now):
    global cnt

    for nxt in lst[now]:
        if not used[nxt]:
            cnt += 1
            used[nxt] = cnt
            dfs(nxt)

used[S] = 1
dfs(S)

for i in range(1, N + 1):
    print(used[i])