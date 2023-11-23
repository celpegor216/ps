from copy import deepcopy

N, M, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

def one():
    global N, M, lst

    for n in range(N // 2):
        lst[n], lst[N - n - 1] = lst[N - n - 1], lst[n]

def two():
    global N, M, lst
    
    for n in range(N):
        for m in range(M // 2):
            lst[n][m], lst[n][M - m - 1] = lst[n][M - m - 1], lst[n][m]

def three():
    global N, M, lst
    
    tmp = [[0] * N for _ in range(M)]

    for m in range(M):
        for n in range(N):
            tmp[m][n] = lst[N - n - 1][m]
    
    lst = deepcopy(tmp)
    N, M = M, N

def four():
    global N, M, lst
    
    tmp = [[0] * N for _ in range(M)]

    for m in range(M):
        for n in range(N):
            tmp[m][n] = lst[n][M - m - 1]
    
    lst = deepcopy(tmp)
    N, M = M, N

def five():
    global N, M, lst
    
    tmp = [[0] * M for _ in range(N)]

    for n in range(N // 2):
        for m in range(M // 2):
            tmp[n][m + M // 2] = lst[n][m]
    
    for n in range(N // 2):
        for m in range(M // 2):
            tmp[n + N // 2][m + M // 2] = lst[n][m + M // 2]
    
    for n in range(N // 2):
        for m in range(M // 2):
            tmp[n + N // 2][m] = lst[n + N // 2][m + M // 2]
    
    for n in range(N // 2):
        for m in range(M // 2):
            tmp[n][m] = lst[n + N // 2][m]

    lst = deepcopy(tmp)

def six():
    global N, M, lst
    
    tmp = [[0] * M for _ in range(N)]

    for n in range(N // 2):
        for m in range(M // 2):
            tmp[n + N // 2][m] = lst[n][m]
    
    for n in range(N // 2):
        for m in range(M // 2):
            tmp[n + N // 2][m + M // 2] = lst[n + N // 2][m]
    
    for n in range(N // 2):
        for m in range(M // 2):
            tmp[n][m + M // 2] = lst[n + N // 2][m + M // 2]
    
    for n in range(N // 2):
        for m in range(M // 2):
            tmp[n][m] = lst[n][m + M // 2]

    lst = deepcopy(tmp)

for command in commands:
    if command == 1:
        one()
    elif command == 2:
        two()
    elif command == 3:
        three()
    elif command == 4:
        four()
    elif command == 5:
        five()
    elif command == 6:
        six()

for line in lst:
    print(*line)