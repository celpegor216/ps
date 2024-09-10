directions = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

while 1:
    N, M = map(int, input().split())

    if N == M == 0:
        break

    lst = [input() for _ in range(N)]
    result = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if lst[i][j] == '*':
                for dy, dx in directions:
                    ny, nx = i + dy, j + dx
                    if 0 <= ny < N and 0 <= nx < M:
                        result[ny][nx] += 1

    for i in range(N):
        for j in range(M):
            print(result[i][j] if lst[i][j] == '.' else '*', end='')
        print()