from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

result_time = 0
result_cnt = 0

while 1:
    # 바깥 공기 탐색
    q = deque()
    q.append((0, 0))
    
    used = [[0] * M for _ in range(N)]
    used[0][0] = 1
    tmp = []

    while q:
        nowy, nowx = q.popleft()

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx

            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx]:
                if lst[ny][nx]:
                    flag = 1
                    tmp.append((ny, nx))
                else:
                    q.append((ny, nx))
                used[ny][nx] = 1

    if not tmp:
        break
    else:
        result_time += 1
        result_cnt = len(tmp)

        for y, x in tmp:
            lst[y][x] = 0

print(result_time)
print(result_cnt)