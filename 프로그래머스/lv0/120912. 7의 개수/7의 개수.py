def solution(array):
    answer = 0
    
    for item in array:
        answer += str(item).count('7')
        
    return answer