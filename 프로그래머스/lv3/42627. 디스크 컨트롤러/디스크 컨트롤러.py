# 해답: https://alreadyusedadress.tistory.com/258

import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    q = []
    
    while i < len(jobs):
        # 현재 시점(now)에 실행할 수 있는 작업들 저장
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(q, (job[1], job[0]))
        
        if q:
            job = heapq.heappop(q)
            start = now
            answer += now - job[1] + job[0]
            now += job[0]
            i += 1
        else:
            now += 1
    
    return answer // i