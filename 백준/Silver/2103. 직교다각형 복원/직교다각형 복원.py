import sys
input = sys.stdin.readline

MAXV = 10001

N = int(input())
lr = [[] for _ in range(MAXV)]
ud = [[] for _ in range(MAXV)]

for _ in range(N):
    y, x = list(map(int, input().split()))

    lr[y].append(x)
    ud[x].append(y)

result = 0

for i in range(MAXV):
    lr[i].sort()
    for j in range(0, len(lr[i]), 2):
        result += lr[i][j + 1] - lr[i][j]

for i in range(MAXV):
    ud[i].sort()
    for j in range(0, len(ud[i]), 2):
        result += ud[i][j + 1] - ud[i][j]

print(result)