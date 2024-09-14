from collections import deque


I, N, K = map(int, input().split())
inks = input()
lst = [list(input()) for _ in range(N)]
cmds = input()

def find():
    for i in range(N):
        for j in range(N):
            if lst[i][j] == '@':
                lst[i][j] = '.'
                return i, j

cy, cx = find()
ink_amount = ink_color = 0

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
char_to_dir_idx = {'U': 3, 'D': 1, 'L': 2, 'R': 0}

for cmd in cmds:
    if cmd in 'UDLR':
        dy, dx = directions[char_to_dir_idx[cmd]]
        ny, nx = cy + dy, cx + dx
        if 0 <= ny < N and 0 <= nx < N and lst[ny][nx] == '.':
            cy, cx = ny, nx
    elif cmd == 'j':
        ink_amount += 1
    elif cmd == 'J':
        if ink_amount:
            q = deque()
            q.append((cy, cx))

            used = [[0] * N for _ in range(N)]

            for _ in range(ink_amount):
                for _ in range(len(q)):
                    y, x = q.popleft()

                    for dy, dx in directions:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < N and not used[ny][nx]:
                            used[ny][nx] = 1
                            q.append((ny, nx))

                            if lst[ny][nx] != '.':
                                lst[ny][nx] = inks[ink_color]

        ink_amount = 0
        ink_color = (ink_color + 1) % I


lst[cy][cx] = '@'
for line in lst:
    print(''.join(line))