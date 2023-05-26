n = int(input())
bucket = [0] * (n + 1)
for i in range(1, n + 1):
    j = i
    while j <= n:
        bucket[j] += i
        j += i

print(sum(bucket))