N = int(input())
lst = [int(input()) for _ in range(N)]

lst.sort()

result = 0

for n in range(N):
    result = max(result, lst[N - 1 - n] * (n + 1))

print(result)