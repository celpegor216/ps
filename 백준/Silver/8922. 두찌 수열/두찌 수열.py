T = int(input())

for _ in range(T):
    N = int(input())
    tup = tuple(map(int, input().split()))

    used = set()
    used.add(tup)

    result = 'ZERO'
    while 1:
        if sum(tup) == 0:
            break

        nxt = tuple(abs(tup[i] - tup[(i + 1) % N]) for i in range(N))

        if nxt in used:
            result = 'LOOP'
            break
        
        used.add(nxt)
        tup = nxt

    print(result)