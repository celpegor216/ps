N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

total = 0
maxv = 0

def find(add_total):
    global total, maxv

    for i in range(N):
        row = 0
        for j in range(M):
            row += str(lst[i][j]).count('9')

        maxv = max(maxv, row)
        if add_total:
            total += row

find(1)
lst = list(map(list, zip(*lst)))
N, M = M, N
find(0)

print(total - maxv)