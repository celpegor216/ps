from collections import deque

N = int(input())
lst = [input() for _ in range(N)]

def bfs(is_red_equals_green):
    used = [[0] * N for _ in range(N)]
    cnt = 0

    if is_red_equals_green:
        colors = {'R': 'RG', 'G': 'RG', 'B': 'B'}
    else:
        colors = {'R': 'R', 'G': 'G', 'B': 'B'}

    for i in range(N):
        for j in range(N):
            if not used[i][j]:
                q = deque()
                q.append((i, j))
                used[i][j] = 1
                cnt += 1

                while q:
                    y, x = q.popleft()

                    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        ny, nx = y + dy, x + dx

                        if 0 <= ny < N and 0 <= nx < N and not used[ny][nx] and lst[ny][nx] in colors[lst[i][j]]:
                            q.append((ny, nx))
                            used[ny][nx] = 1

    return cnt

print(bfs(0), bfs(1))