N, M = map(int, input().split())
lst = [input() for _ in range(N)]

used = [[0] * M for _ in range(N)]

result = 0
for n in range(N):
    for m in range(M):
        if used[n][m]:
            continue

        result += 1

        if lst[n][m] == '-':
            nx = m
            while nx < M and lst[n][nx] == lst[n][m]:
                used[n][nx] = 1
                nx += 1
        else:
            ny = n
            while ny < N and lst[ny][m] == lst[n][m]:
                used[ny][m] = 1
                ny += 1

print(result)