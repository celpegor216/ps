N = int(input())
lst = [int(input()) for _ in range(N)]

result = 0
maxv = 0

for n in range(N - 1, -1, -1):
    if lst[n] > maxv:
        result += 1
        maxv = lst[n]

print(result)