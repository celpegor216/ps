def solution(arr, k):
    answer = []
    
    for item in arr:
        if item not in answer:
            answer.append(item)
        if len(answer) == k:
            break
    
    if len(answer) < k:
        answer += [-1] * (k - len(answer))
    
    return answer