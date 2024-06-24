M, N = map(int, input().split())
lst = list(map(int, input().split()))

start = 1
end = max(lst)
result = 0

while start <= end:
    middle = (start + end) // 2

    cnt = 0

    for item in lst:
        cnt += item // middle
    
    if cnt >= M:
        result = max(result, middle)
        start = middle + 1
    else:
        end = middle - 1

print(result)