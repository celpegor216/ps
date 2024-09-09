N, M, T = map(int, input().split())
# lst[i][j]: i번째 원판에 적힌 j번째 수
lst = [list(map(int, input().split())) for _ in range(N)]
cmds = [list(map(int, input().split())) for _ in range(T)]

# 원판을 아래와 같은 방법으로 총 T번 회전
# i번째 회전할때 사용하는 변수는 xi, di, ki이다.
for x, d, k in cmds:
    # 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다.
    # 원판의 회전은 독립적으로 이루어진다. 2번 원판을 회전했을 때, 나머지 원판은 회전하지 않는다
    for n in range(x - 1, N, x):
        # di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.
        if d == 0:
            lst[n] = lst[n][-k:] + lst[n][:-k]
        else:
            lst[n] = lst[n][k:] + lst[n][:k]

    # 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다.
    checks = []
    total_sum = 0
    total_cnt = 0
    for i in range(N):
        for j in range(M):
            if not lst[i][j]:
                continue

            total_cnt += 1
            total_sum += lst[i][j]

            # (i, 1)은 (i, 2), (i, M)과 인접하다.
            # (i, M)은 (i, M-1), (i, 1)과 인접하다.
            # (i, j)는 (i, j-1), (i, j+1)과 인접하다. (2 ≤ j ≤ M-1)
            if lst[i][j - 1] == lst[i][j] or lst[i][j] == lst[i][(j + 1) % M]:
                checks.append((i, j))
                continue

            # (1, j)는 (2, j)와 인접하다.
            # (N, j)는 (N-1, j)와 인접하다.
            # (i, j)는 (i-1, j), (i+1, j)와 인접하다. (2 ≤ i ≤ N-1)
            if i < N - 1 and lst[i][j] == lst[i + 1][j]:
                checks.append((i, j))
                continue

            if i > 0 and lst[i][j] == lst[i - 1][j]:
                checks.append((i, j))

    if not total_sum:
        break

    # 그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
    if checks:
        for y, x in checks:
            lst[y][x] = 0
    # 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
    else:
        mean = total_sum / total_cnt
        for i in range(N):
            for j in range(M):
                if not lst[i][j]:
                    continue

                if lst[i][j] > mean:
                    lst[i][j] -= 1
                elif lst[i][j] < mean:
                    lst[i][j] += 1

# 원판을 T번 회전시킨 후 원판에 적힌 수의 합
print(sum([sum(line) for line in lst]))