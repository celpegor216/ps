# 접근 방법은 맞았는데 풀이가 틀림
# 해답: https://ongveloper.tistory.com/749

import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

young_happy_min = [21e10] * (N + 2)
young_tired_max = [-1] * (N + 2)
old_happy_max = [-1] * (N + 2)
old_tired_min = [21e10] * (N + 2)

for n in range(1, N + 1):
    young_happy_min[n] = min(young_happy_min[n - 1], lst[n - 1][0]) if lst[n - 1][0] else young_happy_min[n - 1]
    young_tired_max[n] = max(young_tired_max[n - 1], lst[n - 1][1]) if lst[n - 1][1] else young_tired_max[n - 1]

for n in range(N, 0, -1):
    old_happy_max[n] = max(old_happy_max[n + 1], lst[n - 1][0]) if lst[n - 1][0] else old_happy_max[n + 1]
    old_tired_min[n] = min(old_tired_min[n + 1], lst[n - 1][1]) if lst[n - 1][1] else old_tired_min[n + 1]

# 젊은 날 행복도의 최솟값 > 늙은 날 행복도의 최댓값
# 젊은 날 피로도의 최댓값 < 늙은 날 피로도의 최솟값
result = -1
for n in range(1, N):
    if young_happy_min[n] >= old_happy_max[n + 1] and young_tired_max[n] <= old_tired_min[n + 1]:
        result = n

print(result)