def solution(numbers, n):
    answer = 0
    
    for item in numbers:
        answer += item
        if answer > n:
            break
    
    return answer