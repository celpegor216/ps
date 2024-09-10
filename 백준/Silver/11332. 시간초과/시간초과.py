T = int(input())

for _ in range(T):
    S, N, T, L = input().split()
    N = int(N)
    T = int(T)
    L = int(L)
    maxv = (10 ** 8) * L

    result = 'May Pass.'
    if S == 'O(N)':
        if T * T > maxv:
            result = 'TLE!'
    elif S == 'O(2^N)':
        if T * (2 ** N) > maxv:
            result = 'TLE!'
    elif S == 'O(N^2)':
        if T * N ** 2 > maxv:
            result = 'TLE!'
    elif S == 'O(N^3)':
        if T * N ** 3 > maxv:
            result = 'TLE!'
    elif S == 'O(N!)':
        total = T
        for i in range(2, N + 1):
            total *= i

            if total > maxv:
                result = 'TLE!'
                break

    print(result)
