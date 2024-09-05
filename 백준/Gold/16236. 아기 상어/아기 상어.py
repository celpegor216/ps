from collections import deque

# N×N 크기
N = int(input())
M = N
# 물고기 T마리와 아기 상어 1마리
# 한 칸에는 물고기가 최대 1마리 존재
lst = [list(map(int, input().split())) for _ in range(N)]

def find():
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 9:
                lst[i][j] = 0
                return i, j


# 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동
y, x = find()
level = 2
exp = 0

result = 0
while 1:
    # 먹을 수 있는 물고기가 모두 사라질 때가지 반복문 실행
    fish = []

    # 현재 위치에서 bfs로 가장 가까우면서 왼쪽 위에 존재하는 물고기 찾기
    q = deque()
    used = [[0] * M for _ in range(N)]
    q.append((y, x))
    used[y][x] = 1

    move_cnt = 0
    while q:
        move_cnt += 1
        for _ in range(len(q)):
            nowy, nowx = q.popleft()

            for dy, dx in ((0, 1), (1 ,0), (0, -1), (-1, 0)):
                ny, nx = nowy + dy, nowx + dx

                # 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고,
                # 나머지 칸은 모두 지나갈 수 있다.
                # 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
                # 따라서, 크기가 같은 물고기는 먹을 수 없지만,
                # 그 물고기가 있는 칸은 지나갈 수 있다.

                if 0 <= ny < N and 0 <= nx < M and not used[ny][nx]:
                    if lst[ny][nx] == 0 or lst[ny][nx] == level:
                        used[ny][nx] = 1
                        q.append((ny, nx))
                    elif lst[ny][nx] < level:
                        fish.append((ny, nx))

        if fish:
            break

    # 위치 이동해서 물고기 먹고 레벨 확인
    # 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
    # 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
    # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    if fish:
        fish.sort()
        my, mx = fish[0]
        lst[my][mx] = 0
        y, x = my, mx
        exp += 1
        # 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
        if exp == level:
            level += 1
            exp = 0
        result += move_cnt
    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청
    else:
        break


# 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램
print(result)