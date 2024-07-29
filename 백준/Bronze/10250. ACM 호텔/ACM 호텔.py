T = int(input())

for _ in range(T):
    N, M, C = map(int, input().split())

    cnt = 0
    result = ''

    for m in range(1, M + 1):
        if result:
            break

        for n in range(1, N + 1):
            cnt += 1

            if cnt == C:
                result = f'{n}{m:02d}'
                break

    print(result)