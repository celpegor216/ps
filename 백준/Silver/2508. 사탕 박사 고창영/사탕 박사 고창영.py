T = int(input())

for _ in range(T):
    _ = input()
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]

    result = 0
    for i in range(N):
        result += lst[i].count('>o<')

    for j in range(M):
        i = 0
        while i < N - 2:
            if lst[i][j] + lst[i + 1][j] + lst[i + 2][j] == 'vo^':
                result += 1
                i += 3
            else:
                i += 1

    print(result)