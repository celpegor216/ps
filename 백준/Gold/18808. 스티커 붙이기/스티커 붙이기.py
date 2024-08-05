N, M, K = map(int, input().split())
stickers = []
for _ in range(K):
    tmp = list(map(int, input().split()))
    tmp.append([])

    for _ in range(tmp[0]):
        tmp[-1].append(list(map(int, input().split())))

    stickers.append(tmp)

used = [[0] * M for _ in range(N)]

def check(n, m, sticker):
    for _ in range(4):
        for i in range(N - n + 1):
            for j in range(M - m + 1):
                flag = 0

                for k in range(n):
                    if flag:
                        break

                    for l in range(m):
                        if sticker[k][l] and used[i + k][j + l]:
                            flag = 1
                            break

                if not flag:
                    for k in range(n):
                        for l in range(m):
                            if sticker[k][l]:
                                used[i + k][j + l] = 1
                    return

        new_sticker = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_sticker[i][j] = sticker[n - j - 1][i]

        n, m = m, n
        sticker = new_sticker

for n, m, sticker in stickers:
    check(n, m, sticker)

result = 0
for line in used:
    result += sum(line)

print(result)