N, K = map(int, input().split())
# 각 칸의 내구도, 길이 2N
lst = list(map(int, input().split()))

# 올리는 위치는 1번, 내리는 위치는 N번
# 총 2N개의 칸이 있음
# 로봇을 올리는 위치에 올리거나, 로봇이 이동하면 그 칸의 내구도는 1만큼 감소
up_idx = 0    # 1번 위치에 있는 벨트의 인덱스
down_idx = N - 1
robots = []

result = 0
zero_cnt = 0
while 1:
    result += 1

    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    up_idx = (up_idx - 1) % (2 * N)
    down_idx = (down_idx - 1) % (2 * N)

    # 내리는 위치에 로봇이 있다면 즉시 내림
    if down_idx in robots:
        robots.remove(down_idx)

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    new_robots = []
    for i in range(len(robots)):
        nxt = (robots[i] + 1) % (2 * N)
        if nxt not in new_robots and lst[nxt]:
            lst[nxt] -= 1

            # 내리는 위치로 로봇이 이동한다면 즉시 내림
            if nxt != down_idx:
                new_robots.append(nxt)

            if not lst[nxt]:
                zero_cnt += 1
        else:    # 이동할 수 없다면 가만히 있음
            new_robots.append(robots[i])

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if lst[up_idx]:
        new_robots.append(up_idx)
        lst[up_idx] -= 1

        if not lst[up_idx]:
            zero_cnt += 1

    robots = new_robots

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if zero_cnt >= K:
        break


print(result)