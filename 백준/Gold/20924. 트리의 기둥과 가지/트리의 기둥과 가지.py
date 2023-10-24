import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

N, R = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for n in range(N - 1):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))
    lst[b].append((a, c))

G = -1
resultg = 0

# 기둥 길이 찾으면서 기가 노드 찾기
now = R
used = [0] * (N + 1)
used[now] = 1
while 1:
    if (now == R and len(lst[now]) != 1) or (now != R and len(lst[now]) != 2):
        G = now
        break

    for b, c in lst[now]:
        if not used[b]:
            used[b] = 1
            resultg += c
            now = b

# 기가 노드에서 가장 멀리 떨어져있는 가지 찾기
resultb = 0

def dfs(now, total):
    global resultb

    if len(lst[now]) == 1:
        resultb = max(resultb, total)
        return

    for b, c in lst[now]:
        if not used[b]:
            used[b] = 1
            dfs(b, total + c)
            used[b] = 0

dfs(G, 0)

print(resultg, resultb)