def solution(n, times):
    start, end = 1, 10 ** 20
    answer = end
    
    while start <= end:
        middle = (start + end) // 2
        
        temp = 0
        for time in times:
            temp += middle // time
        
        if temp >= n:
            answer = middle
            end = middle - 1
        else:
            start = middle + 1
    
    return answer