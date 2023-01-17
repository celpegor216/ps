def solution(k, score):
    answer = []
    hof = []
    
    for s in score:
        if len(hof) < k:
            hof.append(s)
        else:
            if hof[0] < s:
                hof[0] = s    
        hof.sort()
        answer.append(hof[0])
        
    
    return answer