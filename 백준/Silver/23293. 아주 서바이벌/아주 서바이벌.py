import sys

input = sys.stdin.readline

T, N = map(int, input().split())

# players[i]: 위치, 획득한 소재 아이템들
# 모든 플레이어가 1번 지역(정문)에 모인 채로 게임이 시작
players = [[1, []] for _ in range(N + 1)]

incorrect_logs = []
should_ban = set()

for t in range(1, T + 1):
    # 게임 로그는 "[번호] [플레이어 번호] [행동 코드] [행동 인자]"의 형식
    # 번호 : 로그의 줄 번호이다. 1번부터 T번까지 순서대로 주어진다.
    # 플레이어 번호 : 각 플레이어가 가지는 고유한 번호이다. 1번부터 N번 사이의 번호를 가지게 된다.
    # 행동 코드 : 플레이어가 한 행동이다. 이동은 M(Move), 획득은 F(Farming), 조합은 C(Crafting), 공격은 A(Attack)이다.
    # 행동 인자 : 이동은 새로 이동한 지역의 번호, 획득은 획득한 소재 아이템의 번호, 조합은 조합에 사용된 두 소재 아이템의 번호, 공격은 공격한 플레이어 번호를 행동 인자로 가진다.
    _, player, action, *params = input().split()
    player = int(player)
    params = list(map(int, params))

    # 이동 : 플레이어가 현재 위치한 지역에서 다른 지역으로 이동한다.
    if action == 'M':
        players[player][0] = params[0]

    # 획득 : 플레이어가 현재 위치한 지역(x번 지역)에서 x번 소재 아이템을 획득한다.
    # 한 플레이어가 같은 아이템을 여러 번 획득할 수 있다.
    elif action == 'F':
        players[player][1].append(params[0])

        # 플레이어가 현재 위치한 지역에서 얻을 수 없는 소재 아이템을 획득한 경우
        # 부정행위로 획득한 소재 아이템 역시 획득한 것으로 인정되며,
        if params[0] != players[player][0]:
            incorrect_logs.append(t)

    # 조합 : 플레이어가 가지고 있는 서로 다른 종류의 두 소재 아이템을 1개씩 사용해 장비를 만든다.
    elif action == 'C':
        is_incorrect = 0
        for param in params:
            if param in players[player][1]:
                players[player][1].remove(param)
            else:
                is_incorrect = 1

        # 플레이어가 가지고 있지 않은 소재 아이템을 사용해 조합하는 경우
        # 부정행위로 조합 시 가지고 있는 소재 아이템만이 사용된다.
        if is_incorrect:
            incorrect_logs.append(t)

    # 공격 : 플레이어가 다른 플레이어 한 명을 공격한다.
    else:
        # 플레이어가 다른 지역에 있는 상대 플레이어를 공격하는 경우
        if players[params[0]][0] != players[player][0]:
            incorrect_logs.append(t)
            should_ban.add(player)

for result in (incorrect_logs, should_ban):
    if result:
        print(len(result))
        print(*sorted(result))
    else:
        print(0)
