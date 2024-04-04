# 힌트: 위상정렬
# 해답: https://velog.io/@hanbin/%EB%B0%B1%EC%A4%80-1948%EB%B2%88-%EC%9E%84%EA%B3%84%EA%B2%BD%EB%A1%9C-with-Python

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
children = [[] for _ in range(N + 1)]
parent = [[] for _ in range(N + 1)]
parent_cnt = [0] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    children[a].append((b, c))
    parent[b].append(c)
    parent_cnt[b] += 1

S, E = map(int, input().split())

q = deque()
q.append(S)
result_time = [0] * (N + 1)
result_parent = [[] for _ in range(N + 1)]

while q:
    now = q.popleft()

    for b, c in children[now]:
        parent_cnt[b] -= 1

        next_time = result_time[now] + c

        if result_time[b] < next_time:
            result_time[b] = next_time
            result_parent[b] = [now]
        elif result_time[b] == next_time:
            result_parent[b].append(now)

        if not parent_cnt[b]:
            q.append(b)

print(result_time[E])

q = deque()
q.append(E)

route = set()

while q:
    now = q.popleft()
    for p in result_parent[now]:
        if (now, p) not in route:
            route.add((now, p))
            q.append(p)

print(len(route))