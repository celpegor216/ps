P, W = map(int, input().split())
S = input()

groups = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
G = len(groups)

result = 0
for i in range(len(S)):
    if S[i] == ' ':
        result += P
    else:
        for g in range(G):
            if S[i] in groups[g]:
                result += (groups[g].index(S[i]) + 1) * P

                if i and S[i - 1] in groups[g]:
                    result += W
                
                break

print(result)