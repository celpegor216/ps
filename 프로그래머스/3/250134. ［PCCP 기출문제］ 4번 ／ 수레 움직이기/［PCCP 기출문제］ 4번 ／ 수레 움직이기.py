def solution(maze):
    answer = 21e8
    
    N, M = len(maze), len(maze[0])
    
    red_used = [[0] * M for _ in range(N)]
    blue_used = [[0] * M for _ in range(N)]
    
    rsy = rsx = bsy = bsx = -1
    rey = rex = bey = bex = -1
    
    for n in range(N):
        for m in range(M):
            if maze[n][m] == 1:
                rsy, rsx = n, m
            elif maze[n][m] == 2:
                bsy, bsx = n, m
            elif maze[n][m] == 3:
                rey, rex = n, m
            elif maze[n][m] == 4:
                bey, bex = n, m
    
    red_used[rsy][rsx] = 1
    blue_used[bsy][bsx] = 1
    
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    
    def dfs(level, ry, rx, by, bx):
        nonlocal answer
        
        if level >= answer:
            return
        
        if ry == rey and rx == rex and by == bey and bx == bex:
            answer = min(answer, level)
            return
        
        # 빨간 수레 먼저 이동
        if not (ry == rey and rx == rex):
            for d in range(4):
                rny, rnx = ry + dy[d], rx + dx[d]
                if 0 <= rny < N and 0 <= rnx < M and not red_used[rny][rnx] and maze[rny][rnx] != 5 and not (rny == by and rnx == bx):
                    red_used[rny][rnx] = 1

                    if not (by == bey and bx == bex):
                        for dd in range(4):
                            bny, bnx = by + dy[dd], bx + dx[dd]
                            if 0 <= bny < N and 0 <= bnx < M and not blue_used[bny][bnx] and maze[bny][bnx] != 5 and not (rny == bny and rnx == bnx):
                                blue_used[bny][bnx] = 1
                                dfs(level + 1, rny, rnx, bny, bnx)
                                blue_used[bny][bnx] = 0
                    else:
                        dfs(level + 1, rny, rnx, by, bx)

                    red_used[rny][rnx] = 0
                
        # 파란 수레 먼저 이동
        if not (by == bey and bx == bex):
            for d in range(4):
                bny, bnx = by + dy[d], bx + dx[d]
                if 0 <= bny < N and 0 <= bnx < M and not blue_used[bny][bnx] and maze[bny][bnx] != 5 and not (ry == bny and rx == bnx):
                    blue_used[bny][bnx] = 1

                    if not (ry == rey and rx == rex):
                        for dd in range(4):
                            rny, rnx = ry + dy[dd], rx + dx[dd]
                            if 0 <= rny < N and 0 <= rnx < M and not red_used[rny][rnx] and maze[rny][rnx] != 5 and not (rny == bny and rnx == bnx):
                                red_used[rny][rnx] = 1
                                dfs(level + 1, rny, rnx, bny, bnx)
                                red_used[rny][rnx] = 0
                    else:
                        dfs(level + 1, ry, rx, bny, bnx)

                    blue_used[bny][bnx] = 0      
    
    dfs(0, rsy, rsx, bsy, bsx)
    
    return answer if answer != 21e8 else 0