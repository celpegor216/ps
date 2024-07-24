N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
D = 10001
lst.sort(key=lambda x: (x[1], x[-1]))

used = [0] * D

for p, d in lst:
    minv = 21e8
    minidx = 0

    for i in range(d, 0, -1):
        if used[i] < minv:
            minv = used[i]
            minidx = i

    if p > minv:
        used[minidx] = p

print(sum(used))