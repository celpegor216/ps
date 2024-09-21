N, M = map(int, input().split())

lst_A = [input() for _ in range(N)]
lst_B = [input() for _ in range(N)]


def check():
    for i in range(N):
        for j in range(M):
            y, x = i, j
            
            for dy, dx in ((0, 1), (1, 0)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M:
                    if lst_B[y][x] != lst_B[ny][nx] and lst_A[y][x] == lst_A[ny][nx]:
                        return 'NO'
    
    return 'YES'


print(check())