N, M = map(int, input().split())
lst = []
for _ in range(N):
    S = input()
    line = []
    for s in S:
        if s == '.':
            line.append(0)
        elif s == '/':
            line.append(1)
        else:
            line.append(-1)
    lst.append(line)

used = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not lst[i][j] or used[i][j]:
            continue

        used[i][j] = 1
        
        ny, nx = i + 1, j + lst[i][j]
        while not lst[ny][nx]:
            used[ny][nx] = 2
            ny += 1
            nx += lst[i][j]
        
        used[ny][nx] = 1

print(sum([sum(line) for line in used]) // 2)