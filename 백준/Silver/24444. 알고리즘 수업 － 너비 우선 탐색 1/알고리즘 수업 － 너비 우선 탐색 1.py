from collections import deque
import sys
input = sys.stdin.readline

N, M, S = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

for n in range(1, N + 1):
    lst[n] = sorted(set(lst[n]))

q = deque()
q.append(S)

used = [0] * (N + 1)
used[S] = 1

cnt = 1
while q:
    now = q.popleft()

    for nxt in lst[now]:
        if not used[nxt]:
            cnt += 1
            used[nxt] = cnt
            q.append(nxt)

for i in range(1, N + 1):
    print(used[i])