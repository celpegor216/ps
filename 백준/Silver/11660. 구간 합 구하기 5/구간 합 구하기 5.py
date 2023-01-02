# 해답: https://castlerain.tistory.com/100
# [1, 2, 3, 4, 5]라는 데이터가 있을 때, 누적합은 [1, 3, 6, 10, 15]
# 3 ~ 5까지 합을 구한다면 5까지의 누적합에서 2까지의 누적합을 뺌 15 - 3 = 12

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

memo = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        memo[i][j] += memo[i][j - 1] + memo[i - 1][j] - memo[i - 1][j - 1] + lst[i - 1][j - 1]

for m in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    print(memo[x2][y2] - memo[x1 - 1][y2] - memo[x2][y1 - 1] + memo[x1 - 1][y1 - 1])