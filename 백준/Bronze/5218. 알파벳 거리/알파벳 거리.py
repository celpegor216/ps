T = int(input())

for _ in range(T):
    A, B = input().split()
    N = len(A)

    result = [0] * N
    for n in range(N):
        result[n] = ord(B[n]) - ord(A[n])
        if result[n] < 0:
            result[n] += 26
    
    print('Distances: ', end='')
    print(*result)