import sys
input = lambda: sys.stdin.readline().strip()


N, K = map(int, input().split())
rotated_lsts = [[list(input()) for _ in range(N)]]

d = 0
def find():
    for i in range(N):
        for j in range(N):
            if rotated_lsts[d][i][j] == 'L':
                rotated_lsts[d][i][j] = '.'
                return i, j


memo = dict()


sy, sx = find()
for _ in range(3):
    lst = list(map(list, zip(*rotated_lsts[-1][::-1])))
    rotated_lsts.append(lst)


for _ in range(K):
    cmd = input()

    if cmd == 'L':
        d = (d - 1) % 4
        # 3, 3 > 1, 3    /    2, 4 > 0, 2
        sy, sx = N - 1 - sx, sy
    else:
        d = (d + 1) % 4
        # 1, 1 > 1, 3    /    4, 2 > 2, 0
        sy, sx = sx, N - 1 - sy
    
    if not memo.get((sy, sx, d)):

        ny = sy + 1
        while ny < N and rotated_lsts[d][ny][sx] != 'X':
            ny += 1
        ny -= 1

        memo[(sy, sx, d)] = ny
    
    sy = memo[(sy, sx, d)]


rotated_lsts[d][sy][sx] = 'L'
for line in rotated_lsts[d]:
    print(''.join(line))