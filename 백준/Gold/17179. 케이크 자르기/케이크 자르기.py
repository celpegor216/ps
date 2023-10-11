N, M, L = map(int, input().split())
lst = [0] + [int(input()) for _ in range(M)] + [L]

lst.sort()

for n in range(N):
    Q = int(input())

    start, end = 0, L
    result = 0

    while start <= end:
        middle = (start + end) // 2

        cnt = 0
        before = 0
        for m in range(1, M + 1):
            if lst[m] - lst[before] >= middle:
                cnt += 1
                before = m
        
        if lst[-1] - lst[before] < middle:
            cnt -= 1
        
        if cnt >= Q:
            result = max(result, middle)
            start = middle + 1
        else:
            end = middle -1
    
    print(result)