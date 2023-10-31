N, M, sy, sx, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
moves = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]

# 0번째 자리는 바닥, 2번째 자리는 위
row = [0] * 4
col = [0] * 4

nowy, nowx = sy, sx

for command in commands:
    ny, nx = nowy + moves[command][0], nowx + moves[command][1]

    if 0 <= ny < N and 0 <= nx < M:
        nowy, nowx = ny, nx

        if command == 1:
            row = [row[3]] + row[:3]
            col[0] = row[0]
            col[2] = row[2]
        elif command == 2: 
            row = row[1:] + [row[0]]
            col[0] = row[0]
            col[2] = row[2]
        elif command == 3: 
            col = [col[3]] + col[:3]
            row[0] = col[0]
            row[2] = col[2]
        elif command == 4: 
            col = col[1:] + [col[0]]
            row[0] = col[0]
            row[2] = col[2]

        if lst[ny][nx] == 0:
            lst[ny][nx] = row[0]
        else:
            row[0] = lst[ny][nx]
            col[0] = lst[ny][nx]
            lst[ny][nx] = 0
        
        print(row[2])