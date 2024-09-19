def dfs(level, path):
    global t, result

    if result:
        return

    if level == N:
        t += 1

        if t == T:
            result = path
        return

    for n in range(N):
        if not used[n]:
            used[n] = 1
            dfs(level + 1, path + S[n])
            used[n] = 0


while 1:
    try:
        S, T = input().split()
        T = int(T)
        N = len(S)

        t = 0
        result = ''
        used = [0] * N
        dfs(0, '')

        if not result:
            result = 'No permutation'

        print(f'{S} {T} = {result}')
    except:
        break