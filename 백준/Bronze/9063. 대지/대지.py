N = int(input())

maxy = maxx = -10001
miny = minx = 10001

for _ in range(N):
    x, y = map(int, input().split())

    maxy = max(maxy, y)
    miny = min(miny, y)
    maxx = max(maxx, x)
    minx = min(minx, x)

print((maxx - minx) * (maxy - miny))