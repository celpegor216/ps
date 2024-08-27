N, T = map(int, input().split())
lst = [input().split() for _ in range(N)] + [[T, 'finish']]

# 처음 진행 방향이 오른쪽이므로 오른쪽부터 시작해서 시계방향
# 오른쪽 > 아래 > 왼쪽 > 위
directions = ((1, 0), (0, -1), (-1, 0), (0, 1))

# 현재 위치, 현재 방향, 현재 시각
x = y = d = t = 0

for n in range(N + 1):
    time, cmd = int(lst[n][0]), lst[n][1]
    move_time = time - t    # 방향을 꺾기 전까지 이동한 시간

    x += move_time * directions[d][0]
    y += move_time * directions[d][1]

    if cmd == 'right':
        d = (d + 1) % 4
    elif cmd == 'left':
        d = (d - 1) % 4
    else:
        break

    t = time

print(x, y)