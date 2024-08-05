N = 12
M = 6
lst = [list(input()) for _ in range(N)]

result = 0

while 1:
    # 터뜨리기
    flag = 0

    used = [[0] * M for _ in range(N)]
    for n in range(N):
        for m in range(M):
            if lst[n][m] != '.' and not used[n][m]:
                used[n][m] = 1
                tmp = [(n, m)]
                idx = 0

                while idx < len(tmp):
                    y, x = tmp[idx]

                    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        ny, nx = y + dy, x + dx

                        if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] == lst[n][m] and not used[ny][nx]:
                            used[ny][nx] = 1
                            tmp.append((ny, nx))

                    idx += 1

                if len(tmp) > 3:
                    for n, m in tmp:
                        lst[n][m] = '.'
                    flag = 1

    # 터뜨린 게 없다면 종료
    if not flag:
        break

    # 터뜨린 게 있다면 연쇄 1회 높이고 떨어뜨리기
    result += 1
    for m in range(M):
        for n in range(N - 2, -1, -1):
            if lst[n][m] != '.':
                ny = n + 1
                while 0 <= ny < N and lst[ny][m] == '.':
                    lst[ny - 1][m], lst[ny][m] = lst[ny][m], lst[ny - 1][m]
                    ny += 1

print(result)