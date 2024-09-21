N = int(input())
lst = list(map(int, input().split()))
K = int(input())

MAX = max(lst) * K
possibles = [0] * (MAX + 1)

def dfs(level, start, total):
    if level == K + 1:
        return

    for n in range(start, N):
        possibles[total + lst[n]] = 1
        dfs(level + 1, n, total + lst[n])

dfs(1, 0, 0)

result = possibles[1:].index(0) + 1

if result % 2:
    print(f'jjaksoon win at {result}')
else:
    print(f'holsoon win at {result}')