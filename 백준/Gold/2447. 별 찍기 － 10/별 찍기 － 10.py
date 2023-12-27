N = int(input())

result = [[' '] * N for _ in range(N)]

def func(n, y, x):
    if n == 1:
        result[y][x] = '*'
        return
    
    for i in range(3):
        for j in range(3):
            if not(i == j == 1):
                func(n // 3, y + (n // 3) * i, x + (n // 3) * j)

func(N, 0, 0)

for line in result:
    print(''.join(line))