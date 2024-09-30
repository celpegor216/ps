N = int(input())
lst = []
for _ in range(N):
    n, *tmp = map(int, input().split())
    lst.append(tmp)


def find():
    q = [0]
    n = -1
    used = [[0] * 10 for _ in range(N)]

    while q:
        nq = []

        for now in q:
            if n == N - 1:
                path = [now]
                level = n
                parent = used[level][now]
                while parent:
                    path.append(parent)
                    level -= 1
                    parent = used[level][parent]
                return path[::-1]

            for item in lst[n + 1]:
                if used[n + 1][item] or item == now:
                    continue

                used[n + 1][item] = now
                nq.append(item)

        q = nq
        n += 1

    return [-1]


result = find()

for item in result:
    print(item)
