N = int(input())
lst = [list(input()) for _ in range(N)]

result = 0

for i in range(N):
    flag = 0
    for j in range(N - 1):
        if lst[i][j] != lst[i][j + 1]:
            flag = 1
            lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]

            rowc, colc, col2c = 1, 1, 1

            for k in range(1, N):
                if lst[i][k] != lst[i][k - 1]:
                    result = max(result, rowc)
                    rowc = 1
                else:
                    rowc += 1

                if lst[k][j] != lst[k - 1][j]:
                    result = max(result, colc)
                    colc = 1
                else:
                    colc += 1

                if lst[k][j + 1] != lst[k - 1][j + 1]:
                    result = max(result, col2c)
                    col2c = 1
                else:
                    col2c += 1

            result = max(result, rowc, colc, col2c)

            lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]
    
    if not flag:
        result = N
        break

if result < N:
    for j in range(N):
        flag = 0
        for i in range(N - 1):
            if lst[i][j] != lst[i + 1][j]:
                flag = 1
                lst[i][j], lst[i + 1][j] = lst[i + 1][j], lst[i][j]

                rowc, colc, row2c = 1, 1, 1

                for k in range(1, N):
                    if lst[i][k] != lst[i][k - 1]:
                        result = max(result, rowc)
                        rowc = 1
                    else:
                        rowc += 1

                    if lst[k][j] != lst[k - 1][j]:
                        result = max(result, colc)
                        colc = 1
                    else:
                        colc += 1

                    if lst[i + 1][k] != lst[i + 1][k - 1]:
                        result = max(result, row2c)
                        row2c = 1
                    else:
                        row2c += 1

                result = max(result, rowc, colc, row2c)

                lst[i][j], lst[i + 1][j] = lst[i + 1][j], lst[i][j]
        
        if not flag:
            break

print(result)