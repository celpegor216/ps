'''
14:08
문제 읽고 구현해야 할 부분 작성, 입력 받기, 고정값 배열 작성

'''

# N×N
# 파이어볼 F개
N, F, K = map(int, input().split())
M = N
# y, x, 질량 m, 속력 s, 방향 d
# 서로 다른 두 파이어볼의 위치가 같은 경우는 입력으로 주어지지 않는다.
lst = [list(map(int, input().split())) for _ in range(F)]

# 파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향
directions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

# 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결 (oob 체크 안 함)
for _ in range(K):
    # 한 칸에 2개 이상의 파이어볼이 있는지 확인하기 위함
    # pos[(y, x)]: (y, x) 위치에 있는 파이어볼
    pos = dict()

    # 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
    # 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
    # fireball을 클래스로 만들어서 관리하는게 좋긴 하지만... 귀찮고 잘 모름
    for fireball in lst:
        dy, dx = directions[fireball[-1]]
        s = fireball[-2]
        ny, nx = (fireball[0] + (dy * s)) % N, (fireball[1] + (dx * s)) % M
        fireball[0] = ny
        fireball[1] = nx

        if not pos.get((ny, nx)):
            pos[(ny, nx)] = []
        pos[(ny, nx)].append(fireball)

    # 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
        # 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
        # 파이어볼은 4개의 파이어볼로 나누어진다.
    # 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
        # 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
        # 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
        # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.

    lst = []
    for key, value in pos.items():
        cnt = len(value)

        if cnt < 2:
            lst += value
            continue

        total_m = 0
        total_s = 0
        cnt_odd_d = 0
        cnt_even_d = 0

        for fireball in value:
            total_m += fireball[2]
            total_s += fireball[3]
            if fireball[-1] % 2:
                cnt_odd_d += 1
            else:
                cnt_even_d += 1

        # 질량이 0인 파이어볼은 소멸되어 없어진다.
        if total_m < 5:
            continue

        new_m = total_m // 5
        new_s = total_s // cnt
        new_d = (0, 2, 4, 6) if cnt_odd_d == cnt or cnt_even_d == cnt else (1, 3, 5, 7)

        for i in range(4):
            lst.append([key[0], key[1], new_m, new_s, new_d[i]])

# 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합
result = 0
for _, _, m, _, _ in lst:
    result += m

print(result)