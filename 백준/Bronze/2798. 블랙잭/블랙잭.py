N, M = map(int, input().split())
lst = list(map(int, input().split()))

result = -1
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            total = lst[i] + lst[j] + lst[k]

            if total <= M and M - result > M - total:
                result = total

print(result)