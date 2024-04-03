# 해답: https://ongveloper.tistory.com/526

board = [['0'] * 150 for _ in range(150)]

N1, M1 = map(int, input().split())
P1 = [input() for _ in range(N1)]

for n in range(N1):
    for m in range(M1):
        board[50 + n][50 + m] = P1[n][m]

N2, M2 = map(int, input().split())
P2 = [input() for _ in range(N2)]

result = min((N1 + N2) * max(M1, M2), (M1 + M2) * max(N1, N2))

for d in range(4):
    for i in range(101):
        for j in range(101):
            flag = 0

            for n in range(N2):
                if flag:
                    break

                for m in range(M2):
                    if board[i + n][j + m] == '1' and P2[n][m] == '1':
                        flag = 1
                        break
            
            if not flag:
                width = max(50 + N1, i + N2) - min(i, 50)
                height = max(50 + M1, j + M2) - min(j, 50)
                result = min(result, width * height)

    next_P2 = [''] * M2

    for m in range(M2):
        for n in range(N2):
            next_P2[m] += P2[N2 - n - 1][m]
    
    P2 = next_P2
    N2, M2 = M2, N2

print(result)