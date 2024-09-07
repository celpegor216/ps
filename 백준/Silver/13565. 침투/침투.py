from collections import deque

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

used = [[0] * M for _ in range(N)]

def bfs():
    # 격자의 위쪽을 바깥쪽(outer side), 아래쪽을 안쪽(inner side)
    for j in range(M):
        if not used[0][j] and lst[0][j] == '0':
            used[0][j] = 1

            q = deque()
            q.append((0, j))

            while q:
                y, x = q.popleft()

                if y == N - 1:
                    return 1
                
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] == '0':
                        used[ny][nx] = 1
                        q.append((ny, nx))

print('YES' if bfs() else 'NO')