N = int(input())
S = input()

s = S.count('s')
t = S.count('t')

for n in range(N):
    if s == t:
        print(S[n:])
        break

    if s != t:
        if S[n] == 's':
            s -= 1
        else:
            t -= 1
