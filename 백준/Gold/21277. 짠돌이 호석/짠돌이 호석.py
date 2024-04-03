N1, M1 = map(int, input().split())
P1 = [input() for _ in range(N1)]
N2, M2 = map(int, input().split())
P2 = [input() for _ in range(N2)]

result = max((N1 + N2) * max(M1, M2), (M1 + M2) * max(N1, N2))

for d in range(4):
    for i in range(N1):
        for j in range(M1):
            if not (P1[i][j] == '1' and P2[0][0] == '1'):
                flag = 0

                for n in range(N2):
                    if flag or i + n == N1:
                        break

                    for m in range(M2):
                        if j + m == M1:
                            break

                        if P1[i + n][j + m] == '1' and P2[n][m] == '1':
                            flag = 1
                            break
                
                if not flag:
                    result = min(result, max(N1, N2 + i) * max(M1, M2 + j))

    next_P2 = [''] * M2

    for m in range(M2):
        for n in range(N2):
            next_P2[m] += P2[N2 - n - 1][m]
    
    P2 = next_P2
    N2, M2 = M2, N2

print(result)