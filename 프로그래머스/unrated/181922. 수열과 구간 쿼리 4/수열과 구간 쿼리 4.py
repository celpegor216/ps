def solution(arr, queries):
    for q in queries:
        s, e, k = q
        
        for i in range(s, e + 1):
            if not i % k:
                arr[i] += 1
    
    return arr