def solution(routes):
    answer = 1
    
    routes.sort()
    while routes:
        now = routes.pop()
        
        while routes:
            if routes[-1][0] <= now[0] <= routes[-1][1]:
                routes.pop()
            else:
                answer += 1
                break
    
    return answer