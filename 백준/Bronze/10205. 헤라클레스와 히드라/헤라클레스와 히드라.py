T = int(input())

for t in range(1, T + 1):
    H = int(input())
    cmds = input()
    for cmd in cmds:
        if cmd == 'c':
            H += 1
        else:
            H -= 1

    print(f'Data Set {t}:')
    print(H)
    print()