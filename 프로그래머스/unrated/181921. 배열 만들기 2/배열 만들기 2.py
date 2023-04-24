def solution(l, r):
    answer = []
    
    for i in range(l, r + 1):
        temp = str(i)
        
        if not temp.replace('0', '').replace('5', ''):
            answer.append(i)
    
    return answer if answer else [-1]