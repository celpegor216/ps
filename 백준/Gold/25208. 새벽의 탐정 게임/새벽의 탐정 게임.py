N, M = map(int, input().split())

# 벽이 있는 칸은 #, 빈칸은 ., 탐정의 위치는 D, 도둑의 위치는 R
lst = [input() for _ in range(N)]

sy = sx = ey = ex = -1

# 보드의 테두리, 즉 1행, 1열, N행, M열에 해당하는 칸은 벽
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if lst[i][j] == 'D':
            sy, sx = i, j
        elif lst[i][j] == 'R':
            ey, ex = i, j


directions = ((0, -1), (0, 1), (-1, 0), (1, 0))


# 감옥을 최소 몇 번 굴려야 당신이 게임에서 승리할 수 있을지 알아보자 > bfs
# used 배열을 어떻게 만들 것인지가 관건
def find():
    # used[i][j][k]: 주사위의 바닥면이 k일 때 해당 칸에 도착한 적이 있는지 여부
    used = [[set() for _ in range(M)] for _ in range(N)]

    # 탐정은 자신이 있는 칸에 감옥의 뚫린 면이 바닥을 향하게 하여 놓는다
    top, up, right, down, left, bottom = 0, 1, 2, 3, 4, 5

    used[sy][sx].add((top, up, right, down, left, bottom))

    q = [(sy, sx, top, up, right, down, left, bottom)]
    result = 0
    while q:
        nq = []

        for y, x, t, u, r, d, l, b in q:
            if y == ey and x == ex:
                if b == 5:
                    return result
                else:
                    continue

            for i in range(4):
                dy, dx = directions[i]
                ny, nx = y + dy, x + dx
                if lst[ny][nx] == '#':
                    continue

                nt, nu, nr, nd, nl, nb = t, u, r, d, l, b

                # 왼쪽으로 굴리기
                if i == 0:
                    nt, nr, nb, nl = nr, nb, nl, nt
                # 오른쪽으로 굴리기
                elif i == 1:
                    nt, nr, nb, nl = nl, nt, nr, nb
                # 위쪽으로 굴리기
                elif i == 2:
                    nt, nu, nb, nd = nd, nt, nu, nb
                # 아래쪽으로 굴리기
                else:
                    nt, nu, nb, nd = nu, nb, nd, nt
                
                if (nt, nu, nr, nd, nl, nb) in used[ny][nx]:
                    continue
                
                used[ny][nx].add((nt, nu, nr, nd, nl, nb))
                nq.append((ny, nx, nt, nu, nr, nd, nl, nb))

        q = nq
        result += 1
    
    return -1


print(find())