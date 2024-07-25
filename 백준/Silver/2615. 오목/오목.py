N = 19

lst = [list(map(int, input().split())) for _ in range(N)]

def check():
    for i in range(N):
        for j in range(N):
            if not lst[i][j]:
                continue

            for dy, dx in ((-1, 1), (0, 1), (1, 1), (1, 0)):
                by, bx = i - dy, j - dx

                if 0 <= by < N and 0 <= bx < N and lst[by][bx] == lst[i][j]:
                    continue

                ny, nx = i + dy, j + dx
                cnt = 1

                while 0 <= ny < N and 0 <= nx < N and lst[ny][nx] == lst[i][j]:
                    cnt += 1
                    ny += dy
                    nx += dx

                if cnt == 5:
                    return lst[i][j], i, j

    return 0, 0, 0

side, y, x = check()

print(side)
if side:
    print(y + 1, x + 1)