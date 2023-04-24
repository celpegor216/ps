def solution(myString):
    answer = ''
    
    for item in myString:
        if item < 'l':
            answer += 'l'
        else:
            answer += item
    
    return answer