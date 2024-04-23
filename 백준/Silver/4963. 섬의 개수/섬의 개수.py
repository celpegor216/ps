from collections import deque

while 1:
    M, N = map(int, input().split())

    if N == M == 0:
        break

    lst = [list(map(int, input().split())) for _ in range(N)]
    used = [[0] * M for _ in range(N)]
    result = 0

    for n in range(N):
        for m in range(M):
            if lst[n][m] and not used[n][m]:
                q = deque()
                q.append((n, m))

                used[n][m] = 1

                while q:
                    y, x = q.popleft()

                    for dy, dx in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx]:
                            q.append((ny, nx))
                            used[ny][nx] = 1
                
                result += 1
    
    print(result)