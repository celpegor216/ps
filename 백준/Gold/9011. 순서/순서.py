T = int(input())

for _ in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    result = [0] * (N + 1)
    left = [n for n in range(1, N + 1)]

    for n in range(N, 0, -1):
        if not left or lst[n] >= len(left):
            print('IMPOSSIBLE')
            break

        result[n] = left.pop(lst[n])
    else:
        print(*result[1:])