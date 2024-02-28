# 시간초과
# 해답: https://countrysides.tistory.com/54

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        lst[i][j] *= -1

result = [[0] * N for _ in range(N)]

offset = M // 2

for i in range(offset, N - offset):
    for j in range(offset, N - offset):
        up = i - offset
        left = j - offset
        result[i][j] = lst[up][left]    # 도형 A

        if up - 1 >= 0:    # 도형 B
            result[i][j] -= lst[up - 1][left]
        if left - 1 >= 0:    # 도형 C
            result[i][j] -= lst[up][left - 1]
        if up - 1 >= 0 and left - 1 >= 0:    # 도형 D
            result[i][j] += lst[up - 1][left - 1]
        
        if i - M >= 0:    # 위쪽 빠진 모서리
            result[i][j] += result[i - M][j]
        if j - M >= 0:    # 왼쪽 빠진 모서리
            result[i][j] += result[i][j - M]
        if i - M >= 0 and j - M >= 0:    # 왼쪽 위 추가된 모서리
            result[i][j] -= result[i - M][j - M]

for line in result:
    print(*line)