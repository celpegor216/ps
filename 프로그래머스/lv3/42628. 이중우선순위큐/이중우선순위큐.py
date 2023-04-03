import heapq

def solution(operations):
    q = []
    
    for op in operations:
        command, num = op.split()
        
        if command == 'I':
            heapq.heappush(q, int(num))
        else:
            # 최솟값 삭제
            if q and num == '-1':
                heapq.heappop(q)
            # 최댓값 삭제
            elif q and num == '1':
                temp = []
                for item in q:
                    heapq.heappush(temp, -item)
                heapq.heappop(temp)
                q = []
                for item in temp:
                    heapq.heappush(q, -item)
    
    return [max(q), min(q)] if q else [0, 0]