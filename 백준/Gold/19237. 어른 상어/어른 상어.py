'''
와...................................................
예전에 풀었던 코드 봤는데 오늘 내가 문제를 완전 잘못 이해하고 있었네,,,,,,,,,
한 칸에 남아있을 수 있는 냄새가 여러 개라고 생각해서 크기 K인 deque를 썼었는데
어차피 다른 냄새가 있는 칸으로는 이동하지 않으니까 한 칸에는 하나의 냄새만 남아있어서
굳이 크기가 K일 필요가 없었네,,,,,,, 이거 시간초과 각이었구나,,,,,,,,ㅋ,,,,,,,,,,,
진짜 운 좋았네,,,,,,,,,,,,,,,,,
'''





# N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다
N, M, K = map(int, input().split())
# 상어에는 1 이상 M 이하의 자연수 번호, 모든 번호는 서로 다르다
dic = dict()
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if not tmp[j]:
            continue

        dic[(i, j)] = tmp[j] - 1

D = 4
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

def transform(x):
    return int(x) - 1

# 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고,
# 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다
shark_directions_now = list(map(transform, input().split()))

# 상어마다, 방향마다 우선순위
shark_directions_priority = [[list(map(transform, input().split())) for _ in range(D)] for _ in range(M)]

smells = [[[0] * 2 for _ in range(N)] for _ in range(N)]

for result in range(1, 1001):
    # 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다
    # 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고,
    # 자신의 냄새를 그 칸에 뿌린다
    for pos, idx in dic.items():
        y, x = pos
        smells[y][x] = [idx, K]

    # 각 상어가 이동 방향을 결정할 때는,
    new_dic = dict()
    for pos, idx in dic.items():
        y, x = pos
        d = shark_directions_now[idx]

        nd = -1
        for nxtd in shark_directions_priority[idx][d]:
            dy, dx = directions[nxtd]
            ny, nx = y + dy, x + dx

            if not (0 <= ny < N and 0 <= nx < N):
                continue

            # 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다
            if not smells[ny][nx][-1]:
                nd = nxtd
                break
            # 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다
            # 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다.
            # 우선순위는 상어마다 다를 수 있고,
            # 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다
            elif nd == -1 and idx == smells[ny][nx][0]:
                nd = nxtd

        shark_directions_now[idx] = nd
        ny, nx = y + directions[nd][0], x + directions[nd][1]

        # 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면,
        # 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다
        new_dic[(ny, nx)] = min(new_dic.get((ny, nx), M + 1), idx)

    dic = new_dic

    # 냄새는 상어가 k번 이동하고 나면 사라진다.
    for i in range(N):
        for j in range(N):
            if smells[i][j][-1]:
                smells[i][j][-1] -= 1

    # 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지를 구하는 프로그램
    # 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력
    if len(dic) == 1:
        print(result)
        break
else:
    print(-1)