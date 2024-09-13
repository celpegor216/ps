# 블록을 놓은 횟수 Q
Q = int(input())

greenN = blueM = 6
greenM = blueN = 4

green = [[0] * greenM for _ in range(greenN)]
blue = [[0] * blueM for _ in range(blueN)]


# 블록은 보드에 놓인 이후에 다른 블록과 합쳐지지 않는다


def add_block_green(t, x):
    # 블록의 이동은 다른 블록을 만나거나 보드의 경계를 만나기 전까지 계속해서 이동
    blocks = [[0, x]]
    if t == 2:
        blocks.append([0, x + 1])
    elif t == 3:
        blocks.append([1, x])

    for _ in range(greenN):
        flag = 0

        for bi, bj in blocks:
            if bi + 1 >= greenN or green[bi + 1][bj]:
                flag = 1
                break

        if not flag:
            for block in blocks:
                block[0] += 1
        else:
            break

    for bi, bj in blocks:
        green[bi][bj] = 1


def add_block_blue(t, y):
    # t = 1: 크기가 1×1인 블록을 (x, y)에 놓은 경우
    # t = 2: 크기가 1×2인 블록을 (x, y), (x, y+1)에 놓은 경우
    # t = 3: 크기가 2×1인 블록을 (x, y), (x+1, y)에 놓은 경우
    blocks = [[y, 0]]
    if t == 2:
        blocks.append([y, 1])
    elif t == 3:
        blocks.append([y + 1, 0])

    for _ in range(blueM):
        flag = 0

        for bi, bj in blocks:
            if bj + 1 >= blueM or blue[bi][bj + 1]:
                flag = 1
                break

        if not flag:
            for block in blocks:
                block[1] += 1
        else:
            break

    for bi, bj in blocks:
        blue[bi][bj] = 1


def remove_filled_green():
    # 초록색 보드에서 어떤 행이 타일로 가득 차 있다면, 그 행의 타일은 모두 사라진다.
    # 사라진 이후에는 초록색 보드에서 사라진 행의 위에 있는 블록이 사라진 행의 수만큼 아래로 이동한다.
    lines = []

    for i in range(2, greenN):
        if sum(green[i]) == greenM:
            lines.append(i)

    new_green = [[0] * greenM for _ in range(greenN)]
    for j in range(greenM):
        idx = greenN - 1
        for i in range(greenN - 1, -1, -1):
            if i in lines:
                continue
            new_green[idx][j] = green[i][j]
            idx -= 1

    return len(lines), new_green


def remove_filled_blue():
    # 파란색의 경우는 열이 타일로 가득 차 있으면, 그 열의 타일이 모두 사라지며,
    # 사라진 이후에는 파란색 보드에서 사라진 열의 왼쪽에 있는 블록이 사라진 열의 수만큼 오른쪽으로 이동
    lines = []

    for j in range(2, blueM):
        if sum([blue[i][j] for i in range(blueN)]) == blueN:
            lines.append(j)

    new_blue = [[0] * blueM for _ in range(blueN)]
    for i in range(blueN):
        idx = blueM - 1
        for j in range(blueM - 1, -1, -1):
            if j in lines:
                continue
            new_blue[i][idx] = blue[i][j]
            idx -= 1

    return len(lines), new_blue


def push_green():
    # 블록이 있는 행의 수만큼 아래 행에 있는 타일이 사라지고,
    # 초록색 보드의 모든 블록이 사라진 행의 수만큼 아래로 이동하고,
    move_cnt = 0
    for i in range(2):
        for j in range(greenM):
            if green[i][j]:
                move_cnt += 1
                break

    if move_cnt:
        return [[0] * 4 for _ in range(move_cnt)] + [line[:] for line in green[:greenN - move_cnt]]
    else:
        return green


def push_blue():
    # 블록이 있는 열의 수만큼 오른쪽 열에 있는 타일이 사라지고,
    # 파란색 보드의 모든 블록이 사라진 열의 수만큼 이동
    move_cnt = 0
    for j in range(2):
        for i in range(blueN):
            if blue[i][j]:
                move_cnt += 1
                break

    if move_cnt:
        new_blue = [[0] * blueM for _ in range(blueN)]
        for i in range(blueN):
            for j in range(blueM - move_cnt):
                new_blue[i][j + move_cnt] = blue[i][j]
        return new_blue
    else:
        return blue


result = 0
for _ in range(Q):
    # 블록을 놓은 위치가 순서대로 주어졌을 때,
    t, y, x = map(int, input().split())

    # 초록색 보드에 블록 놓기
    add_block_green(t, x)

    # 파란색 보드에 블록 놓기
    add_block_blue(t, y)

    # 초록색 보드에 가득 찬 행 확인
    green_lines, green = remove_filled_green()
    result += green_lines

    # 파란색 보드에 가득 찬 열 확인
    blue_lines, blue = remove_filled_blue()
    result += blue_lines

    # 점수는 사라진 행 또는 열의 수
    # 행이나 열이 타일로 가득찬 경우와 연한 칸에 블록이 있는 경우가 동시에 발생할 수 있다.
    # 이 경우에는 행이나 열이 타일로 가득 찬 경우가 없을 때까지 점수를 획득하는 과정이 모두 진행된 후,
    # 연한 칸에 블록이 있는 경우를 처리해야 한다.

    # 초록색 보드의 0, 1번 행에 블록이 있으면,
    green = push_green()

    # 파란색 보드의 0, 1번 열에 블록이 있으면,
    blue = push_blue()

# 얻은 점수와 초록색 보드와 파란색 보드에 타일이 있는 칸의 개수
print(result)

cnt = 0
for line in green:
    cnt += sum(line)
for line in blue:
    cnt += sum(line)
print(cnt)
