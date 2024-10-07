# N×N
N = int(input())

# 학생은 총 K번의 사격을 진행하며, 1번부터 K번까지의 총알을 차례대로 발사
# 각 총알은 공격력 정보를 가지고 있다
K = int(input())

# 보드 판에서 표적이 있는 위치는 1 이상의 자연수, 표적이 없는 곳은 정수 0
# 표적이 있는 위치의 값은 초기 체력(시작 시점의 현재 체력)
original = [list(map(int, input().split())) for _ in range(N)]

bullets = list(map(int, input().split()))


def shoot(level, now, now_original, i, j):
    nxt = [line[:] for line in now]
    nxt_original = [line[:] for line in now_original]

    score = 0

    # 총알은 가장 왼쪽 열(1열)에서 시작해
    # 왼쪽에서 오른쪽으로 수평으로 한 칸씩 이동하며 날아감
    # 총알이 표적에 닿으면 현재 체력이 총알의 공격력만큼 감소
    # 총알은 표적을 관통하지 못 하고, 표적에 닿은 총알은 즉시 사라진다
    nxt[i][j] -= bullets[level]

    # 값이 10 이상인 표적은 보너스 표적이다. 보너스 표적은 별도의 초기 체력이 없다
    # 보너스 표적을 맞히는 순간 총알의 공격력과 상관없이 총알과 보너스 표적이 함께 사라지며,
    # 그 즉시 보너스 표적에 적힌 점수만큼 점수를 더한다
    # 보너스 표적은 사라진 뒤에 새로운 표적을 생성하지 않는다
    if now_original[i][j] > 9:
        score += now_original[i][j]
        nxt[i][j] = 0
        nxt_original[i][j] = 0
    else:
        # 일반 표적의 초기 체력은 1 이상 9 이하의 자연수
        if nxt[i][j] <= 0:
            # 총알에 닿아 현재 체력이 0 이하가 되면 표적은 사라진다
            # 해당 표적의 초기 체력만큼 점수를 얻는다
            score += now_original[i][j]
            nxt[i][j] = 0
            nxt_original[i][j] = 0

            # 사라진 표적 위치의 상, 하, 좌, 우 위치 중에서 빈 칸(표적이 없는 곳)인 모든 위치에 대하여,
            # 사라진 표적의 초기 체력의 1/4의 값을 초기 체력으로 가지는 새로운 표적이 생성된다
            # 소수점 아래는 버리며, 만약 그 값이 0인 경우에는 새로운 표적은 생성되지 않는다
            if 3 < now_original[i][j]:
                value = now_original[i][j] // 4
                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ny, nx = i + dy, j + dx
                    if 0 <= ny < N and 0 <= nx < N and not nxt[ny][nx]:
                        nxt[ny][nx] = value
                        nxt_original[ny][nx] = value

    return score, nxt, nxt_original


result = 0

def dfs(level, total, now, now_original):
    global result

    if level == K:
        result = max(result, total)
        return

    # 한 번의 사격을 할 때는 1행부터 N행까지 중에서 하나의 행을 선택
    for i in range(N):
        for j in range(N):
            if now[i][j]:
                score, nxt, nxt_original = shoot(level, now, now_original, i, j)
                dfs(level + 1, total + score, nxt, nxt_original)
                break


dfs(0, 0, original, original)


# K번의 사격으로 얻을 수 있는 점수의 최댓값
print(result)