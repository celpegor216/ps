def solution(arr):
    answer = -1
    
    n = len(arr)
    
    for i in range(n):
        if answer != -1:
            break
        for j in range(n):
            if arr[i][j] != arr[j][i]:
                answer = 0
                break
    
    if answer != 0:
        answer = 1
    
    return answer