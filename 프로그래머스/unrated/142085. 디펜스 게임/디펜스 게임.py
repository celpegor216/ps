# 해답: https://school.programmers.co.kr/questions/40982

import heapq

def solution(n, k, enemy):
    heap = enemy[:k]
    heapq.heapify(heap)
    
    for i in range(k, len(enemy)):
        heapq.heappush(heap, enemy[i])
        n -= heapq.heappop(heap)
        if n < 0:
            return i
    
    return len(enemy)