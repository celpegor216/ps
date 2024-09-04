# N×N 크기
N, T, K = map(int, input().split())
M = N
# 겨울에 추가되는 양분의 양
add = [list(map(int, input().split())) for _ in range(N)]
# 가장 처음에 양분은 모든 칸에 5만큼
land = [[5] * M for _ in range(N)]
# 같은 1×1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다
trees = [[[] for _ in range(M)] for _ in range(N)]

directions = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

# T개의 나무를 구매해 땅에 심었다
# r과 c는 1부터 시작
for _ in range(T):
    y, x, z = map(int, input().split())
    trees[y - 1][x - 1].append(z)

for _ in range(K):
    # 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
    # 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다.
    # 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
    # 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
    for i in range(N):
        for j in range(M):
            if not trees[i][j]:
                continue

            dead = 0

            tmp = sorted(trees[i][j])
            trees[i][j] = []
            for tree in tmp:
                if land[i][j] < tree:
                    # 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다.
                    # 소수점 아래는 버린다.
                    dead += tree // 2
                else:
                    land[i][j] -= tree
                    trees[i][j].append(tree + 1)

            # 여름에는 봄에 죽은 나무가 양분으로 변하게 된다.
            land[i][j] += dead

    # 가을에는 나무가 번식한다.
    # 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
    # 어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다.
    # 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
    for i in range(N):
        for j in range(M):
            for tree in trees[i][j]:
                if not tree % 5:
                    for dy, dx in directions:
                        ny, nx = i + dy, j + dx
                        if 0 <= ny < N and 0 <= nx < M:
                            trees[ny][nx].append(1)

    # 겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다.
    # 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
    for i in range(N):
        for j in range(M):
            land[i][j] += add[i][j]

# K년이 지난 후 살아남은 나무의 수
result = 0
for i in range(N):
    for j in range(M):
        result += len(trees[i][j])

print(result)