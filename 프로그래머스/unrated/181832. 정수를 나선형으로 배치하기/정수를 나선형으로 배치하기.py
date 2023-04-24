def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    num = 1
    N = n
    y, x = 0, -1
    d = 1
    
    while num <= N ** 2:
        for i in range(n):
            x += d
            answer[y][x] = num
            num += 1
        
        n -= 1
        for i in range(n):
            y += d
            answer[y][x] = num
            num += 1
        
        d *= -1
    
    return answer