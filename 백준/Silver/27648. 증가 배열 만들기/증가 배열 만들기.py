N, M, K = map(int, input().split())

if N + M - 1 > K:
    print('NO')
else:
    print('YES')

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            print(i + j - 1, end=' ')
        print()