N, M = map(int, input().split())
lst = [list(input()) for _ in range(3 * N)]

for n in range(N):
    for m in range(M):
        tmp = lst[n * 3 + 1][m * 8 + 1:(m + 1) * 8]
        if tmp[-2] == '.':
            tmp.pop()
        tmp.pop()

        length = len(tmp)

        a = int(tmp[0])
        b = int(tmp[2])
        c = int(tmp[4]) if length == 5 else int(''.join(tmp[4:6]))

        if a + b == c:
            for i in range(length):
                lst[n * 3][m * 8 + 1 + i] = '*'
            lst[n * 3 + 1][m * 8] = '*'
            if length == 5:
                lst[n * 3 + 1][m * 8 + 6] = '*'
            else:
                lst[n * 3 + 1][m * 8 + 7] = '*'
            for i in range(length):
                lst[n * 3 + 2][m * 8 + 1 + i] = '*'
        else:
            lst[n * 3][m * 8 + 3] = '/'
            lst[n * 3 + 1][m * 8 + 2] = '/'
            lst[n * 3 + 2][m * 8 + 1] = '/'

for line in lst:
    print(''.join(line))