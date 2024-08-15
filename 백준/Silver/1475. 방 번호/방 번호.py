N = int(input())

bucket = [0] * 10

while N:
    bucket[N % 10] += 1
    N //= 10

result = 0
for i in range(10):
    if i in (6, 9):
        result = max(result, (bucket[6] + bucket[9] + 1) // 2)
    else:
        result = max(result, bucket[i])

print(result)