A, B = map(int, input().split())
R = int(input())

used = [[0] * (R + 1) for _ in range(R + 1)]
used[A][B] = 1

x, y = A, B
result = 1

while 1:
    if (x + 1) + (y + 1) < R:
        x += 1
        y += 1
    else:
        x //= 2
        y //= 2

    if used[x][y]:
        print(result)
        break

    used[x][y] = 1
    result += 1