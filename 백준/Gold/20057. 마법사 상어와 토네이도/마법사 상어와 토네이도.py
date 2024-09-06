# N×N
N = int(input())
M = N
# A[r][c]는 (r, c)에 있는 모래의 양
lst = [list(map(int, input().split())) for _ in range(N)]

# 왼쪽부터 반시계방향
directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
# 왼쪽 기준 x에서 y로 이동할 때 y의 모래가 흩날리는 비율들
tmp = [
    [0, 0, 0.02, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0.05, 0, 0, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0]
]
# 방향 별로 이동할 때 모래가 흩날리는 비율들
percentages = [tmp]
for _ in range(3):
    percentages.append(list(zip(*percentages[-1]))[::-1])

# 토네이도의 시작 방향은 왼쪽
d = 0
# 토네이도를 시전하면 격자의 가운데 칸부터 토네이도의 이동이 시작
y = x = N // 2

now_cnt = 0
max_cnt = 1
need_to_increase_max_cnt = 2

# 토네이도는 한 번에 한 칸 이동
# 우선 토네이도 제대로 돌아가는지 확인 > 완료
# 토네이도가 소멸되었을 때, 격자의 밖으로 나간 모래의 양
result = 0
while 1:
    y += directions[d][0]
    x += directions[d][1]

    if not (0 <= y < N and 0 <= x < M):
        break

    # 토네이도가 x에서 y로 이동하면, y의 모든 모래가 비율과 α가 적혀있는 칸으로 이동
    # 현재 y, x가 이동한 위치이므로
    original = lst[y][x]
    left = lst[y][x]
    if left:
        for i in range(5):
            for j in range(5):
                if not percentages[d][i][j]:
                    continue
                ny, nx = y + i - 2, x + j - 2

                # 비율이 적혀있는 칸으로 이동하는 모래의 양은 y에 있는 모래의 해당 비율만큼이고,
                # 계산에서 소수점 아래는 버린다.
                c = int(original * percentages[d][i][j])
                left -= c

                if 0 <= ny < N and 0 <= nx < M:
                    lst[ny][nx] += c
                else:
                    result += c

        # α로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같다.
        # 모래가 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해진다
        lst[y][x] = 0
        ny, nx = y + directions[d][0], x + directions[d][1]
        if 0 <= ny < N and 0 <= nx < M:
            lst[ny][nx] += left
        else:
            result += left

    now_cnt += 1

    if now_cnt == max_cnt:
        now_cnt = 0
        d = (d + 1) % 4
        need_to_increase_max_cnt -= 1

        if not need_to_increase_max_cnt:
            max_cnt += 1
            need_to_increase_max_cnt = 2


print(result)