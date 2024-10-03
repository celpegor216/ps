def noob(i, j):
    return 0<=i<4 and 0<=j<4


def move_fish(sea, fish):
    for n in range(1, 17):
        if fish[n]:
            i, j = fish[n][0], fish[n][1]
            d = fish[n][2]
            di, dj = DIR[d]
            ni, nj = i+di, j+dj
            if noob(ni, nj) and sea[ni][nj] != -1:
                if sea[ni][nj] == 0:  # 빈 칸일 때
                    fish[n] = [ni, nj, d]
                    sea[ni][nj] = n
                    sea[i][j] = 0
                else:  # 다른 물고기가 있을 때
                    ano_fish = sea[ni][nj]
                    fish[n] = [ni, nj, d]
                    fish[ano_fish][0], fish[ano_fish][1] = i, j
                    sea[i][j], sea[ni][nj] = sea[ni][nj], sea[i][j]

            else:
                cnt = 0
                while 1:
                    if noob(ni, nj) and sea[ni][nj] != -1:
                        break
                    if cnt == 8:
                        break
                    d = (d+1)%8
                    di, dj = DIR[d]
                    ni, nj = i+di, j+dj
                    cnt += 1
                if cnt != 8:
                    if sea[ni][nj] == 0:
                        fish[n] = [ni, nj, d]
                        sea[ni][nj] = n
                        sea[i][j] = 0
                    else:
                        ano_fish = sea[ni][nj]
                        fish[n] = [ni, nj, d]
                        fish[ano_fish][0], fish[ano_fish][1] = i, j
                        sea[i][j], sea[ni][nj] = sea[ni][nj], sea[i][j]
    return sea, fish


def move_shark(res, arr, shark, fish, ni, nj):
    sx, sy = shark[0], shark[1]
    if noob(ni, nj) and arr[ni][nj] != 0:  # iob고 물고기가 있을 때
        tmp_fish = arr[ni][nj]
        res += tmp_fish
        shark = [ni, nj, fish[tmp_fish][2]]
        fish[tmp_fish] = []
        arr[sx][sy] = 0
        arr[ni][nj] = -1

    return arr, shark, fish, res


def dfs(res, arr, fish, shark):
    global total

    sx, sy, sd = shark
    di, dj = DIR[sd]
    cnt = 0

    for mul in range(1, 4):
        ni, nj = sx+di*mul, sy+dj*mul
        if noob(ni, nj) and arr[ni][nj] != 0 and arr[ni][nj] != -1:  # oob가 아니고 물고기가 있는 칸만
            tmp_arr = [lst[:] for lst in arr]
            tmp_fish = [lst[:] for lst in fish]
            tmp_shark = shark[:]

            new_arr, new_shark, renew_info, tot = move_shark(res, tmp_arr, tmp_shark, tmp_fish, ni, nj)
            new_arr, renew_info = move_fish(new_arr, renew_info)
            dfs(tot, new_arr, renew_info, new_shark)
        else:
            cnt += 1
    if cnt == 3:  # 이동 못할 때 return 처리 해주기
        total = max(total, res)
        return


sea = [[0 for _ in range(4)] for _ in range(4)]
DIR = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
fish = [[] for _ in range(17)]
i, j = 0, 0
total = 0  # 최종 출력 변수
for _ in range(4):
    a, b, c, d, e, f, g, h = map(int, input().split())
    fish[a] = [i, j, b-1]
    fish[c] = [i, j+1, d-1]
    fish[e] = [i, j+2, f-1]
    fish[g] = [i, j+3, h-1]
    sea[i][j] = a
    sea[i][j+1] = c
    sea[i][j+2] = e
    sea[i][j+3] = g
    i += 1

# 상어의 시작 위치와, 시작 지점에 있는 물고기 먹고 시작해줌
shark = [0, 0, fish[sea[0][0]][2]]
fish[sea[0][0]] = []
total += sea[0][0]
sea[0][0] = -1  # 상어는 -1로 표시해주기

# 물고기 한 번 이동한 뒤, 상어가 움직이는 것부터 케이스가 갈리니까
# 초기 물고기 이동은 메인에서 함수 돌려주고, 상어가 움직이는 것부터는 dfs 안에서 돌려주기

sea, fish = move_fish(sea, fish)
dfs(total, sea, fish, shark)
print(total)