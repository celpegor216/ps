N = int(input())
lst = list(map(int, input().split()))
MAX = max(lst)

bucket = [0] * (MAX + 1)

for item in lst:
    bucket[item] += 1

for i in range(1, MAX):
    bucket[i + 1] += bucket[i]

result = [0] * N

for n in range(N - 1, -1, -1):
    bucket[lst[n]] -= 1
    result[n] = bucket[lst[n]]

print(*result)