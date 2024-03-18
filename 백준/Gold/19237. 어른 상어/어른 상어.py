import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

sharks = dict()
used = [[[0, 0] for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if lst[i][j]:
            sharks[lst[i][j]] = [lst[i][j], i, j]
            used[i][j] = [lst[i][j], K]

tmp = list(map(int, input().split()))
for m in range(M):
    sharks[m + 1].append(tmp[m])

directions = [(), (-1, 0), (1, 0), (0, -1), (0, 1)]
sharks_directions = [[]] + [[[]] + [list(map(int, input().split())) for _ in range(4)] for _ in range(M)]

result = 0

while len(sharks.keys()) > 1 and result <= 1000:
    # 번호가 작은 상어부터 이동
    tmp_sharks = dict()
    tmp_used = [[[] for _ in range(N)] for _ in range(N)]

    for key in sorted(sharks.keys()):
        nown, nowy, nowx, nowd = sharks[key]

        flag = 0
        mine = []

        for d in sharks_directions[nown][nowd]:
            ny, nx = nowy + directions[d][0], nowx + directions[d][1]

            if 0 <= ny < N and 0 <= nx < N:
                if not used[ny][nx][0]:
                    tmp_used[ny][nx].append([nown, d])
                    flag = 1
                    break
                elif used[ny][nx][0] == nown and not mine:
                    mine = [ny, nx, d]
            
        if not flag and mine:
            tmp_used[mine[0]][mine[1]].append([nown, mine[2]])
    
    # 1초마다 냄새가 옅어짐
    for i in range(N):
        for j in range(N):
            if used[i][j][1]:
                used[i][j][1] -= 1

                if not used[i][j][1]:
                    used[i][j][0] = 0
    
    for i in range(N):
        for j in range(N):
            if tmp_used[i][j]:
                tmp_used[i][j].sort(key=lambda x: x[0])

                n, d = tmp_used[i][j][0]
                used[i][j] = [n, K]
                tmp_sharks[n] = [n, i, j, d]
    
    sharks = tmp_sharks
    result += 1

print(result if result <= 1000 else -1)