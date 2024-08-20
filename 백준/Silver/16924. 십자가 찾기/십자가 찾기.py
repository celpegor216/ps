# 십자가는 겹칠 수 있지만 범위를 벗어나서는 안 된다

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

maxv = min(N // 2, M // 2)  # 십자가가 가질 수 있는 최대 크기
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

used = [[0] * M for _ in range(N)]

result = []
for n in range(1, N - 1):
    for m in range(1, M - 1):
        if lst[n][m] == '*':
            v = 0

            for i in range(1, maxv + 1):
                flag = 0

                for dy, dx in directions:
                    ny, nx = n + dy * i, m + dx * i
                    if not (0 <= ny < N and 0 <= nx < M) or lst[ny][nx] != '*':
                        flag = 1
                        break
                else:
                    v = i

                if flag:
                    break

            if v:
                result.append((n + 1, m + 1, v))
                used[n][m] = 1

                for dy, dx in directions:
                    for i in range(1, v + 1):
                        used[n + dy * i][m + dx * i] = 1

flag = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == '*' and not used[i][j]:
            flag = 1
            break

    if flag:
        break

if flag:
    print(-1)
else:
    print(len(result))
    for line in result:
        print(*line)