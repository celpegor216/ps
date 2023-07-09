N, M = map(int, input().split())
lst = [input() for _ in range(N)]

result = 'z' * 20

for n in range(N):
    now = ''
    for m in range(M):
        if lst[n][m] == '#':
            if len(now) > 1:
                result = min(result, now)
            now = ''
        else:
            now += lst[n][m]
    if len(now) > 1:
        result = min(result, now)

for m in range(M):
    now = ''
    for n in range(N):
        if lst[n][m] == '#':
            if len(now) > 1:
                result = min(result, now)
            now = ''
        else:
            now += lst[n][m]
    if len(now) > 1:
        result = min(result, now)

print(result)