S = input()
N = len(S)

for i in range(0, N, 10):
    if i + 10 <= N:
        print(S[i:i + 10])
    else:
        print(S[i:])