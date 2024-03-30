N = int(input())
lst = sorted(map(int, input().split()))

result_value = 21e10
result = []

for i in range(N):
    for j in range(i + 1, N):
        now = lst[i] + lst[j]

        start, end = j + 1, N - 1

        while start <= end:
            middle = (start + end) // 2

            tmp = abs(now + lst[middle])
            if result_value > tmp:
                result_value = tmp
                result = [lst[i], lst[j], lst[middle]]

            if now + lst[middle] > 0:
                end = middle - 1
            else:
                start = middle + 1

print(*result)