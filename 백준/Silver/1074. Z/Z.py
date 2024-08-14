N, y, x = map(int, input().split())

cnt = 0
result = 0
def visit(sy, sx, n):
    global result, cnt

    if result:
        return

    if sy == y and sx == x:
        result = cnt
        return

    if n == 1:
        cnt += 1
    else:
        half = n // 2
        for ny in (sy, sy + half):
            for nx in (sx, sx + half):
                if ny <= y < ny + half and nx <= x < nx + half:
                    visit(ny, nx, half)
                else:
                    cnt += half ** 2

visit(0, 0, 2 ** N)

print(result)