N, M = map(int, input().split())
lst = [input() for _ in range(N)]

def check(start):
    arr = [[0] * M for _ in range(N)]
    opp = 'W' if start == 'B' else 'B'

    for i in range(N):
        for j in range(M):
            if (i + j) % 2 == 0 and lst[i][j] != start:
                arr[i][j] = 1
            elif (i + j) % 2 == 1 and lst[i][j] != opp:
                arr[i][j] = 1

    return arr

lst_w = check('W')
lst_b = check('B')

minV = 999999999999999999

for i in range(N - 7):
    for j in range(M - 7):
        total_w = 0
        for k in range(8):
            for l in range(8):
                total_w += lst_w[i + k][j + l]

        total_b = 0
        for k in range(8):
            for l in range(8):
                total_b += lst_b[i + k][j + l]

        minV = min(minV, total_w, total_b)

print(minV)