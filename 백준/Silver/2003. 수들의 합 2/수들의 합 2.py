N, M = map(int, input().split())
lst = list(map(int, input().split()))

result = 0

start = 0
now = 0

for end in range(N):
    now += lst[end]

    while now > M:
        now -= lst[start]
        start += 1
    
    if now == M:
        result += 1

print(result)