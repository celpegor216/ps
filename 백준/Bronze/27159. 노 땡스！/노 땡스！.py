N = int(input())
lst = sorted(map(int, input().split()))

result = 0
minv = lst[0]
for n in range(1, N):
    if lst[n] > lst[n - 1] + 1:
        result += minv
        minv = lst[n]
result += minv

print(result)