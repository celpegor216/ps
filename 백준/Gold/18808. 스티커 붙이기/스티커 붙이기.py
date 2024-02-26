N, M, K = map(int, input().split())
used = [[0] * M for _ in range(N)]

def find(R, C, sticker):
    if R > N or C > M:
        return False

    for i in range(N - R + 1):
        for j in range(M - C + 1):
            flag = 0

            for r in range(R):
                if flag:
                    break

                for c in range(C):
                    if used[i + r][j + c] and sticker[r][c]:
                        flag = 1
                        break
            
            if not flag:
                for r in range(R):
                    for c in range(C):
                        if used[i + r][j + c] == 0 and sticker[r][c]:
                            used[i + r][j + c] = 1
                return True

    return False

for _ in range(K):
    R, C = list(map(int, input().split()))
    lst = [list(map(int, input().split())) for _ in range(R)]

    for i in range(4):
        if find(R, C, lst):
            break
        else:
            tmp = [[] for _ in range(C)]
            for c in range(C):
                for r in range(R - 1, -1, -1):
                    tmp[c].append(lst[r][c])

            lst = [tmp[c][:] for c in range(C)]
            R, C = C, R

result = 0
for n in range(N):
    for m in range(M):
        result += used[n][m]

print(result)