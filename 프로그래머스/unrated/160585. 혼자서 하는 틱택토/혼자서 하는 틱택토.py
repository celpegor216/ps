def solution(board):
    # O로 완성한 줄의 수, X로 완성한 줄의 수, O의 개수, X의 개수 구하기
    complete_o = 0
    complete_x = 0
    cnt_o = 0
    cnt_x = 0
    
    for i in range(3):
        if board[i] == 'O' * 3:
            complete_o += 1
        elif board[i] == 'X' * 3:
            complete_x += 1
        
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'O':
                complete_o += 1
            elif board[0][i] == 'X':
                complete_x += 1
    
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'O':
            complete_o += 1
        elif board[0][0] == 'X':
            complete_x += 1
    
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'O':
            complete_o += 1
        elif board[0][2] == 'X':
            complete_x += 1
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                cnt_o += 1
            elif board[i][j] == 'X':
                cnt_x += 1
                
    # O는 두 줄 완성 가능, 이때 모든 칸이 다 차 있어야 함
    if complete_o == 2 and cnt_o == 5 and cnt_x == 4:
        return 1
    
    # 이 외에는 완성한 줄 수를 합쳤을 때 1보다 크면 안 됨
    if complete_o + complete_x > 1:
        return 0
    
    # O로 한 줄 완성했을 때 X의 개수는 O보다 하나 적어야 함
    if complete_o == 1 and cnt_o != cnt_x + 1:
        return 0
    
    # X로 한 줄 완성했을 때 O의 개수는 X와 같아야 함
    if complete_x == 1 and cnt_o != cnt_x:
        return 0
    
    # 둘 다 완성을 못 했을 때, X의 개수는 O보다 하나 적거나 같아야 함
    if complete_o == complete_x == 0 and not(cnt_x == cnt_o or cnt_x + 1 == cnt_o):
        return 0
    
    return 1