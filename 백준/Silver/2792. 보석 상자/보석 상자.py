N, M = map(int, input().split())
lst = [int(input()) for _ in range(M)]

start, end = 1, max(lst)
result = 0

while start <= end:
    middle = (start + end) // 2

    cnt = 0
    for item in lst:
        if item <= middle:
            cnt += 1
        else:
            cnt += item // middle
            if item % middle:
                cnt += 1

    if cnt <= N:
        result = middle
        end = middle - 1
    else:
        start = middle + 1

print(result)