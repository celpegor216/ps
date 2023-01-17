def solution(board, moves):
    answer = 0
    
    N = len(board)
    stack = []
    
    for move in moves:
        temp = 0
        
        move -= 1
        
        for n in range(N):
            if board[n][move]:
                temp = board[n][move]
                board[n][move] = 0
                break
        
        if temp:
            if stack and temp == stack[-1]:
                stack.pop()
                answer += 1
            else:
                stack.append(temp)
            
    return answer * 2