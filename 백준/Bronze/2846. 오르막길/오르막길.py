N = int(input())
lst = list(map(int, input().split()))

result = 0
low = 0
for i in range(1, N):
    if lst[i] <= lst[i - 1]:
        result = max(result, lst[i - 1] - lst[low])
        low = i

result = max(result, lst[-1] - lst[low])

print(result)