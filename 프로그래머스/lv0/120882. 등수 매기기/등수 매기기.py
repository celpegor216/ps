def solution(score):
    N = len(score)
    
    answer = [0] * N
    
    lst = [(sum(score[i]) / 2, i) for i in range(N)]
    
    lst.sort(reverse=True)
    
    rank = 1
    now = lst[0][0]
    
    for i in range(N):
        if lst[i][0] == now:
            answer[lst[i][1]] = rank
        else:
            rank = i + 1
            now = lst[i][0]
            answer[lst[i][1]] = rank
    
    return answer