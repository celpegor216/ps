import heapq

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
memo = [[] for _ in range(N)]

for n in range(N):
    result = [21e10] * N
    result[n] = 0

    q = []
    heapq.heappush(q, (0, n))

    while q:
        start_via_cost, via = heapq.heappop(q)

        for i in range(N):
            if i != via and result[i] > start_via_cost + lst[via][i]:
                result[i] = start_via_cost + lst[via][i]
                heapq.heappush(q, (result[i], i))
    
    memo[n] = result[:]

for m in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    
    if memo[A][B] <= C:
        print("Enjoy other party")
    else:
        print("Stay here")