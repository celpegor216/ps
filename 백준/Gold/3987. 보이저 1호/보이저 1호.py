N, M = map(int, input().split())
lst = [input() for _ in range(N)]
sy, sx = map(lambda x: int(x) - 1, input().split())

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
directions_string = 'URDL'
# 현재 방향이 d일 때 /를 만났을 때와 \를 만났을 때 변경되는 방향
next_directions = {
    '/': [1, 0, 3, 2],
    '\\': [3, 2, 1, 0]
}

result_d = -1
result_time = -1

for sd in range(4):
    y, x, d = sy, sx, sd

    # y, x 좌표에 d 방향으로 접근한 적이 있는지 확인
    used = [[[0] * 4 for _ in range(M)] for _ in range(N)]
    time = 0

    while 1:
        time += 1

        dy, dx = directions[d]
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if lst[ny][nx] == 'C':    # 블랙홀을 만나서 종료
                if time > result_time:
                    result_time = time
                    result_d = sd
                break

            if used[ny][nx][d]:    # 무한 루프에 빠져서 종료
                result_d = sd
                result_time = 'Voyager'
                break

            used[ny][nx][d] = 1
            y = ny
            x = nx

            if lst[ny][nx] in '/\\':
                d = next_directions[lst[ny][nx]][d]

        else:    # 항성계를 벗어나서 종료
            if time > result_time:
                result_time = time
                result_d = sd
            break

    if result_time == 'Voyager':
        break


print(directions_string[result_d])
print(result_time)