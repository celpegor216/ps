while 1:
    s = list(map(int, input().split()))

    if s == [0]:
        break

    k = s.pop(0)

    def dfs(level, before, path):
        if level == 6:
            print(*path)
            return

        for i in range(before + 1, k):
            dfs(level + 1, i, path + [s[i]])

    dfs(0, -1, [])
    print()