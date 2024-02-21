# 시간초과 -> heapq을 사용하지 않아도 됨

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
add = [list(map(int, input().split())) for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
land = [[5] * N for _ in range(N)]

for m in range(M):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

for k in range(K):
    for i in range(N):
        for j in range(N):
            tree[i][j].sort()

            tmp = []
            dead = 0

            # 봄
            for n in range(len(tree[i][j])):
                if land[i][j] >= tree[i][j][n]:
                    land[i][j] -= tree[i][j][n]
                    tmp.append(tree[i][j][n] + 1)
                else:
                    dead += tree[i][j][n] // 2
                    
            # 여름
            tree[i][j] = tmp
            land[i][j] += dead
    
    for i in range(N):
        for j in range(N):
            # 가을
            for now in tree[i][j]:
                if not now % 5:
                    for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < N:
                            tree[ni][nj].append(1)

            # 겨울
            land[i][j] += add[i][j]

result = 0
for i in range(N):
    for j in range(N):
        result += len(tree[i][j])

print(result)