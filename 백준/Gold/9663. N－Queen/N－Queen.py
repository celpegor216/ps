N = int(input())

result = 0

col = [0] * N
cross_left = [0] * N * 2 # N - (i - j)
cross_right = [0] * N * 2 # i + j

def dfs(level):
    global result

    if level == N:
        result += 1
        return

    for n in range(N):
        cl = N - (level - n)
        cr = level + n
        if not col[n] and not cross_left[cl] and not cross_right[cr]:
            col[n] = 1
            cross_left[cl] = 1
            cross_right[cr] = 1
            dfs(level + 1)
            col[n] = 0
            cross_left[cl] = 0
            cross_right[cr] = 0

dfs(0)

print(result)