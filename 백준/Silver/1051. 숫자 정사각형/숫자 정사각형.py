N, M = map(int, input().split())
lst = [list(map(int, input())) for _ in range(N)]

result = 1

for n in range(N):
    for m in range(M):
        cnt = 1
        while n + cnt < N and m + cnt < M:
            if lst[n][m] == lst[n + cnt][m] == lst[n][m + cnt] == lst[n + cnt][m + cnt]:
                result = max(result, cnt + 1)
            cnt += 1

print(result ** 2)