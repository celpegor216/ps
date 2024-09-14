N, M = map(int, input().split())
used = [[0] * M for _ in range(N)]

def transform(x):
    return int(x) - 1

queen = list(map(transform, input().split()))[1:]
knights = list(map(transform, input().split()))[1:]
pawn = list(map(transform, input().split()))[1:]

queen_directions = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
knights_directions = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))

def initial_fill(lst):
    for i in range(0, len(lst), 2):
        used[lst[i]][lst[i + 1]] = 2

for lst in (queen, knights, pawn):
    initial_fill(lst)

for i in range(0, len(queen), 2):
    y, x = queen[i], queen[i + 1]

    for dy, dx in queen_directions:
        ny, nx = y + dy, x + dx
        while 0 <= ny < N and 0 <= nx < M and used[ny][nx] != 2:
            used[ny][nx] = 1
            ny += dy
            nx += dx

for i in range(0, len(knights), 2):
    y, x = knights[i], knights[i + 1]
    
    for dy, dx in knights_directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and used[ny][nx] != 2:
            used[ny][nx] = 1

print(sum([line.count(0) for line in used]))