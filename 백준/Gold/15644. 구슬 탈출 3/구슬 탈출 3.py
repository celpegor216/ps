from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

ry = rx = by = bx = oy = ox = -1

for n in range(N):
    for m in range(M):
        if board[n][m] == 'R':
            ry, rx = n, m
            board[n][m] = '.'
        elif board[n][m] == 'B':
            by, bx = n, m
            board[n][m] = '.'
        elif board[n][m] == 'O':
            oy, ox = n, m

used = set()
used.add((ry, rx, by, bx))

q = deque()
q.append((ry, rx, by, bx, 0, ''))

result_cnt = -1
result_path = ''

def move(y, x, dy, dx, oppo_y, oppo_x):
    while 1:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if board[ny][nx] == '.' and not (ny == oppo_y and nx == oppo_x):
                y += dy
                x += dx
            elif board[ny][nx] == 'O':
                y += dy
                x += dx
                break
            else:
                break
        else:
            break
    
    return y, x

while q:
    now_ry, now_rx, now_by, now_bx, now_cnt, now_path = q.popleft()

    if now_cnt > 10:
        break

    if now_by == oy and now_bx == ox:
        continue

    if now_ry == oy and now_rx == ox:
        result_cnt = now_cnt
        result_path = now_path
        break

    # 위로 움직임
    if now_ry < now_by:
        nry, nrx = move(now_ry, now_rx, -1, 0, now_by, now_bx)
        nby, nbx = move(now_by, now_bx, -1, 0, nry, nrx)
        if (nry, nrx, nby, nbx) not in used:
            used.add((nry, nrx, nby, nbx))
            q.append((nry, nrx, nby, nbx, now_cnt + 1, now_path + 'U'))
    else:
        nby, nbx = move(now_by, now_bx, -1, 0, now_ry, now_rx)
        nry, nrx = move(now_ry, now_rx, -1, 0, nby, nbx)
        if (nry, nrx, nby, nbx) not in used:
            used.add((nry, nrx, nby, nbx))
            q.append((nry, nrx, nby, nbx, now_cnt + 1, now_path + 'U'))

    # 아래로 움직임
    if now_ry > now_by:
        nry, nrx = move(now_ry, now_rx, 1, 0, now_by, now_bx)
        nby, nbx = move(now_by, now_bx, 1, 0, nry, nrx)
        if (nry, nrx, nby, nbx) not in used:
            used.add((nry, nrx, nby, nbx))
            q.append((nry, nrx, nby, nbx, now_cnt + 1, now_path + 'D'))
    else:
        nby, nbx = move(now_by, now_bx, 1, 0, now_ry, now_rx)
        nry, nrx = move(now_ry, now_rx, 1, 0, nby, nbx)
        if (nry, nrx, nby, nbx) not in used:
            used.add((nry, nrx, nby, nbx))
            q.append((nry, nrx, nby, nbx, now_cnt + 1, now_path + 'D'))

    # 왼쪽으로 움직임
    if now_rx < now_bx:
        nry, nrx = move(now_ry, now_rx, 0, -1, now_by, now_bx)
        nby, nbx = move(now_by, now_bx, 0, -1, nry, nrx)
        if (nry, nrx, nby, nbx) not in used:
            used.add((nry, nrx, nby, nbx))
            q.append((nry, nrx, nby, nbx, now_cnt + 1, now_path + 'L'))
    else:
        nby, nbx = move(now_by, now_bx, 0, -1, now_ry, now_rx)
        nry, nrx = move(now_ry, now_rx, 0, -1, nby, nbx)
        if (nry, nrx, nby, nbx) not in used:
            used.add((nry, nrx, nby, nbx))
            q.append((nry, nrx, nby, nbx, now_cnt + 1, now_path + 'L'))

    # 오른쪽으로 움직임
    if now_rx > now_bx:
        nry, nrx = move(now_ry, now_rx, 0, 1, now_by, now_bx)
        nby, nbx = move(now_by, now_bx, 0, 1, nry, nrx)
        if (nry, nrx, nby, nbx) not in used:
            used.add((nry, nrx, nby, nbx))
            q.append((nry, nrx, nby, nbx, now_cnt + 1, now_path + 'R'))
    else:
        nby, nbx = move(now_by, now_bx, 0, 1, now_ry, now_rx)
        nry, nrx = move(now_ry, now_rx, 0, 1, nby, nbx)
        if (nry, nrx, nby, nbx) not in used:
            used.add((nry, nrx, nby, nbx))
            q.append((nry, nrx, nby, nbx, now_cnt + 1, now_path + 'R'))

print(result_cnt)
if result_cnt != -1:
    print(result_path)