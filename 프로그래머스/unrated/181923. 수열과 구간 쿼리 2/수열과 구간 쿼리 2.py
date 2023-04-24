def solution(arr, queries):
    answer = []
    
    for q in queries:
        temp = 21e8
        s, e, k = q
        
        for i in range(s, e + 1):
            if arr[i] > k and arr[i] < temp:
                temp = arr[i]
        
        if temp != 21e8:
            answer.append(temp)
        else:
            answer.append(-1)
    
    return answer