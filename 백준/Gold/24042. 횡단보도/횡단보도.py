import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
for m in range(M):
    a, b = list(map(int, input().split()))
    lst[a].append((m, b))    # m: 신호 시작 시간
    lst[b].append((m, a))

result = [-1] * (N + 1)
result[1] = 0

q = []
heapq.heappush(q, (0, 0, 1))   # 총 소요 시간, 현재 주기의 순서, 현재 지역

while q:
    cost, order, via = heapq.heappop(q)

    if result[via] != -1 and cost > result[via]:
        continue

    if via == N:
        continue

    for idx, nxt in lst[via]:
        if idx >= order:
            nxt_cost = cost + idx - order + 1
        else:
            nxt_cost = cost + M - order + idx + 1
        if result[nxt] == -1 or nxt_cost < result[nxt]:
            result[nxt] = nxt_cost
            heapq.heappush(q, (nxt_cost, idx + 1, nxt))

print(result[-1])