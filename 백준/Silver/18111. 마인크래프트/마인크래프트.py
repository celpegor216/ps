N, M, B = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

for n in range(N):
    for m in range(M):
        B += lst[n][m]

# 가능한 최대 높이
max_height = B // (N * M)

result_time = 21e8
result_height = 0

for h in range(max_height + 1):
    time = 0

    for n in range(N):
        for m in range(M):
            if lst[n][m] > h:
                time += (lst[n][m] - h) * 2
            elif lst[n][m] < h:
                time += h - lst[n][m]

    if result_time > time:
        result_time = time
        result_height = h
    elif result_time == time:
        result_height = max(result_height, h)

print(result_time, result_height)