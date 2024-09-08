N, M = map(int, input().split())
lst = [input() for _ in range(N)]

results = [0] * 5


def check(i, j):
    cnt = 0

    for y in range(2):
        for x in range(2):
            if lst[i + y][j + x] == '#':
                return -1
            elif lst[i + y][j + x] == 'X':
                cnt += 1

    return cnt


for i in range(N - 1):
    for j in range(M - 1):    
        cnt = check(i, j)

        if cnt != -1:
            results[cnt] += 1

print(*results, sep='\n')