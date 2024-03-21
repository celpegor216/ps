N, M = map(int, input().split())
lst = [input() for _ in range(N)]

result = -1

for i in range(N):
    for j in range(M):
        # lst[i][j]에서 시작
        if int(lst[i][j]) ** 0.5 == int(int(lst[i][j]) ** 0.5):
            result = max(result, int(lst[i][j]))

        for n in range(-i, N - i):
            for m in range(-j, M - j):
                # i는 n만큼, j는 m만큼 증가
                if n == m == 0:
                    continue

                num = lst[i][j]
                ni, nj = i + n, j + m

                while 0 <= ni < N and 0 <= nj < M:
                    num += lst[ni][nj]

                    if int(num) ** 0.5 == int(int(num) ** 0.5):
                        result = max(result, int(num))
                    
                    ni += n
                    nj += m

print(result)