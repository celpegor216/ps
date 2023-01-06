def solution(arr):
    answer = [arr[0]]
    
    now = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] != now:
            now = arr[i]
            answer.append(now)
    
    return answer