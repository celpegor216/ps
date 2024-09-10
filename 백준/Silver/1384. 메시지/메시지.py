tc = 0
while 1:
    tc += 1

    N = int(input())

    if not N:
        break

    lst = [input().split() for _ in range(N)]

    flag = 0
    print('Group', tc)
    for i in range(N):
        for j in range(1, N):
            if lst[i][j] == 'N':
                print(f'{lst[(i - j) % N][0]} was nasty about {lst[i][0]}')
                flag = 1
    if not flag:
        print('Nobody was nasty')
    print()