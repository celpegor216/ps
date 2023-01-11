def solution(numbers, k):
    answer = 0
    
    j = 1
    
    while j < k:
        answer += 2
        if answer == len(numbers):
            answer = 0
        elif answer == len(numbers) + 1:
            answer = 1
        j += 1
    
    return answer + 1