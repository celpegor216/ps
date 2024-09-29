T = int(input())


def find():
    q = [(sy, sx, F)]
    used = [[0] * M for _ in range(N)]
    used[sy][sx] = 1

    while q:
        nq = []

        for y, x, f in q:
            if y == ey and x == ex:
                return 1
            
            if not f:
                return
            
            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = y + dy, x + dx
                if not (0 <= ny < N and 0 <= nx < M) or used[ny][nx]:
                    continue

                if lst[ny][nx] - lst[y][x] > f:
                    continue
                
                used[ny][nx] = 1
                nq.append((ny, nx, f - 1))
        
        q = nq


for _ in range(T):
    N, M, O, F, sy, sx, ey, ex = map(int, input().split())
    sy -= 1
    sx -= 1
    ey -= 1
    ex -= 1
    lst = [[0] * M for _ in range(N)]
    for _ in range(O):
        y, x, l = map(int, input().split())
        lst[y - 1][x - 1] = l
    
    print('잘했어!!' if find() else '인성 문제있어??')