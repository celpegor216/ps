T = int(input())

for _ in range(T):
    S, P = input().split()
    S = S.replace(P, ' ')
    print(len(S))