N, M = map(int, input().split())
maxv = max(N, M)
T = int(input())
stickers = []
for _ in range(T):
    a, b = map(int, input().split())
    if max(a, b) > maxv:
        T -= 1
        continue
    stickers.append((a, b, a * b))


def horizontal(ay, ax, by, bx):
    return max(ay, by) <= N and ax + bx <= M

def vertical(ay, ax, by, bx):
    return ay + by <= N and max(ax, bx) <= M

result = 0
for i in range(T - 1):
    for j in range(i + 1, T):
        now = stickers[i][-1] + stickers[j][-1]

        iy, ix, jy, jx = stickers[i][0], stickers[i][1], stickers[j][0], stickers[j][1]
        for ay, ax, by, bx in ((iy, ix, jy, jx), (ix, iy, jy, jx), (iy, ix, jx, jy), (ix, iy, jx, jy)):
            if horizontal(ay, ax, by, bx) or vertical(ay, ax, by, bx):
                result = max(result, now)
                break

print(result)
