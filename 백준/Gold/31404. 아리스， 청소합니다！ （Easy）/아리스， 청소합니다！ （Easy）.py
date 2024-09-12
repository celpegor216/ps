N, M = map(int, input().split())
y, x, d = map(int, input().split())

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

# 규칙표 A, B는 각 칸에 대응, 회전 각도가 적혀져 있음
rule_A = [list(map(int, input())) for _ in range(N)]
rule_B = [list(map(int, input())) for _ in range(N)]

# 처음에 모든 칸은 먼지로 뒤덮여 있습니다.
# 청소한 칸이면 1, 아니면 0
cleaned = [[0] * M for _ in range(N)]
last_cleaned = [-1, -1, -1, -1]


result = 0
while 1:
    result += 1

    if y == last_cleaned[0] and x == last_cleaned[1]:
        last_cleaned[2] += 1

    # 이후 로봇 청소기는 매 단위 시간마다 다음과 같은 이동을 반복합니다.
    # 현재 칸에 먼지가 있다면 먼지를 제거합니다.
    flag = 0

    if not cleaned[y][x]:
        cleaned[y][x] = 1
        flag = 1
        last_cleaned = [y, x, 0, result]

    if flag:
        # 방금 먼지를 제거했다면 규칙표 A에서 현재 좌표에 적힌만큼 시계방향으로 회전
        d = (d + rule_A[y][x]) % 4
    else:
        # 그렇지 않다면 규칙표 B 참조
        d = (d + rule_B[y][x]) % 4

    # 바라보는 방향으로 한 칸 전진
    y += directions[d][0]
    x += directions[d][1]

    # 이동을 마친 후에, 로봇 청소기가 영역 밖으로 벗어났다면 작동을 중지합니다.
    # 또한, 지금부터 위의 과정을 아무리 반복해도 더이상 먼지를 제거할 수 없는 경우에도 작동을 중지합니다.
    if not(0 <= y < N and 0 <= x < M) or last_cleaned[2] == 4:
        result = last_cleaned[-1]
        break


print(result)