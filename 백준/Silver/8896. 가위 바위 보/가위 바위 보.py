T = int(input())

for _ in range(T):
    N = int(input())
    lst = [input() for _ in range(N)]
    K = len(lst[0])

    alive = [n for n in range(N)]
    for k in range(K):
        R = []
        S = []
        P = []

        for n in alive:
            if lst[n][k] == 'R':
                R.append(n)
            elif lst[n][k] == 'S':
                S.append(n)
            else:
                P.append(n)

        if R and S and not P:
            alive = R
        elif R and P and not S:
            alive = P
        elif S and P and not R:
            alive = S

    if len(alive) == 1:
        print(alive[0] + 1)
    else:
        print(0)