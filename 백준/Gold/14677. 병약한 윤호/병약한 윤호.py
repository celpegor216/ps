N = int(input()) * 3
S = input()

result = 0
pills = 'BLD'

used = set()

def dfs(level, s, e):
    global result

    result = max(result, level)

    if s > e:
        return

    if S[s] == pills[level % 3] and (level + 1, s + 1, e) not in used:
        used.add((level + 1, s + 1, e))
        dfs(level + 1, s + 1, e)
    if S[e] == pills[level % 3] and (level + 1, s, e - 1) not in used:
        used.add((level + 1, s, e - 1))
        dfs(level + 1, s, e - 1)

used.add((0, 0, N - 1))
dfs(0, 0, N - 1)

print(result)