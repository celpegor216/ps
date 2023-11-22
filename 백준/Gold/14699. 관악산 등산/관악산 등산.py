from collections import deque

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heights = [0] + list(map(int, input().split()))
graph = [set() for _ in range(N + 1)]

for m in range(M):
    a, b = map(int, input().split())
    
    if heights[a] > heights[b]:
        graph[a].add(b)
    else:
        graph[b].add(a)

q = deque()
result = [1] * (N + 1)

for n in range(1, N + 1):
    if graph[n]:
        q.append((n, 1))

while q:
    now, cnt = q.popleft()

    if result[now] > cnt:
        continue

    for item in graph[now]:
        if result[item] < cnt + 1:
            result[item] = cnt + 1
            q.append((item, cnt + 1))

for item in result[1:]:
    print(item)