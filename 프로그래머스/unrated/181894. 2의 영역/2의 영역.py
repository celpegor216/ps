def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if arr[i] == 2:
            answer.append(i)
    
    if not answer:
        answer = [-1]
    elif len(answer) == 1:
        answer = [2]
    else:
        answer = arr[answer[0]:answer[-1] + 1]
    
    return answer