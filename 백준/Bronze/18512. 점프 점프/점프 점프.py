X, Y, P1, P2 = map(int, input().split())

P1s = [P1 + X * x for x in range(100)]
P2s = [P2 + Y * x for x in range(100)]

if P1s[0] < P2s[0]:
    result = -1
    for item in P1s:
        if item in P2s:
            result = item
            break
    print(result)
else:
    result = -1
    for item in P2s:
        if item in P1s:
            result = item
            break
    print(result)