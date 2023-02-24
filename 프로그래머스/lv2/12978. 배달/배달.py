import heapq

def solution(N, road, K):
    lst = [[] for _ in range(N + 1)]
    
    for r in road:
        a, b, c = r
        lst[a].append((c, b))
        lst[b].append((c, a))
    
    INF = 21e8
    result = [INF] * (N + 1)
    result[1] = 0
    
    q = []
    heapq.heappush(q, (0, 1))
    
    while q:
        start_via_cost, via = heapq.heappop(q)
        
        for item in lst[via]:
            start_via_target_cost = start_via_cost + item[0]
            if start_via_target_cost < result[item[1]]:
                heapq.heappush(q, (start_via_target_cost, item[1]))
                result[item[1]] = start_via_target_cost
    
    answer = 0
    
    for r in result:
        if r <= K:
            answer += 1
                
    return answer