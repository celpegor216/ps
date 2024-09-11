M = input()
length = len(M)

maxv = -1
maxs = 'No Jam'

N = int(input())
for _ in range(N):
    S, V = input().split()
    V = int(V)

    idx = 0
    for i in range(len(S)):
        if S[i] == M[idx]:
            idx += 1

        if idx == length:
            v = V / (len(S) - length)
            if maxv < v:
                maxv = v
                maxs = S
            break

print(maxs)