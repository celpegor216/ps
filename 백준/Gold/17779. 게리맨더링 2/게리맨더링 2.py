N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

result = 21e8

for x in range(N - 3):
    for y in range(1, N - 1):
        for d1 in range(1, N):
            if not (0 <= y - d1):
                break

            for d2 in range(1, N):
                if x + d1 + d2 >= N or y + d2 >= N:
                    break
                used = [[-1] * N for _ in range(N)]

                for d in range(d1 + 1):
                    used[x + d][y - d] = 4
                    used[x + d2 + d][y + d2 - d] = 4
                for d in range(d2 + 1):
                    used[x + d][y + d] = 4
                    used[x + d1 + d][y - d1 + d] = 4
                
                for i in range(N):
                    if used[i].count(4) > 1:
                        for j in range(used[i].index(4) + 1, N):
                            if used[i][j] == 4:
                                break

                            used[i][j] = 4

                for r in range(N):
                    for c in range(N):
                        if used[r][c] != -1: continue

                        if 0 <= r < x + d1 and 0 <= c <= y:
                            used[r][c] = 0
                        elif 0 <= r <= x + d2 and y < c < N:
                            used[r][c] = 1
                        elif x + d1 <= r < N and 0 <= c < y - d1 + d2:
                            used[r][c] = 2
                        elif x + d2 < r < N and y - d1 + d2 <= c < N:
                            used[r][c] = 3
                
                part = [0] * 5

                for i in range(N):
                    for j in range(N):
                        part[used[i][j]] += lst[i][j]
                
                result = min(max(part) - min(part), result)
                
print(result)