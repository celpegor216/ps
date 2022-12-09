# 먹을 수 있는 물고기가 많으면 가장 가까운 물고기(위쪽, 왼쪽 우선)를 먹음
# 이동에 1초 걸리고 먹는 건 시간 안 걸림
# 더 이상 먹을 수 있는 물고기가 없어질 때까지 몇 초?

from collections import deque

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

shark_position = (-1, -1)
shark_size = 2 # 상어의 처음 크기 2
eat_cnt = 0 # 크기와 같은 수의 물고기를 먹으면 크기가 1 증가
fish_lst = [] # 물고기 정보 (y, x, 크기)
result = 0 # 더 이상 먹을 수 있는 물고기가 없어질 때까지 걸린 시간

# 상어와 물고기의 초기 위치 저장
for i in range(N):
    for j in range(N):
        if lst[i][j] == 9:
            shark_position = (i, j)
            lst[i][j] = 0
        elif lst[i][j] > 0:
            fish_lst.append((i, j, lst[i][j]))

def bfs():
    global lst, shark_position, shark_size, eat_cnt, result, fish_lst
    q = deque()
    used = [[0] * N for _ in range(N)]

    q.append((shark_position[0], shark_position[1], 0))
    used[shark_position[0]][shark_position[1]] = 1

    eat_fish = []

    while q:
        nowy, nowx, nowt = q.popleft()

        if 0 < lst[nowy][nowx] < shark_size:
            if not eat_fish:
                eat_fish = [nowy, nowx, nowt]
            else:
                if nowt < eat_fish[2]:
                    eat_fish = [nowy, nowx, nowt]
                elif nowt == eat_fish[2]:
                    if (eat_fish[0] > nowy) or (eat_fish[0] == nowy and eat_fish[1] > nowx):
                        eat_fish = [nowy, nowx, nowt]
                else:
                    break

        for dy, dx in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < N and not used[ny][nx] and lst[ny][nx] <= shark_size:
                used[ny][nx] = 1
                q.append((ny, nx, nowt + 1))

    if eat_fish:
        eat_cnt += 1
        if shark_size == eat_cnt:
            shark_size += 1
            eat_cnt = 0
        eat_y, eat_x = eat_fish[0], eat_fish[1]
        fish_lst.remove((eat_y, eat_x, lst[eat_y][eat_x]))
        lst[eat_y][eat_x] = 0
        shark_position = (eat_y, eat_x)
        result += eat_fish[2]
        return 1
    else:
        return 0

# 물고기가 없어질 때까지 반복
while fish_lst:
    # 먹을 수 있는 물고기가 있는지 체크
    flag = 0

    for fish in fish_lst:
        if fish[2] < shark_size:
            flag = 1
            break

    if flag:
    # bfs로 가장 가까우면서 먹을 수 있는 물고기 탐색해서 먹기
        res = bfs()
        if not res:
            break
    else:
        break

print(result)