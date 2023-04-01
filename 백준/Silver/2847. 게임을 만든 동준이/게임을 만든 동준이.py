N = int(input())
lst = [int(input()) for _ in range(N)]

result = 0
for n in range(N - 2, -1, -1):
    if lst[n + 1] <= lst[n]:
        result += lst[n] - lst[n + 1] + 1
        lst[n] = lst[n + 1] - 1

print(result)