from collections import deque


I, N, K = map(int, input().split())
colors = input()
lst = [list(input()) for _ in range(N)]
cmds = input()

directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
char_to_dir_idx = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

def find():
    for i in range(N):
        for j in range(N):
            if lst[i][j] == '@':
                lst[i][j] = '.'
                return i, j

y, x = find()
ink_amount = ink_color = 0

for cmd in cmds:
    if cmd in 'UDLR':
        dy, dx = directions[char_to_dir_idx[cmd]]
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < N and lst[ny][nx] == '.':
            y, x = ny, nx
    elif cmd == 'j':
        ink_amount += 1
    elif cmd == 'J':
        if ink_amount:
            q = deque()
            q.append((y, x))

            used = [[0] * N for _ in range(N)]
            used[y][x] = 1

            for _ in range(ink_amount):
                for _ in range(len(q)):
                    cy, cx = q.popleft()

                    for dy, dx in directions:
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < N and 0 <= nx < N and not used[ny][nx]:
                            used[ny][nx] = 1
                            q.append((ny, nx))

                            if lst[ny][nx] != '.':
                                lst[ny][nx] = colors[ink_color]

        
        ink_color = (ink_color + 1) % I
        ink_amount = 0


lst[y][x] = '@'
for line in lst:
    print(''.join(line))