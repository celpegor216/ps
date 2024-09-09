tc = 0
while 1:
    tc += 1

    N = int(input())

    if not N:
        break

    lst = [input() for _ in range(N)]
    used = [0] * N

    for _ in range(2 * N - 1):
        idx, _ = input().split()
        used[int(idx) - 1] += 1

    for n in range(N):
        if used[n] == 1:
            print(tc, lst[n])
            break