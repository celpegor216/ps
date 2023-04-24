def solution(arr):
    answer = arr[:]
    
    if len(answer) > 1:
        for i in range(1, 12):
            if 2 ** (i - 1) <= len(arr) <= 2 ** i:
                answer += [0] * (2 ** i - len(arr))
                break
            
    return answer