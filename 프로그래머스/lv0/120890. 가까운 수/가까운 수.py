def solution(array, n):
    answer = 9999
    
    for num in array:
        if abs(num - n) < abs(answer - n):
            answer = num
        elif abs(num - n) == abs(answer - n):
            answer = min(num, answer)
    
    return answer