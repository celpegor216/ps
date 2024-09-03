from collections import deque

TC = int(input())

for _ in range(TC):
    M, N = map(int, input().split())
    lst = [list(input()) for _ in range(N)]

    person = []
    fire = []
    used = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if lst[i][j] == '@':
                person.append((i, j, 2, 0))
                lst[i][j] = '.'
                used[i][j] = 2
            elif lst[i][j] == '*':
                fire.append((i, j, 1, 0))
                lst[i][j] = '.'
                used[i][j] = 1

    # 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다
    # 상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다

    # 불이 먼저 움직인 다음에 상근이가 이동
    q = deque(fire + person)

    result = 'IMPOSSIBLE'
    while q:
        y, x, t, cnt = q.popleft()

        if t == 2 and (y in (0, N - 1) or x in (0, M - 1)):
            result = cnt + 1
            break

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] == '.':
                # 사람은 자기가 있었던 곳이나 불이 있었던 곳에 갈 수 없음
                # 불은 사람이 있었던 곳에는 갈 수 있음
                if (t == 2 and not used[ny][nx]) or (t == 1 and used[ny][nx] != 1):
                    used[ny][nx] = t
                    q.append((ny, nx, t, cnt + 1))

    print(result)