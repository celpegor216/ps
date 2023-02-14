# 해답: https://school.programmers.co.kr/questions/43364

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    dev, pic = 0, 0

    for i in range(n - 1, -1, -1):
        cnt = 0
        
        dev -= deliveries[i]
        pic -= pickups[i]
        
        while dev < 0 or pic < 0:
            dev += cap
            pic += cap
            cnt += 1
        
        answer += (i + 1) * 2 * cnt
    
    return answer