N = int(input())

if N < 2:
    print(N)
else:
    before = 1
    now = 1

    for _ in range(N - 2):
        tmp = before
        before = now
        now += tmp

    print(now)