import heapq
import sys
input = sys.stdin.readline

N, M, X, Y = map(int, input().split())
lst = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())

    lst[a].append((b, c))
    lst[b].append((a, c))

q = []
heapq.heappush(q, (0, Y))

costs = [21e8] * N
costs[Y] = 0

while q:
    cost, now = heapq.heappop(q)

    if costs[now] < cost:
        continue

    for next_item, next_cost in lst[now]:
        new_cost = cost + next_cost
        if costs[next_item] > new_cost:
            costs[next_item] = new_cost
            heapq.heappush(q, (new_cost, next_item))

costs.sort()

result = 1
half = X // 2
left = half

for cost in costs:
    if left >= cost:
        left -= cost
        if left == cost:
            left = half
            result += 1
    else:
        if cost > half:
            result = -1
            break
        else:
            left = half - cost
            result += 1

print(result)