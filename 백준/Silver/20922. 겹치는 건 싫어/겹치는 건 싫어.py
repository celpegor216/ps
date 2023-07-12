N, K = map(int, input().split())
lst = list(map(int, input().split()))

start, end = 0, 0
bucket = [0] * 100001
bucket[lst[0]] = 1
result = 1
now = 1

while start < N:
    if end < N - 1 and bucket[lst[end + 1]] < K:
        end += 1
        bucket[lst[end]] += 1
        now += 1
    else:
        now -= 1
        bucket[lst[start]] -= 1
        start += 1
    
    if start == end:
        start += 1
        end += 1
    
    result = max(result, now)

print(result)