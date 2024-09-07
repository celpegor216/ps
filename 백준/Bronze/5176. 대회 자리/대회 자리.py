T = int(input())

for _ in range(T):
    P, M = map(int, input().split())

    used = [0] * (M + 1)
    result = 0

    for _ in range(P):
        m = int(input())

        if not used[m]:
            used[m] = 1
        else:
            result += 1

    print(result)