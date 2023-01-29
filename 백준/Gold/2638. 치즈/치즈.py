from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

# 1. 외부 공기와 내부 공기 구분
# 2. 남은 치즈 수 카운트


def bfs_air(y, x, air_type):
    q = deque()
    q.append((y, x))

    used = [[0] * M for _ in range(N)]
    used[y][x] = 1
    lst[y][x] = air_type

    while q:
        nowy, nowx = q.popleft()

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] == 0:
                used[ny][nx] = 1
                lst[ny][nx] = air_type
                q.append((ny, nx))


cheese = 0

bfs_air(0, 0, 2)

for n in range(1, N - 1):
    for m in range(1, M - 1):
        if lst[n][m] == 0:
            bfs_air(n, m, 3)
        elif lst[n][m] == 1:
            cheese += 1


# 반복문 - 남은 치즈 없으면 종료
# 1. 치즈 녹이기 - 카운트 줄이기
# 2. 남은 치즈 있으면 내부 공기가 외부 공기랑 맞닿았는지 확인해서 외부 공기로 변경


def bfs_cheese(y, x):
    global used, cheese

    q = deque()
    q.append((y, x))

    used[y][x] = 1

    temp = []

    while q:
        nowy, nowx = q.popleft()

        cnt = 0

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < M:
                # 옆 칸이 아직 방문하지 않은 치즈라면 방문
                if not used[ny][nx] and lst[ny][nx] == 1:
                    used[ny][nx] = 1
                    q.append((ny, nx))
                # 옆 칸이 외부 공기라면 카운트 증가
                elif lst[ny][nx] == 2:
                    cnt += 1

        if cnt > 1:
            temp.append((nowy, nowx))

    for y, x in temp:
        lst[y][x] = 2
        cheese -= 1

def bfs_check(y, x):
    global used

    q = deque()
    q.append((y, x))

    used[y][x] = 1

    flag = 0
    temp = []
    temp.append((y, x))

    while q:
        nowy, nowx = q.popleft()

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < M:
                # 옆 칸이 아직 방문하지 않은 내부 공기라면 방문
                if not used[ny][nx] and lst[ny][nx] == 3:
                    used[ny][nx] = 1
                    temp.append((ny, nx))
                    q.append((ny, nx))
                # 옆 칸이 외부 공기라면 플래그 변경
                elif lst[ny][nx] == 2:
                    flag = 1

    if flag:
        for y, x in temp:
            lst[y][x] = 2

result = 0

while cheese > 0:
    used = [[0] * M for _ in range(N)]

    for n in range(1, N - 1):
        for m in range(1, M - 1):
            if not used[n][m] and lst[n][m] == 1:
                bfs_cheese(n, m)

    for n in range(1, N - 1):
        for m in range(1, M - 1):
            if not used[n][m] and lst[n][m] == 3:
                bfs_check(n, m)

    result += 1

print(result)