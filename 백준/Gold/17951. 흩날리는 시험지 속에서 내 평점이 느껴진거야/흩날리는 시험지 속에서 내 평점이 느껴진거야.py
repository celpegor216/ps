N, K = map(int, input().split())
lst = list(map(int, input().split()))

start, end = 0, N * 20
result = start

while start <= end:
    middle = (start + end) // 2

    cnt = 0
    total = 0
    for item in lst:
        total += item

        if total >= middle:
            cnt += 1
            total = 0
    
    if cnt == K:
        result = max(result, middle)
        start = middle + 1
    elif cnt > K:
        start = middle + 1
    else:
        end = middle - 1

print(result)