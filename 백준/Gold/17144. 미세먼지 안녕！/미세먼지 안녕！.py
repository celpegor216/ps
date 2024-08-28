N, M, T = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
airs = []

# 공기청정기는 항상 1번 열에 설치
for i in range(N):
    if lst[i][0] == -1:
        airs.append(i)
        airs.append(i + 1)
        break

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

for _ in range(T):
    # lst_change[i][j]: (i, j)칸이 먼지 확산 이후에 변해야 하는 양
    lst_change = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if lst[i][j] <= 0:
                continue

            # 미세먼지는 인접한 네 방향으로 확산
            for dy, dx in directions:
                ny, nx = i + dy, j + dx

                # 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
                if not (0 <= ny < N and 0 <= nx < M) or lst[ny][nx] == -1:
                    continue

                change = lst[i][j] // 5

                # 확산되는 양은 5를 나눈 값에 소수점은 버린다
                lst_change[ny][nx] += change

                # 남은 미세먼지의 양은 (5를 나눈 값)×(확산된 방향의 개수)
                lst_change[i][j] -= change

    # 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다
    for i in range(N):
        for j in range(M):
            lst[i][j] += lst_change[i][j]

    # 공기청정기가 작동
    # 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고,
    # 공기청정기로 들어간 미세먼지는 모두 정화

    # 위쪽 공기청정기의 바람은 반시계방향으로 순환
    for n in range(airs[0] - 1, 0, -1):
        lst[n][0] = lst[n - 1][0]

    for m in range(M - 1):
        lst[0][m] = lst[0][m + 1]

    for n in range(airs[0]):
        lst[n][-1] = lst[n + 1][-1]

    for m in range(M - 1, 1, -1):
        lst[airs[0]][m] = lst[airs[0]][m - 1]

    lst[airs[0]][1] = 0

    # 아래쪽 공기청정기의 바람은 시계방향으로 순환
    for n in range(airs[1] + 1, N - 1):
        lst[n][0] = lst[n + 1][0]

    for m in range(M - 1):
        lst[-1][m] = lst[-1][m + 1]

    for n in range(N - 1, airs[1], -1):
        lst[n][-1] = lst[n - 1][-1]

    for m in range(M - 1, 1, -1):
        lst[airs[1]][m] = lst[airs[1]][m - 1]

    lst[airs[1]][1] = 0


# T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양
result = 0
for line in lst:
    result += sum(line)

# air 2개가 -1이라서 2 더함
print(result + 2)