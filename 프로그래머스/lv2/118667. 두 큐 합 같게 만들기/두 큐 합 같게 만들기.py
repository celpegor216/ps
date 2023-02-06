# 해답: https://a-littlecoding.tistory.com/m/123

from collections import deque

def solution(queue1, queue2):
    answer = -1
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    total = sum1 + sum2
    
    if not total % 2:
        idx = 0
        limit = len(queue1) * 4

        while idx < limit:
            if sum1 > sum2:            
                t = q1.popleft()
                q2.append(t)
                sum1 -= t
                sum2 += t
            elif sum1 < sum2:
                t = q2.popleft()
                q1.append(t)
                sum1 += t
                sum2 -= t
            else:
                answer = idx
                break

            idx += 1
    
    return answer