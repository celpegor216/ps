K = int(input())
S = input()
N = len(S)

for k in range(0, N, K):
    print(S[k], end='')