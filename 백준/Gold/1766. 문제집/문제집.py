# 위상정렬은 맞는 것 같은데 풀이가 떠오르지 않음
# 해답: https://hongcoding.tistory.com/94

import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

children = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)    # 진입차수 == 부모의 수

for m in range(M):
    a, b = map(int, input().split())

    children[a].append(b)
    in_degree[b] += 1

q = []    # 진입차수가 0인 요소들만 추가

for i in range(1, N + 1):
    if not in_degree[i]:
        heapq.heappush(q, i)

result = []

while q:
    now = heapq.heappop(q)

    result.append(now)

    for child in children[now]:
        in_degree[child] -= 1

        if not in_degree[child]:
            heapq.heappush(q, child)

print(*result)