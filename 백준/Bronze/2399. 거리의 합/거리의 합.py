N = int(input())
lst = list(map(int, input().split()))

result = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        result += abs(lst[i] - lst[j]) * 2

print(result)