import heapq

def solution(n, works):
    if sum(works) > n:
    
        q = []
    
        for w in works:
            heapq.heappush(q, -w)
    
        for i in range(n):
            heapq.heappush(q, heapq.heappop(q) + 1)
    
        return sum([x ** 2 for x in q])
    else:
        return 0