n = int(input())

if n == 1:
    print(1)
else:
    before_2 = 0
    before_1 = 1
    now = 0

    for i in range(1, n):
        now = before_2 + before_1
        before_2 = before_1
        before_1 = now

    print(now)