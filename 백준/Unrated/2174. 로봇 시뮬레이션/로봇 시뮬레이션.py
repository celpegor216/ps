# 반례 참고
# 움직이는 도중에 로봇에 충돌하는 경우를 고려하지 않음


M, N = map(int, input().split())

# 로봇 수, 명령 수
K, Q = map(int, input().split())

char_to_d = {'N': 3, 'W': 2, 'E': 0, 'S': 1}
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 좌표, 방향(NWES)
lst = [[0] * M for _ in range(N)]
info = [[]]
for k in range(1, K + 1):
    x, y, d = input().split()
    x = int(x) - 1
    y = N - int(y)
    d = char_to_d[d]
    info.append([y, x, d])
    lst[y][x] = k

# 명령을 내리는 로봇, 명령의 종류(위에 나와 있는), 명령의 반복 회수
cmds = [input().split() for _ in range(Q)]

def run():
    for idx, cmd_type, repeats in cmds:
        idx = int(idx)
        repeats = int(repeats)

        if cmd_type == 'L':
            info[idx][-1] = (info[idx][-1] - repeats) % 4
        elif cmd_type == 'R':
            info[idx][-1] = (info[idx][-1] + repeats) % 4
        else:
            y, x, d = info[idx]
            dy, dx = directions[d]
            ny, nx = y, x
            for _ in range(repeats):
                ny += dy
                nx += dx
                if not (0 <= ny < N and 0 <= nx < M):
                    return f'Robot {idx} crashes into the wall'
                elif lst[ny][nx]:
                    return f'Robot {idx} crashes into robot {lst[ny][nx]}'

            lst[y][x] = 0
            info[idx][0] = ny
            info[idx][1] = nx
            lst[ny][nx] = idx

    return 'OK'

print(run())