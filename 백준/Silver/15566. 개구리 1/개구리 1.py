N, M = map(int, input().split())
interests = [[]] + [list(map(int, input().split())) for _ in range(N)]
favorites = [[]] + [sorted(set(map(int, input().split()))) for _ in range(N)]
bridges = [list(map(int, input().split())) for _ in range(M)]

result = []
flowers = [0] * (N + 1)
used = [0] * (N + 1)

for i in range(1, N + 1):
    if len(favorites[i]) == 1 and not flowers[favorites[i][0]]:
        flowers[favorites[i][0]] = i
        used[i] = 1

def check():
    for a, b, t in bridges:
        if interests[flowers[a]][t - 1] != interests[flowers[b]][t - 1]:
            return False
    return True

def use(level):
    global result

    if result:
        return

    if level == N + 1:
        flag = check()

        if flag:
            result = flowers[1:]
        return
    
    if not used[level]:
        for item in favorites[level]:
            if not flowers[item]:
                flowers[item] = level
                used[level] = 1
                use(level + 1)
                flowers[item] = 0
                used[level] = 0
    else:
        use(level + 1)

use(1)

if result:
    print('YES')
    print(*result)
else:
    print('NO')