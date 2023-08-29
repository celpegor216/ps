from collections import deque

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]

L = int(input())
moves = dict()

for l in range(L):
    time, command = input().split()
    moves[int(time)] = command

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

length = 1
snakes = deque()
snakes.append([1, 1])
d = 0

cnt = 0
while 1:
    y, x = snakes[-1]

    if moves.get(cnt):
        if moves[cnt] == 'D':
            d += 1
            if d > 3:
                d = 0
        else:
            d -= 1
            if d < 0:
                d = 3

    ny, nx = y + directions[d][0], x + directions[d][1]
    
    if not (0 < ny <= N and 0 < nx <= N) or [ny, nx] in snakes:
        break

    snakes.append([ny, nx])
    if [ny, nx] in apples:
        apples.remove([ny, nx])
    else:
        snakes.popleft()
    
    cnt += 1

print(cnt + 1)