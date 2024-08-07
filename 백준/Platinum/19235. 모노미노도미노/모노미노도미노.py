# 엣지 케이스를 더 못 찾겠음
# 해답: https://hooongs.tistory.com/297


Q = int(input())

N, M = 6, 4
blue = [[0] * M for _ in range(N)]
green = [[0] * M for _ in range(N)]


# 블록 추가
def add_blue(t, x):
    y = 1
    if t == 3:    # 세로 2칸
        while y < N and not blue[y][x] and not blue[y][x - 1]:
            y += 1
        y -= 1
        blue[y][x] = blue[y][x - 1] = 2
    else:
        while y < N and not blue[y][x]:
            y += 1
        y -= 1
        blue[y][x] = 1
        if t == 2:
            blue[y - 1][x] = 1


def add_green(t, x):
    y = 1
    if t == 2:    # 가로 2칸
        while y < N and not green[y][x] and not green[y][x + 1]:
            y += 1
        y -= 1
        green[y][x] = green[y][x + 1] = 2
    else:
        while y < N and not green[y][x]:
            y += 1
        y -= 1
        green[y][x] = 1
        if t == 3:
            green[y - 1][x] = 1


# 터뜨리기
def pop(lst, lst_type):
    global result, blue, green

    while 1:
        popped = 0

        for i in range(2, N):
            flag = 0
            for j in range(M):
                if not lst[i][j]:
                    flag = 1
                    break

            if not flag:
                result += 1
                popped = 1

                for j in range(M):
                    lst[i][j] = 0

        if not popped:
            break

        for i in range(N - 2, -1, -1):
            for j in range(M):
                if lst[i][j] == 1 and not lst[i + 1][j]:
                    ni = i + 1
                    while ni < N and not lst[ni][j]:
                        ni += 1
                    ni -= 1
                    lst[i][j] = 0
                    lst[ni][j] = 1

                # 파란색 보드의 2 * 1 블록 / 초록색 보드에서 1 * 2 블록: 양쪽을 한 번에 확인해야 함
                elif j < M - 1 and lst[i][j] == lst[i][j + 1] == 2:
                    ni = i + 1
                    while ni < N and not lst[ni][j] and not lst[ni][j + 1]:
                        ni += 1
                    ni -= 1
                    lst[i][j] = lst[i][j + 1] = 0
                    lst[ni][j] = lst[ni][j + 1] = 2

    move_cnt = 0
    for i in range(2):
        for j in range(M):
            if lst[i][j]:
                move_cnt += 1
                break

    if move_cnt:
        if lst_type == 'B':
            blue = [[0] * M for _ in range(move_cnt)] + [line[:] for line in lst[:N - move_cnt]]
        else:
            green = [[0] * M for _ in range(move_cnt)] + [line[:] for line in lst[:N - move_cnt]]


result = 0
for _ in range(Q):
    t, y, x = map(int, input().strip().split())

    add_blue(t, M - y - 1)
    add_green(t, x)

    pop(blue, 'B')
    pop(green, 'G')



cnt = 0
for line in blue[2:]:
    cnt += M - line.count(0)
for line in green[2:]:
    cnt += M - line.count(0)

print(result)
print(cnt)