from collections import deque

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

coins = []
for i in range(N):
    for j in range(M):
        if lst[i][j] == 'o':
            coins.append([i, j])

q = deque()
q.append((*coins[0], *coins[1], 0))

used = set()
used.add((*coins[0], *coins[1]))

def bfs():
    while q:
        ay, ax, by, bx, cnt = q.popleft()

        if cnt == 10:
            break

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nay, nax, nby, nbx = ay + dy, ax + dx, by + dy, bx + dx

            # 동전이 이동하려는 방향에 칸이 없으면 동전은 보드 바깥으로 떨어진다.
            flag_a = flag_b = 0
            if not (0 <= nay < N and 0 <= nax < M):
                flag_a = 1
            if not (0 <= nby < N and 0 <= nbx < M):
                flag_b = 1

            # 둘 다 떨어진 경우
            if flag_a and flag_b:
                continue

            # 둘 다 떨어지지 않은 경우
            elif not (flag_a or flag_b):
                # 동전이 이동하려는 칸이 벽이면, 동전은 이동하지 않는다.
                if lst[nay][nax] == '#':
                    nay, nax = ay, ax
                if lst[nby][nbx] == '#':
                    nby, nbx = by, bx

                # 그 외의 경우에는 이동하려는 방향으로 한 칸 이동한다.
                # 이동하려는 칸에 동전이 있는 경우에도 한 칸 이동한다.
                if (nay, nax, nby, nbx) not in used:
                    used.add((nay, nax, nby, nbx))
                    q.append((nay, nax, nby, nbx, cnt + 1))

            else:
                return cnt + 1

    # 두 동전을 떨어뜨릴 수 없거나, 버튼을 10번보다 많이 눌러야 한다면, -1을 출력
    return -1

print(bfs())