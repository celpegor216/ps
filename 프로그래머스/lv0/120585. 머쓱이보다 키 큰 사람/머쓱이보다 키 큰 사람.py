def solution(array, height):
    answer = 0
    
    for item in array:
        if item > height:
            answer += 1
    
    return answer