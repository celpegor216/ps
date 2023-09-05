N, M = map(int, input().split())
lst = [input() for _ in range(N)]
used = [[0] * M for _ in range(N)]
dic = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
result = 0

for n in range(N):
    for m in range(M):
        if not used[n][m]:
            used[n][m] = 1
            paths = [(n, m)]
            
            ny, nx = n + dic[lst[n][m]][0], m + dic[lst[n][m]][1]
            while 1:
                if 0 <= ny < N and 0 <= nx < M:
                    if (ny, nx) in paths:
                        result += 1
                        break
                    elif used[ny][nx]:
                        break
                    else:
                        used[ny][nx] = 1
                        paths.append((ny, nx))
                        ny, nx = ny + dic[lst[ny][nx]][0], nx + dic[lst[ny][nx]][1]
                else:
                    result += 1
                    break

print(result)