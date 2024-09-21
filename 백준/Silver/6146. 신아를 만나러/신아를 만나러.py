ey, ex, K = map(int, input().split())

MAX = 1000
lst = [[0] * (MAX + 1) for _ in range(MAX + 1)]

for _ in range(K):
    y, x = map(lambda x: int(x) + 500, input().split())
    lst[y][x] = 1


def find():
    q = [(500, 500)]

    result = 0
    while q:
        nq = []

        for y, x in q:
            if y - 500 == ey and x - 500 == ex:
                return result
            
            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = y + dy, x + dx
                if 0 <= ny <= MAX and 0 <= nx <= MAX and not lst[ny][nx]:
                    lst[ny][nx] = 1
                    nq.append((ny, nx))
        
        q = nq
        result += 1


print(find())