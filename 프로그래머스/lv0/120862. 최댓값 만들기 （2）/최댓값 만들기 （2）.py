def solution(numbers):
    answer = -21e8
    
    numbers.sort()
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] * numbers[j] > answer:
                answer = numbers[i] * numbers[j]
    
    return answer