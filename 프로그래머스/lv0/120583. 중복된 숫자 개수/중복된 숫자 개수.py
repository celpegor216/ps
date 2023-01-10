def solution(array, n):
    answer = 0
    
    for item in array:
        if item == n:
            answer += 1
    
    return answer