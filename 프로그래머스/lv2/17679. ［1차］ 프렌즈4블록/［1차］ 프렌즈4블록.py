def solution(m, n, board):
    answer = 0
    
    for i in range(m):
        board[i] = list(board[i])
    
    while 1:
        temp = set()
        
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != -1:
                    start = board[i][j]

                    flag = 0

                    for k in range(2):
                        if not flag:
                            for l in range(2):
                                if board[i + k][j + l] != start:
                                    flag = 1
                                    break

                    if not flag:
                        for k in range(2):
                            for l in range(2):
                                temp.add((i + k, j + l))   
        
        if len(temp) >= 4:
            for y, x in temp:
                board[y][x] = -1
                answer += 1
                
            for j in range(n):
                for i in range(m - 1, 0, -1):
                    if board[i][j] == -1:
                        for k in range(i - 1, -1, -1):
                            if board[k][j] != -1:
                                board[k][j], board[i][j] = board[i][j], board[k][j]
                                break
        else:
            break
    
    return answer