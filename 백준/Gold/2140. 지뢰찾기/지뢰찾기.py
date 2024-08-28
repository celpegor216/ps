# 문제를 제대로 안 읽어서 쓸모없는 고민을 길게 했군...
# 보드의 테두리가 모두 열려있고, 그 외는 모두 닫혀있는 상태에서 시작함

from collections import deque

N = int(input())
lst = []
for _ in range(N):
    S = input()
    tmp = []
    for s in S:
        if s.isdigit():
            tmp.append(int(s))
        else:
            tmp.append(s)
    lst.append(tmp)

directions_4 = ((0, 1), (1, 0), (0, -1), (-1, 0))
directions_8 = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

if N <= 2:
    print(0)
else:
    # used[i][j] == 1 > 폭탄이 있어야 함
    # used[i][j] == -1 > 폭탄이 없어야 함
    # used[i][j] == 0 > 폭탄이 있을 수도 없을 수도 있음
    # used[i][j] == 2 > 체크한 테두리
    used = [[0] * N for _ in range(N)]

    # 모서리에서 시작해서 옆으로 한 칸씩 퍼지기
    q = deque()

    for y, x in ((0, 0), (0, N - 1), (N - 1, 0), (N - 1, N - 1)):
        q.append((y, x))
        used[y][x] = 2

    while q:
        y, x = q.popleft()

        blanks = []
        cnt_yes_bomb = 0

        for dy, dx in directions_8:
            ny, nx = y + dy, x + dx
            if 1 <= ny < N - 1 and 1 <= nx < N - 1:
                if used[ny][nx] == 1:
                    cnt_yes_bomb += 1
                elif used[ny][nx] == 0:
                    blanks.append((ny, nx))

        # 폭탄을 더하면 안 됨
        if cnt_yes_bomb == lst[y][x]:
            for i, j in blanks:
                used[i][j] = -1
        else:
            for i, j in blanks:
                used[i][j] = 1

        for dy, dx in directions_4:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            if (ny in (0, N - 1) or nx in (0, N - 1)) and used[ny][nx] != 2:
                used[ny][nx] = 2
                q.append((ny, nx))

    result = 0

    for line in used[1:-1]:
        for item in line[1:-1]:
            if item != -1:
                result += 1

    print(result)