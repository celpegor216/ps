def solution(board, h, w):
    answer = 0
    
    N, M = len(board), len(board[0])
    
    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = h + dy, w + dx
        if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == board[h][w]:
            answer += 1
    
    return answer