N = int(input())
lst = [[0] * 101 for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(10):
        for j in range(10):
            lst[x + i][y + j] = 1

result = 100

for i in range(1, 101):
    for j in range(1, 101):
        if lst[i][j]:
            tmp = [[0] * 101 for _ in range(101)]
            tmp[i][j] = 1
            for x in range(100):
                if i + x > 100 or lst[i + x][j] == 0:
                    break
                for y in range(100):
                    if j + y > 100 or lst[i + x][j + y] == 0:
                        break
                    
                    tmp[i + x][j + y] = tmp[i + x - 1][j + y] + tmp[i + x][j + y - 1] - tmp[i + x - 1][j + y - 1] + 1
                    result = max(result, tmp[i + x][j + y])

print(result)