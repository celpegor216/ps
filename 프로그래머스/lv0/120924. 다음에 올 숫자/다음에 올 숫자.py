def solution(common):
    answer = 0
    
    if common[0] - common[1] == common[1] - common[2]:
        answer = common[-1] + (common[1] - common[0])
    else:
        answer = common[-1] * (common[1] / common[0])
    
    return answer