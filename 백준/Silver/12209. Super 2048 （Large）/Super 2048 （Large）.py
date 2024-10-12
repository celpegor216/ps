TC = int(input())


# 왼쪽으로 밀기 기준
cmd_to_rotate_cnt = {'left': 0, 'down': 1, 'right': 2, 'up': 3}


for tc in range(1, TC + 1):
    N, cmd = input().split()
    N = int(N)

    lst = [list(map(int, input().split())) for _ in range(N)]

    rotate_cnt = cmd_to_rotate_cnt[cmd]

    for _ in range(rotate_cnt):
        lst = list(map(list, zip(*lst[::-1])))

    new_lst = [[0] * N for _ in range(N)]
    for i in range(N):
        idx = 0
        for j in range(N):
            if not lst[i][j]:
                continue

            if new_lst[i][idx] == lst[i][j]:
                new_lst[i][idx] *= 2
                idx += 1
            else:
                if new_lst[i][idx]:
                    idx += 1
                new_lst[i][idx] = lst[i][j]

    lst = new_lst
    for _ in range(rotate_cnt):
        lst = list(map(list, zip(*lst)))[::-1]

    print(f'Case #{tc}:')
    for line in lst:
        print(*line)