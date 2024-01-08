# 해답: https://velog.io/@7h13200/Python%EB%B0%B1%EC%A4%80-19951%EB%B2%88-%ED%83%9C%EC%83%81%EC%9D%B4%EC%9D%98-%ED%9B%88%EB%A0%A8%EC%86%8C-%EC%83%9D%ED%99%9C

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 변화량 배열
order = [0] * (N + 1)

for m in range(M):
    a, b, k = map(int, input().split())

    order[a - 1] += k
    order[b] -= k

# 변화량 누적
change = 0

for n in range(N):
    change += order[n]
    print(lst[n] + change, end=" ")