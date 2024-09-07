N, M = map(int, input().split())
original = [input() for _ in range(N)]
target = [input() for _ in range(N)]

for n in range(N):
    flag = 0

    for m in range(M):
        if not(original[n][m] == target[n][m * 2] == target[n][m * 2 + 1]):
            flag = 1
            break
    
    if flag:
        print('Not Eyfa')
        break
else:
    print('Eyfa')