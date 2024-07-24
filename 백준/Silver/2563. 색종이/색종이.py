T = int(input())
N = 100

used = [[0] * N for _ in range(N)]

for _ in range(T):
    y, x = map(int, input().split())

    y -= 1
    x -= 1

    for i in range(10):
        for j in range(10):
            used[y + i][x + j] = 1

result = 0

for line in used:
    result += sum(line)

print(result)