import sys
input = sys.stdin.readline


T = int(input())

MAX = 10 ** 5

for _ in range(T):
    N = int(input())
    lst = [[] for _ in range(MAX + 1)]

    for _ in range(N):
        x, y = map(int, input().split())
        lst[x].append(y)

    ny = nx = 0
    results = [(-1, -1)]
    while nx <= MAX:
        if lst[nx]:
            now_lst = sorted(lst[nx])

            # 아래로 탐색
            if ny == now_lst[0]:
                ranges = range(len(now_lst))
            else:
            # 위로 탐색
                ranges = range(len(now_lst) - 1, -1, -1)

            for i in ranges:
                results.append((nx, now_lst[i]))
            ny = now_lst[i]

        nx += 1

    _, *queries = list(map(int, input().split()))

    for query in queries:
        print(*results[query])