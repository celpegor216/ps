N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]


def clockwise(lst):
    res = [[] for _ in range(N)]
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            res[N - 1 - i + j].append(lst[i][j])
    return res


def anti_clockwise(lst):
    res = [[] for _ in range(N)]
    for i in range(N):
        now = N - 1
        for j in range(i, N):
            res[j].append(lst[now][now - i])
            now -= 1
    return res


def symmetry(lst):
    return [line[::-1] for line in lst]


used = []
result = 21e8
def dfs(now):
    global result

    used.append(now)
    total = 0
    for i in range(N):
        for j in range(i + 1):
            total += now[i][j] ^ B[i][j]

    result = min(result, total)

    clockwise_now = clockwise(now)
    if clockwise_now not in used:
        dfs(clockwise_now)

    anti_clockwise_now = anti_clockwise(now)
    if anti_clockwise_now not in used:
        dfs(anti_clockwise_now)

    symmetry_now = symmetry(now)
    if symmetry_now not in used:
        dfs(symmetry_now)


dfs(A)

print(result)