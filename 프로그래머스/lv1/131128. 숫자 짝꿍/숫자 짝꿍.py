def solution(X, Y):
    answer = ''
    
    for i in range(9, -1, -1):
        s = str(i)
        answer += s * min(X.count(s), Y.count(s))
    
    if not answer:
        answer = '-1'
    elif answer.count('0') == len(answer):
        answer = '0'
    
    return answer