R, C, T = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(R)]
up = 0
down = 0

for i in range(R):
    if lst[i][0] == -1:
        up = i
        down = i + 1
        break

# 미세먼지 확산
def diffusion():
    temp = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if lst[r][c] > -1:
                n = lst[r][c] // 5
                cnt = 0
                for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and lst[nr][nc] != -1:
                        temp[nr][nc] += n
                        cnt += 1
                lst[r][c] -= (lst[r][c] // 5) * cnt

    for r in range(R):
        for c in range(C):
            lst[r][c] += temp[r][c]


# 공기청정기 작동
def airpurifier():
    # up
    temp1 = lst[up][-1]
    temp2 = lst[0][-1]
    temp3 = lst[0][0]

    for c in range(C - 1, 1, -1):
        lst[up][c] = lst[up][c - 1]
    lst[up][1] = 0

    for r in range(up - 1):
        lst[r][-1] = lst[r + 1][-1]
    lst[up - 1][-1] = temp1

    for c in range(C - 1):
        lst[0][c] = lst[0][c + 1]
    lst[0][-2] = temp2

    for r in range(up - 1, 1, -1):
        lst[r][0] = lst[r - 1][0]
    lst[1][0] = temp3


    # down
    temp1 = lst[down][-1]
    temp2 = lst[-1][-1]
    temp3 = lst[-1][0]

    for c in range(C - 1, 1, -1):
        lst[down][c] = lst[down][c - 1]
    lst[down][1] = 0

    for r in range(R - 1, down + 1, -1):
        lst[r][-1] = lst[r - 1][-1]
    lst[down + 1][-1] = temp1

    for c in range(C - 1):
        lst[-1][c] = lst[-1][c + 1]
    lst[-1][-2] = temp2

    for r in range(down + 1, R - 1):
        lst[r][0] = lst[r + 1][0]
    lst[-2][0] = temp3


for t in range(T):
    diffusion()
    airpurifier()

result = 0

for line in lst:
    for item in line:
        if item != -1:
            result += item

print(result)