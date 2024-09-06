from collections import deque


N, M, P = map(int, input().split())
# ‘.’은 이동할 수 있는 길, ‘X’는 이동할 수 없는길,
# 알파벳 소문자는 플레이어의 아이디이며 ‘B’는 보스몬스터의 위치
lst = [input() for _ in range(N)]
# 플레이어의 아이디와 dps, dps란 1초당 얼만큼의 보스몬스터의 체력을 줄일 수 있는지
# players[name]: dps, 보스몬스터의 위치로 도착한 시각
players = dict()
for _ in range(P):
    name, dps = input().split()
    players[name] = int(dps)
# 보스몬스터의 HP
hp = int(input())

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 모든 플레이어는 보스몬스터가 소환되면 보스몬스터의 위치로 최대한 빠른 경로로 이동하며
# 플레이어는 상, 하, 좌, 우로 이동할 수 있고 이동에 소요되는 시간은 1초
arrived = []

for i in range(N):
    for j in range(M):
        # 알파벳 소문자는 플레이어의 아이디
        if not lst[i][j].islower():
            continue

        q = deque()
        q.append((i, j))

        used = [[0] * M for _ in range(N)]
        used[i][j] = 1

        while q:
            y, x = q.popleft()

            if lst[y][x] == 'B':
                arrived.append((used[y][x] - 1, players[lst[i][j]]))
                break

            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                # 한 지점에 여러명의 플레이어가 위치할 수 있다
                if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] != 'X':
                    used[ny][nx] = used[y][x] + 1
                    q.append((ny, nx))

# 이동한 경우 공격을 바로 시작
# 공격에 소모되는 시간은 1초이며
# 보스와 같은 위치에 있는 모든 플레이어의 공격은 동시에 이뤄진다
# 최대 몇 명의 플레이어가 전리품을 가져갈 수 있는지 계산
arrived.sort()

time = 0
total_dps = 0
for i in range(len(arrived)):
    t, dps = arrived[i]
    if time == 0:
        time = t
        total_dps = dps
    else:
        if time != t:
            hp -= (t - time) * total_dps
            time = t

            if hp <= 0:
                print(i)
                break
        total_dps += dps
else:
    print(len(arrived))