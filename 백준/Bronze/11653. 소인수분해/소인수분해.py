N = int(input())

now = 2

while N > 1:
    if not N % now:
        print(now)
        N //= now
    else:
        now += 1