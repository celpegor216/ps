# N * M
N, M = map(int, input().split())

# p는 플레이어, .은 빈칸, m은 몬스터, *은 장애물, g는 목적지
# p와 g는 하나만 주어지며 m은 하나 이상
# 가장자리는 무조건 장애물
lst = [list(input()) for _ in range(N)]

# 몬스터의 수
K = int(input())
monsters_idx = dict()
monsters_hp = list(map(int, input().split()))
monsters_md = list(map(int, input().split()))
monsters_exp = list(map(int, input().split()))

# 명령어 수
_ = int(input())
cmds = input().split()

# 플레이어는 공격력 attack, 공격 사거리 attack_dist, 이동속도 speed, 레벨 level, 경험치 exp, 요구 경험치 need_exp
# 공격력 5, 공격 사거리 1, 이동속도 1, 레벨 1, 경험치 0, 요구 경험치 10 으로 시작
attack, attack_dist, speed, level, exp, need_exp = 5, 1, 1, 1, 0, 10

py = px = -1
midx = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == 'p':
            lst[i][j] = '.'
            py, px = i, j
        elif lst[i][j] == 'm':
            monsters_idx[(i, j)] = midx
            midx += 1

# 사용한 행동력
used = 0
pills = 0
is_overdose = 0


directions = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}


# 스킵이가 한 행동이 불가능한 행동이었을 경우 게임은 그 행동을 무시하고 다음 행동을 실행
# 이 때 행동력은 소모되지 않는다
for cmd in cmds:
    # 순간이동
    # - 행동력 1을 소모해 상하좌우 중 한 방향을 정해 정확히 이동속도만큼 떨어진 위치로 이동
    # - 이동할 위치가 좌표 범위 밖이거나 장애물 혹은 몬스터가 있으면 움직일 수 없다.
    if cmd in 'udlr':
        dy, dx = directions[cmd]
        ny, nx = py + dy * speed, px + dx * speed
        if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] not in 'm*':
            py, px = ny, nx
            used += 1
            if is_overdose:
                is_overdose -= 1

    # 대기
    # - 행동력 1을 소모해 아무 행동도 하지 않는다.
    elif cmd == 'w':
        used += 1
        if is_overdose:
            is_overdose -= 1

    # 공격
    # - 행동력 3을 소모해 상하좌우 중 한 방향으로 투사체를 발사한다.
    # - 투사체는 발사된 방향으로 공격 사거리만큼의 거리를 한 칸씩 움직이며
    #   투사체와 몬스터가 같은 위치에 있게 되면 몬스터의 체력이
    #   (플레이어의 공격력 - 몬스터의 방어력)만큼 감소한다.
    # - 단, 플레이어의 공격력이 몬스터의 방어력보다 낮은 경우 몬스터의 체력은 감소하지 않는다.
    # - 만약 이 행동으로 인해 몬스터의 체력이 0 이하가 되면
    #   그 자리는 빈칸이 되고 플레이어는 경험치를 획득한다.
    # - 투사체가 이동할 다음 좌표에 장애물이 있는 경우 투사체는 사라진다.
    # - 투사체는 장애물을 제외한 다른 물체를 만나도 사라지거나 행동을 멈추지 않는다.
    elif cmd[0] == 'a' and not is_overdose:
        used += 3
        dy, dx = directions[cmd[1]]
        ny, nx = py, px
        for _ in range(attack_dist):
            ny += dy
            nx += dx

            if lst[ny][nx] == '*':
                break

            if lst[ny][nx] == 'm':
                midx = monsters_idx[(ny, nx)]
                damage = attack - monsters_md[midx]
                if damage > 0:
                    monsters_hp[midx] -= damage
                    if monsters_hp[midx] <= 0:
                        lst[ny][nx] = '.'
                        exp += monsters_exp[midx]


    # 약 먹기
    # - 행동력 2를 소모해 이동속도가 1 증가 혹은 감소하는 약을 먹는다.
    #   이동속도가 0인 경우 음수로 내려가지 않는다. 이때 행동력은 그대로 소모된다.
    # - 약을 5번 먹을 때마다 OVERDOSE 상태가 되며 OVERDOSE 상태에서는 순간이동,
    #   대기를 제외한 다른 행동을 할 수 없다.
    # - OVERDOSE 상태가 된 후 행동력을 10 이상 소모할 경우 OVERDOSE 상태는 해제된다.
    elif cmd == 'du' and not is_overdose:
        used += 2
        speed += 1
        pills += 1
        if pills == 5:
            pills = 0
            is_overdose = 10

    elif cmd == 'dd' and not is_overdose:
        used += 2
        if speed:
            speed -= 1
        pills += 1
        if pills == 5:
            pills = 0
            is_overdose = 10

    # 클리어
    # - 플레이어가 목적지와 같은 좌표에 있으면 행동력 0을 소모해 스테이지를 클리어한다.
    # - 게임을 클리어한 후 캐릭터는 다른 행동을 할 수 없다.
    elif cmd == 'c' and not is_overdose:
        if lst[py][px] == 'g':
            break

    # 한 가지 행동이 끝난 후 경험치를 얻어 요구 경험치 이상이 되면,
    # 경험치 < 요구 경험치를 만족할 때까지 레벨이 상승하고 경험치를 요구 경험치만큼 뺀다.
    # 레벨이 l일 때 레벨업하면 공격력이 l만큼, 공격 사거리가 1만큼, 요구 경험치가 10만큼 증가
    while exp >= need_exp:
        attack += level
        attack_dist += 1
        exp -= need_exp
        level += 1
        need_exp += 10


print(level, exp)
print(used)
lst[py][px] = 'p'
for line in lst:
    print(''.join(line))
for item in monsters_hp:
    if item > 0:
        print(item, end=' ')