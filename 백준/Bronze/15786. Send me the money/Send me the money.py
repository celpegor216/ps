N, Q = map(int, input().split())
S = input()

for _ in range(Q):
    P = input()
    M = len(P)

    n = m = 0
    while n < N and m < M:
        if S[n] == P[m]:
            n += 1
        m += 1
    
    if n == N:
        print('true')
    else:
        print('false')