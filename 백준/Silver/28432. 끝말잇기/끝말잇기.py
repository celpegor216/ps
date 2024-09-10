N = int(input())
lst = [input() for _ in range(N)]
M = int(input())
candidates = []
for _ in range(M):
    tmp = input()
    if tmp not in lst:
        candidates.append(tmp)

for i in range(N):
    if lst[i] == '?':
        s = e = ''
        if i > 0:
            s = lst[i - 1][-1]
        if i < N - 1:
            e = lst[i + 1][0]

        for candidate in candidates:
            if (not s or candidate[0] == s) and (not e or candidate[-1] == e):
                print(candidate)
                break
        break