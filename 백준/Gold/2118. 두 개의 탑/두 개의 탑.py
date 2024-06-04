N = int(input())
lst = [int(input()) for _ in range(N)]

total = sum(lst)
half = total // 2

result = 0
now = 0

start = end = 0

while end < N:
    if now < half:
        now += lst[end]
        end += 1
    else:
        now -= lst[start]
        start += 1
    
    result = max(result, min(now, total - now))

print(result)