N = int(input())
lst = list(map(int, input().split()))

result = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        tmp = (lst[i] - lst[j]) * 2
        result += tmp if tmp > 0 else -tmp

print(result)