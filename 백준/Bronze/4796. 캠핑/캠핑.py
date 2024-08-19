tc = 0

while 1:
    L, P, V = map(int, input().split())

    if L == P == V == 0:
        break

    tc += 1

    print(f'Case {tc}: {L * (V // P) + min(L, V % P)}')