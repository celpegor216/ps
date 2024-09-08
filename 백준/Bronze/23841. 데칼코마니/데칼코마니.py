N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if lst[i][j] == '.':
            continue
        
        lst[i][M - j - 1] = lst[i][j]

for line in lst:
    print(''.join(line))