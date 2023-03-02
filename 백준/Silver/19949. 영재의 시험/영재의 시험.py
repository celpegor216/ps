lst = list(map(int, input().split()))

result = 0

def dfs(level, path):
    global result

    if level == 10:
        total = 0
        for i in range(10):
            if path[i] == lst[i]:
                total += 1
        if total >= 5:
            result += 1
        return

    for i in range(1, 6):
        if len(path) > 1 and path[-1] == i and path[-2] == i:
                continue
        else:
            dfs(level + 1, path + [i])

dfs(0, [])

print(result)