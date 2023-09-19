# 힌트: 이분 탐색, 누적합
# 해답: https://wooono.tistory.com/624

import sys
input = sys.stdin.readline

N, H = map(int, input().split())
downToUp = [0] * (H + 1)
upToDown = [0] * (H + 1)

for n in range(N):
    num = int(input())

    if not n % 2:
        downToUp[num] += 1
    else:
        upToDown[num] += 1
    
for h in range(H - 1, 0, -1):
    downToUp[h] += downToUp[h + 1]
    upToDown[h] += upToDown[h + 1]

minv = 21e8
minc = 0

# 전체 높이 기준 잘리는 개수 파악
for i in range(1, H + 1):
    tmp = downToUp[i] + upToDown[H - i + 1]

    if tmp < minv:
        minv = tmp
        minc = 1
    elif tmp == minv:
        minc += 1

print(minv, minc)