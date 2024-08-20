T = int(input())

for _ in range(T):
    cmds = input()

    maxy = maxx = miny = minx = 0

    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))    # 북, 동, 남, 서

    y = x = d = 0

    for cmd in cmds:
        if cmd == 'F':
            y += directions[d][0]
            x += directions[d][1]
        elif cmd == 'B':
            y -= directions[d][0]
            x -= directions[d][1]
        elif cmd == 'L':
            d -= 1
            if d < 0:
                d = 3
        else:
            d += 1
            if d > 3:
                d = 0

        maxy = max(maxy, y)
        miny = min(miny, y)
        maxx = max(maxx, x)
        minx = min(minx, x)

    print((maxy - miny) * (maxx - minx))