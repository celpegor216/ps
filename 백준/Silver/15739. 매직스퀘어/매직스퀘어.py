N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

def find():
    used = [0] * (N ** 2 + 1)
    rows = [0] * N
    cols = [0] * N
    cross = [0] * 2    # 좌상우하, 좌하우상

    for i in range(N):
        for j in range(N):
            if used[lst[i][j]]:
                return 0

            used[lst[i][j]] = 1

            rows[i] += lst[i][j]
            cols[j] += lst[i][j]

            if i == j:
                cross[0] += lst[i][j]

            if i + j == N - 1:
                cross[1] += lst[i][j]

    total = (N * (N ** 2 + 1)) // 2

    for i in range(N):
        if rows[i] != total:
            return 0

        if cols[i] != total:
            return 0

    for i in range(2):
        if cross[i] != total:
            return 0

    return 1

print('TRUE' if find() else 'FALSE')