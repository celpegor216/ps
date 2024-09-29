tc = 0

blocks = [
    [[1], [1], [1], [1]],
    [[1, 1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1], [1, 1], [1, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[0, 1], [0, 1], [1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[1, 1], [1, 0], [1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[0, 1], [1, 1], [0, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 0], [1, 1], [1, 0]],
    [[1, 1], [1, 1]]
]

while 1:
    tc += 1
    N = int(input())

    if not N:
        break

    lst = [list(map(int, input().split())) for _ in range(N)]

    result = (10 ** 6) * (N ** 2) * -2
    for block in blocks:
        H, W = len(block), len(block[0])
        for i in range(N - H + 1):
            for j in range(N - W + 1):
                total = 0
                for h in range(H):
                    for w in range(W):
                        total += lst[i + h][j + w] * block[h][w]
                result = max(result, total)
    
    print(f'{tc}. {result}')