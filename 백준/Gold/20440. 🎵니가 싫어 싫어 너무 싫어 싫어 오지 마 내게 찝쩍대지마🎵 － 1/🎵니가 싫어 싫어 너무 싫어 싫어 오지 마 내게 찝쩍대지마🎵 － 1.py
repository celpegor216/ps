import sys
input = sys.stdin.readline

N = int(input())
times = dict()

for _ in range(N):
    s, e = map(int, input().split())
    times[s] = times.get(s, 0) + 1
    times[e] = times.get(e, 0) - 1

maxc = 0
maxs = maxe = -1

nowc = 0
nows = []

for key in sorted(times.keys()):
    value = times[key]

    if value > 0:
        nows.append(key)
    elif value < 0:
        if maxc < nowc:
            maxc = nowc
            maxs = nows[-1]
            maxe = key
        nows.pop()

    nowc += value

print(maxc)
print(maxs, maxe)