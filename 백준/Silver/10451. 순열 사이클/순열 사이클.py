T = int(input())

for _ in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    used = [0] * (N + 1)
    result = 0

    for n in range(1, N + 1):
        if not used[n]:
            result += 1

            used[n] = 1
            now = lst[n]
            while not used[now]:
                used[now] = 1
                now = lst[now]

    print(result)