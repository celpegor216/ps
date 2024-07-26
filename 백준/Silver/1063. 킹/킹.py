king, stone, Q = input().split()
N = 8

kx, ky = ord(king[0]) - ord('A'), int(king[1]) - 1
sx, sy = ord(stone[0]) - ord('A'), int(stone[1]) - 1

directions = {'R': (0, 1), 'L': (0, -1), 'B': (-1, 0), 'T': (1, 0), 'RT': (1, 1), 'LT': (1, -1), 'RB': (-1, 1), 'LB': (-1, -1)}

for _ in range(int(Q)):
    command = input()

    dy, dx = directions[command]

    nky, nkx = ky + dy, kx + dx

    if 0 <= nky < N and 0 <= nkx < N:
        if nky == sy and nkx == sx:
            nsy, nsx = sy + dy, sx + dx
            if 0 <= nsy < N and 0 <= nsx < N:
                sy, sx = nsy, nsx
                ky, kx = nky, nkx
        else:
            ky, kx = nky, nkx

print(f'{chr(ord("A") + kx)}{ky + 1}')
print(f'{chr(ord("A") + sx)}{sy + 1}')