# 아무리 봐도 로직의 어느 부분이 틀렸는지 모르겠다... 망했다...
# 코드트리 틀린 부분 테스트 케이스 참고함


from collections import deque

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

ry = rx = by = bx = -1

# 상자의 바깥 부분은 전부 장애물로 막혀있게 주어진다
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if lst[i][j] == 'R':
            ry, rx = i, j
            lst[i][j] = '.'
        elif lst[i][j] == 'B':
            by, bx = i, j
            lst[i][j] = '.'

q = deque()
q.append((ry, rx, by, bx, 0))

used = dict()
used[(ry, rx, by, bx)] = 1


def move(y, x):
    ny, nx = y + dy, x + dx
    while 0 <= ny < N and 0 <= nx < M and lst[ny][nx] == '.':
        ny += dy
        nx += dx

    if not (0 <= ny < N and 0 <= nx < M) or lst[ny][nx] == '#':
        ny -= dy
        nx -= dx

    return ny, nx


# 빨간색 사탕을 밖으로 빼내기 위해 기울여야 하는 최소 횟수
result = -1
while q:
    now_ry, now_rx, now_by, now_bx, cnt = q.popleft()

    # 10번 이내에 빨간색 사탕을 밖으로 빼내는 것이 불가능하다면, −1을 출력
    if cnt > 10:
        break

    if lst[now_ry][now_rx] == 'O':
        result = cnt
        break

    # 사탕을 밖으로 빼기 위해서는 상자를 위, 아래, 왼쪽, 오른쪽 방향으로 기울일 수 있는데,
    # 기울어진 방향으로 사탕은 장애물 혹은 다른 사탕에 부딪히기 전 까지 미끄러지게 되며,
    # 미끄러지는 도중에 상자를 다른 방향으로 기울일 수는 없습니다

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nry, nrx = move(now_ry, now_rx)
        nby, nbx = move(now_by, now_bx)

        if lst[nby][nbx] != 'O':
            if nby == nry and nbx == nrx:
                # 빨간 구슬 먼저 이동
                if now_ry * dy > now_by * dy or now_rx * dx > now_bx * dx:
                    nby -= dy
                    nbx -= dx
                # 파란 구슬 먼저 이동
                else:
                    nry -= dy
                    nrx -= dx
            if not used.get((nry, nrx, nby, nbx)):
                used[(nry, nrx, nby, nbx)] = 1
                q.append((nry, nrx, nby, nbx, cnt + 1))

print(result)