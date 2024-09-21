N, M = map(int, input().split())
lst = [input() for _ in range(N)]
sy, sx = map(lambda x: int(x) - 1, input().split())

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
char_to_dir = {'R': 0, 'D': 1, 'L': 2, 'U': 3}


# bfs로 그룹 나누기
group_cnt = 0
groups = [[-1] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if groups[i][j] != -1:
            continue

        q = [(i, j)]
        groups[i][j] = group_cnt

        while q:
            nq = []

            for y, x in q:
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and groups[ny][nx] == -1 and lst[ny][nx] == lst[i][j]:
                        groups[ny][nx] = group_cnt
                        q.append((ny, nx))
            
            q = nq
        
        group_cnt += 1

# group_with_w[i]: i번째 그룹이 시야에 들어와있는지 확인
group_with_w = [0] * group_cnt

cmds = input()
for cmd in cmds:
    if cmd == 'W':
        group_with_w[groups[sy][sx]] = 1
    else:
        dy, dx = directions[char_to_dir[cmd]]
        sy += dy
        sx += dx

# 얼마나 넓은 시야를 확보했을지 계산
result = [['#'] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if group_with_w[groups[i][j]]:
            result[i][j] = '.'

result[sy][sx] = '.'
for dy, dx in directions:
    ny, nx = sy + dy, sx + dx
    if 0 <= ny < N and 0 <= nx < M:
        result[ny][nx] = '.'

for line in result:
    print(''.join(line))