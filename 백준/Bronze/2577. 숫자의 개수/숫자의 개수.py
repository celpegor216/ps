N = 3
M = 10

total = 1

for _ in range(N):
    total *= int(input())

bucket = [0] * M

while total:
    bucket[total % 10] += 1
    total //= 10

for m in range(M):
    print(bucket[m])