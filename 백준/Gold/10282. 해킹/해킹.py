import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, D, C = map(int, input().strip().split())
    lst = [[] for _ in range(N + 1)]

    for _ in range(D):
        a, b, s = map(int, input().split())
        lst[b].append((a, s))
    
    result = [21e8] * (N + 1)
    result[C] = 0

    q = []
    heapq.heappush(q, (0, C))

    while q:
        cost, now = heapq.heappop(q)

        for target, target_cost in lst[now]:
            if result[target] > cost + target_cost:
                result[target] = cost + target_cost
                heapq.heappush(q, (result[target], target))
    
    result_cnt = 0
    result_time = 0

    for n in range(1, N + 1):
        if result[n] != 21e8:
            result_cnt += 1
            result_time = max(result_time, result[n])
    
    print(result_cnt, result_time)