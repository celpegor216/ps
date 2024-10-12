import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

sy = sx = -1
exits = []
people = []

for i in range(N):
    for j in range(M):
        if lst[i][j] == 'H':
            sy, sx = i, j
            lst[i][j] = '.'
        elif lst[i][j] == 'P':
            people.append((i, j))
            lst[i][j] = '.'
        elif lst[i][j] == '#':
            exits.append((i, j))


# 한별이의 모든 출구로의 최단 경로 찾기
def find_min_path(sy, sx, exit_cnts):
    q = [(sy, sx)]

    used = [[-1] * M for _ in range(N)]
    used[sy][sx] = 0

    left = exit_cnts
    while q:
        nq = []

        for y, x in q:
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] != 'X' and used[ny][nx] == -1:
                    used[ny][nx] = used[y][x] + 1
                    nq.append((ny, nx))

                    if lst[ny][nx] == '#':
                        left -= 1

        if not left:
            break
        q = nq
    
    return used


used = find_min_path(sy, sx, len(exits))

presents = [[0] * M for _ in range(N)]


def check_presents(sy, sx):
    q = [(sy, sx)]

    tmp_used = [[-1] * M for _ in range(N)]
    tmp_used[sy][sx] = 0

    while q:            
        nq = []

        for y, x in q:
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] != 'X' and tmp_used[ny][nx] == -1:
                    tmp_used[ny][nx] = tmp_used[y][x] + 1
                    nq.append((ny, nx))

                    if used[ny][nx] >= tmp_used[ny][nx]:
                        presents[ny][nx] += 1
        
        q = nq


for y, x in people:
    check_presents(y, x)


# 출구들에서 거꾸로 가면서 최댓값 찾기
result = 0

q = []
tmp_used = [[0] * M for _ in range(N)]

for y, x in exits:
    if used[y][x] == -1:
        continue
    
    q.append((y, x))
    tmp_used[y][x] = 1
    result = max(result, presents[y][x])

while q:
    nq = []

    for y, x in q:
        if used[y][x] == 0:
            continue

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not tmp_used[ny][nx] and used[ny][nx] == used[y][x] - 1:
                nq.append((y, x))
                tmp_used[ny][nx] = 1
                result = max(result, presents[y][x])
    
    q = nq


print(result)