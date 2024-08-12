import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
orders = dict()

for n in range(N):
    k, *lst = list(map(int, input().split()))

    for item in lst:
        if not orders.get(item):
            orders[item] = []
        heapq.heappush(orders[item], n)

result = [0] * N

dishes = list(map(int, input().split()))
for dish in dishes:
    if orders.get(dish):
        result[heapq.heappop(orders[dish])] += 1

print(*result)