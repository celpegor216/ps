# 인덱스 에러 해결하기 위해 반례 참고함 > init 함수 반환값 순서를 틀림...
# 동굴 밖을 벗어나더라도 탐색을 종료하면 안 됨


from collections import deque


N, M = map(int, input().split())
# 1: 석순, 2: 아리, 3: 보스
lst = [list(map(int, input().split())) for _ in range(N)]
A_HP, A_ATTACK, B_HP, B_ATTACK = map(int, input().split())

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 아리는 동굴 안의 격자판 중 한 칸에, 보스는 아리와 상하좌우 인접한 칸 중 한 칸에 위치한 상태로 전투가 시작
# 전투가 시작될 때 보스의 진행 방향은 보스가 아리를 바라보고 있는 방향이며, 아리의 첫 진행 방향도 보스의 진행 방향과 동일
def init():
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 3:
                lst[i][j] = 0
                for d in range(4):
                    ny, nx = i + directions[d][0], j + directions[d][1]
                    if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] == 2:
                        lst[ny][nx] = 0
                        return ny, nx, d, i, j, d


A_Y, A_X, A_DIR, B_Y, B_X, B_DIR = init()


result = ''
def check():
    global result
    if A_HP <= 0:
        result = 'CAVELIFE...'
        return 1
    elif B_HP <= 0:
        result = 'VICTORY!'
        return 1

# 아리와 보스 모두 동굴 벽이나 석순이 자란 칸으로 이동할 수 없으며, 둘이 동시에 한 칸에 있을 수는 없다.
# 전투 중, 아리와 보스는 각자의 현재 진행 방향으로 한 칸 이동할 수 있으며 진행 방향은 상하좌우 네 방향 중 하나
# 전투 중 아리와 보스 둘 중 체력이 먼저 0 보다 작거나 같게 되는 쪽이 패배하며 전투는 그 즉시 끝나게 된다
def play():
    global A_HP, B_HP, A_Y, A_X, B_Y, B_X, A_DIR, B_DIR

    while 1:
        A_NY, A_NX = A_Y, A_X

        # 아리의 공격
        #    아리는 D만큼의 데미지로 보스를 한 번 공격
        B_HP -= A_ATTACK

        if check():
            return

        # 아리의 이동
        #    아리는 현재 진행 방향으로 한 칸 이동
        #    아리가 현재 진행 방향으로 이동할 수 없는 경우, 이동할 수 있는 진행 방향을 찾을 때까지 제자리에서 오른쪽으로 90도씩 회전하고 회전할 때마다 체력을 1 소모한다. 이동할 수 있는 진행 방향을 찾았을 때, 해당 방향으로 한 칸 이동한다.
        #    4번을 회전하고도 진행 방향을 찾지 못한 경우 현재 위치한 칸에서 아리의 이동 차례를 마친다.
        for _ in range(4):
            ny, nx = A_Y + directions[A_DIR][0], A_X + directions[A_DIR][1]

            if 0 <= ny < N and 0 <= nx < M and not lst[ny][nx] and (ny, nx) != (B_Y, B_X):
                A_NY, A_NX = ny, nx
                break

            A_DIR = (A_DIR + 1) % 4
            A_HP -= 1

            if check():
                return

        # 보스의 공격
        #    현재 위치한 칸을 중심으로 현재 진행 방향에서 시작해서 시계 방향으로 탐색을 진행
        #    석순을 발견하는 순간 찾는 과정을 멈추고 석순이 위치한 칸에 보스의 공격력인 E만큼의 체력을 가지는 부하 몬스터를 한 마리 소환
        #    동굴의 모든 칸을 확인하고도 석순을 발견하지 못한다면 보스는 그대로 자신의 공격 차례를 마친다.
        ty, tx = B_Y, B_X
        add_move_amount = 0
        move_amount = 1
        move_d = B_DIR
        monster = None
        cnt = 1
        while cnt < N * M:
            for _ in range(move_amount):
                ty += directions[move_d][0]
                tx += directions[move_d][1]

                if 0 <= ty < N and 0 <= tx < M:
                    cnt += 1
                    if lst[ty][tx] == 1:
                        monster = (ty, tx)
                        break
            
            if monster:
                break
            
            move_d = (move_d + 1) % 4
            add_move_amount += 1

            if add_move_amount == 2:
                add_move_amount = 0
                move_amount += 1

        #    부하 몬스터는 아리에게 최단 거리로 이동하여 아리를 공격하고 사라지며, 부하 몬스터가 사라져야만 보스의 공격 차례가 끝나고 보스의 다음 이동이 가능
        #    부하 몬스터는 상하좌우로 한 칸씩 이동 가능하며, 한 칸 이동할 때마다 자신의 체력을 1 소모한다. 부하 몬스터는 동굴 벽 혹은 보스나 석순이 위치한 칸으로 이동할 수 없다. 부하 몬스터가 아리가 있는 칸에 도착했을 때 남은 체력만큼 아리에게 데미지를 입히고 사라지며, 만약 아리에게 가는 도중 체력이 0이 되었거나 아리에게 도착할 수 없었다면 부하 몬스터는 데미지를 입히지 못하고 사라진다.
        if monster:
            q = deque()
            used = [[0] * M for _ in range(N)]
            q.append((monster[0], monster[1], B_ATTACK))
            used[monster[0]][monster[1]] = 1

            while q:
                y, x, c = q.popleft()

                if not c:
                    continue

                if (y, x) == (A_NY, A_NX):
                    A_HP -= c
                    break

                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and not lst[ny][nx] and (ny, nx) != (B_Y, B_X):
                        q.append((ny, nx, c - 1))
                        used[ny][nx] = 1

        if check():
            return
        
        # 보스의 이동
        #    아리가 마지막으로 이동하기 전 위치한 칸으로 이동하고, 아리가 마지막으로 이동하고 난 후의 진행 방향과 같은 방향을 가진다.
        #     만약, 아리의 마지막 이동 차례에서 아리가 이동할 수 없었다면 보스도 현재 위치한 칸에서 이동 차례를 마친다.
        B_DIR = A_DIR

        if A_Y == A_NY and A_X == A_NX:
            continue

        B_Y, B_X = A_Y, A_X
        A_Y, A_X = A_NY, A_NX

play()

print(result)