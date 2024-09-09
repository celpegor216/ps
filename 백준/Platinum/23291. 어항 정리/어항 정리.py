# 어항은 M개
M, K = map(int, input().split())
N = 1
# 가장 처음에 어항은 일렬, 물고기가 한 마리 이상
# 칸에 적힌 값은 그 어항에 들어있는 물고기의 수
lst = [list(map(int, input().split()))]

directions = ((0, 1), (1, 0))

def change_numbers_and_flatten():
    global lst, N, M

    # 모든 인접한 두 어항에 대해서, 물고기 수의 차이를 구한다. 이 차이를 5로 나눈 몫을 d
    # d가 0보다 크면, 두 어항 중 물고기의 수가 많은 곳에 있는 물고기 d 마리를 적은 곳에 있는 곳으로 보낸다
    # 이 과정은 모든 인접한 칸에 대해서 "동시에 발생"
    diffs = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not lst[i][j]:
                continue

            for dy, dx in directions:
                ny, nx = i + dy, j + dx

                if not (0 <= ny < N and 0 <= nx < M) or not lst[ny][nx]:
                    continue

                diff = abs(lst[i][j] - lst[ny][nx]) // 5
                if diff:
                    if lst[i][j] > lst[ny][nx]:
                        diffs[i][j] -= diff
                        diffs[ny][nx] += diff
                    else:
                        diffs[i][j] += diff
                        diffs[ny][nx] -= diff

    new_lst = []
    for j in range(M):
        for i in range(N - 1, -1, -1):
            if lst[i][j]:
                lst[i][j] += diffs[i][j]
                new_lst.append(lst[i][j])

    # 이제 다시 어항을 바닥에 일렬로 놓아야 한다.
    # 가장 왼쪽에 있는 어항부터, 그리고 아래에 있는 어항부터 가장 위에 있는 어항까지 순서대로 바닥에 놓아야 한다
    lst = [new_lst[:]]
    N = 1
    M = len(new_lst)


result = 0
while 1:
    # 물고기가 가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수 차이가
    # K 이하가 되려면 어항을 몇 번 정리해야하는지?
    if max(lst[0]) - min(lst[0]) <= K:
        break

    # 먼저, 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다
    # 만약, 그러한 어항이 여러개라면 물고기의 수가 최소인 어항 모두에 한 마리씩 넣는다
    minv = min(lst[0])
    for i in range(M):
        if lst[0][i] == minv:
            lst[0][i] += 1

    # 먼저, 가장 왼쪽에 있는 어항을 그 어항의 오른쪽에 있는 어항의 위에 올려 놓아
    # 2개 이상 쌓여있는 어항을 모두 공중 부양시킨 다음, 전체를 시계방향으로 90도 회전
    # 이후 공중 부양시킨 어항을 바닥에 있는 어항의 위에 올려놓는다
    # 바닥의 가장 왼쪽에 있는 어항 위에 공중 부양시킨 어항 중 가장 왼쪽에 있는 어항이 있어야 한다
    # 공중 부양시킨 어항 중 가장 오른쪽에 있는 어항의 아래에 바닥에 있는 어항이 있을때까지 반복
    r_cnt = 1
    c_cnt = 1
    while 1:
        if M - c_cnt < r_cnt:
            break

        tmp = []
        for j in range(c_cnt):
            t = []
            for i in range(N - 1, -1, -1):
                t.append(lst[i][j])
            tmp.append(t)

        diff = M - c_cnt - r_cnt
        new_lst = []
        for line in tmp:
            new_lst.append(line + [0] * diff)
        new_lst.append(lst[-1][c_cnt:])

        lst = new_lst
        N = len(lst)
        M = len(lst[0])
        if r_cnt == c_cnt:
            r_cnt += 1
        else:
            c_cnt += 1

    # 공중 부양 작업이 모두 끝나면, 어항에 있는 물고기의 수를 조절 + 바닥에 일렬로
    change_numbers_and_flatten()

    # 다시 공중 부양 작업을 해야 한다.
    # 이번에는 가운데를 중심으로 왼쪽 N/2개를 공중 부양시켜
    # 전체를 시계 방향으로 180도 회전 시킨 다음, 오른쪽 N/2개의 위에 놓아야 한다
    # 이 작업은 두 번 반복, 두 번 반복하면 바닥에 있는 어항의 수는 N/4개
    for _ in range(2):
        tmp = [lst[n][:M // 2] for n in range(N)]
        for _ in range(2):
            tmp = list(map(list, zip(*tmp[::-1])))
        lst = tmp + [lst[n][M // 2:] for n in range(N)]
        N *= 2
        M //= 2

    # 여기서 다시 위에서 한 물고기 조절 작업을 수행하고, 바닥에 일렬로 놓는 작업을 수행한다
    change_numbers_and_flatten()

    result += 1

print(result)