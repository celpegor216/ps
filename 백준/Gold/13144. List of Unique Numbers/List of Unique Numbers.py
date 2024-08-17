N = int(input())
lst = list(map(int, input().split()))

MAX = 10 ** 5
bucket = [-1] * (MAX + 1)

start = 0
result = 0
for n in range(N):
    while start <= bucket[lst[n]]:
        bucket[lst[start]] -= 1
        start += 1
    
    bucket[lst[n]] = n
    
    result += n - start + 1

print(result)