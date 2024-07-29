N = int(input())
target = int(input())

lst = [[0] * N for _ in range(N)]

y = x = N // 2
num = 1
d = -1
cnt = 1

result = []

while 1:
    # 상하
    for _ in range(cnt):
        if num == target:
            result = [y + 1, x + 1]

        lst[y][x] = num
        y += d
        num += 1

    if num > N ** 2:
        break

    # 우좌
    for _ in range(cnt):
        if num == target:
            result = [y + 1, x + 1]

        lst[y][x] = num
        x -= d
        num += 1

    d *= -1
    cnt += 1

for line in lst:
    print(*line)

print(*result)