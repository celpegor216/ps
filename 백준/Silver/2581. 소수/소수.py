M = int(input())
N = int(input())

bucket = [0] * (N + 1)
bucket[1] = 1

for i in range(2, N + 1):
    j = 2
    while i * j <= N:
        bucket[i * j] = 1
        j += 1

result = 0
min_v = 0

for i in range(M, N + 1):
    if not bucket[i]:
        result += i
        if not min_v:
            min_v = i

if result == 0:
    print(-1)
else:
    print(result)
    print(min_v)