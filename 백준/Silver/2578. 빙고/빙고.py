N = 5

lst = [list(map(int, input().split())) for _ in range(N)]
call = []

for _ in range(N):
    call += list(map(int, input().split()))

used = [[0] * N for _ in range(N)]

for n in range(N ** 2):
    now = call[n]

    for i in range(N):
        for j in range(N):
            if lst[i][j] == now:
                used[i][j] = 1

    cnt = 0

    # 가로
    for i in range(N):
        if sum(used[i]) == N:
            cnt += 1

    # 세로
    for j in range(N):
        if sum(used[y][j] for y in range(N)) == N:
            cnt += 1

    # 왼쪽위 - 오른쪽아래 대각선
    if sum(used[i][i] for i in range(N)) == N:
        cnt += 1

    # 왼쪽아래 - 오른쪽위 대각선
    if sum(used[i][N - i - 1] for i in range(N)) == N:
        cnt += 1

    if cnt >= 3:
        print(n + 1)
        break