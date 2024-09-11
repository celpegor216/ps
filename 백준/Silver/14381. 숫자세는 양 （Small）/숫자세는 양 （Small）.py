TC = int(input())

for tc in range(1, TC + 1):
    N = input()

    if N == '0':
        result = 'INSOMNIA'
    else:
        used = [0] * 10
        now = N

        while 1:
            for n in now:
                used[int(n)] = 1

            if sum(used) == 10:
                break

            now = str(int(now) + int(N))

        result = now

    print(f'Case #{tc}: {result}')