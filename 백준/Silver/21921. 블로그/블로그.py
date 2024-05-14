N, X = map(int, input().split())
lst = list(map(int, input().split()))

now = sum(lst[:X])
maxv = now
maxc = 1

for n in range(N - X):
    now -= lst[n]
    now += lst[n + X]

    if maxv == now:
        maxc += 1
    elif maxv < now:
        maxv = now
        maxc = 1

if maxv == 0:
    print('SAD')
else:
    print(maxv)
    print(maxc)