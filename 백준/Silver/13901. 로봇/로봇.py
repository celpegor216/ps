# 로봇은 사용자가 지정한 방향을 일직선으로 움직인다.
# 이동 중 벽이나 방문한 지역, 장애물을 만날 경우 로봇은 사용자가 지정한 다음 방향으로 움직인다.
# 사용자가 지정한 다음 방향이 없다면 맨 처음 방향으로 돌아가서 위의 과정을 반복한다.
# 로봇이 움직일 수 없을 경우 동작을 멈춘다.


N, M = map(int, input().split())

used = [[0] * M for _ in range(N)]

K = int(input())
for _ in range(K):
    y, x = list(map(int, input().split()))
    used[y][x] = 1

y, x = map(int, input().split())
used[y][x] = 1

direction_order = list(map(lambda n: int(n) - 1, input().split()))
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

idx = 0
while 1:
    for i in range(4):
        d = direction_order[idx]
        dy, dx = directions[d]
        cnt = 1
        while 1:
            ny = y + dy * cnt
            nx = x + dx * cnt
            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx]:
                used[ny][nx] = 1
                cnt += 1
            else:
                cnt -= 1
                break
        idx = (idx + 1) % 4
        if cnt:
            y = ny - dy
            x = nx - dx
            break
    else:    # 이동 방향을 모두 탐색했음에도 움직일 수 없는 경우 동작을 범춤
        break

print(y, x)