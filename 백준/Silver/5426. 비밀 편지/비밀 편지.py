T = int(input())

for _ in range(T):
    S = input()
    N = int(len(S) ** 0.5)
    for i in range(N - 1, -1, -1):
        for j in range(N):
            print(S[i + j * N], end='')
    print()