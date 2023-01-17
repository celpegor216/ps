def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    
    length = len(score)
    for i in range(0, length, m):
        if i + m <= length:
            answer += min(score[i:i+m]) * m
    
    return answer