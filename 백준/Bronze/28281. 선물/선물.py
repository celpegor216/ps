N, X = map(int, input().split())
lst = list(map(int, input().split()))

result = 10 ** 10
for n in range(N - 1):
    result = min(result, X * (lst[n] + lst[n + 1]))

print(result)