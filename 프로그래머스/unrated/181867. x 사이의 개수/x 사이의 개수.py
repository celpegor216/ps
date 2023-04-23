def solution(myString):
    answer = []
    
    lst = myString.split('x')
    
    for item in lst:
        answer.append(len(item))
    
    return answer