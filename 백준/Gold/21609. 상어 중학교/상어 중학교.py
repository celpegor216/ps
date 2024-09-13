# 크기가 N×N, 일반 블록은 C가지 색상
N, C = map(int, input().split())
# 검은색 블록은 -1, 무지개 블록은 0, 블록이 없는 빈 칸은 -2
lst = [list(map(int, input().split())) for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def check(max_blocks, max_rainbow_cnt, max_min_row, max_min_col, blocks, rainbow_cnt, min_row, min_col):
    # 크기가 가장 큰 블록 그룹을 찾는다.
    if len(max_blocks) < len(blocks):
        return True
    elif len(max_blocks) > len(blocks):
        return False

    # 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹,
    if max_rainbow_cnt < rainbow_cnt:
        return True
    elif max_rainbow_cnt > rainbow_cnt:
        return False

    # 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을,
    if max_min_row < min_row:
        return True
    elif max_min_row > min_row:
        return False

    # 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
    if max_min_col < min_col:
        return True
    else:
        return False


def find():
    # 블록 그룹은 연결된 블록의 집합
    # 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록,
    # 그러한 블록이 여러개면 열의 번호가 가장 작은 블록

    max_blocks = []
    max_rainbow_cnt = -1
    max_min_row = max_min_col = -1

    # 검은색 블록과 무지개 블록, 빈 칸 제외한 블록들이 사용되었는지 표시
    used = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if lst[i][j] < 1 or used[i][j]:
                continue

            blocks = []
            blocks.append((i, j))

            rainbow_cnt = 0

            min_row = i
            min_col = j

            # 이전까지 사용한 블록 + 이번에 사용할 블록 표시
            tmp_used = [line[:] for line in used]
            tmp_used[i][j] = 1
            used[i][j] = 1

            idx = 0
            while idx < len(blocks):
                y, x = blocks[idx]

                for dy, dx in directions:
                    ny, nx = y + dy, x + dx

                    # 그룹에는 일반 블록이 적어도 하나 있어야 하며 일반 블록의 색은 모두 같아야 한다
                    # 검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다
                    if 0 <= ny < N and 0 <= nx < N and lst[ny][nx] in (0, lst[i][j]) and not tmp_used[ny][nx]:
                        tmp_used[ny][nx] = 1
                        blocks.append((ny, nx))

                        if lst[ny][nx] == 0:
                            rainbow_cnt += 1
                        else:
                            used[ny][nx] = 1

                            # 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록,
                            # 그러한 블록이 여러개면 열의 번호가 가장 작은 블록
                            if ny < min_row or (ny == min_row and nx < min_col):
                                min_row = ny
                                min_col = nx

                idx += 1

            flag = check(max_blocks, max_rainbow_cnt, max_min_row, max_min_col, blocks, rainbow_cnt, min_row, min_col)

            if flag:
                max_blocks = blocks[:]
                max_rainbow_cnt = rainbow_cnt
                max_min_row = min_row
                max_min_col = min_col

    return max_blocks


def gravity(tmp_lst):
    # 격자에 중력이 작용하면 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동
    # 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속 된다
    new_lst = [[-2] * N for _ in range(N)]

    for j in range(N):
        stack = []
        for i in range(N - 1, -1, -1):
            if tmp_lst[i][j] != -2:
                stack.append((tmp_lst[i][j], i))

        idx = N - 1
        for a, b in stack:
            if a == -1:
                idx = b
            new_lst[idx][j] = a
            idx -= 1

    return new_lst


def rotate(tmp_lst):
    # 90도 반시계 방향으로 회전
    new_lst = [[-2] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_lst[i][j] = tmp_lst[j][N - 1 - i]

    return new_lst


result = 0
# 오토 플레이는 다음과 같은 과정이 블록 그룹이 존재하는 동안 계속해서 반복
while 1:
    # 1. 크기가 가장 큰 블록 그룹을 찾는다.
    blocks = find()

    # 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며
    if len(blocks) <= 1:
        break

    # 2. 1에서 찾은 블록 그룹의 모든 블록을 제거한다.
    # 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B ** 2점을 획득한다.
    result += len(blocks) ** 2
    for y, x in blocks:
        lst[y][x] = -2

    # 3. 격자에 중력이 작용한다.
    lst = gravity(lst)

    # 4. 격자가 90도 반시계 방향으로 회전한다.
    lst = rotate(lst)

    # 5. 다시 격자에 중력이 작용한다.
    lst = gravity(lst)


# 오토 플레이가 모두 끝났을 때 획득한 점수의 합
print(result)
