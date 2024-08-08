while 1:
    try:
        M, P, L, E, R, S, N = map(int, input().split())

        for _ in range(N):
            l = M * E
            M = 0    # 유충을 낳음

            p = L // R    # 번데기가 됨

            m = P // S    # 성충이 됨

            M, P, L = m, p, l

        print(M)
    except:
        break