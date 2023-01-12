def solution(keyinput, board):
    v, h = board[0] // 2, board[1] // 2
    answer = [0, 0]
    
    dic = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}
    
    for key in keyinput:
        x = answer[0] + dic[key][0]
        y = answer[1] + dic[key][1]
        
        if -v <= x <= v and -h <= y <= h:
            answer[0] = x
            answer[1] = y
    
    return answer