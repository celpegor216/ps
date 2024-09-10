N, M = map(int, input().split())
lst = [input() for _ in range(5 * N + 1)]

y = x = 1

result = [0] * 5

for n in range(N):
    for m in range(M):
        for i in range(4):
            if lst[y + i][x] == '.':
                result[i] += 1
                break
        else:
            result[4] += 1

        x += 5
    y += 5
    x = 1

print(*result)