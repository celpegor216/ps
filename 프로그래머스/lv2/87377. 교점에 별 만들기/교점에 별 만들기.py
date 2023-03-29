def solution(line):
    length = len(line)
    cross = set()
    INF = 10e12
    up, down, left, right = INF, -INF, INF, -INF
    
    for i in range(length):
        for j in range(i + 1, length):
            A, B, E = line[i]
            C, D, F = line[j]
            
            div = A * D - B * C
            
            x = (B * F - E * D) / div if div else (B * F - E * D)
            y = (E * C - A * F) / div if div else (E * C - A * F)
            
            if x == int(x) and y == int(y) and A * D - B * C != 0 and -INF <= x <= INF and -INF <= y <= INF:
                x = int(x)
                y = int(y)
                cross.add((y, x))
                
                if y < up:
                    up = y
                if y > down:
                    down = y
                if x < left:
                    left = x
                if x > right:
                    right = x
    
    answer = [['.'] * (right - left + 1) for _ in range(down - up + 1)]
    
    for c in cross:
        answer[c[0] - up][c[1] - left] = '*'
    
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
        
    answer = answer[::-1]
        
    return answer