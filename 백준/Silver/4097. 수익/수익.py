import sys
input = sys.stdin.readline

while 1:
    N = int(input())

    if N == 0:
        break

    now = -21e8
    result = now

    for _ in range(N):
        a = int(input())

        if now + a > a:
            now += a
        else:
            now = a
        
        result = max(result, now)

    print(result)