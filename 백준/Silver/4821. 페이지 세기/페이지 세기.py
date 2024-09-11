while 1:
    N = int(input())

    if not N:
        break

    lst = input().split(',')
    used = [0] * (N + 1)
    for item in lst:
        tmp = list(map(int, item.split('-')))

        if len(tmp) == 1:
            if tmp[0] <= N:
                used[tmp[0]] = 1
        else:
            a, b = tmp
            for i in range(a, b + 1):
                if i > N:
                    break
                used[i] = 1

    print(sum(used))