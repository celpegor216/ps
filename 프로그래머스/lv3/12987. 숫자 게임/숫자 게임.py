import heapq

def solution(A, B):
    answer = 0
    
    a = []
    b = []
    
    for item in A:
        heapq.heappush(a, -item)
    for item in B:
        heapq.heappush(b, -item)
    
    while a:
        temp_a, temp_b = heapq.heappop(a), heapq.heappop(b)
        
        if temp_a > temp_b:
            answer += 1
        else:
            heapq.heappush(b, temp_b)
    
    return answer