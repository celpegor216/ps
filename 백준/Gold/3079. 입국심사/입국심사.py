N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]

lst.sort()
result = M * lst[-1]

start, end = 0, result

while start <= end:
    middle = (start + end) // 2
    
    cnt = 0
    for i in range(N):
        cnt += middle // lst[i]
    
    if cnt >= M:
        result = middle
        end = middle - 1
    else:
        start = middle + 1

print(result)