# 시간 초과
# 해답: https://velog.io/@7h13200/Python%EB%B0%B1%EC%A4%80-15806%EB%B2%88-%EC%98%81%EC%9A%B0%EC%9D%98-%EA%B8%B0%EC%88%99%EC%82%AC-%EC%B2%AD%EC%86%8C

from collections import deque
import sys
input = sys.stdin.readline

N, M, K, T = map(int, input().split())

# used[k][i][j]: 홀수/짝수(k)일 때 i, j까지 도달하는 데 걸리는 최단 시간
# 초기 곰팡이는 1일 후 모두 사라지므로 초기화하지 않음
used = [[[21e8] * N for _ in range(N)] for _ in range(2)]

mold = deque()
for _ in range(M):
    y, x = list(map(int, input().split()))
    
    y -= 1
    x -= 1
    
    mold.append((y, x, 0))

while mold:
    nowy, nowx, nowt =  mold.popleft()

    nextt = nowt + 1

    for dy, dx in ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)):
        ny, nx = nowy + dy, nowx + dx
        if 0 <= ny < N and 0 <= nx < N and used[nextt % 2][ny][nx] == 21e8:
            used[nextt % 2][ny][nx] = nextt
            mold.append((ny, nx, nextt))

result = 'NO'

for _ in range(K):
    y, x = list(map(int, input().split()))

    y -= 1
    x -= 1

    if used[T % 2][y][x] <= T:
        result = 'YES'

print(result)