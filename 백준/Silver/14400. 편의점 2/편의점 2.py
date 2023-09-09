N = int(input())
xs = []
ys = []

for n in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

xs.sort()
ys.sort()

if N % 2:
    mx = xs[N // 2]
else:
    mx1 = xs[N // 2]
    mx2 = xs[N // 2 - 1]

    if sum([abs(x - mx1) for x in xs]) < sum([abs(x - mx2) for x in xs]):
        mx = mx1
    else:
        mx = mx2

if N % 2:
    my = ys[N // 2]
else:
    my1 = ys[N // 2]
    my2 = ys[N // 2 - 1]

    if sum([abs(y - my1) for y in ys]) < sum([abs(y - my2) for y in ys]):
        my = my1
    else:
        my = my2

print(sum([abs(x - mx) for x in xs]) + sum([abs(y - my) for y in ys]))