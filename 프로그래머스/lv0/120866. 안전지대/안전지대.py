def solution(board):
    answer = 0
    
    N = len(board)
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                for di, dj in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 0:
                        board[ni][nj] = 2
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                answer += 1
    
    return answer