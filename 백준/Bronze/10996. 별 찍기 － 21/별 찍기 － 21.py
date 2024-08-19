N = int(input())

if N == 1:
    print('*')
else:
    lines = [
        '* ' * ((N + 1) // 2),
        ' *' * (N // 2)
    ]

    for n in range(N):
        for line in lines:
            print(line)