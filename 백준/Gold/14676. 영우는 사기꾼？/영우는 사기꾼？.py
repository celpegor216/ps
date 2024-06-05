N, M, K = map(int, input().split())

parents = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    parents[b].append(a)

build = [0] * (N + 1)
commands = [list(map(int, input().split())) for _ in range(K)]
result = 'King-God-Emperor'

for a, b in commands:
    if a == 1:
        flag = 0

        for parent in parents[b]:
            if not build[parent]:
                flag = 1
                break

        if not flag:
            build[b] += 1
        else:
            result = 'Lier!'
            break
    elif a == 2:
        if not build[b]:
            result = 'Lier!'
            break
        else:
            build[b] -= 1

print(result)