N = int(input())

def dfs(level, now):
    if level == N:
        return now

    for i in range(1, 4):
        tmp = now + [i]

        size = 1
        while size * 2 <= level + 1:
            if tmp[-size:] == tmp[-(size * 2):-size]:
                break
            size += 1
        else:
            result = dfs(level + 1, tmp)

            if result:
                return result

print(*dfs(0, []), sep='')