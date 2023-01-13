def solution(num, total):
    answer = [x for x in range(num)]
    
    temp = sum(answer)
    
    while 1:
        if temp == total:
            break
        elif temp < total:
            temp -= answer[0]
            answer = answer[1:] + [answer[-1] + 1]
            temp += answer[-1]
        else:
            temp -= answer[-1]
            answer = [answer[0] - 1] + answer[:-1]
            temp += answer[0]
    
    return answer