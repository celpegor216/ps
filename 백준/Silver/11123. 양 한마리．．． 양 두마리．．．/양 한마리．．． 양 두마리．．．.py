from collections import deque

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]

    used = [[0] * M for _ in range(N)]
    result = 0
    for n in range(N):
        for m in range(M):
            if lst[n][m] == '#' and not used[n][m]:
                result += 1
                
                used[n][m] = 1
                q = deque()
                q.append((n, m))

                while q:
                    nowy, nowx = q.popleft()

                    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        ny, nx = nowy + dy, nowx + dx

                        if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] == '#' and not used[ny][nx]:
                            used[ny][nx] = 1
                            q.append((ny, nx))
    
    print(result)