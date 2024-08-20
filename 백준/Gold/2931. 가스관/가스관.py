N, M = map(int, input().split())
lst = [input() for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 하나라도 찾으면 바로 종료하기 위해 함수 사용
def find_missing():
    for i in range(N):
        for j in range(M):
            if lst[i][j] not in 'MZ':
                continue

            y, x = i, j

            # 탐색할 방향 찾기
            d = -1
            for k in range(4):
                dy, dx = directions[k]
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] != '.':
                    d = k
                    break

            # 끊기는 점 탐색
            while 1:
                ny, nx = y + directions[d][0], x + directions[d][1]

                # 직선 파이프는 방향을 바꿔줄 필요 없이 계속 진행하면 됨
                if lst[ny][nx] == '1':
                    if d == 2:  # 오른쪽에서 들어오는 경우(현재 방향이 왼쪽)
                        d = 1
                    else:  # 아래에서 들어오는 경우(현재 방향이 위쪽)
                        d = 0
                elif lst[ny][nx] == '2':
                    if d == 2:  # 오른쪽에서 들어오는 경우(현재 방향이 왼쪽)
                        d = 3
                    else:  # 위에서 들어오는 경우(현재 방향이 아래쪽)
                        d = 0
                elif lst[ny][nx] == '3':
                    if d == 0:  # 왼쪽에서 들어오는 경우(현재 방향이 오른쪽)
                        d = 3
                    else:  # 위에서 들어오는 경우(현재 방향이 아래쪽)
                        d = 2
                elif lst[ny][nx] == '4':
                    if d == 0:  # 왼쪽에서 들어오는 경우(현재 방향이 오른쪽)
                        d = 1
                    else:  # 아래에서 들어오는 경우(현재 방향이 위쪽)
                        d = 2
                elif lst[ny][nx] == '.':
                    # 하나의 블록만 지워졌기 때문에 한 점에서 출발해서 끊기는 점을 찾으면 다른 점에서 굳이 또 탐색할 필요 없음
                    return ny, nx

                y, x = ny, nx


missing = find_missing()

# i번째 방향으로 탐색할 때 있으면 연결해야 하는 블록
can_connect = ['-+34', '|+23', '-+12', '|+14']
need_connection = [0] * 4
for i in range(4):
    dy, dx = directions[i]
    ny, nx = missing[0] + dy, missing[1] + dx
    if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] in can_connect[i]:
        need_connection[i] = 1

result = ''
if sum(need_connection) == 4:
    result = '+'
elif need_connection[0] and need_connection[2]:
    result = '-'
elif need_connection[1] and need_connection[3]:
    result = '|'
elif need_connection[0] and need_connection[1]:
    result = 1
elif need_connection[0] and need_connection[3]:
    result = 2
elif need_connection[2] and need_connection[3]:
    result = 3
elif need_connection[2] and need_connection[1]:
    result = 4

print(missing[0] + 1, missing[1] + 1, result)