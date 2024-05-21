N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]

start, end = 1, max(lst)
result = 0

while start <= end:
    middle = (start + end) // 2

    cnt = 0
    if middle:
        for item in lst:
            cnt += item // middle

    if cnt >= K:
        result = max(result, middle)
        start = middle + 1
    else:
        end = middle - 1

print(result)