for i in range(3):
    a, b = input().split()
    a = list(map(int, a.split(':')))
    b = list(map(int, b.split(':')))

    result = 0

    while 1:
        tmp = a[0] * 10000 + a[1] * 100 + a[2]

        if not tmp % 3:
            result += 1

        flag = 1

        for j in range(3):
            if a[j] != b[j]:
                flag = 0
                break
        
        if flag:
            break

        a[2] += 1
        if a[2] == 60:
            a[2] = 0
            a[1] += 1
        if a[1] == 60:
            a[1] = 0
            a[0] += 1
        if a[0] == 24:
            a[0] = 0
        
    print(result)