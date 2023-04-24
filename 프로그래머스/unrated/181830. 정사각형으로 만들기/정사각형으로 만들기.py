def solution(arr):
    n = len(arr)
    m = len(arr[0])
    
    if n > m:
        for i in range(n):
            arr[i] += [0] * (n - m)
    else:
        for i in range(m - n):
            arr.append([0] * m)
    
    return arr