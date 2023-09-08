N, K = map(int, input().split())
lst = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])

result = 0

start, end = 0, 0
now = 0

while start < N and end < N:
    if lst[start][1] + 2 * K >= lst[end][1]:
        now += lst[end][0]
        end += 1
    else:
        now -= lst[start][0]
        start += 1
    result = max(result, now)

print(result)