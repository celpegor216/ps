N = int(input())
M = int(input())
lst = list(map(int, input().split()))

start, end = 1, N
result = end

while start <= end:
    middle = (start + end) // 2

    check = 1
    now = 0
    for x in lst:
        if x - middle > now:
            check = 0
            break
        now = x + middle
    
    if check and now >= N:
        result = middle
        end = middle - 1
    else:
        start = middle + 1

print(result)