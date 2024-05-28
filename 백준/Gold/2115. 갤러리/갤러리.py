from collections import deque

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

used = [[0] * M for _ in range(N)]
walls = [[[0] * 4 for _ in range(M)] for _ in range(N)]
d = ((0, 1), (1, 0), (0, -1), (-1, 0))

for n in range(N):
    for m in range(M):
        if lst[n][m] == '.' and not used[n][m]:
            used[n][m] = 1

            q = deque()
            q.append((n, m))

            while q:
                y, x = q.popleft()

                for i in range(4):
                    dy, dx = d[i]
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M:
                        if lst[ny][nx] == 'X':
                            walls[ny][nx][i] = 1
                        elif not used[ny][nx]:
                            used[ny][nx] = 1
                            q.append((ny, nx))
            
result = 0

# 가로 방향
for n in range(N):
    down_cnt = 0    # 1
    up_cnt = 0    # 3
    for m in range(M):
        if walls[n][m][1]:
            down_cnt += 1
        else:
            result += down_cnt // 2
            down_cnt = 0
        
        if walls[n][m][3]:
            up_cnt += 1
        else:
            result += up_cnt // 2
            up_cnt = 0

for m in range(M):
    right_cnt = 0    # 0
    left_cnt = 0    # 2

    for n in range(N):
        if walls[n][m][0]:
            right_cnt += 1
        else:
            result += right_cnt // 2
            right_cnt = 0
        
        if walls[n][m][2]:
            left_cnt += 1
        else:
            result += left_cnt // 2
            left_cnt = 0
        
print(result)