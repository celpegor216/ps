from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

lands = dict()

for n in range(N):
    for m in range(M):
        if lst[n][m]:
            lands[(n, m)] = 1

def bfs():
    result = 0

    while lands:
        tmp = []
        for n, m in lands.keys():
            cnt = 0

            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = n + dy, m + dx
                if 0 <= ny < N and 0 <= nx < M and not lst[ny][nx]:
                    cnt += 1
            
            if lst[n][m] <= cnt:
                tmp.append((n, m))
            else:
                lst[n][m] -= cnt
        
        for n, m in tmp:
            lands.pop((n, m))
            lst[n][m] = 0
        
        result += 1

        flag = 0

        used = [[0] * M for _ in range(N)]
        q = deque()

        for n, m in lands.keys():
            if not used[n][m]:
                if not flag:
                    flag = 1
                    used[n][m] = 1
                    q.append((n, m))

                    while q:
                        y, x = q.popleft()

                        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                            ny, nx = y + dy, x + dx
                            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx]:
                                used[ny][nx] = 1
                                q.append((ny, nx))
                else:
                    return result
    
    if not lands:
        return 0

print(bfs())