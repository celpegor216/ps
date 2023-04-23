def solution(arr):
    answer = []
    
    for item in arr:
        answer += [item] * item
    
    return answer