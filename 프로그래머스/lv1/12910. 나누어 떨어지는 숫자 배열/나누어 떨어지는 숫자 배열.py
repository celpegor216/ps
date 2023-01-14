def solution(arr, divisor):
    answer = []
    
    for item in arr:
        if not item % divisor:
            answer.append(item)
    
    if not answer:
        answer = [-1]
    else:
        answer.sort()
    
    return answer