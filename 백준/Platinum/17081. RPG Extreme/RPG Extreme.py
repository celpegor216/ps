N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
moves = input()
moves_dict = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
moves_length = len(moves)
ornaments = ["HR", "RE", "CO", "EX", "DX", "HU", "CU"]

# 레벨, 현재 체력, 최대 체력, 공격력, 무기 공격력, 방어력, 무기 방어력, 현재 경험치, 최대 경험치, 가지고 있는 장신구
status = [1, 20, 20, 2, 0, 2, 0, 0, 5, set()]
y = x = -1    # 현재 위치
sy = sx = -1    # 부활을 위해 필요한 첫 시작 위치

K = L = 0
for n in range(N):
    for m in range(M):
        if lst[n][m] in '&M':
            K += 1
        elif lst[n][m] == 'B':
            L += 1
        elif lst[n][m] == '@':
            y = sy = n
            x = sx = m
            lst[n][m] = '.'

monsters = dict()    # y, x, 이름, 공격력, 방어력, 체력, 경험치
for _ in range(K):
    tmp = input().split()
    for i in range(7):
        if i == 2:
            continue
        tmp[i] = int(tmp[i])
    monsters[(tmp[0] - 1, tmp[1] - 1)] = tmp[2:]

boxes = dict()    # y, x, 타입, 공격력/방어력/효과
for _ in range(L):
    tmp = input().split()
    for i in range(4):
        if i == 2:
            continue

        if i == 3 and tmp[2] == 'O':
            continue
        tmp[i] = int(tmp[i])
    boxes[(tmp[0] - 1, tmp[1] - 1)] = tmp[2:]

# 여기까지 입력
# -----------------------------------------------------------

def check_reincarnation(is_battle):
    global y, x

    if 'RE' in status[-1]:
        status[-1].remove('RE')
        status[1] = status[2]
        y = sy
        x = sx
        return 1


def check_spike():
    if 'DX' in status[-1]:
        status[1] -= 1
    else:
        status[1] -= 5

    if status[1] <= 0:
        res = check_reincarnation(0)
        if not res:
            return (1, "YOU HAVE BEEN KILLED BY SPIKE TRAP..")

def check_monster(my, mx):
    monster = monsters[(my, mx)]
    monster_max_health = monster[3]

    if lst[my][mx] == 'M' and 'HU' in status[-1]:
        status[1] = status[2]

    idx = 0

    while 1:

        # 첫 번째 공격에서 CO만 있는 경우 / CO와 DX가 같이 있는 경우
        if idx == 0 and 'CO' in status[-1]:
            if 'DX' not in status[-1]:
                monster[3] -= max(1, (status[3] + status[4]) * 2 - monster[2])
            else:
                monster[3] -= max(1, (status[3] + status[4]) * 3 - monster[2])
        else:
            monster[3] -= max(1, status[3] + status[4] - monster[2])

        if monster[3] <= 0:
            break

        if not(idx == 0 and lst[my][mx] == 'M' and 'HU' in status[-1]):
            status[1] -= max(1, monster[1] - status[5] - status[6])

            if status[1] <= 0:
                res = check_reincarnation(1)
                if not res:
                    return (1, f"YOU HAVE BEEN KILLED BY {monster[0]}..")
                else:
                    monster[3] = monster_max_health
                    return

        idx += 1


    # 이긴 경우
    if 'HR' in status[-1]:
        status[1] += 3
        if status[1] > status[2]:
            status[1] = status[2]

    if 'EX' in status[-1]:
        status[7] += int(monster[-1] * 1.2)
    else:
        status[7] += monster[-1]

    if status[7] >= status[8]:
        status[0] += 1
        status[2] += 5
        status[3] += 2
        status[5] += 2
        status[1] = status[2]
        status[7] = 0
        status[8] = status[0] * 5

    if lst[my][mx] == 'M':
        lst[my][mx] = '.'
        return (0, 'YOU WIN!')
    lst[my][mx] = '.'


def print_result(is_death, result):
    if not is_death:
        lst[y][x] = '@'

    for line in lst:
        print(''.join(line))

    if status[1] < 0:
        status[1] = 0

    print(f'Passed Turns : {move + 1}')
    print(f'LV : {status[0]}')
    print(f'HP : {status[1]}/{status[2]}')
    print(f'ATT : {status[3]}+{status[4]}')
    print(f'DEF : {status[5]}+{status[6]}')
    print(f'EXP : {status[7]}/{status[8]}')
    print(result)

# 여기까지 필요한 함수
# --------------------------------------------------------------
# 이 아래로 실행

result = 0

for move in range(moves_length):
    dy, dx = moves_dict[moves[move]]
    ny, nx = y + dy, x + dx

    if not(0 <= ny < N and 0 <= nx < M) or lst[ny][nx] == '#':
        if lst[y][x] == '^':
            result = check_spike()
            if result:
                break
        continue

    y = ny
    x = nx

    if lst[ny][nx] == 'B':
        box_type, spec = boxes[(ny, nx)]
        if box_type == 'W':
            status[4] = spec
        elif box_type == 'A':
            status[6] = spec
        else:
            if len(status[-1]) < 4:
                status[-1].add(spec)
        lst[ny][nx] = '.'
    elif lst[ny][nx] == '^':
        result = check_spike()
    elif lst[ny][nx] in '&M':
        result = check_monster(ny, nx)

    if result:
        break

if result:
    print_result(*result)
else:
    print_result(0, 'Press any key to continue.')