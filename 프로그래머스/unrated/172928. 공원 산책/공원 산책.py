def solution(park, routes):
    N, M = len(park), len(park[0])
    
    y, x = -1, -1
    
    for n in range(N):
        if y != -1:
            break
            
        for m in range(M):
            if park[n][m] == 'S':
                y, x = n, m
                break
    
    for route in routes:
        cmd, num = route.split()
        num = int(num)
        
        if cmd == 'N':
            dy, dx = -1, 0
        elif cmd == 'S':
            dy, dx = 1, 0
        elif cmd == 'W':
            dy, dx = 0, -1
        elif cmd == 'E':
            dy, dx = 0, 1
        
        ny, nx = y + dy * num, x + dx * num
        
        if 0 <= ny < N and 0 <= nx < M:
            flag = 0
            
            for i in range(1, num + 1):
                if park[y + dy * i][x + dx * i] == 'X':
                    flag = 1
                    break
            
            if not flag:
                y, x = ny, nx
    
    return [y, x]