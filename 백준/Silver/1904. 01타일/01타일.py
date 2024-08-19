N = int(input())

if N <= 2:
    print(N)
else:
    before = 1
    now = 2
    for _ in range(N - 2):
        before = (before + now) % 15746
        now, before = before, now
    print(now)