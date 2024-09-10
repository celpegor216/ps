T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    used = [0] * N * 2
    result = []
    for n in range(N * 2):
        if used[n]:
            continue

        used[n] = 1
        original = (lst[n] * 4) // 3
        for m in range(n + 1, N * 2):
            if not used[m] and lst[m] == original:
                used[m] = 1
                break

        result.append(lst[n])

    print(f'Case #{tc}:', *result)