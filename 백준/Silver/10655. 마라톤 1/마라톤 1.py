import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
total = 0

distance = [0] * (N - 1)
for n in range(N - 1):
    distance[n] = abs(lst[n][0] - lst[n + 1][0]) + abs(lst[n][1] - lst[n + 1][1])
    total += distance[n]

skipped = -21e8
for n in range(N - 2):
    tmp = abs(lst[n][0] - lst[n + 2][0]) + abs(lst[n][1] - lst[n + 2][1])
    skipped = max(skipped, distance[n] + distance[n + 1] - tmp)

print(total - skipped)