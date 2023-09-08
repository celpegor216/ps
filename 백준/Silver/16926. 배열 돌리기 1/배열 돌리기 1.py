from copy import deepcopy

N, M, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

if N >= M:
    idx = M // 2
    if M % 2:
        idx += 1
else:
    idx = N // 2
    if N % 2:
        idx += 1

result = [[0] * M for _ in range(N)]

for i in range(idx):
    tmp = []

    for n in range(i, N - i - 1):
        tmp.append(lst[n][i])
    
    for m in range(i, M - i - 1):
        tmp.append(lst[N - i - 1][m])
    
    for n in range(N - i - 1, i, -1):
        tmp.append(lst[n][M - i - 1])
    
    for m in range(M - i - 1, i, -1):
        tmp.append(lst[i][m])
    
    length = len(tmp)
    
    start = (length - (R % length)) % length

    for n in range(i, N - i - 1):
        result[n][i] = tmp[start]
        start += 1
        if start == length:
            start = 0

    for m in range(i, M - i - 1):
        result[N - i - 1][m] = tmp[start]
        start += 1
        if start == length:
            start = 0
    
    for n in range(N - i - 1, i, -1):
        result[n][M - i - 1] = tmp[start]
        start += 1
        if start == length:
            start = 0
    
    for m in range(M - i - 1, i, -1):
        result[i][m] = tmp[start]
        start += 1
        if start == length:
            start = 0

for line in result:
    print(*line)