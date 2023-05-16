N, S = map(int, input().split())
lst = list(map(int, input().split()))

if sum(lst) < S:
    print(0)
else:
    start, end = 0, 0
    total = lst[0]
    answer = N
    
    while start < N:
        if total >= S:
            if end - start + 1 < answer:
                answer = end - start + 1
                if answer == 1:
                    break
            total -= lst[start]
            start += 1
        else:
            end += 1
            
            if end >= N:
                break
            
            total += lst[end]
    
    print(answer)