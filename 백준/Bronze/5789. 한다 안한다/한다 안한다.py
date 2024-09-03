T = int(input())

for _ in range(T):
    S = input()
    N = len(S)
    print('Do-it' if S[N // 2 - 1] == S[N // 2] else 'Do-it-Not')