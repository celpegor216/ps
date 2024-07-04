T = int(input())

for _ in range(T):
    F, R, N = map(int, input().split())
    lst = [[] for _ in range(F + 1)]

    for _ in range(N):
        f, r = map(int, input().split())
        lst[f].append(r)
    
    result = F * 2 + R + 1
    for f in range(1, F + 1):
        if not lst[f]:
            continue

        lst[f].sort()
        length = len(lst[f])

        tmp = 21e8

        for i in range(length):
            if i == length - 1:
                tmp = min(tmp, lst[f][i], R - lst[f][0] + 1)
            else:
                tmp = min(tmp, lst[f][i] + (R - lst[f][i + 1] + 1))

        result += tmp * 2

    print(result)