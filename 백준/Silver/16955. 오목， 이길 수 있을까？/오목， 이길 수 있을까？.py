N = 10
lst = [list(input()) for _ in range(N)]

target = 'X' * 5

def check():
    # 가로
    for line in lst:
        if target in ''.join(line):
            return 1

    # 세로
    lst_t = list(map(list, zip(*lst)))
    for line in lst_t:
        if target in ''.join(line):
            return 1

    # 왼쪽위 - 오른쪽아래 대각선
    lurd = [''] * N * 2
    for i in range(N):
        for j in range(N):
            lurd[i - j + N] += lst[i][j]

    for line in lurd:
        if target in line:
            return 1

    # 왼쪽아래 - 오른쪽위 대각선
    ldru = [''] * N * 2
    for i in range(N):
        for j in range(N):
            ldru[i + j] += lst[i][j]

    for line in ldru:
        if target in line:
            return 1

    return 0

def find():
    for i in range(N):
        for j in range(N):
            if lst[i][j] != '.':
                continue

            lst[i][j] = 'X'

            if check():
                return 1

            lst[i][j] = '.'

    return 0

print(find())