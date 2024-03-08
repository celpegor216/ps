N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(K)]
lst.sort(key=lambda x: (-x[0], x[1]))

start, end = 1, 2 ** 32
result = end

while start <= end:
    middle = (start + end) // 2

    total = 0
    cnt = 0

    for k in range(K):
        if lst[k][1] <= middle:
            total += lst[k][0]
            cnt += 1
        
        if cnt == N:
            break
    
    if total >= M and cnt == N:
        result = min(result, middle)
        end = middle - 1
    else:
        start = middle + 1

if result == 2 ** 32:
    print(-1)
else:
    print(result)