# 힌트: bfs

from collections import deque

def solution(storey):
    q = deque()
    q.append((storey, 0))
    
    answer = 21e8
    
    while q:
        nown, nowc = q.popleft()
        
        if nown == 0:
            answer = min(answer, nowc)
            continue
            
        if nowc >= answer:
            continue
        
        q.append((nown // 10, nowc + nown % 10))
        q.append((nown // 10 + 1, nowc + 10 - (nown % 10)))
    
    return answer