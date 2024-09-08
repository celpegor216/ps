T = int(input())

for _ in range(T):
    input()

    N, M = map(int, input().split())
    S = sorted(map(int, input().split()), reverse=True)
    B = sorted(map(int, input().split()), reverse=True)
    s = N - 1
    b = M - 1

    while 1:
        if S[s] < B[b]:
            s -= 1
        else:
            b -= 1
        
        if s < 0:
            print('B')
            break
        elif b < 0:
            print('S')
            break