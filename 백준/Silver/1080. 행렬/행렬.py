N, M = map(int, input().split())
before = [list(input()) for _ in range(N)]
after = [list(input()) for _ in range(N)]

result = 0

for n in range(N - 2):
    for m in range(M - 2):
        if before[n][m] != after[n][m]:
            result += 1

            for i in range(3):
                for j in range(3):
                    if before[n + i][m + j] == '1':
                        before[n + i][m + j] = '0'
                    else:
                        before[n + i][m + j] = '1'

for n in range(N):
    if result == -1:
        break

    for m in range(M):
        if before[n][m] != after[n][m]:
            result = -1
            break

print(result)