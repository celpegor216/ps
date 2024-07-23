N = 1001
M = int(input())

used = [[0] * N for _ in range(N)]
cnt = [0] * (M + 1)

for m in range(1, M + 1):
    x, y, J, I = map(int, input().split())

    for i in range(I):
        for j in range(J):
            if used[y + i][x + j]:
                cnt[used[y + i][x + j]] -= 1
            used[y + i][x + j] = m
            cnt[m] += 1

for item in cnt[1:]:
    print(item)