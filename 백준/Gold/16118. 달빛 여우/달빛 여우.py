# 시간초과 해결 못 함
# 해답: https://ibocon.tistory.com/258

import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for m in range(M):
    a, b, d = map(int, input().split())

    lst[a].append((b, d * 2))
    lst[b].append((a, d * 2))

INF = int(1e9)

fox = [INF] * (N + 1)
fox[1] = 0

q = []
heapq.heappush(q, (0, 1))

while q:
    cost, via = heapq.heappop(q)

    if fox[via] < cost:
        continue

    for t, c in lst[via]:
        if fox[t] > cost + c:
            fox[t] = cost + c
            heapq.heappush(q, (fox[t], t))

# 늑대는 * 1/2 > * 2 > * 1/2 > * 2 > ...
wolf = [[INF, INF] for _ in range(N + 1)]
wolf[1][0] = 0

q = []
heapq.heappush(q, (0, 1, 0))

while q:
    cost, via, isRunning = heapq.heappop(q)

    if (not isRunning and wolf[via][0] < cost) or (isRunning and wolf[via][1] < cost):
        continue

    for t, c in lst[via]:
        # 이전에 뛰지 않아서 지금 뛸 차례
        if not isRunning and wolf[t][1] > cost + c // 2:
            wolf[t][1] = cost + c // 2
            heapq.heappush(q, (wolf[t][1], t, 1))
        # 이전에 뛰어서 지금 쉴 차례
        elif isRunning and wolf[t][0] > cost + c * 2:
            wolf[t][0] = cost + c * 2
            heapq.heappush(q, (wolf[t][0], t, 0))

result = 0

for n in range(2, N + 1):
    if fox[n] < min(wolf[n]):
        result += 1

print(result)